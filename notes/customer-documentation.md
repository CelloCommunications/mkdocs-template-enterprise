# Sharing Private Documentation with Customers
 - https://customer1.cello.co.nz
 - https://customer2.cello.co.nz
## Available Methods

### 1. GitHub Organizations with Private Repository Access

**Best for**: Organizations that already use GitHub or need version control visibility.

#### Setup Process:
1. Create a separate GitHub organization for customer documentation
2. Move the relevant documentation repository into this organization
3. Invite customer users with specific roles:
   - Use "Read" access for basic viewing
   - Use "Triage" access if they need to create issues
4. Configure branch protection rules to prevent accidental changes

#### Advantages:
- Full version control
- Granular access control
- Professional appearance
- Customers can raise issues directly

#### Disadvantages:
- Requires customers to have GitHub accounts
- May need paid GitHub seats for private repos

### 2. Protected GitHub Pages with Authentication

**Best for**: Customers who need simple web access without GitHub accounts.

#### Setup Process:
1. Keep your documentation in a private repository
2. Set up authentication using one of these methods:

   a) Basic Authentication with Cloudflare:
   ```yaml
   # In your mkdocs.yml
   plugins:
     - auth:
         enabled: true
         backends:
           - type: basic
             users:
               customer1: 'hashedpassword123'
   ```

   b) OAuth2 with Auth0:
   ```yaml
   # In your mkdocs.yml
   plugins:
     - auth:
         enabled: true
         backends:
           - type: oauth2
             config:
               client_id: 'your_client_id'
               client_secret: 'your_client_secret'
               authorize_url: 'https://your-tenant.auth0.com/authorize'
               token_url: 'https://your-tenant.auth0.com/oauth/token'
   ```

3. Deploy using a custom domain with HTTPS
4. Set up access controls in your authentication provider

### 3. Subdomain Method with Separate Deployments

**Best for**: Complete separation between different customers' documentation.

#### Setup Process:
1. Create separate branches or repositories for each customer
2. Configure GitHub Pages to deploy to custom subdomains:
   ```yaml
   # customer1-docs.your-company.com
   cname: customer1-docs.your-company.com
   ```

3. Set up DNS records for each subdomain
4. Implement authentication per subdomain

## Best Practices

### Security
1. Regular access review
2. Audit logging enabled
3. HTTPS enforced
4. Sensitive information scrubbed
5. Authentication tokens rotated regularly

### Documentation Organization
1. Use clear customer-specific branches
2. Maintain a master template
3. Document only what's relevant to each customer
4. Version control customer-specific configurations

### Maintenance
1. Regular link checking
2. Automated deployment testing
3. Access monitoring
4. Regular backup verification

## Implementation Steps

1. **Assessment**
   - Identify documentation to be shared
   - List authorized users
   - Determine access requirements

2. **Setup**
   - Configure chosen sharing method
   - Set up authentication
   - Test access controls

3. **Deployment**
   - Deploy to production
   - Verify access works
   - Document processes

4. **Monitoring**
   - Set up access logging
   - Configure alerts
   - Monitor usage patterns

## Troubleshooting

Common issues and solutions:

1. **Access Denied**
   - Verify user permissions
   - Check authentication configuration
   - Confirm IP allowlisting

2. **Deployment Failed**
   - Check build logs
   - Verify branch protection rules
   - Confirm GitHub Pages settings

3. **Content Not Updated**
   - Clear cache
   - Check build status
   - Verify deployment workflow

## Security Considerations

1. **Access Control**
   - Implement least privilege
   - Regular access reviews
   - Clear offboarding process

2. **Data Protection**
   - No sensitive data in docs
   - Regular content audits
   - Secure transmission

3. **Monitoring**
   - Access logging
   - Failed login alerts
   - Usage analytics