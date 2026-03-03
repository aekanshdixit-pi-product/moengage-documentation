#!/usr/bin/env python3
"""Fix remaining MDX syntax errors - Phase 2.

Handles:
1. Curly braces (acorn errors): {{...}} Jinja patterns
2. Standalone { and } characters
3. <> empty angle brackets
4. <PlaceholderText> that looks like JSX tags
5. Inline components on same line as content
6. Components in table cells
"""
import os
import re

def is_in_code_context(line, pos):
    """Check if position is inside backtick span or code block indicator."""
    backtick_count = 0
    in_backtick = False
    for i in range(pos):
        if line[i] == '`':
            in_backtick = not in_backtick
    return in_backtick


def fix_jinja_curlies(filepath):
    """Wrap {{...}} Jinja patterns in backtick code spans."""
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')
    in_code_block = False
    in_frontmatter = False
    fm_count = 0

    for idx in range(len(lines)):
        line = lines[idx]

        if line.strip() == '---':
            fm_count += 1
            if fm_count <= 2:
                in_frontmatter = fm_count == 1
                if fm_count == 2:
                    in_frontmatter = False
                continue

        if in_frontmatter:
            continue

        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if '{{' not in line:
            continue

        new_line = _wrap_jinja_in_backticks(line)
        if new_line != line:
            lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def _wrap_jinja_in_backticks(line):
    """Wrap {{...}} patterns in backticks, preserving existing backtick spans."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            j = i + 1
            while j < len(line) and line[j] != '`':
                j += 1
            if j < len(line):
                result.append(line[i:j+1])
                i = j + 1
            else:
                result.append(line[i:])
                break
        elif line[i:i+2] == '{{':
            close = line.find('}}', i + 2)
            if close >= 0:
                expr = line[i:close+2]
                # Check if there's a nested }} (like default("{{...}}")}})
                remaining = line[close+2:]
                if remaining.startswith('}}'):
                    expr = line[i:close+4]
                    close += 2
                result.append('`' + expr + '`')
                i = close + 2
            else:
                result.append(line[i])
                i += 1
        else:
            j = i
            while j < len(line) and line[j] != '`' and line[j:j+2] != '{{':
                j += 1
            result.append(line[i:j])
            i = j

    return ''.join(result)


def fix_standalone_braces(filepath):
    """Fix standalone { and } characters that MDX interprets as expressions."""
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')
    in_code_block = False
    fm_count = 0

    for idx in range(len(lines)):
        line = lines[idx]

        if line.strip() == '---':
            fm_count += 1
            continue

        if fm_count < 2:
            continue

        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if '{' not in line and '}' not in line:
            continue

        # Skip lines that have {{ (handled by jinja fixer)
        if '{{' in line or '}}' in line:
            continue

        # Skip lines where braces are inside backticks
        # Find standalone { or } that aren't in backtick spans
        new_line = _escape_standalone_braces(line)
        if new_line != line:
            lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def _escape_standalone_braces(line):
    """Escape standalone { and } in a line, preserving backtick spans."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            j = i + 1
            while j < len(line) and line[j] != '`':
                j += 1
            if j < len(line):
                result.append(line[i:j+1])
                i = j + 1
            else:
                result.append(line[i:])
                break
        elif line[i] == '{':
            # Check if this is part of a JSX expression or component attribute
            # For safety, only escape if the brace appears to be standalone text
            # Look at surrounding context
            before = line[:i].rstrip()
            if before.endswith('-') or before.endswith('|') or i == 0 or line[i-1] == ' ':
                result.append("\\{")
                i += 1
            else:
                result.append(line[i])
                i += 1
        elif line[i] == '}':
            before = line[:i].rstrip()
            after = line[i+1:].lstrip() if i + 1 < len(line) else ''
            if not after or after[0] in (' ', '\n', '\r') or after.startswith('right') or after.startswith('/'):
                result.append("\\}")
                i += 1
            else:
                result.append(line[i])
                i += 1
        else:
            j = i
            while j < len(line) and line[j] not in ('`', '{', '}'):
                j += 1
            result.append(line[i:j])
            i = j
    return ''.join(result)


