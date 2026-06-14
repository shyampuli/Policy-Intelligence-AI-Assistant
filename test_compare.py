from utils.pdf_reader import extract_text
from utils.section_splitter import split_into_sections
from utils.comparator import compare_sections

old_text = extract_text("old_policy.pdf")

new_text = extract_text("new_policy.pdf")

old_sections = split_into_sections(old_text)

new_sections = split_into_sections(new_text)

for section in old_sections:

    if section in new_sections:

        score = compare_sections(
            old_sections[section],
            new_sections[section]
        )

        print(section)
        print(score)
        print("-"*50)