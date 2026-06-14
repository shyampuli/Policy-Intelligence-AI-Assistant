from openai import OpenAI
import json
import re

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="abc123"
)


def remove_thinking(text):

    text = re.sub(
        r'<think>.*?</think>',
        '',
        text,
        flags=re.DOTALL
    )

    return text.strip()


def extract_json(text):

    text = remove_thinking(text)

    match = re.search(
        r'\{.*\}',
        text,
        re.DOTALL
    )

    if match:

        try:
            return json.loads(
                match.group()
            )

        except:
            pass

    return None


def analyze_change(
    old_text,
    new_text
):

    prompt = f"""
You are a policy compliance analyst.

Compare:

OLD POLICY:
{old_text}

NEW POLICY:
{new_text}

Return ONLY JSON.

{{
    "change_summary":"",
    "business_impact":"",
    "regulatory_impact":"",
    "risk_level":"Low",
    "recommendation":""
}}

Risk Rules:

High:
- Authentication
- Passwords
- Access Control
- Security Controls
- Financial Controls

Medium:
- Operational Changes
- HR Policies
- Remote Work

Low:
- Version Updates
- Date Changes
- Formatting Changes
"""

    try:

        response = client.chat.completions.create(
            model="Qwen3-4B",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = (
            response
            .choices[0]
            .message
            .content
        )

        parsed = extract_json(
            content
        )

        if parsed:
            return parsed

        return {

            "change_summary":
            content[:300],

            "business_impact":
            "Minimal business impact",

            "regulatory_impact":
            "No major regulatory impact",

            "risk_level":
            "Low",

            "recommendation":
            "Manual review suggested"
        }

    except Exception as e:

        return {

            "change_summary":
            str(e),

            "business_impact":
            "",

            "regulatory_impact":
            "",

            "risk_level":
            "Unknown",

            "recommendation":
            ""
        }


def generate_executive_summary(
    context
):

    prompt = f"""
Create an executive summary.

Analysis:

{context}

Include:

1. Key changes
2. Business impact
3. Regulatory impact
4. Recommendations

Maximum 200 words.
"""

    try:

        response = client.chat.completions.create(
            model="Qwen3-4B",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    except Exception as e:

        return str(e)


def policy_chatbot(
    question,
    context
):

    prompt = f"""
You are a Compliance Copilot.

POLICY ANALYSIS:

{context}

QUESTION:

{question}

Answer professionally.
"""

    try:

        response = client.chat.completions.create(
            model="Qwen3-4B",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    except Exception as e:

        return str(e)


def create_summary_context(
    results
):

    context = ""

    for result in results:

        context += f"""

Section:
{result['section']}

Change:
{result['change_summary']}

Business Impact:
{result['business_impact']}

Regulatory Impact:
{result['regulatory_impact']}

Risk:
{result['risk_level']}

Recommendation:
{result['recommendation']}

---------------------------------------
"""

    return context