# Workflows Approach

My justification for using the `actions/deploy-pages` action over the `mkdocs gh-deploy` approach [shown here](https://github.com/squidfunk/mkdocs-material/blob/master/docs/publishing-your-site.md)

## Overview

1. **mkdocs gh-deploy approach**:

- Pros:
  - Simpler workflow (fewer steps)
  - Built-in to MkDocs
- Cons:
  - Requires git credentials setup
  - Less control over deployment process

- Doesn't use GitHub's native Pages deployment

1. **Our current approach**:

- Pros:
  - Uses official GitHub Pages actions
  - Better artifact handling
  - More explicit control
  - Integrates with GitHub's deployment system
  - No git credentials needed
  - Better security model
  - Supports Preview Deployments

1. **Conclusion:**

Our current workflow using `actions/deploy-pages` is actually superior because:

- It's more maintainable
- Better integrated with GitHub
- More secure
- More features
- More transparent

Recommendation: Keep our current workflow - it's the better approach than the official docs suggest.

To expand on the key differences with some added detail:

### 1. Artifact Handling

- **Our Approach**:

  ```yaml
  - uses: actions/upload-pages-artifact@v3
  - uses: actions/deploy-pages@v4
  ```

  - Separate build and deploy steps
  - Artifacts are properly versioned
  - Can be downloaded for debugging
  - Supports retention policies

- **gh-deploy**:
  - Single command deployment
  - No artifact preservation
  - Harder to debug failed deployments

### 2. Security Model

- **Our Approach**:

  ```yaml
  permissions:
    contents: read
    pages: write
    id-token: write
  ```

  - Granular permissions
  - OIDC token authentication
  - Minimal required access

- **gh-deploy**:
  - Requires repository write access
  - Uses less secure PAT tokens
  - Broader permissions scope

### 3. Preview Deployments

- **Our Approach**:

  ```yaml
  environment:
    name: github-pages
    url: ${{ steps.deployment.outputs.page_url }}
  ```

  - Supports PR preview deployments
  - Environment protection rules
  - Deployment URLs in PR comments

### 4. Integration Features

- **Our Approach**:
  - Deployment status checks
  - GitHub deployment API integration
  - Deployment history
  - Status badges
  - Branch protection rules support

### 5. Cache Management

- **Our Approach**:

  ```yaml
  - name: Generate cache key
    id: cache-key
    run: |
      echo "week=$(date --utc '+%V')" >> $GITHUB_OUTPUT
      echo "hash=$(sha256sum mkdocs.yml | cut -d ' ' -f 1)" >> $GITHUB_OUTPUT
  ```

  - Content-aware caching
  - Weekly rotation
  - Configuration-based invalidation

Our current approach is more robust and enterprise-ready.
