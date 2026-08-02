import streamlit as st
import json
from resume_parser import extract_text_from_pdf, clean_text
from analyzer import calculate_match_score, analyze_with_ai

# Page config
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

# Title
st.markdown("""
    <h1 style='text-align: center; color: #6366f1;'>
        📄 AI Resume Screener
    </h1>
    <p style='text-align: center; color: #6b7280;'>
        Match resumes against job descriptions instantly using AI
    </p>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Resume Upload here")
    uploaded_file = st.file_uploader("Uplaod your Resume in PDF format", type="pdf")

with col2:
    st.subheader("💼 Job Description")
    job_description = st.text_area(
        "paste Job Description here",
        height=200,
        placeholder="We are looking for a Python developer..."
    )

st.divider()

if st.button("🔍 Analyze Resume", use_container_width=True):
    if not uploaded_file:
        st.error("❌ Must Upload your Resume first!")
    elif not job_description:
        st.error("❌ Write the Job Description first!")
    else:
        
        analysis = None
        ai_raw = ""
        
        with st.spinner("Analyzing Resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            resume_text = clean_text(resume_text)
            score = calculate_match_score(resume_text, job_description)
            ai_raw = analyze_with_ai(resume_text, job_description)
            
            try:
                ai_raw = ai_raw.strip()
                if "```json" in ai_raw:
                    ai_raw = ai_raw.split("```json")[1].split("```")[0]
                elif "```" in ai_raw:
                    ai_raw = ai_raw.split("```")[1].split("```")[0]
                analysis = json.loads(ai_raw)
            except Exception as e:
                st.error(f"Error: {e}")
                analysis = None
        
        st.success("✅ Analysis complete!")
        st.divider()
        
        st.subheader("📊 Match Score")
        
        if score >= 70:
            st.metric("Match Score", f"{score}%", "Strong Match ✅")
        elif score >= 40:
            st.metric("Match Score", f"{score}%", "Moderate Match ⚠️")
        else:
            st.metric("Match Score", f"{score}%", "Weak Match ❌")
        
        st.progress(score / 100)
        
        if analysis:
            st.divider()
            
            col3, col4 = st.columns(2)
            
            with col3:
                st.subheader("✅ Matching Skills")
                for skill in analysis.get("matching_skills", []):
                    st.success(f"✓ {skill}")
                
                st.subheader("📊 AI Match %")
                exp = analysis.get("match_percentage", 0)
                st.info(f"🎯 AI Score: {exp}%")
            
            with col4:
                st.subheader("❌ Missing Skills")
                for skill in analysis.get("missing_skills", []):
                    st.error(f"✗ {skill}")
                
                st.subheader("🎯 Recommendation")
                rec = analysis.get("recommendations", "N/A")
                if rec == "Hire":
                    st.success("✅ HIRE — Strong Candidate!")
                elif rec == "Maybe":
                    st.warning("⚠️ MAYBE — Consider Interview")
                else:
                    st.error("❌ REJECT — Not a Good Fit")
            
            st.divider()
            st.subheader("📝 AI Summary")
            st.info(analysis.get("explanation", "N/A"))
            
