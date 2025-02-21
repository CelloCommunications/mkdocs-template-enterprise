"""
Process GitHub user attachments in markdown files.

This script finds GitHub user-attachment URLs in markdown files and downloads them
to local assets directories, updating the markdown files to reference local paths.
"""

import os
import re
import uuid
import mimetypes
import logging
import sys
from typing import Dict, Match, Optional, Tuple
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

try:
    import requests
    from requests.exceptions import RequestException
except ImportError:
    logging.error("'requests' package is required. Install it using 'pip install requests'")
    raise

def get_extension_from_url_and_content(url: str, content_type: Optional[str] = None) -> str:
    """
    Determine file extension from URL and content type.

    Args:
        url: The URL of the file
        content_type: The content-type header from the response (optional)

    Returns:
        str: The file extension including the dot (e.g. '.png')
    """
    # Try to get extension from URL first
    parsed_url = urlparse(url)
    path = parsed_url.path
    ext = os.path.splitext(path)[1]

    if ext:
        return ext.lower()

    # If no extension in URL, try content-type
    if content_type:
        ext = mimetypes.guess_extension(content_type)
        if ext:
            return ext.lower()

    # Default to .bin if we can't determine the type
    return '.bin'

def download_and_save_file(url: str, local_path: str) -> None:
    """
    Download a file from URL and save it locally.

    Args:
        url: The URL to download from
        local_path: The local path to save to
    """
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(local_path, 'wb') as file:
        file.write(response.content)
    logging.info("Downloaded: %s -> %s", url, local_path)

def get_url_and_text(match: Match, pattern_type: str) -> Tuple[str, str]:
    """
    Extract URL and text from a regex match.

    Args:
        match: The regex match object
        pattern_type: The type of pattern that matched

    Returns:
        Tuple[str, str]: The URL and display text
    """
    if pattern_type == 'direct_link':
        url = match.group(1)
        text = url
    else:
        text = match.group(1)
        url = match.group(2)
    return url, text

def process_attachment(url: str, text: str, assets_dir: str, pattern_type: str) -> str:
    """
    Process a single attachment URL.

    Args:
        url: The attachment URL
        text: The display text
        assets_dir: Directory to save attachments
        pattern_type: Type of pattern matched

    Returns:
        str: Updated markdown text
    """
    try:
        # Download the file and get content type
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        content_type = response.headers.get('content-type')

        # Generate filename
        ext = get_extension_from_url_and_content(url, content_type)
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = str(uuid.uuid4())
        if not os.path.splitext(filename)[1]:
            filename += ext

        local_path = os.path.join(assets_dir, filename)
        relative_path = os.path.join('assets', filename)

        # Download if doesn't exist
        if not os.path.exists(local_path):
            try:
                download_and_save_file(url, local_path)
            except (IOError, OSError) as e:
                logging.error("Failed to write file %s: %s", local_path, str(e))
                return None

        # Return appropriate markdown based on pattern type
        if pattern_type == 'image_link':
            return f'![{text}]({relative_path})'
        if pattern_type == 'markdown_link':
            return f'[{text}]({relative_path})'
        return relative_path

    except RequestException as err:
        logging.error("Error downloading %s: %s", url, str(err))
        return None
    except (ValueError, OSError) as err:
        logging.error("Error processing %s: %s", url, str(err))
        return None

def process_markdown_file(file_path: str) -> None:
    """
    Process a markdown file to download and update GitHub user-attachment references.

    Args:
        file_path: Path to the markdown file to process
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except IOError as e:
        logging.error("Failed to read file %s: %s", file_path, str(e))
        return

    # Regular expressions for different types of attachments
    patterns: Dict[str, str] = {
        'markdown_link': r'\[([^\]]*)\]\((https://github\.com/user-attachments/[^)]+)\)',
        'image_link': r'!\[([^\]]*)\]\((https://github\.com/user-attachments/[^)]+)\)',
        'direct_link': r'(https://github\.com/user-attachments/[^\s)}>]+)'
    }

    # Get the directory where the markdown file is located
    file_dir = os.path.dirname(file_path)
    assets_dir = os.path.join(file_dir, 'assets')

    try:
        os.makedirs(assets_dir, exist_ok=True)
    except OSError as e:
        logging.error("Failed to create assets directory %s: %s", assets_dir, str(e))
        return

    def handle_match(match: Match, pattern_type: str) -> str:
        """Handle a single regex match."""
        url, text = get_url_and_text(match, pattern_type)
        result = process_attachment(url, text, assets_dir, pattern_type)
        return result if result is not None else match.group(0)

    # Process all patterns
    new_content = content
    for pattern_type, pattern in patterns.items():
        new_content = re.sub(
            pattern,
            lambda m, pt=pattern_type: handle_match(m, pt),
            new_content
        )

    # Only write if content changed
    if new_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            logging.info("Updated: %s", file_path)
        except IOError as e:
            logging.error("Failed to write updates to %s: %s", file_path, str(e))

def main() -> None:
    """
    Main function to process all markdown files in the repository.
    """
    try:
        # Walk through repository looking for markdown files
        for root, _, files in os.walk('.'):
            if '.git' in root or 'node_modules' in root:
                logging.debug("Skipping directory: %s", root)
                continue
            for file in files:
                if file.endswith(('.md', '.mdx', '.markdown')):
                    file_path = os.path.join(root, file)
                    try:
                        logging.info("Processing file: %s", file_path)
                        process_markdown_file(file_path)
                    except (IOError, OSError) as e:
                        logging.error("Error processing %s: %s", file_path, str(e))
    except (IOError, OSError) as e:
        logging.error("Fatal error: %s", str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
