from rapidfuzz import fuzz

def compare_sections(old_text, new_text):

    if not old_text and not new_text:
        return 100, "No Change"

    if not old_text:
        return 0, "Added"

    if not new_text:
        return 0, "Removed"

    score = fuzz.token_sort_ratio(
        old_text,
        new_text
    )

    if score >= 95:
        change = "No Change"

    elif score >= 70:
        change = "Modified"

    else:
        change = "Major Change"

    return round(score, 2), change