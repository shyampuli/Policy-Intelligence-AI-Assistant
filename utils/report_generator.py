from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
        filename,
        executive_summary,
        analysis_results
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Policy Comparison Analysis Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 12))

    summary_heading = Paragraph(
        "Executive Summary",
        styles["Heading1"]
    )

    content.append(summary_heading)

    content.append(
        Paragraph(
            executive_summary,
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    details_heading = Paragraph(
        "Section Analysis",
        styles["Heading1"]
    )

    content.append(details_heading)

    for result in analysis_results:

        content.append(
            Paragraph(
                result["section"],
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Risk:</b> {result['risk_level']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Change:</b> {result['change_summary']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Business Impact:</b> {result['business_impact']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Regulatory Impact:</b> {result['regulatory_impact']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Recommendation:</b> {result['recommendation']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

    doc.build(content)

    return filename