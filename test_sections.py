from utils.pdf_reader import extract_text
from utils.section_splitter import split_into_sections

text = extract_text("old_policy.pdf")

sections = split_into_sections(text)

for key in sections:

    print("\n")
    print("="*50)
    print(key)
    print("="*50)
    print(sections[key][:300])