def fix_empty_angle_brackets(filepath):
    """Fix <> in content that MDX interprets as JSX fragment."""
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')
    in_code_block = False

    for idx in range(len(lines)):
        line = lines[idx]

        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if '<>' not in line:
            continue

        # Replace <> with &lt;&gt; but not inside backticks
        new_line = _fix_empty_brackets_in_line(line)
        if new_line != line:
            lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def _fix_empty_brackets_in_line(line):
    """Replace <> with escaped version, preserving backtick spans."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            j = i + 1
            while j < len(line) and line[j] != '`':
                j += 1
            if j < len(line):
                result.append(line[i:j+1])
                i = j + 1
            else:
                result.append(line[i:])
                break
        elif line[i:i+2] == '<>':
            result.append('`<>`')
            i += 2
        else:
            j = i
            while j < len(line) and line[j] != '`' and line[j:j+2] != '<>':
                j += 1
            result.append(line[i:j])
            i = j
    return ''.join(result)


def fix_placeholder_angle_brackets(filepath):
    """Fix <PlaceholderText> patterns that look like JSX tags."""
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')
    in_code_block = False

    KNOWN_COMPONENTS = {
        'Info', 'Warning', 'Note', 'Tip', 'Accordion', 'Tabs', 'Tab',
        'Card', 'CardGroup', 'Steps', 'Step', 'Check', 'Frame',
        'ResponseField', 'Expandable', 'CodeGroup', 'ParamField',
        'Snippet', 'img', 'a', 'br', 'hr', 'p', 'div', 'span',
        'table', 'thead', 'tbody', 'tr', 'td', 'th', 'ul', 'ol', 'li',
        'strong', 'em', 'code', 'pre', 'blockquote', 'h1', 'h2', 'h3',
        'h4', 'h5', 'h6', 'sup', 'sub', 'Variation', 'Update', 'Icon'
    }

    for idx in range(len(lines)):
        line = lines[idx]

        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Find <Word_Word> patterns that are NOT known components
        # Pattern: < followed by text with underscores/spaces, followed by >
        matches = list(re.finditer(r'<([A-Z][A-Za-z_\\ ]+?)>', line))
        if not matches:
            continue

        new_line = line
        offset = 0
        for m in matches:
            tag_name = m.group(1).replace('\\', '').replace('_', '').strip()
            # Skip known components
            if tag_name in KNOWN_COMPONENTS:
                continue
            # This is a placeholder - wrap in backticks
            start = m.start() + offset
            end = m.end() + offset
            replacement = '`' + m.group(0) + '`'
            new_line = new_line[:start] + replacement + new_line[end:]
            offset += len(replacement) - (end - start)

        if new_line != line:
            lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def fix_inline_components(filepath):
    """Move inline components (on same line as content) to their own lines."""
    with open(filepath) as f:
        content = f.read()

    original = content
    COMPONENTS = ['Info', 'Warning', 'Note', 'Tip']

    for comp in COMPONENTS:
        # Pattern: text content followed by <Component> on same line
        # (the component should be on its own line)
        pattern = re.compile(
            r'([^\n]+\S)\s*(<' + comp + r'(?:\s[^>]*)?>)\s*\n(.*?)\n(\s*</' + comp + r'>)',
            re.DOTALL
        )
        while True:
            m = pattern.search(content)
            if not m:
                break
            before_text = m.group(1)
            open_tag = m.group(2)
            inner = m.group(3)
            close_tag = m.group(4)

            # Get indentation of the line
            line_start = content.rfind('\n', 0, m.start()) + 1
            full_line = content[line_start:m.start()] + m.group(1)
            indent = len(full_line) - len(full_line.lstrip())
            indent_str = ' ' * indent

            replacement = (
                before_text + '\n\n' +
                indent_str + open_tag + '\n' +
                inner + '\n' +
                close_tag
            )
            content = content[:m.start()] + replacement + content[m.end():]

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False


def fix_escaped_quotes_in_attributes(filepath):
    """Fix \\" in component attributes - replace with &quot; or use single quotes."""
    with open(filepath) as f:
        content = f.read()

    original = content

    # Pattern: <Component title="...\\"...\\"...">
    # Fix by replacing \" with single quotes around the attribute value
    content = re.sub(
        r'(<Accordion\s+title=)"(.*?\\?".*?\\?".*?)"(>)',
        lambda m: _fix_accordion_quotes(m),
        content
    )

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False


def _fix_accordion_quotes(match):
    """Fix escaped quotes in Accordion title attributes."""
    prefix = match.group(1)
    value = match.group(2)
    suffix = match.group(3)

    # Replace \" with real quotes and use single quotes for attribute
    cleaned = value.replace('\\"', '"').replace('\\', '')
    # Use {" "} JSX expression to handle quotes
    return prefix + '{`' + cleaned + '`}' + suffix


if __name__ == '__main__':
    os.chdir('/Users/mallikarjun.dhulange/Documents/moengage-documentation')

    print("=" * 60)
    print("Phase 2a: Fixing Jinja {{...}} curly braces")
    print("=" * 60)
    count = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_jinja_curlies(path):
                    count += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {count} files fixed\n')

    print("=" * 60)
    print("Phase 2b: Fixing standalone { } characters")
    print("=" * 60)
    count2 = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_standalone_braces(path):
                    count2 += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {count2} files fixed\n')

    print("=" * 60)
    print("Phase 2c: Fixing empty <> angle brackets")
    print("=" * 60)
    count3 = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_empty_angle_brackets(path):
                    count3 += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {count3} files fixed\n')

    print("=" * 60)
    print("Phase 2d: Fixing <Placeholder> angle brackets")
    print("=" * 60)
    count4 = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_placeholder_angle_brackets(path):
                    count4 += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {count4} files fixed\n')

    print("=" * 60)
    print("Phase 2e: Fixing escaped quotes in attributes")
    print("=" * 60)
    count5 = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_escaped_quotes_in_attributes(path):
                    count5 += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {count5} files fixed\n')

    total = count + count2 + count3 + count4 + count5
    print("=" * 60)
    print(f"TOTAL Phase 2: {total} files fixed")
    print("=" * 60)
