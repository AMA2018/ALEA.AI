#!/bin/bash

# Make sure git-filter-repo can be found
FILTER_REPO="./git-filter-repo"
if [ ! -f "$FILTER_REPO" ]; then
    echo "git-filter-repo not found. Please make sure it is in the current directory."
    exit 1
fi

# Create a mapping file directly
echo "Creating new commit messages..."
MAPPING_FILE=$(mktemp)

# Get all commits
git log --format="%H" > all_commits.txt

# Create message mapping
while read -r commit_hash; do
    message=$(python3 rewrite_commits.py)
    echo "$commit_hash $message" >> "$MAPPING_FILE"
done < all_commits.txt

# Display a sample
echo "Sample of new commit messages:"
head -5 "$MAPPING_FILE"

# Run git-filter-repo
echo "Rewriting Git history..."
$FILTER_REPO --force --message-callback "
# Load the mapping
mapping = {}
with open('$MAPPING_FILE', 'r') as f:
    for line in f:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            mapping[parts[0]] = parts[1]

# Return the new message or keep the original
commit_id = commit.original_id.decode('utf-8')
if commit_id in mapping:
    return mapping[commit_id].encode('utf-8')
return commit.message
"

# Clean up
rm "$MAPPING_FILE" all_commits.txt

echo "History has been successfully rewritten!" 