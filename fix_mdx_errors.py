#!/usr/bin/env python3
"""Fix MDX syntax errors for Mintlify deployment.

Phase 1: Fix component indentation inside list items.
Components like <Info>, <Warning>, <Note>, <Tip>, <Accordion> that are
indented (inside a list item) but whose content/closing tag is at a lower
indentation level. This causes MDX parsing errors.
"""
import os
import re

COMPONENTS = ['Info', 'Warning', 'Note', 'Tip', 'Accordion']

def fix_component_indentation(filepath):
    """Fix component blocks inside list items by adjusting indentation."""
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        if indent == 0:
            i += 1
            continue

        matched_comp = None
        for comp in COMPONENTS:
            if stripped.startswith(f'<{comp}') and not stripped.startswith(f'</{comp}'):
                matched_comp = comp
                break

        if matched_comp is None:
            i += 1
            continue

        close_tag = f'</{matched_comp}>'
        j = i + 1
        while j < len(lines):
            if close_tag in lines[j]:
                break
            j += 1
        else:
            i += 1
            continue

        close_stripped = lines[j].lstrip()
        close_indent = len(lines[j]) - len(close_stripped)

        if close_indent >= indent:
            i = j + 1
            continue

        min_indent = float('inf')
        for k in range(i + 1, j + 1):
            if lines[k].strip():
                line_indent = len(lines[k]) - len(lines[k].lstrip())
                min_indent = min(min_indent, line_indent)
        if min_indent == float('inf'):
            min_indent = 0

        add_spaces = indent - min_indent
        if add_spaces > 0:
            add_str = ' ' * add_spaces
            for k in range(i + 1, j + 1):
                if lines[k].strip():
                    lines[k] = add_str + lines[k]

        i = j + 1

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def fix_curly_braces(filepath):
    """Fix unescaped curly braces outside code blocks/backticks.
    
    Wraps {{...}} Jinja patterns and standalone { } in backtick code spans.
    """
    with open(filepath) as f:
        content = f.read()

    original = content
    lines = content.split('\n')
    in_code_block = False
    in_frontmatter = False
    frontmatter_count = 0

    for idx in range(len(lines)):
        line = lines[idx]

        if line.strip() == '---':
            frontmatter_count += 1
            if frontmatter_count <= 2:
                in_frontmatter = frontmatter_count == 1
                if frontmatter_count == 2:
                    in_frontmatter = False
                continue

        if in_frontmatter:
            continue

        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Skip lines that are already entirely inside backticks
        # or are image/link references
        if not ('{' in line or '}' in line):
            continue

        # Find {{...}} patterns not already in backticks
        # We need to be careful: don't modify content inside existing backtick spans
        new_line = _escape_curlies_in_line(line)
        if new_line != line:
            lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def _escape_curlies_in_line(line):
    """Escape {{...}} and standalone { } patterns in a line, preserving backtick spans."""
    parts = []
    i = 0
    in_backtick = False

    while i < len(line):
        if line[i] == '`':
            # Find matching backtick
            j = i + 1
            while j < len(line) and line[j] != '`':
                j += 1
            if j < len(line):
                parts.append(line[i:j+1])
                i = j + 1
            else:
                parts.append(line[i:])
                break
        elif line[i:i+2] == '{{':
            # Find matching }}
            j = i + 2
            depth = 1
            while j < len(line) - 1:
                if line[j:j+2] == '{{':
                    depth += 1
                    j += 2
                elif line[j:j+2] == '}}':
                    depth -= 1
                    if depth == 0:
                        j += 2
                        break
                    j += 2
                else:
                    j += 1
            else:
                j = len(line)
                # Find at least one }}
                close_pos = line.find('}}', i + 2)
                if close_pos >= 0:
                    j = close_pos + 2

            expr = line[i:j]
            # Only wrap if not already in backticks and looks like Jinja
            if '{{' in expr and '}}' in expr:
                parts.append('`' + expr + '`')
            else:
                parts.append(expr)
            i = j
        elif line[i] == '{':
            # Standalone { - check if it's a JSX expression or just a character
            # Find matching }
            j = line.find('}', i + 1)
            if j >= 0:
                inner = line[i+1:j]
                # If it contains code-like content, wrap in backticks
                if any(c in inner for c in ['\\', '"', "'", ':', '=']):
                    parts.append('`' + line[i:j+1] + '`')
                    i = j + 1
                else:
                    # Escape the single brace
                    parts.append('{\'{\'}')
                    i += 1
            else:
                # Standalone { without closing - escape it
                parts.append('{\'{\'}')
                i += 1
        elif line[i] == '}':
            # Standalone } without opening {
            parts.append('{\'}\'}')
            i += 1
        else:
            # Regular character
            j = i
            while j < len(line) and line[j] not in ('`', '{', '}'):
                j += 1
            parts.append(line[i:j])
            i = j

    return ''.join(parts)


def fix_backslash_html(filepath):
    """Fix backslash-escaped HTML tags like \\<a ...\\> that MDX can't parse."""
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

        # Fix \<tag...\> patterns - wrap in backticks
        if '\\<' in line:
            # Replace \<...\> with `<...>`
            new_line = re.sub(r'\\<([^\\]*?)\\>', r'`<\1>`', line)
            if new_line != line:
                lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def fix_empty_angle_brackets(filepath):
    """Fix <> in content that MDX interprets as empty JSX tags."""
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

        # Fix <> that's not in a link/url context by replacing with &lt;&gt;
        # But be careful - <> in URLs like href="..." should be left alone
        # Actually, the error is about <> in link text or content
        # The safest fix: if <> appears outside of href="...", replace it
        if '<>' in line and '`' not in line:
            # Only fix if it's not already in backticks
            new_line = line.replace('<>', '`<>`')
            if new_line != line:
                lines[idx] = new_line

    new_content = '\n'.join(lines)
    if new_content != original:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


if __name__ == '__main__':
    os.chdir('/Users/mallikarjun.dhulange/Documents/moengage-documentation')

    print("=" * 60)
    print("Phase 1: Fixing component indentation in list items")
    print("=" * 60)
    fixed_indent = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_component_indentation(path):
                    fixed_indent += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {fixed_indent} files fixed\n')

    print("=" * 60)
    print("Phase 2: Fixing backslash-escaped HTML tags")
    print("=" * 60)
    fixed_backslash = 0
    for root, dirs, files in os.walk('user-guide'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.mdx'):
                path = os.path.join(root, f)
                if fix_backslash_html(path):
                    fixed_backslash += 1
                    print(f'  Fixed: {path}')
    print(f'  -> {fixed_backslash} files fixed\n')

    print("=" * 60)
    print(f"TOTAL: {fixed_indent + fixed_backslash} files fixed")
    print("=" * 60)
