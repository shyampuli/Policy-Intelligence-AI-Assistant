import re

def split_into_sections(text):

    sections = {}

    current_heading = "Introduction"

    sections[current_heading] = ""

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 0:

            # treat short lines as headings

            if len(line) < 50:

                current_heading = line

                sections[current_heading] = ""

            else:

                sections[current_heading] += line + "\n"

    return sections