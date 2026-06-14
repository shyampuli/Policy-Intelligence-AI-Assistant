from utils.impact_analyzer import analyze_change

old_text = """
Passwords must contain 8 characters.
"""

new_text = """
Passwords must contain 12 characters.
Multi-factor authentication is mandatory.
"""

result = analyze_change(
    old_text,
    new_text
)

print(result)