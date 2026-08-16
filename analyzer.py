import os 
from groq import Groq
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()  

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  

def calculate_match_score(resume_text, job_description):
    """TF-IDF se match score nikalta hai"""
    vectorizer = TfidfVectorizer(stop_words='english')  
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def analyze_with_ai(resume_text, job_description):  
    """Groq AI se detailed analysis karo"""
    prompt = f"""
Analyze this resume against the job description and provide:
1. Match Percentage
2. Strong matching skills (list)
3. Missing skills (list)
4. Overall recommendation (Hire/Maybe/Reject)
5. Brief explanation (2-3 lines)

Resume:
{resume_text[:2000]}

Job Description:
{job_description[:1000]}

Respond in JSON format only:
{{
    "match_percentage": number,
    "matching_skills": [list],
    "missing_skills": [list],
    "recommendations": "Hire/Maybe/Reject",
    "explanation": "text"
}}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b", 
        messages=[{"role": "user", "content": prompt}],  
        max_tokens=1000,
        temperature=0.1
    )

    return response.choices[0].message.content
