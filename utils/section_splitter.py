import re

def split_into_sections(text):
    """
    Extract only real policy sections such as:
    1.0 Objective & Scope
    2.0 Asset Identification & Classifications
    3.0 Physical Perimeter Protocols
    """

    sections = {}

    lines = text.splitlines()

    current_heading = None
    current_content = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Match real section headers only
        if re.match(r'^[1-9]\d*\.\d+\s+[A-Za-z]', line):

            # Save previous section
            if current_heading:
                sections[current_heading] = "\n".join(
                    current_content
                ).strip()

            current_heading = line
            current_content = []

        else:

            if current_heading:
                current_content.append(line)

    if current_heading:
        sections[current_heading] = "\n".join(
            current_content
        ).strip()

    return sections