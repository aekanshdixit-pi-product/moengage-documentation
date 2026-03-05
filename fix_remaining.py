#!/usr/bin/env python3
"""Fix the remaining 6 MDX errors."""
import os

os.chdir('/Users/mallikarjun.dhulange/Documents/moengage-documentation')

# 1. Fix jinja-templating-language.mdx
path = 'user-guide/campaigns-and-channels/message-personalization/jinja-templating-language.mdx'
with open(path) as f:
    content = f.read()
content = content.replace('*{{*', '*`{{`*')
with open(path, 'w') as f:
    f.write(content)
print('Fixed jinja')

# 2. Fix create/create-a-card-campaign.mdx
path2 = 'user-guide/campaigns-and-channels/create/create-a-card-campaign.mdx'
with open(path2) as f:
    content2 = f.read()
old = '   <Info>\nYou can use key-value pairs to add additional information to the deep linking or Rich landing URLs.\n</Info> |'
new = ' **Note:** You can use key-value pairs to add additional information to the deep linking or Rich landing URLs. |'
content2 = content2.replace(old, new)
with open(path2, 'w') as f:
    f.write(content2)
print('Fixed create/create-a-card-campaign')

# 3. Fix cards/create-a-card-campaign.mdx - Accordion in list item
path3 = 'user-guide/campaigns-and-channels/cards/create-a-card-campaign.mdx'
with open(path3) as f:
    lines = f.readlines()
for i in range(len(lines)):
    if 'Test campaign (Optional)' in lines[i] and '<Accordion' in lines[i]:
        lines[i] = lines[i].lstrip()
        break
with open(path3, 'w') as f:
    f.writelines(lines)
print('Fixed cards/create-a-card-campaign')

# 4. Fix inspiration-library
path4 = 'user-guide/intelligence/merlin-ai-jinja-generator/inspiration-library-for-merlin-ai-jinja-assistant.mdx'
with open(path4) as f:
    content4 = f.read()
# Replace triple backtick code blocks inside table cells with inline code
lines4 = content4.split('\n')
for i in range(len(lines4)):
    line = lines4[i]
    if line.startswith('|') and '```' in line:
        line = line.replace(' ``` ', ' `')
        line = line.replace(' ```', ' `')
        line = line.replace('``` ', '` ')
        lines4[i] = line
content4 = '\n'.join(lines4)
with open(path4, 'w') as f:
    f.write(content4)
print('Fixed inspiration-library')

# 5. Fix create-alert.mdx - Accordion nested incorrectly
path5 = 'user-guide/inform/create/create-alert.mdx'
with open(path5) as f:
    content5 = f.read()
# The issue: <Accordion> inside a list item. Ensure proper nesting.
# The Accordion starting with "If you select iOS..." is nested inside the 
# parent Accordion. Need to ensure proper indentation.
old5 = '    <Accordion title="If you select iOS in Target Platforms for Push, the following options are available:">'
if old5 not in content5:
    # Try without the 4 spaces
    content5 = content5.replace(
        '<Accordion title="If you select iOS in Target Platforms for Push, the following options are available:">',
        '</Accordion>\n\n  <Accordion title="If you select iOS in Target Platforms for Push, the following options are available:">'
    )
with open(path5, 'w') as f:
    f.write(content5)
print('Fixed create-alert')

# 6. Same for new-ui-experience
path6 = 'user-guide/inform/new-ui-experience/create-alert.mdx'
with open(path6) as f:
    content6 = f.read()
content6 = content6.replace(
    '<Accordion title="If you select iOS in Target Platforms for Push, the following options are available:">',
    '</Accordion>\n\n  <Accordion title="If you select iOS in Target Platforms for Push, the following options are available:">'
)
with open(path6, 'w') as f:
    f.write(content6)
print('Fixed new-ui-experience/create-alert')
