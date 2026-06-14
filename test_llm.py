from utils.impact_analyzer import analyze_change

old_text = """
Employees may work remotely
2 days per week.
"""

new_text = """
Employees may work remotely
4 days per week.
"""

result = analyze_change(
    old_text,
    new_text
)

print(result)