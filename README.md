# 📄 Policy Intelligence Assistant

## Overview

Policy Intelligence Assistant is an AI-powered document comparison platform that helps organizations analyze differences between legacy and modernized policy documents, identify compliance risks, understand regulatory impact, and generate executive-level summaries.

The solution automates policy review workflows by leveraging AI, semantic comparison, risk classification, and report generation, significantly reducing manual effort and review time.

Built as part of the **AMD x TCS Hackathon 2026**, the solution runs on **AMD Instinct MI300X GPUs** using the **ROCm AI ecosystem**.

---

# Problem Statement

Organizations frequently update internal policies to align with changing business requirements, security standards, and regulatory frameworks.

Manually comparing policy versions is:

* Time-consuming
* Error-prone
* Difficult to scale
* Challenging for compliance teams

There is a need for an intelligent system that can:

* Compare legacy and updated policies
* Identify changes automatically
* Assess business and regulatory impact
* Classify risk levels
* Generate executive summaries
* Provide compliance insights through conversational AI

---

# Solution Architecture

```text
Legacy Policy PDF
        │
        ▼
PDF Text Extraction
        │
        ▼
Section Detection & Parsing
        │
        ▼
Policy Comparison Engine
        │
        ▼
Risk Classification
        │
        ▼
AI Impact Analysis
        │
        ▼
Executive Summary Generator
        │
        ▼
Compliance Copilot Chatbot
        │
        ▼
PDF Report Generation
```

---

# Key Features

### Policy Comparison

* Upload legacy and modernized policy PDFs
* Automatic section-level comparison
* Similarity scoring

### Risk Classification

Categorizes policy changes as:

* High Risk
* Medium Risk
* Low Risk

### Interactive Dashboard

* Risk metrics
* Visual analytics
* Risk distribution charts

### AI Compliance Copilot

Ask natural language questions such as:

* What changed in the policy?
* Which sections have the highest risk?
* What compliance actions are recommended?

### Executive Summary

Generates management-ready summaries covering:

* Key changes
* Business impact
* Regulatory impact
* Recommendations

### PDF Report Generation

Download a professional analysis report containing:

* Section comparison results
* Risk classifications
* Recommendations
* Executive summary

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI & NLP

* Qwen / Gemma (via vLLM)
* OpenAI Compatible API
* RapidFuzz

## Visualization

* Plotly
* Pandas

## Document Processing

* PyMuPDF (fitz)

## Reporting

* ReportLab

## Infrastructure

* AMD Instinct MI300X
* ROCm
* AMD Developer Cloud

---

# Project Structure

```text
policy-assistant/
│
├── app.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── section_splitter.py
│   ├── comparator.py
│   ├── impact_analyzer.py
│   └── report_generator.py
│
├── requirements.txt
│
└── README.md
```

---

# How To Run

## 1. Clone Repository

```bash
git clone <repository-url>
cd policy-assistant
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Start LLM Server

Example using Qwen:

```bash
vllm serve Qwen/Qwen3-4B \
--served-model-name Qwen3-4B \
--api-key abc123 \
--port 8000
```

## 5. Run Application

```bash
streamlit run app.py
```

## 6. Open Browser

```text
http://localhost:8501
```

---

# 📸 Screenshots

## Dashboard

<img width="2474" height="1300" alt="Screenshot 2026-06-14 194357" src="https://github.com/user-attachments/assets/1780f741-eca4-4a2c-a5fb-96f5f8aa4291" />

## Risk Analysis

<img width="2502" height="1232" alt="Screenshot 2026-06-14 194423" src="https://github.com/user-attachments/assets/da288238-c65f-4550-a34b-e9dbc7dd1af0" />
<img width="2472" height="1320" alt="Screenshot 2026-06-14 194511" src="https://github.com/user-attachments/assets/8d2474ab-0b5b-4e90-a7b6-d82a4c3a28fe" />


## Executive Summary

<img width="2468" height="1272" alt="Screenshot 2026-06-14 194553" src="https://github.com/user-attachments/assets/c154cdec-deb3-48a4-a677-08c5d3d8ae0b" />


## Compliance Copilot

<img width="2458" height="1276" alt="Screenshot 2026-06-14 194817" src="https://github.com/user-attachments/assets/b9e6f585-f5f8-441c-b6c4-9022c13ddad9" />


## PDF Report

<img width="2472" height="320" alt="Screenshot 2026-06-14 195249" src="https://github.com/user-attachments/assets/43be59f1-54f3-4534-9353-8a9d87ee365f" />
<img width="936" height="1236" alt="Screenshot 2026-06-14 195750" src="https://github.com/user-attachments/assets/1d318747-462f-40f5-b038-4caf230bb3cf" />
<img width="950" height="1298" alt="Screenshot 2026-06-14 195810" src="https://github.com/user-attachments/assets/338f4f97-8134-4b99-978c-9fc2ba6d7be5" />



# Business Impact

The solution enables organizations to:

* Reduce policy review effort
* Improve compliance visibility
* Accelerate regulatory assessments
* Enhance governance processes
* Improve decision-making with AI-driven insights

---

# 🔮 Future Enhancements

* Multi-document comparison
* Regulatory framework mapping
* RAG-powered compliance knowledge base
* Fine-tuned policy-specific LLM
* Multi-language policy support
* Real-time collaboration features

---

# AMD x TCS Hackathon 2026

Built using AMD Instinct MI300X GPUs and ROCm software stack as part of the AMD x TCS Hackathon challenge:

**Policy & Document Comparison Assistant**

Compare legacy and modernized policies, identify differences, and explain regulatory impact using AI.
