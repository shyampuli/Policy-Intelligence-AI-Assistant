from rapidfuzz import fuzz

def compare_sections(old_text,new_text):

    score = fuzz.ratio(old_text,new_text)

    if score > 95:
        change = "No Change"

    elif score > 70:
        change = "Modified"

    else:
        change = "Major Change"

    return score, change