# Fortigate Notes

> [!TIP]
> Blair if this is wrong in any way please adjust or let me know. Cheers mate!

Blair, obviously you wont need this conf but it would be cool to have this idea of a conf working by someone that knows our Fortigate firewall.

> [!NOTE]
> We could obscure the port if you wish by changing it to what ever you want. Then I could adjust my workflow accordingly

[Fortigate-Policy](../scripts/fortigate-github-policy.conf)

## GitHub Actions IP Ranges

Main curl: `curl https://api.github.com/meta`

Get the IP ranges for GitHub Actions via Linux

```bash
#!/bin/bash

echo "# GitHub Actions IP Ranges (Major blocks only):"
curl -s https://api.github.com/meta | \
jq -r '.actions[]' | \
grep -v ':' | \
grep -E '^[0-9]+\.[0-9]+\.0\.0/(16|15|14|13|12)' | \
sort -t. -k1,1n -k2,2n | \
uniq

echo -e "\n# Number of major blocks found:"
curl -s https://api.github.com/meta | \
jq -r '.actions[]' | \
grep -v ':' | \
grep -E '^[0-9]+\.[0-9]+\.0\.0/(16|15|14|13|12)' | \
wc -l
```

```txt
 base 3.12.4  shadmin @ devops ❯ ~ ❯ ./github-actions-ip-extractor.sh
# GitHub Actions IP Ranges (Major blocks only):
4.148.0.0/16
4.151.0.0/16
4.152.0.0/15
4.154.0.0/15
4.156.0.0/15
4.175.0.0/16
4.180.0.0/16
4.207.0.0/16
4.208.0.0/15
9.163.0.0/16
13.64.0.0/16
13.65.0.0/16
13.74.0.0/16
13.79.0.0/16
13.80.0.0/15
13.82.0.0/16
13.83.0.0/16
13.84.0.0/15
13.89.0.0/16
13.90.0.0/16
13.91.0.0/16
13.92.0.0/16
13.95.0.0/16
20.3.0.0/16
20.4.0.0/16
20.7.0.0/16
20.8.0.0/16
20.10.0.0/16
20.16.0.0/16
20.22.0.0/16
20.23.0.0/16
20.31.0.0/16
20.56.0.0/16
20.61.0.0/16
20.71.0.0/16
20.73.0.0/16
20.76.0.0/16
20.86.0.0/16
20.96.0.0/16
20.101.0.0/16
20.103.0.0/16
20.110.0.0/16
20.121.0.0/16
20.122.0.0/16
20.124.0.0/16
20.126.0.0/16
20.127.0.0/16
20.160.0.0/16
20.161.0.0/16
20.166.0.0/16
20.171.0.0/16
20.185.0.0/16
20.223.0.0/16
20.224.0.0/16
20.225.0.0/16
20.229.0.0/16
20.232.0.0/16
20.245.0.0/16
40.68.0.0/16
40.71.0.0/16
40.76.0.0/16
40.88.0.0/16
40.116.0.0/16
40.121.0.0/16
40.124.0.0/16
48.217.0.0/16
50.85.0.0/16
51.124.0.0/16
51.136.0.0/16
51.144.0.0/16
52.160.0.0/16
52.162.0.0/16
52.164.0.0/16
52.166.0.0/16
52.167.0.0/16
52.168.0.0/16
52.169.0.0/16
52.170.0.0/16
52.171.0.0/16
52.173.0.0/16
52.174.0.0/16
52.177.0.0/16
52.186.0.0/16
52.188.0.0/16
52.224.0.0/16
52.226.0.0/16
52.241.0.0/16
57.153.0.0/16
74.235.0.0/16
98.64.0.0/16
104.42.0.0/16
108.141.0.0/16
108.142.0.0/15
172.168.0.0/15
172.170.0.0/16
172.174.0.0/16
172.175.0.0/16
172.176.0.0/15
172.179.0.0/16
172.180.0.0/15
172.182.0.0/16
172.183.0.0/16
172.184.0.0/15
172.190.0.0/15
172.200.0.0/16
172.201.0.0/16
172.211.0.0/16

# Number of major blocks found:
107
```

Get the IP ranges for GitHub Actions via Fortigate

```txt
# If you want to generate Fortigate config directly:
echo "config firewall address"
curl -s https://api.github.com/meta | jq -r '.actions[]' | awk '{
    printf("    edit \"GitHub-Actions-Range-%d\"\n        set type iprange\n        set comment \"GitHub Actions Runner IP range\"\n        set subnet %s\n    next\n", NR, $1)
}'
echo "end"
```
