# GitHub User Attachments Processor

## Overview

This solution addresses a specific security concern with GitHub's web-based file attachment feature. When users drag and drop files (images, PDFs, etc.) into GitHub's web editor while editing markdown files, GitHub hosts these files on their CDN at `github.com/user-attachments/`. These files remain publicly accessible even when used in private repositories, potentially exposing sensitive information.

## Components

### 1. GitHub Workflow (`process-attachments.yml`)

Location: `.github/workflows/process-attachments.yml`

Purpose:

- Monitors changes to markdown files (`.md`, `.mdx`, `.markdown`)
- Triggers automatically on push events
- Runs the Python script to process attachments
- Commits and pushes any changes back to the repository

Key Features:

- Runs on Ubuntu latest
- Uses Python 3.x
- Requires write permissions to repository contents
- Maintains commit history with `fetch-depth: 0`
- Uses GitHub Actions bot for commits

### 2. Python Script (`process_attachments.py`)

Location: `.github/scripts/process_attachments.py`

Purpose:

- Scans markdown files for GitHub user-attachment URLs
- Downloads referenced files to local assets directory
- Updates markdown links to reference local files
- Maintains file organization by keeping assets near their referencing documents

Supported Link Types:

1. Markdown links: `[text](https://github.com/user-attachments/...)`
2. Image links: `![alt](https://github.com/user-attachments/...)`
3. Direct URLs: `https://github.com/user-attachments/...`

Features:

- Intelligent file extension detection
- Content-type based fallback for extensions
- UUID generation for unnamed files
- Skip processing of `.git` and `node_modules` directories
- Maintains relative paths for asset references
- Error handling for failed downloads
- File deduplication (won't download same file twice)

## Workflow Process

1. **Detection**:
   - Workflow triggers when markdown files are changed
   - Python script scans modified files for user-attachment URLs

2. **Processing**:
   - For each attachment URL found:
     1. Creates an `assets` directory next to the markdown file
     2. Downloads the file if not already present
     3. Determines appropriate file extension
     4. Generates filename if none exists
     5. Updates markdown to reference local path

3. **Committing**:
   - Changes are committed using GitHub Actions bot
   - Commits only occur if files were modified
   - Changes are pushed back to the same branch

## Security Benefits

- Prevents sensitive files from remaining publicly accessible
- Maintains file privacy by moving attachments into the repository
- Keeps files under version control
- Preserves file organization with local assets directories

## Usage

The system works automatically once installed. When users:

1. Edit markdown files through GitHub's web interface
2. Drag and drop files into the editor
3. Commit their changes

The workflow will:

1. Detect the new user-attachment URLs
2. Download the files
3. Update the markdown
4. Commit the changes

No manual intervention is required after initial setup.

## Implementation Notes

- Files are stored in an `assets` directory next to each markdown file
- Original filenames are preserved when possible
- UUIDs are used for files without names
- File extensions are determined from:
  1. Original URL
  2. Content-type header
  3. Default to `.bin` if undeterminable
- Relative paths are used in markdown to maintain portability

## Limitations

- Only processes markdown files
- Requires GitHub Actions to be enabled
- Needs repository write permissions
- Cannot process files that are deleted from GitHub's CDN before the workflow runs

## Error Handling

- Failed downloads preserve original URLs
- Network timeouts are handled gracefully
- Missing dependencies trigger clear error messages
- File system errors are caught and logged

## Dependencies

- Python 3.x
- `requests` library for downloads
- GitHub Actions
