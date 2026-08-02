# 📄 AI Resume Screener

AI-powered tool that matches resumes against job descriptions and provides instant hiring recommendations.

## Features
- PDF resume upload and parsing
- TF-IDF based match score (0-100%)
- Matching and missing skills detection
- AI hiring recommendation (Hire / Maybe / Reject)
- Detailed candidate explanation

## Tech Stack
- Python, Streamlit, Groq API (LLaMA 3.3), PyPDF2, Scikit-learn

## Installation

```bash
git clone https://github.com/Abdul-Samad43/ai-resume-screener.git
cd ai-resume-screener
pip install -r requirements.txt
```

Add your Groq API key in `.env`: GROQ_API_KEY=your_key_here
Run:
```bash
streamlit run app.py
```

## Built By
**Abdul Samad** — AI Engineer
