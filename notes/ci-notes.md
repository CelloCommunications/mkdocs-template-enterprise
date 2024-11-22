# CI Documentation

## Workflow Implementation

To implement an action that pushes the artifact to the specified server, update the `ci.yml` workflow file. This implementation uses `scp` to securely copy files to the server.

### CI Workflow File

```yaml
name: ci
on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
  pull_request:
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.x
          cache: 'pip'
          cache-dependency-path: '**/requirements.txt'

      - name: Generate cache key
        id: cache-key
        run: |
          echo "week=$(date --utc '+%V')" >> $GITHUB_OUTPUT
          echo "hash=$(sha256sum mkdocs.yml | cut -d ' ' -f 1)" >> $GITHUB_OUTPUT

      - name: Cache dependencies
        uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ steps.cache-key.outputs.week }}-${{ steps.cache-key.outputs.hash }}
          path: |
            ~/.cache/pip
            ~/.local/lib/python*/site-packages
          restore-keys: |
            mkdocs-material-${{ steps.cache-key.outputs.week }}-
            mkdocs-material-

      - name: Install dependencies
        run: pip install mkdocs-material

      - name: Build documentation
        run: mkdocs build

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'site'
          name: github-pages

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
        with:
          artifact_name: github-pages

      - name: Setup SSH on GitHub Actions Ubuntu runner
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key
          ssh-keyscan -H -p 65222 ${{ secrets.SERVER_IP }} >> ~/.ssh/known_hosts
          chmod 600 ~/.ssh/known_hosts

      - name: Deploy to remote server in our Datacenter
        run: |
          # Create remote directory if it doesn't exist
          ssh -i ~/.ssh/deploy_key -p 65222 ${{ secrets.SERVER_USER }}@${{ secrets.SERVER_IP }} "mkdir -p /home/${{ secrets.SERVER_USER }}/site"

          # Sync files using rsync (I'm changing from scp for rsync to use diff updates)
          rsync -avz --delete \
            -e "ssh -i ~/.ssh/deploy_key -p 65222" \
            site/ \
            ${{ secrets.SERVER_USER }}@${{ secrets.SERVER_IP }}:/home/${{ secrets.SERVER_USER }}/site/

          # Verify deployment
          ssh -i ~/.ssh/deploy_key -p 65222 ${{ secrets.SERVER_USER }}@${{ secrets.SERVER_IP }} "ls -la /home/${{ secrets.SERVER_USER }}/site"
```

## SSH Deployment Setup

### 1. Server Setup

```bash
# Connect to the target server
ssh admin@10.1.25.200

# Create dedicated docs user with minimal privileges (Ubuntu 22.04)
sudo adduser --system --shell /bin/bash --group --home /home/docs docs

# Create required directories
sudo -u docs mkdir -p /home/docs/site
sudo -u docs mkdir -p /home/docs/.ssh
sudo -u docs chmod 700 /home/docs/.ssh

# Verify user and directories
id docs  # Verify user exists
ls -la /home/docs  # Should show docs:docs ownership

# Note: The docs user is intentionally not added to sudo group
# as it only needs permissions to receive and serve documentation files
```

### 2. Generate SSH Keys

```sh
# Generate a dedicated SSH key pair
ssh-keygen -t ed25519 -C "github-actions-deploy" -f ~/.ssh/github_actions_deploy

# Verify key generation and permissions
ls -la ~/.ssh/github_actions_deploy*
# Private key should show: -rw------- (600)
# Public key should show: -rw-r--r-- (644)

# Install public key
sudo -u docs tee /home/docs/.ssh/authorized_keys < ~/.ssh/github_actions_deploy.pub
sudo -u docs chmod 600 /home/docs/.ssh/authorized_keys

# Verify setup
id docs  # Verify user exists
ls -la /home/docs/site  # Should show docs:docs ownership
ls -la /home/docs/.ssh  # Should show drwx------ (700)
ls -la /home/docs/.ssh/authorized_keys  # Should show -rw------- (600)
lsb_release -a  # Verify Ubuntu version
```

### 3. GitHub Repository Configuration

1. Navigate to repository settings:
   - Go to Settings > Secrets and variables > Actions
   - Click "New repository secret"

2. Add required secrets:
   - `SSH_PRIVATE_KEY`: Content of `~/.ssh/github_actions_deploy` private key
   - `SERVER_IP`: Your deployment server IP
   - `DC_USERNAME`: Deployment user (e.g., `docs`)

3. Verify secret configuration:
   - Check that `SSH_PRIVATE_KEY` includes BEGIN/END markers
   - Verify secret names match workflow references
   - Ensure key permissions are correct (600) before copying

### 4. Connection Testing

```bash
# Test SSH connection
ssh -i ~/.ssh/github_actions_deploy -v docs@10.1.25.200

# Test file transfer
touch test.txt
scp -i ~/.ssh/github_actions_deploy test.txt docs@10.1.25.200:/home/docs/site/

# Verify site directory permissions
ssh -i ~/.ssh/github_actions_deploy docs@10.1.25.200 "ls -la /home/docs/site"
```

## Security Best Practices

- Protect newly generated deployment keys
  - Add `.ssh/github_actions_deploy*` to `.gitignore` before generating keys
  - Verify with: `grep "github_actions_deploy" .gitignore`
  - This prevents accidental commits of the keys during setup process
- Maintain restrictive file permissions
  - Private keys: 600
  - SSH directory: 700
  - Deployment directory: owned by docs user
- Implement regular key rotation
- Monitor GitHub Actions logs for deployment issues
- Use most restrictive permissions possible for docs user
- Verify Ubuntu version and keep system updated
