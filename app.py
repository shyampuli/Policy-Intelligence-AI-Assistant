import streamlit as st
import pandas as pd
import plotly.express as px

from utils.pdf_reader import extract_text
from utils.section_splitter import split_into_sections
from utils.comparator import compare_sections

from utils.impact_analyzer import (
    analyze_change,
    generate_executive_summary,
    create_summary_context,
    policy_chatbot
)

from utils.report_generator import (
    generate_pdf_report
)

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Policy Intelligence Assistant",
    layout="wide"
)

st.title("📄 Policy Intelligence Assistant")

st.markdown(
    """
    Compare Legacy vs Modernized Policies
    using AI-powered compliance analysis.
    """
)

# ---------------------------------
# FILE UPLOAD
# ---------------------------------

old_pdf = st.file_uploader(
    "Upload Legacy Policy PDF",
    type=["pdf"]
)

new_pdf = st.file_uploader(
    "Upload Modernized Policy PDF",
    type=["pdf"]
)

# ---------------------------------
# PROCESS
# ---------------------------------

if old_pdf and new_pdf:

    with open("old_policy.pdf", "wb") as f:
        f.write(old_pdf.read())

    with open("new_policy.pdf", "wb") as f:
        f.write(new_pdf.read())

    st.success("Both PDFs uploaded successfully")

    # ---------------------------------
    # EXTRACT TEXT
    # ---------------------------------

    with st.spinner("Extracting text..."):

        old_text = extract_text("old_policy.pdf")
        new_text = extract_text("new_policy.pdf")

    # ---------------------------------
    # SPLIT SECTIONS
    # ---------------------------------

    old_sections = split_into_sections(old_text)
    new_sections = split_into_sections(new_text)

    # DEBUG
    st.subheader("Debug Sections")
    st.write("Old Sections")
    st.write(list(old_sections.keys()))
    st.write("New Sections")
    st.write(list(new_sections.keys()))

    # ---------------------------------
    # ANALYSIS
    # ---------------------------------

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    results = []

    all_sections = set(list(old_sections.keys()) + list(new_sections.keys()))

    for section in all_sections:

        skip_words = ["effective date", "version", "status", "document id"]

        if any(word in section.lower() for word in skip_words):
            continue

        old_content = old_sections.get(section, "")
        new_content = new_sections.get(section, "")

        # Ignore tiny fragments
        if (len(old_content.strip()) < 50 and len(new_content.strip()) < 50):
            continue

        score, change = compare_sections(old_content, new_content)

        # Default analysis for unchanged sections
        analysis = {
            "change_summary": "No significant changes detected",
            "business_impact": "No significant business impact",
            "regulatory_impact": "No significant regulatory impact",
            "risk_level": "Low",
            "recommendation": "No action required"
        }

        # Only call LLM if section changed
        if change != "No Change":
            analysis = analyze_change(old_content, new_content)

        risk = analysis.get("risk_level", "Low")

        if risk == "High":
            high_risk += 1
        elif risk == "Medium":
            medium_risk += 1
        else:
            low_risk += 1

        results.append({
            "section": section,
            "change": change,
            "score": score,
            "old": old_content,
            "new": new_content,
            "change_summary": analysis.get("change_summary", ""),
            "business_impact": analysis.get("business_impact", ""),
            "regulatory_impact": analysis.get("regulatory_impact", ""),
            "risk_level": analysis.get("risk_level", "Low"),
            "recommendation": analysis.get("recommendation", "")
        })

    # ---------------------------------
    # DASHBOARD
    # ---------------------------------

    st.header("📊 Risk Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔴 High Risk", high_risk)
    col2.metric("🟡 Medium Risk", medium_risk)
    col3.metric("🟢 Low Risk", low_risk)

    # ---------------------------------
    # RISK CHART
    # ---------------------------------

    risk_df = pd.DataFrame({
        "Risk": ["High", "Medium", "Low"],
        "Count": [high_risk, medium_risk, low_risk]
    })

    fig = px.pie(risk_df, names="Risk", values="Count", title="Risk Distribution")

    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------
    # SECTION ANALYSIS
    # ---------------------------------

    st.header("🔍 Section Analysis")

    if len(results) == 0:
        st.warning("No policy sections detected.")

    for item in results:

        risk = item["risk_level"]

        if risk == "High":
            icon = "🔴"
        elif risk == "Medium":
            icon = "🟡"
        else:
            icon = "🟢"

        section_name = item["section"].replace("\n", " ").strip()

        st.subheader(f"{icon} {section_name}")
        st.caption(f"Similarity Score: {item['score']}%")

        st.write(f"**Change Type:** {item['change']}")
        st.write(f"**Risk Level:** {item['risk_level']}")
        st.write(f"**Change Summary:** {item['change_summary']}")
        st.write(f"**Business Impact:** {item['business_impact']}")
        st.write(f"**Regulatory Impact:** {item['regulatory_impact']}")
        st.write(f"**Recommendation:** {item['recommendation']}")

        with st.expander("View Policy Details"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Legacy Policy")
                st.text(item["old"])

            with col2:
                st.markdown("### Modernized Policy")
                st.text(item["new"])

        st.divider()

    # ---------------------------------
    # EXECUTIVE SUMMARY
    # ---------------------------------

    st.header("📋 Executive Summary")

    if st.button("Generate Executive Summary"):
        context = create_summary_context(results)
        summary = generate_executive_summary(context)
        st.session_state["summary"] = summary

    if "summary" in st.session_state:
        st.success(st.session_state["summary"])

    # ---------------------------------
    # CHATBOT
    # ---------------------------------

    st.header("🤖 Compliance Copilot")

    question = st.text_input("Ask a question")

    if question:
        context = create_summary_context(results)
        answer = policy_chatbot(question, context)
        st.write(answer)

    # ---------------------------------
    # REPORT
    # ---------------------------------

    st.header("📄 Download Report")

    if st.button("Generate PDF Report"):
        context = create_summary_context(results)
        summary = generate_executive_summary(context)

        filename = generate_pdf_report("policy_report.pdf", summary, results)

        with open(filename, "rb") as file:
            st.download_button(
                label="⬇ Download Report",
                data=file,
                file_name="Policy_Report.pdf",
                mime="application/pdf"
            )
