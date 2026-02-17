import json
import re
from pathlib import Path

# Read docs.json
with open('docs.json', 'r') as f:
    docs = json.load(f)

# Extract all referenced IDs
referenced_ids = set()

def extract_ids(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            extract_ids(v)
    elif isinstance(obj, list):
        for item in obj:
            extract_ids(item)
    elif isinstance(obj, str) and obj.startswith('developer-guide/'):
        parts = obj.split('/')
        if len(parts) >= 3:
            file_id = parts[-1]
            referenced_ids.add(file_id)

extract_ids(docs)

# Find all .mdx files
developer_guide_path = Path('developer-guide')
all_mdx_files = list(developer_guide_path.rglob('*.mdx'))

# Extract IDs from filenames and check if referenced
unreferenced_files = []

for mdx_file in all_mdx_files:
    rel_path = mdx_file.relative_to(developer_guide_path)
    directory = str(rel_path.parent)
    filename = mdx_file.stem
    
    if filename.isdigit():
        if filename not in referenced_ids:
            unreferenced_files.append((directory, filename, str(mdx_file)))
    else:
        unreferenced_files.append((directory, filename, str(mdx_file)))

# Read titles from frontmatter
results = []
for directory, file_id, full_path in unreferenced_files:
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Try to find title in frontmatter
            title_match = re.search(r'^---\s*\n.*?title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
            else:
                # Try alternative format
                title_match = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', content[:500])
                if title_match:
                    title = title_match.group(1).strip()
                else:
                    title = 'NO TITLE FOUND'
        results.append((directory, file_id, title))
    except Exception as e:
        results.append((directory, file_id, f'ERROR: {str(e)}'))

# Sort and write to file
results.sort(key=lambda x: (x[0], x[1]))
with open('unreferenced_output.txt', 'w') as f:
    for directory, file_id, title in results:
        f.write(f'{directory}/{file_id} - "{title}"\n')
print('Done. Results written to unreferenced_output.txt')
