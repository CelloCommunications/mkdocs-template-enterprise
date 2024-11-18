'''py
import requests
import re
import json
import time
from typing import Dict, Optional

class PHPIPAMClient:
    def __init__(self, base_url: str, token: str):
        """Initialize PHPIPAM client with base URL and authentication token."""
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "phpipam-token": token,
            "Content-Type": "application/json"
        }

    def get_next_available_ip(self, subnet_id: str, max_retries: int = 10) -> Optional[str]:
        """Get next available IP address from specified subnet."""
        endpoint = f"{self.base_url}/addresses/first_free/{subnet_id}/"
        
        for retry in range(max_retries):
            try:
                response = requests.get(endpoint, headers=self.headers)
                
                if response.status_code == 200:
                    data = response.json()
                    if not data.get('data'):
                        print(f"No free IP addresses in subnet {subnet_id}")
                        return None
                    return data['data']
                
                elif response.status_code == 429:  # Rate limit
                    wait_time = (retry + 1) * 1  # Progressive backoff
                    time.sleep(wait_time)
                    continue
                    
                else:
                    print(f"Failed to get IP. Status: {response.status_code}")
                    return None
                    
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                if retry == max_retries - 1:
                    raise
                time.sleep(1)
                
        return None

    def reserve_ip(self, subnet_id: str, ip_address: str, hostname: str, description: str) -> bool:
        """Reserve an IP address in PHPIPAM."""
        endpoint = f"{self.base_url}/addresses/"
        
        payload = {
            "subnetId": subnet_id,
            "ip": ip_address,
            "description": description,
            "hostname": hostname,
            "tag": 2,
            "excludePing": 1,
            "PTRignore": 1
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            return response.status_code == 201
        except requests.exceptions.RequestException as e:
            print(f"Failed to reserve IP: {e}")
            return False

class ConfigGenerator:
    def __init__(self, ipam_client: PHPIPAMClient):
        """Initialize config generator with PHPIPAM client."""
        self.ipam_client = ipam_client
        self.parameter_cache = {}  # Cache for resolved parameters

    def process_config_file(self, template_path: str, output_path: str, subnet_mappings: Dict[str, str]) -> bool:
        """
        Process Cisco config template and generate final config with resolved parameters.
        
        Args:
            template_path: Path to template config file
            output_path: Path where to save generated config
            subnet_mappings: Dictionary mapping parameter names to subnet IDs
        """
        try:
            with open(template_path, 'r') as f:
                template = f.read()

            # Find all parameters in template
            parameters = re.findall(r'<([^>]+)>', template)
            
            # Process each parameter
            for param in parameters:
                if param.startswith('IP_ADDRESS_'):
                    subnet_id = subnet_mappings.get(param)
                    if not subnet_id:
                        print(f"No subnet mapping found for {param}")
                        continue
                        
                    # Get and cache IP address if not already cached
                    if param not in self.parameter_cache:
                        ip_address = self.ipam_client.get_next_available_ip(subnet_id)
                        if not ip_address:
                            return False
                        self.parameter_cache[param] = ip_address
                        
                    # Replace parameter in template
                    template = template.replace(f'<{param}>', self.parameter_cache[param])

            # Save processed config
            with open(output_path, 'w') as f:
                f.write(template)
                
            return True

        except Exception as e:
            print(f"Error processing config: {e}")
            return False

# Example usage
def main():
    # Initialize PHPIPAM client
    ipam_client = PHPIPAMClient(
        base_url="https://your-phpipam-instance/api",
        token="your-ipam-token"
    )
    
    # Initialize config generator
    generator = ConfigGenerator(ipam_client)
    
    # Define subnet mappings
    subnet_mappings = {
        "IP_ADDRESS_MANAGEMENT": "123",  # Subnet ID for management network
        "IP_ADDRESS_DATA": "456",        # Subnet ID for data network
    }
    
    # Process config
    success = generator.process_config_file(
        template_path="cisco_template.txt",
        output_path="generated_config.txt",
        subnet_mappings=subnet_mappings
    )
    
    if success:
        print("Configuration generated successfully")
    else:
        print("Failed to generate configuration")

if __name__ == "__main__":
    main()
