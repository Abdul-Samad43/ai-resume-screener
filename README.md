# 📄 AI Resume Screener

An AI-powered resume screening tool that instantly matches resumes against job descriptions and provides intelligent hiring recommendations — powered by **Groq API (openai/gpt-oss-120b)** and **TF-IDF similarity scoring**.

---

## 🚀 Features

- 📤 Upload PDF resumes with one click
- 📊 TF-IDF based match score (0–100%)
- ✅ Matching skills detection
- ❌ Missing skills identification
- 🎯 AI hiring recommendation (Hire / Maybe / Reject)
- 📝 Detailed candidate explanation powered by AI
- ⚡ Instant results with a clean, interactive UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Groq API (`openai/gpt-oss-120b`) |
| Similarity Scoring | TF-IDF + Cosine Similarity (Scikit-learn) |
| PDF Parsing | PyPDF2 |
| UI | Streamlit |
| Environment | Python-dotenv |

---

## 📁 Project Structure

```
ai-resume-screener/
├── app.py              # Streamlit UI and main application
├── analyzer.py         # AI analysis and TF-IDF match scoring
├── resume_parser.py    # PDF text extraction and cleaning
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Abdul-Samad43/ai-resume-screener.git
cd ai-resume-screener
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:
```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Open the app in your browser (usually `http://localhost:8501`)
2. Upload a candidate's resume in **PDF format**
3. Paste the **Job Description** in the text area
4. Click **🔍 Analyze Resume**
5. View the match score, skills breakdown, and AI recommendation

---

## 📊 How Scoring Works

| Score Range | Result |
|-------------|--------|
| 70% and above | ✅ Strong Match — Recommended to Hire |
| 40% – 69% | ⚠️ Moderate Match — Consider Interview |
| Below 40% | ❌ Weak Match — Not a Good Fit |

The score is calculated using **TF-IDF Cosine Similarity** between the resume and job description text, combined with an **AI-generated analysis** from Groq.

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
scikit-learn
PyPDF2
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Groq API key for AI analysis |

---

## ⚠️ Notes

- Only PDF resumes are supported
- Never commit your `.env` file — it contains your API key
- Resume text is limited to 2000 characters and job description to 1000 characters for AI analysis

---

## 👨‍💻 Built By

**Abdul Samad** — AI Engineer 

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
