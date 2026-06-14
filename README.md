📄 Policy Intelligence Assistant
================================

🚀 Overview
-----------

Policy Intelligence Assistant is an AI-powered document comparison platform that helps organizations analyze differences between legacy and modernized policy documents, identify compliance risks, understand regulatory impact, and generate executive-level summaries.

The solution automates policy review workflows by leveraging AI, semantic comparison, risk classification, and report generation, significantly reducing manual effort and review time.

Built as part of the **AMD x TCS Hackathon 2026**, the solution runs on **AMD Instinct MI300X GPUs** using the **ROCm AI ecosystem**.

🎯 Problem Statement
====================

Organizations frequently update internal policies to align with changing business requirements, security standards, and regulatory frameworks.

Manually comparing policy versions is:

*   Time-consuming
    
*   Error-prone
    
*   Difficult to scale
    
*   Challenging for compliance teams
    

There is a need for an intelligent system that can:

*   Compare legacy and updated policies
    
*   Identify changes automatically
    
*   Assess business and regulatory impact
    
*   Classify risk levels
    
*   Generate executive summaries
    
*   Provide compliance insights through conversational AI
    

🏗️ Solution Architecture
=========================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Legacy Policy PDF          │          ▼  PDF Text Extraction          │          ▼  Section Detection & Parsing          │          ▼  Policy Comparison Engine          │          ▼  Risk Classification          │          ▼  AI Impact Analysis          │          ▼  Executive Summary Generator          │          ▼  Compliance Copilot Chatbot          │          ▼  PDF Report Generation   `

⚙️ Key Features
===============

### 📑 Policy Comparison

*   Upload legacy and modernized policy PDFs
    
*   Automatic section-level comparison
    
*   Similarity scoring
    

### ⚠️ Risk Classification

Categorizes policy changes as:

*   High Risk
    
*   Medium Risk
    
*   Low Risk
    

### 📊 Interactive Dashboard

*   Risk metrics
    
*   Visual analytics
    
*   Risk distribution charts
    

### 🤖 AI Compliance Copilot

Ask natural language questions such as:

*   What changed in the policy?
    
*   Which sections have the highest risk?
    
*   What compliance actions are recommended?
    

### 📝 Executive Summary

Generates management-ready summaries covering:

*   Key changes
    
*   Business impact
    
*   Regulatory impact
    
*   Recommendations
    

### 📄 PDF Report Generation

Download a professional analysis report containing:

*   Section comparison results
    
*   Risk classifications
    
*   Recommendations
    
*   Executive summary
    

🛠️ Tech Stack
==============

Frontend
--------

*   Streamlit
    

Backend
-------

*   Python
    

AI & NLP
--------

*   Qwen / Gemma (via vLLM)
    
*   OpenAI Compatible API
    
*   RapidFuzz
    

Visualization
-------------

*   Plotly
    
*   Pandas
    

Document Processing
-------------------

*   PyMuPDF (fitz)
    

Reporting
---------

*   ReportLab
    

Infrastructure
--------------

*   AMD Instinct MI300X
    
*   ROCm
    
*   AMD Developer Cloud
    

📂 Project Structure
====================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   policy-assistant/  │  ├── app.py  │  ├── utils/  │   ├── pdf_reader.py  │   ├── section_splitter.py  │   ├── comparator.py  │   ├── impact_analyzer.py  │   └── report_generator.py  │  ├── requirements.txt  │  └── README.md   `

▶️ How To Run
=============

1\. Clone Repository
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone   cd policy-assistant   `

2\. Create Virtual Environment
------------------------------

### Windows

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  venv\Scripts\activate   `

### Linux / Mac

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python3 -m venv venv  source venv/bin/activate   `

3\. Install Dependencies
------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

4\. Start LLM Server
--------------------

Example using Qwen:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   vllm serve Qwen/Qwen3-4B \  --served-model-name Qwen3-4B \  --api-key abc123 \  --port 8000   `

5\. Run Application
-------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

6\. Open Browser
----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:8501   `

📸 Screenshots
==============

Dashboard
---------

(Add screenshot)

Risk Analysis
-------------

(Add screenshot)

Executive Summary
-----------------

(Add screenshot)

Compliance Copilot
------------------

(Add screenshot)

PDF Report
----------

(Add screenshot)

🎥 Demo Video
=============

Demo Video Link:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Add Demo Video URL Here   `

📈 Business Impact
==================

The solution enables organizations to:

*   Reduce policy review effort
    
*   Improve compliance visibility
    
*   Accelerate regulatory assessments
    
*   Enhance governance processes
    
*   Improve decision-making with AI-driven insights
    

🔮 Future Enhancements
======================

*   Multi-document comparison
    
*   Regulatory framework mapping
    
*   RAG-powered compliance knowledge base
    
*   Fine-tuned policy-specific LLM
    
*   Multi-language policy support
    
*   Real-time collaboration features
    

👥 Team
=======

### Team Name

team-642

### Team Members

*   Shyamprasad Puli
    
*   Add Team Member
    
*   Add Team Member
    

🏆 AMD x TCS Hackathon 2026
===========================

Built using AMD Instinct MI300X GPUs and ROCm software stack as part of the AMD x TCS Hackathon challenge:

**Policy & Document Comparison Assistant**

Compare legacy and modernized policies, identify differences, and explain regulatory impact using AI.
