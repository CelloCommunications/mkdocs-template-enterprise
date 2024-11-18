# mkdocs-template-enterprise

> CodeMap Source: Local directory: `C:\Users\shane\Dropbox\cello\git\mkdocs-template-enterprise`

This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.

## Document Table of Contents

The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.

<!-- TOC -->

- [mkdocs-template-enterprise](#mkdocs-template-enterprise)
  - [Document Table of Contents](#document-table-of-contents)
  - [Repo File Tree](#repo-file-tree)
  - [Repo File Contents](#repo-file-contents)
    - [.gitignore](#gitignore)
    - [kickstart.ps1](#kickstartps1)
    - [kickstart.sh](#kickstartsh)
    - [mkdocs.yml](#mkdocsyml)
    - [README.md](#readmemd)
    - [requirements.txt](#requirementstxt)
    - [.github/copilot-instructions.md](#githubcopilot-instructionsmd)
    - [.github/workflows/ci.yml](#githubworkflowsciyml)
    - [.vscode/settings.json](#vscodesettingsjson)
    - [docs/changelog.md](#docschangelogmd)
    - [docs/index.md](#docsindexmd)
    - [docs/guide/annotations.md](#docsguideannotationsmd)
    - [docs/guide/config.md](#docsguideconfigmd)
    - [docs/guide/grid.md](#docsguidegridmd)
    - [docs/guide/installation.md](#docsguideinstallationmd)
    - [notes/notes.md](#notesnotesmd)
    - [notes/privacy.md](#notesprivacymd)
    - [notes/token-access-enable.png](#notestoken-access-enablepng)
    - [notes/workflows.md](#notesworkflowsmd)

<!-- /TOC -->

## Repo File Tree

This file tree represents the actual structure of the repository. It's crucial for understanding the organization of the codebase.

```tree
.
├── .github/
│   ├── workflows/
│   │   ├── ci-for-non-insiders.zip
│   │   ├── ci.yml
│   │   └── ci.zip
│   └── copilot-instructions.md
├── .vscode/
│   └── settings.json
├── docs/
│   ├── guide/
│   │   ├── annotations.md
│   │   ├── config.md
│   │   ├── grid.md
│   │   ├── index.md
│   │   └── installation.md
│   ├── changelog.md
│   └── index.md
├── notes/
│   ├── notes.md
│   ├── privacy.md
│   ├── token-access-enable.png
│   └── workflows.md
├── .gitignore
├── README.md
├── kickstart.ps1
├── kickstart.sh
├── mkdocs.yml
└── requirements.txt

6 directories, 22 files
```

## Repo File Contents

The following sections present the content of each file in the repository. Large and binary files are acknowledged but their contents are not displayed.

### .gitignore

```ini
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

### kickstart.ps1

```powershell
# Check for gh CLI installation
if (gh --version 2>&1) {
  Write-Host "GitHub CLI is installed" -ForegroundColor Green
} else {
  Write-Host "GitHub CLI is not installed" -ForegroundColor Yellow
  Write-Host "To install GitHub CLI, visit: https://github.com/cli/cli#installation"
  exit 1
}

# Define the GitHub account or organization name
$githubAccount = "CelloCommunications" # Change this to your personal account name if needed

# Initialize a new git repository
git init -b main

# Get the name of the current repository from the top-level directory
$repoName = Split-Path -Leaf (git rev-parse --show-toplevel)

# Create a new repository on GitHub using the gh CLI
gh repo create $githubAccount/$repoName --private --confirm

# Add the remote repository
git remote add origin "https://github.com/$githubAccount/$repoName.git"

# Add all files in the current directory to the git repository
git add .

# Commit the changes
git commit -m "Initial commit"

# Push the changes to GitHub
git push -u origin main

# Define a hashtable where the key is the name of the secret and the value is the secret value
$secrets = @{
  "DOCKERHUB_TOKEN"    = $env:DOCKERHUB_TOKEN
  "DOCKERHUB_USERNAME" = $env:DOCKERHUB_USERNAME
  "GALAXY_API_KEY"     = $env:GALAXY_API_KEY
  # Add more secrets here as needed
}

# Check if environment variables exist
$missingVars = @()
foreach ($key in $secrets.Keys) {
  if ([string]::IsNullOrEmpty($secrets[$key])) {
    $missingVars += $key
  }
}

if ($missingVars.Count -ne 0) {
  # Print 2 blank lines here to make the output easier to read
  Write-Host "`n`nThe following environment variables are missing, but you dont have to use them:"
  foreach ($var in $missingVars) {
    Write-Host $var
  }
  Write-Host "You may add them to your $profile file or set them in the current session"
  exit 1
}

# Loop through each secret to set it for the current repository
foreach ($key in $secrets.Keys) {
  $value = $secrets[$key]
  $command = "echo -n $value | gh secret set $key --repo=$githubAccount/$repoName"
  Invoke-Expression $command
}

# Tag and push after setting the secrets
$commitMessage = "tagging initial version"
$tagVersion = "0.0.1"
$tagMessage = "Initial version"

git commit --allow-empty -m $commitMessage
git tag -a $tagVersion -m $tagMessage

# Ask the user if the current git tag and message are correct
# Print 2 blank lines here to make the output easier to read
Write-Host "`n`nThe current git tag is $tagVersion with the message '$tagMessage'. Is this correct? (yes/no)"
$answer = Read-Host

if ($answer -match "^[Yy]") {
  git push origin $tagVersion
} else {
  Write-Host "Please edit the git tag and message in this script."
}
```

### kickstart.sh

```bash
#!/bin/bash

# Define color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check for gh CLI installation
if command -v gh &>/dev/null; then
  echo -e "${GREEN}GitHub CLI is installed${NC}"
else
  echo -e "${YELLOW}GitHub CLI is not installed${NC}"
  echo "To install GitHub CLI, visit: https://github.com/cli/cli#installation"
  exit 1
fi

# Define the GitHub account or organization name
githubAccount="CelloCommunications" # Change this to your personal account name if needed

# Initialize a new git repository
git init -b main

# Get the name of the current repository from the top-level directory
repoName=$(basename "$(git rev-parse --show-toplevel)")

# Create a new repository on GitHub using the gh CLI
gh repo create "$githubAccount/$repoName" --private --confirm

# Add the remote repository
git remote add origin "https://github.com/$githubAccount/$repoName.git"

# Add all files in the current directory to the git repository
git add .

# Commit the changes
git commit -m "Initial commit"

# Push the changes to GitHub
git push -u origin main

# Define an associative array where the key is the name of the secret and the value is the secret value
declare -A secrets
secrets=(
  ["DOCKERHUB_TOKEN"]="$DOCKERHUB_TOKEN"
  ["DOCKERHUB_USERNAME"]="$DOCKERHUB_USERNAME"
  ["GALAXY_API_KEY"]="$GALAXY_API_KEY"
  # Add more secrets here as needed
)

# Check if environment variables exist
missingVars=()
for key in "${!secrets[@]}"; do
  if [ -z "${secrets[$key]}" ]; then
    missingVars+=("$key")
  fi
done

if [ ${#missingVars[@]} -ne 0 ]; then
  # Print 2 blank lines here to make the output easier to read
  echo -e "\n\nThe following environment variables are missing, but you dont have to use them:"
  for var in "${missingVars[@]}"; do
    echo "$var"
  done
  echo "You may add them to your .bashrc file or set them in the current session"
  exit 1
fi

# Loop through each secret to set it for the current repository
for key in "${!secrets[@]}"; do
  value=${secrets[$key]}
  command="echo -n $value | gh secret set $key --repo=$githubAccount/$repoName"
  eval "$command"
done

# Tag and push after setting the secrets
commitMessage="tagging initial version"
tagVersion="0.0.1"
tagMessage="Initial version"

git commit --allow-empty -m "$commitMessage"
git tag -a $tagVersion -m "$tagMessage"

# Ask the user if the current git tag and message are correct
# Print 2 blank lines here to make the output easier to read
echo -e "\n\nThe current git tag is $tagVersion with the message '$tagMessage'. Is this correct? (yes/no)"
read -r answer

if [ "$answer" != "${answer#[Yy]}" ]; then
  git push origin $tagVersion
else
  echo "Please edit the git tag and message in this script."
fi
```

### mkdocs.yml

```yml
# Project information
site_name: Mkdocs Material Example
site_description: Just a tester

# Repository
repo_name: cellocommunications/mkdocs-material-example
repo_url: https://github.com/CelloCommunications/mkdocs-template-enterprise
edit_uri: blob/main/docs/

# Copyright
copyright: Copyright &copy; cellocommunications

# nav:
#   - Welcome: index.md
#   - User Guide:
#       - guide/index.md
#       - Installation: guide/installation.md
#       - Basics: guide/basics.md
#       - Configuration: guide/config.md
#   - Changelog: changelog.md

theme:
  name: material
  features:
    - content.tooltips
    - content.action.edit
    - content.action.meta
    - content.action.view
    - header.autohide
    - navigation.instant
    - navigation.tracking
    - content.code.annotate
    - toc.integrate
    - toc.follow
    - navigation.path
    - navigation.top
    - navigation.tabs
    - navigation.footer
    - content.code.copy
    - content.footnote.tooltips
  icon:
    repo: fontawesome/brands/github
  palette:
    # Palette toggle for light mode
    - media: '(prefers-color-scheme: light)'
      scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
      primary: indigo
      accent: indigo

    # Palette toggle for dark mode
    - media: '(prefers-color-scheme: dark)'
      scheme: slate
      primary: black
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

markdown_extensions:
  - abbr
  - attr_list
  - md_in_html
  - admonition
  - def_list
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.critic
  - pymdownx.caret
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.tilde
  - pymdownx.details
  - pymdownx.keys
  - pymdownx.blocks.caption
  - pymdownx.superfences
    # custom_fences:
    #   - name: mermaid
    #     class: mermaid
    #     format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - tables
  - footnotes
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg

plugins:
  - search
  - tags
  # - meta

extra_css:
  - static/extra.css
```

### README.md

````markdown
# MkDocs Template

[![ci](https://github.com/CelloCommunications/mkdocs-template-enterprise/actions/workflows/ci.yml/badge.svg)](https://github.com/CelloCommunications/mkdocs-template-enterprise/actions/workflows/ci.yml)

[[toc]]

## Default Deployment Location

View doc output here:

```txt
https://<username>.github.io/<repository-name>
```

<https://cellocommunications.github.io/mkdocs-template-enterprise/>

## Private Pages Configuration

Configure GitHub Pages for private access, restricting it to organization members only.

[privacy](notes/privacy.md)

## Workflow Concepts

Workflow concepts for managing documentation with GitHub Pages with more advanced features.

[workflows](notes/workflows.md)

## CoPilot Instructions

Your Copilot preferences are set via concise plain language instructions here.

[copilot](.github/copilot-instructions.md)
````

### requirements.txt

```ini
mkdocs-material
```

### .github/copilot-instructions.md

````markdown
# CoPilot Instructions

## Conventional Commits

- We always use the "Conventional Commits" standards when writing commit messages. This helps us automate the release process and generate changelogs.
    - Use Conventional Commit messages.
    - Use Conventional Commit standards.
````

### .github/workflows/ci.yml

```yml
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
          name: github-pages # Explicit artifact name

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
        with:
          artifact_name: github-pages # Match the upload name
```

### .vscode/settings.json

```json
{
  "yaml.schemas": {
    "https://json.schemastore.org/mkdocs-1.6.json": "file:///c%3A/Users/shane/git/mkdocs-material-example/mkdocs.yml"
  },
  "cSpell.words": [
    "adipiscing",
    "amet",
    "auctor",
    "consectetur",
    "consequat",
    "Curabitur",
    "cursus",
    "elit",
    "euismod",
    "feugiat",
    "finibus",
    "justo",
    "nulla",
    "Nulla",
    "Phasellus",
    "posuere",
    "tortor"
  ]
}
```

### docs/changelog.md

````markdown
# Changelog

This is the changelog page of this project. More details please check the github repo.
````

### docs/index.md

````markdown
# Welcome to MkDocs Test

Repo is here [mkdocs-template-enterprise](https://github.com/CelloCommunications/mkdocs-template-enterprise).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.
* yadda yadda yadda

Image test:

![GVLIUhUW4AAJHD-](https://github.com/user-attachments/assets/8bb21993-a551-4d2d-8dab-a77d493b47da)

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
````

### docs/guide/annotations.md

````markdown
---
icon: material/alert-outline
---

# Admonitions

Admonitions, also known as _call-outs_, are an excellent choice for including
side content without significantly interrupting the document flow. Material for
MkDocs provides several different types of admonitions and allows for the
inclusion and nesting of arbitrary content.

## Configuration

This configuration enables admonitions, allows to make them collapsible and to
nest arbitrary content inside admonitions. Add the following lines to
`mkdocs.yml`:

``` yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

### Admonition icons

<!-- md:version 8.3.0 -->

Each of the supported admonition types has a distinct icon, which can be changed
to any icon bundled with the theme, or even a [custom icon]. Add the following
lines to `mkdocs.yml`:

``` yaml
theme:
  icon:
    admonition:
      <type>: <icon> # (1)!
```

1. Enter a few keywords to find the perfect icon using our [icon search] and
    click on the shortcode to copy it to your clipboard:

    <div class="mdx-iconsearch" data-mdx-component="iconsearch">
      <input class="md-input md-input--stretch mdx-iconsearch__input" placeholder="Search icon" data-mdx-component="iconsearch-query" value="alert" />
      <div class="mdx-iconsearch-result" data-mdx-component="iconsearch-result" data-mdx-mode="file">
        <div class="mdx-iconsearch-result__meta"></div>
        <ol class="mdx-iconsearch-result__list"></ol>
      </div>
    </div>

??? example "Expand to show alternate icon sets"

    === ":octicons-mark-github-16: Octicons"

        ``` yaml
        theme:
          icon:
            admonition:
              note: octicons/tag-16
              abstract: octicons/checklist-16
              info: octicons/info-16
              tip: octicons/squirrel-16
              success: octicons/check-16
              question: octicons/question-16
              warning: octicons/alert-16
              failure: octicons/x-circle-16
              danger: octicons/zap-16
              bug: octicons/bug-16
              example: octicons/beaker-16
              quote: octicons/quote-16
        ```


    === ":fontawesome-brands-font-awesome: FontAwesome"

        ``` yaml
        theme:
          icon:
            admonition:
              note: fontawesome/solid/note-sticky
              abstract: fontawesome/solid/book
              info: fontawesome/solid/circle-info
              tip: fontawesome/solid/bullhorn
              success: fontawesome/solid/check
              question: fontawesome/solid/circle-question
              warning: fontawesome/solid/triangle-exclamation
              failure: fontawesome/solid/bomb
              danger: fontawesome/solid/skull
              bug: fontawesome/solid/robot
              example: fontawesome/solid/flask
              quote: fontawesome/solid/quote-left
        ```

  [icon search]: icons-emojis.md#search

## Usage

Admonitions follow a simple syntax: a block starts with `!!!`, followed by a
single keyword used as a [type qualifier]. The content of the block follows on
the next line, indented by four spaces:

``` markdown title="Admonition"
!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

  [type qualifier]: #supported-types

### Changing the title

By default, the title will equal the type qualifier in titlecase. However, it
can be changed by adding a quoted string containing valid Markdown (including
links, formatting, ...) after the type qualifier:

``` markdown title="Admonition with custom title"
!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note "Phasellus posuere in sem ut cursus"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

### Removing the title

Similar to [changing the title], the icon and title can be omitted entirely by
adding an empty string directly after the type qualifier. Note that this will
not work for [collapsible blocks]:

``` markdown title="Admonition without title"
!!! note ""

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note ""

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

  [changing the title]: #changing-the-title
  [collapsible blocks]: #collapsible-blocks

### Collapsible blocks

When [Details] is enabled and an admonition block is started with `???` instead
of `!!!`, the admonition is rendered as a collapsible block with a small toggle
on the right side:

``` markdown title="Admonition, collapsible"
??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

Adding a `+` after the `???` token renders the block expanded:

``` markdown title="Admonition, collapsible and initially expanded"
???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

???+ note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

### Inline blocks

Admonitions can also be rendered as inline blocks (e.g., for sidebars), placing
them to the right using the `inline` + `end` modifiers, or to the left using
only the `inline` modifier:

=== ":octicons-arrow-right-16: inline end"

    !!! info inline end "Lorem ipsum"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

    ``` markdown
    !!! info inline end "Lorem ipsum"

        Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Nulla et euismod nulla.
        Curabitur feugiat, tortor non consequat
        finibus, justo purus auctor massa, nec
        semper lorem quam in massa.
    ```

    Use `inline end` to align to the right (left for rtl languages).

=== ":octicons-arrow-left-16: inline"

    !!! info inline "Lorem ipsum"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

    ``` markdown
    !!! info inline "Lorem ipsum"

        Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Nulla et euismod nulla.
        Curabitur feugiat, tortor non consequat
        finibus, justo purus auctor massa, nec
        semper lorem quam in massa.
    ```

    Use `inline` to align to the left (right for rtl languages).

__Important__: admonitions that use the `inline` modifiers _must_ be declared
prior to the content block you want to place them beside. If there's
insufficient space to render the admonition next to the block, the admonition
will stretch to the full width of the viewport, e.g., on mobile view ports.

### Supported types

Following is a list of type qualifiers provided by Material for MkDocs, whereas
the default type, and thus fallback for unknown type qualifiers, is `note`[^1]:

  [^1]:
    Previously, some of the supported types defined more than one qualifier.
    For example, authors could use `summary` or `tldr` as alternative qualifiers
    to render an [`abstract`](#+type:abstract) admonition. As this increased the
    size of the CSS that is shipped with Material for MkDocs, the additional
    type qualifiers are now all deprecated and will be removed in the next major
    version. This will also be mentioned in the upgrade guide.

<!-- md:option type:note -->

:   !!! note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:abstract -->

:   !!! abstract

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:info -->

:   !!! info

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:tip -->

:   !!! tip

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:success -->

:   !!! success

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:question -->

:   !!! question

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:warning -->

:   !!! warning

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:failure -->

:   !!! failure

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:danger -->

:   !!! danger

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:bug -->

:   !!! bug

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:example -->

:   !!! example

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

<!-- md:option type:quote -->

:   !!! quote

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
        euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
        purus auctor massa, nec semper lorem quam in massa.

## Customization

### Classic admonitions

Prior to version <!-- md:version 8.5.6 -->, admonitions had a slightly
different appearance:

!!! classic "Note"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

If you want to restore this appearance, add the following CSS to an
[additional style sheet]:

<style>
  .md-typeset .admonition.classic {
    border-width: 0;
    border-left-width: 4px;
  }
</style>

=== ":octicons-file-code-16: `docs/stylesheets/extra.css`"

    ``` css
    .md-typeset .admonition,
    .md-typeset details {
      border-width: 0;
      border-left-width: 4px;
    }
    ```

=== ":octicons-file-code-16: `mkdocs.yml`"

    ``` yaml
    extra_css:
      - stylesheets/extra.css
    ```

### Custom admonitions

If you want to add a custom admonition type, all you need is a color and an
`*.svg` icon. Copy the icon's code from the [`.icons`][custom icons] folder
and add the following CSS to an [additional style sheet]:

<style>
  :root {
    --md-admonition-icon--pied-piper: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M244 246c-3.2-2-6.3-2.9-10.1-2.9-6.6 0-12.6 3.2-19.3 3.7l1.7 4.9zm135.9 197.9c-19 0-64.1 9.5-79.9 19.8l6.9 45.1c35.7 6.1 70.1 3.6 106-9.8-4.8-10-23.5-55.1-33-55.1zM340.8 177c6.6 2.8 11.5 9.2 22.7 22.1 2-1.4 7.5-5.2 7.5-8.6 0-4.9-11.8-13.2-13.2-23 11.2-5.7 25.2-6 37.6-8.9 68.1-16.4 116.3-52.9 146.8-116.7C548.3 29.3 554 16.1 554.6 2l-2 2.6c-28.4 50-33 63.2-81.3 100-31.9 24.4-69.2 40.2-106.6 54.6l-6.3-.3v-21.8c-19.6 1.6-19.7-14.6-31.6-23-18.7 20.6-31.6 40.8-58.9 51.1-12.7 4.8-19.6 10-25.9 21.8 34.9-16.4 91.2-13.5 98.8-10zM555.5 0l-.6 1.1-.3.9.6-.6zm-59.2 382.1c-33.9-56.9-75.3-118.4-150-115.5l-.3-6c-1.1-13.5 32.8 3.2 35.1-31l-14.4 7.2c-19.8-45.7-8.6-54.3-65.5-54.3-14.7 0-26.7 1.7-41.4 4.6 2.9 18.6 2.2 36.7-10.9 50.3l19.5 5.5c-1.7 3.2-2.9 6.3-2.9 9.8 0 21 42.8 2.9 42.8 33.6 0 18.4-36.8 60.1-54.9 60.1-8 0-53.7-50-53.4-60.1l.3-4.6 52.3-11.5c13-2.6 12.3-22.7-2.9-22.7-3.7 0-43.1 9.2-49.4 10.6-2-5.2-7.5-14.1-13.8-14.1-3.2 0-6.3 3.2-9.5 4-9.2 2.6-31 2.9-21.5 20.1L15.9 298.5c-5.5 1.1-8.9 6.3-8.9 11.8 0 6 5.5 10.9 11.5 10.9 8 0 131.3-28.4 147.4-32.2 2.6 3.2 4.6 6.3 7.8 8.6 20.1 14.4 59.8 85.9 76.4 85.9 24.1 0 58-22.4 71.3-41.9 3.2-4.3 6.9-7.5 12.4-6.9.6 13.8-31.6 34.2-33 43.7-1.4 10.2-1 35.2-.3 41.1 26.7 8.1 52-3.6 77.9-2.9 4.3-21 10.6-41.9 9.8-63.5l-.3-9.5c-1.4-34.2-10.9-38.5-34.8-58.6-1.1-1.1-2.6-2.6-3.7-4 2.2-1.4 1.1-1 4.6-1.7 88.5 0 56.3 183.6 111.5 229.9 33.1-15 72.5-27.9 103.5-47.2-29-25.6-52.6-45.7-72.7-79.9zm-196.2 46.1v27.2l11.8-3.4-2.9-23.8zm-68.7-150.4l24.1 61.2 21-13.8-31.3-50.9zm84.4 154.9l2 12.4c9-1.5 58.4-6.6 58.4-14.1 0-1.4-.6-3.2-.9-4.6-26.8 0-36.9 3.8-59.5 6.3z"/></svg>')
  }
  .md-typeset .admonition.pied-piper,
  .md-typeset details.pied-piper {
    border-color: rgb(43, 155, 70);
  }
  .md-typeset .pied-piper > .admonition-title,
  .md-typeset .pied-piper > summary {
    background-color: rgba(43, 155, 70, 0.1);
  }
  .md-typeset .pied-piper > .admonition-title::before,
  .md-typeset .pied-piper > summary::before {
    background-color: rgb(43, 155, 70);
    -webkit-mask-image: var(--md-admonition-icon--pied-piper);
            mask-image: var(--md-admonition-icon--pied-piper);
  }
</style>

=== ":octicons-file-code-16: `docs/stylesheets/extra.css`"

    ``` css
    :root {
      --md-admonition-icon--pied-piper: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M244 246c-3.2-2-6.3-2.9-10.1-2.9-6.6 0-12.6 3.2-19.3 3.7l1.7 4.9zm135.9 197.9c-19 0-64.1 9.5-79.9 19.8l6.9 45.1c35.7 6.1 70.1 3.6 106-9.8-4.8-10-23.5-55.1-33-55.1zM340.8 177c6.6 2.8 11.5 9.2 22.7 22.1 2-1.4 7.5-5.2 7.5-8.6 0-4.9-11.8-13.2-13.2-23 11.2-5.7 25.2-6 37.6-8.9 68.1-16.4 116.3-52.9 146.8-116.7C548.3 29.3 554 16.1 554.6 2l-2 2.6c-28.4 50-33 63.2-81.3 100-31.9 24.4-69.2 40.2-106.6 54.6l-6.3-.3v-21.8c-19.6 1.6-19.7-14.6-31.6-23-18.7 20.6-31.6 40.8-58.9 51.1-12.7 4.8-19.6 10-25.9 21.8 34.9-16.4 91.2-13.5 98.8-10zM555.5 0l-.6 1.1-.3.9.6-.6zm-59.2 382.1c-33.9-56.9-75.3-118.4-150-115.5l-.3-6c-1.1-13.5 32.8 3.2 35.1-31l-14.4 7.2c-19.8-45.7-8.6-54.3-65.5-54.3-14.7 0-26.7 1.7-41.4 4.6 2.9 18.6 2.2 36.7-10.9 50.3l19.5 5.5c-1.7 3.2-2.9 6.3-2.9 9.8 0 21 42.8 2.9 42.8 33.6 0 18.4-36.8 60.1-54.9 60.1-8 0-53.7-50-53.4-60.1l.3-4.6 52.3-11.5c13-2.6 12.3-22.7-2.9-22.7-3.7 0-43.1 9.2-49.4 10.6-2-5.2-7.5-14.1-13.8-14.1-3.2 0-6.3 3.2-9.5 4-9.2 2.6-31 2.9-21.5 20.1L15.9 298.5c-5.5 1.1-8.9 6.3-8.9 11.8 0 6 5.5 10.9 11.5 10.9 8 0 131.3-28.4 147.4-32.2 2.6 3.2 4.6 6.3 7.8 8.6 20.1 14.4 59.8 85.9 76.4 85.9 24.1 0 58-22.4 71.3-41.9 3.2-4.3 6.9-7.5 12.4-6.9.6 13.8-31.6 34.2-33 43.7-1.4 10.2-1 35.2-.3 41.1 26.7 8.1 52-3.6 77.9-2.9 4.3-21 10.6-41.9 9.8-63.5l-.3-9.5c-1.4-34.2-10.9-38.5-34.8-58.6-1.1-1.1-2.6-2.6-3.7-4 2.2-1.4 1.1-1 4.6-1.7 88.5 0 56.3 183.6 111.5 229.9 33.1-15 72.5-27.9 103.5-47.2-29-25.6-52.6-45.7-72.7-79.9zm-196.2 46.1v27.2l11.8-3.4-2.9-23.8zm-68.7-150.4l24.1 61.2 21-13.8-31.3-50.9zm84.4 154.9l2 12.4c9-1.5 58.4-6.6 58.4-14.1 0-1.4-.6-3.2-.9-4.6-26.8 0-36.9 3.8-59.5 6.3z"/></svg>')
    }
    .md-typeset .admonition.pied-piper,
    .md-typeset details.pied-piper {
      border-color: rgb(43, 155, 70);
    }
    .md-typeset .pied-piper > .admonition-title,
    .md-typeset .pied-piper > summary {
      background-color: rgba(43, 155, 70, 0.1);
    }
    .md-typeset .pied-piper > .admonition-title::before,
    .md-typeset .pied-piper > summary::before {
      background-color: rgb(43, 155, 70);
      -webkit-mask-image: var(--md-admonition-icon--pied-piper);
              mask-image: var(--md-admonition-icon--pied-piper);
    }
    ```

=== ":octicons-file-code-16: `mkdocs.yml`"

    ``` yaml
    extra_css:
      - stylesheets/extra.css
    ```

After applying the customization, you can use the custom admonition type:

``` markdown title="Admonition with custom type"
!!! pied-piper "Pied Piper"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! pied-piper "Pied Piper"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>
````

### docs/guide/config.md

````markdown
# Config

None to speak of yet ...
````

### docs/guide/grid.md

````markdown
---
icon: material/view-grid-plus
---

# Grids

Material for MkDocs makes it easy to arrange sections into grids, grouping
blocks that convey similar meaning or are of equal importance. Grids are just
perfect for building index pages that show a brief overview of a large section
of your documentation.

## Configuration

This configuration enables the use of grids, allowing to bring blocks of
identical or different types into a rectangular shape. Add the following lines
to `mkdocs.yml`:

``` yaml
markdown_extensions: # (1)!
  - attr_list
  - md_in_html
```

1. Note that some of the examples listed below use [icons and emojis], which
    have to be [configured separately].

See additional configuration options:

- [Attribute Lists]
- [Markdown in HTML]

  [icons and emojis]: #
  [configured separately]: #
  [Attribute Lists]: #
  [Markdown in HTML]: #

## Usage

Grids come in two flavors: [card grids], which wrap each element in a card that
levitates on hover, and [generic grids], which allow to arrange arbitrary block
elements in a rectangular shape.

  [card grids]: #using-card-grids
  [generic grids]: #using-generic-grids

### Using card grids

<!-- md:version 9.5.0 -->
<!-- md:flag experimental -->

Card grids wrap each grid item with a beautiful hover card that levitates on
hover. They come in two slightly different syntaxes: [list] and [block syntax],
adding support for distinct use cases.

  [list]: #list-syntax
  [block syntax]: #block-syntax

#### List syntax

The list syntax is essentially a shortcut for [card grids], and consists of an
unordered (or ordered) list wrapped by a `div` with both, the `grid` and `cards`
classes:

``` html title="Card grid"
<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

<div class="result" markdown>
  <div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

  </div>

</div>

List elements can contain arbitrary Markdown, as long as the surrounding `div`
defines the `markdown` attribute. Following is a more complex example, which
includes icons and links:

``` html title="Card grid, complex example"
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>
```

<div class="result" markdown>
  <div class="grid cards" markdown>

- :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`][mkdocs-material] with [`pip`][pip] and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started][getting started]

- :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference][reference]

- :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization][customization]

- :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License][license]

  </div>

</div>

If there's insufficient space to render grid items next to each other, the items
will stretch to the full width of the viewport, e.g. on mobile viewports. If
there's more space available, grids will render in items of 3 and more, e.g.
when [hiding both sidebars].

  [mkdocs-material]: https://pypistats.org/packages/mkdocs-material
  [pip]: #
  [getting started]: #
  [reference]: #
  [customization]: #
  [license]: #
  [GitHub]: #
  [hiding both sidebars]: #

#### Block syntax

The block syntax allows for arranging cards in grids __together with other
elements__, as explained in the section on [generic grids]. Just add the `card`
class to any block element inside a `grid`:

``` html title="Card grid, blocks"
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

<div class="result" markdown>
  <div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

  </div>
</div>

While this syntax may seem unnecessarily verbose at first, the previous example
shows how card grids can now be mixed with other elements that will also stretch
to the grid.

### Using generic grids

<!-- md:version 9.5.0 -->
<!-- md:flag experimental -->

Generic grids allow for arranging arbitrary block elements in a grid, including
[admonitions], [code blocks], [content tabs] and more. Just wrap a set of blocks
by using a `div` with the `grid` class:

```` html title="Generic grid"
<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>
````

<div class="result" markdown>
  <div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

  </div>
</div>

  [admonitions]: #
  [code blocks]: #
  [content tabs]: #
````

### docs/guide/index.md

````markdown
# Get Started

This is the get started tutorial.
````

### docs/guide/installation.md

````markdown
# Installation
````

### notes/notes.md

````markdown
# Notes

[[toc]]

## GitHub Copilot

<https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot>

## GitHub Repo Sizes

GitHub recommends keeping repositories small, ideally under 1 GB and strongly under 5 GB. Smaller repositories are easier to work with, maintain, and clone.

* [](https://docs.github.com/repositories/working-with-files/managing-large-files/about-large-files-on-github)

    About large files on GitHub

    Repository size limits We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended.

* **Push size**

    The maximum push size is 2 GB.

    * [](https://docs.github.com/en/get-started/using-git/troubleshooting-the-2-gb-push-limit#:~:text=Troubleshooting%20the%202%20GB%20push%20limit%20%2D%20GitHub%20Docs.)

        Troubleshooting the 2 GB push limit - GitHub Docs

        Troubleshooting the 2 GB push limit - GitHub Docs.

        GitHub Docs

* **Commit listings**

    The compare view and pull requests pages limit the number of commits displayed to 250. The Commits tab limits the number of commits displayed to 10,000.

    * [](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)

        Repository limits - GitHub Docs

        Commit listings limits The compare view and pull requests pages display a list of commits between the base and head revisions. The...

        GitHub Docs

* **GitHub Pages**

    The recommended limit for source repositories is 1 GB, and the maximum size for published sites is also 1 GB.

    * [link](https://docs.github.com/en/enterprise-server@3.13/pages/getting-started-with-github-pages/about-github-pages#:~:text=GitHub%20Pages%20source%20repositories%20have,no%20larger%20than%201%20GB.)

    * [link](https://docs.github.com/repositories/working-with-files/managing-large-files/about-large-files-on-github)

    About large files on GitHub

    Repository size limits We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended.

<https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github>

## MkDocs Material Insiders

<https://squidfunk.github.io/mkdocs-material/insiders/getting-started/>

<https://github.com/sponsors/squidfunk?success=true>

## Confirm Invitation to Insiders Program

<https://github.com/squidfunk/mkdocs-material-insiders/invitations> and accept the invitation.

## Steps to Add GitHub Personal Access Token (PAT)

For a GitHub "organization" we firstly need to enable token access org wide here:

<https://github.com/organizations/CelloCommunications/settings/personal-access-tokens-onboarding>

![Token Access Enable](token-access-enable.png)

<https://github.com/settings/tokens/new>

Once thats enabled, we can create a token for the repo here:

<https://github.com/organizations/CelloCommunications/settings/personal-access-tokens/active>

1. **Create Personal Access Token**
   * Go to GitHub Settings → Developer Settings → Personal Access Tokens
   * Click "Generate new token (classic)"
   * Note/Name: `MKDOCS_MATERIAL_INSIDERS`
   * Select scopes:
     * `repo` (full control)
   * Generate token and copy it

2. **Add Secret to Repository**
   * Go to repository Settings <https://github.com/cellocommunications/mkdocs-material-example/settings/secrets/actions>
   * Navigate to Security → Secrets and variables → Actions
   * Click "New repository secret"
   * Name: `GH_TOKEN`
   * Value: *paste your PAT*
   * Click "Add secret"

3. **Verify Workflow Access**
   * The workflow already references the secret correctly:

    ```yaml
    env:
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
    ```

4. **Commit Message for Documentation**

```txt
docs(ci): add instructions for GitHub token setup
```
````

### notes/privacy.md

````markdown

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
````

### notes/token-access-enable.png

```txt
[Large or binary file detected. File Type: image/png, Size: 334686 bytes]
```

### notes/workflows.md

````markdown
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
````

> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.