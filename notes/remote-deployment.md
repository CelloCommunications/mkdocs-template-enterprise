# Remote Deployment Configuration

Idea to configure dual deployment of the MkDocs site to both GitHub Pages and a datacenter server.

Uses a straight forward approach to deploy the MkDocs site to our datacenter server using either SCP or Rsync rather than faphing around with Docker containers, github runners or other complex solutions.

> [!WARNING]
> yet to be tested ...

[[toc]]

## Overview

The setup enables:

- Building the documentation once
- Deploying to GitHub Pages (existing functionality)
- Deploying to a datacenter server (new functionality)

## Implementation Steps

### 1. Required Secrets

Add these secrets to your GitHub repository (Settings > Secrets and variables > Actions):

```yaml
DC_HOST: "your.datacenter.com"
DC_USERNAME: "deployment-user"
DC_SSH_KEY: "private-ssh-key"
```

### 2. Deployment Options

#### Option A: SFTP/SCP Deployment

```yaml
- name: Deploy to Datacenter
  uses: appleboy/scp-action@master
  with:
    host: ${{ secrets.DC_HOST }}
    username: ${{ secrets.DC_USERNAME }}
    key: ${{ secrets.DC_SSH_KEY }}
    source: "site/*"
    target: "/path/to/webroot"
```

#### Option B: Rsync Deployment

```yaml
- name: Deploy to Datacenter
  run: |
    mkdir -p ~/.ssh
    echo "${{ secrets.DC_SSH_KEY }}" > ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa
    rsync -avz --delete site/ ${{ secrets.DC_USERNAME }}@${{ secrets.DC_HOST }}:/path/to/webroot/
```

### 3. Complete Workflow Example

```yaml
name: Deploy Documentation
on:
  push:
    branches: [main]
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
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install mkdocs-material

      - name: Build documentation
        run: mkdocs build

      # GitHub Pages Deployment
      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'site'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4

      # Datacenter Deployment
      - name: Deploy to Datacenter
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.DC_HOST }}
          username: ${{ secrets.DC_USERNAME }}
          key: ${{ secrets.DC_SSH_KEY }}
          source: "site/*"
          target: "/path/to/webroot"
```

## Security Considerations

1. **Access Control**
   - Use a dedicated deployment user in your datacenter
   - Restrict SSH key permissions to only what's needed
   - Consider IP allowlisting if your datacenter supports it
   - Use environment protection rules in GitHub Actions

2. **Validation & Monitoring**

   ```yaml
   # Add health check step
   - name: Verify Datacenter Deployment
     run: |
       curl --fail https://your.datacenter.com/docs/ || exit 1
   ```

## Best Practices

1. **Deployment Protection**
   - Use environment protection rules to require approval
   - Add status checks to verify both deployments
   - Implement smoke tests
   - Add deployment notifications (e.g., to Slack)

2. **Rollback Strategy**
   - Keep previous versions of the site
   - Implement version tagging
   - Use symlinks for easy rollback:

     ```bash
     ln -sfn /path/to/webroot/versions/$(date +%Y%m%d_%H%M%S) /path/to/webroot/current
     ```

## Troubleshooting

1. **Common Issues**
   - SSH key permissions (should be 600)
   - Firewall rules blocking deployment
   - Directory permissions in target location
   - Network connectivity issues

2. **Verification Steps**
   - Test SSH connection manually first
   - Verify target directory permissions
   - Check deployment logs in GitHub Actions
   - Validate site accessibility after deployment

## Additional Notes

- The workflow triggers on changes to `docs/` directory and `mkdocs.yml`
- Manual deployment is possible using workflow_dispatch
- Both deployments use the same built site content
- Consider implementing staging environments if needed
