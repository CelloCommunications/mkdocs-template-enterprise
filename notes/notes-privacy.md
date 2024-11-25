
# Private Pages Configuration

This document outlines how to configure GitHub Pages for private access, restricting it to organization members only.

## Setting Up Private Access

### Repository Settings

1. Navigate to your repository settings:
   - Go to Settings > Pages
   - Under "Access Control"
   - Select "Restrict access to members of your organization"

### Organization Settings

1. Configure organization permissions:
   - Navigate to Organization Settings
   - Go to Member privileges
   - Under "Base permissions", ensure access to private pages is enabled

### Deployment Protection

1. Set up environment protection:
   - Go to Repository Settings > Environments > github-pages
   - Configure protection rules:
     - Required reviewers (if needed)
     - Restrict to specific branches (typically `main`)
     - Add any deployment branch restrictions

## Security Notes

- Access requires GitHub authentication
- Only organization members can view pages
- Public cache/CDN features are disabled for private pages
- Branch protection rules still apply to deployments

## Verification

To verify the setup:

1. Log out of GitHub and try accessing the pages
2. You should be redirected to GitHub login
3. Only organization members should see content after login
4. Non-members should receive a 404 error

## Important Considerations

- Private pages are only available for GitHub Enterprise accounts
- All repository collaborators must be organization members
- Search engine indexing is automatically disabled
- External embeds might not work due to authentication requirements
