# Email Generation Assistant

## Overview
This project implements an AI-powered Email Generation Assistant that creates professional emails based on:
- Intent
- Key Facts
- Tone

The system uses Large Language Models (LLMs) via Groq API and evaluates performance using custom-defined metrics.

---

## Features
- Generates structured, professional emails
- Uses advanced prompt engineering (role + instructions + few-shot)
- Evaluates outputs using custom metrics
- Compares two LLM models

---

## Models Used
- llama-3.1-8b-instant (Groq)
- llama-3.1-70b-versatile (Groq)

---

## 🛠 Prompt Engineering Strategy
The system uses:
- **Role-based prompting** → ensures professional tone
- **Instruction constraints** → enforces fact inclusion
- **Few-shot examples** → improves consistency and structure

---

## Custom Evaluation Metrics

### 1. Fact Coverage Score (FCS)
Measures how many input facts are correctly included in the generated email.

### 2. Tone Alignment Score (TAS)
Uses an LLM-as-a-judge approach to evaluate how well the email matches the requested tone.

### 3. Structure & Quality Score (QS)
Evaluates grammar, clarity, and proper email formatting.

---

## ⚙️ Installation & Setup

```bash
pip install -r requirements.txt
