# AI Email Automation Assistant

A Python-based AI automation project that uses an LLM API to generate professional email replies.

## Features
- Accepts email content as input
- Supports multiple reply tones
- Uses a Gemini LLM API
- Generates replies automatically
- Simple Streamlit interface

## Tech Stack
- Python
- Google Gemini API
- REST/API integration
- Streamlit
- JSON/API data handling
- Git/GitHub

## Setup

1. Install Python.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file from `.env.example`.
5. Add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

6. Run:

```bash
streamlit run app.py
```

## Workflow

Email Input -> Python -> Gemini LLM API -> Generated Reply

## Purpose

This project demonstrates a simple AI-powered automation workflow for reducing repetitive email response tasks.
