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
