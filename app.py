import streamlit as st
from sentence_transformers import SentenceTransformer, util

# 🔥 MUST be first Streamlit command
st.set_page_config(
    page_title="PlagiarismProof",
    page_icon="🔥",
    layout="centered"
)

# --- BACKEND LOGIC ---
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def check_plagiarism(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return float(score[0][0]) * 100

# --- UI ---
st.title("🔥 PlagiarismProof")
st.subheader("The AI Assignment Paraphraser Detector")
st.write("Paste the original text and the student's submission below.")

col1, col2 = st.columns(2)

with col1:
    original_text = st.text_area("📄 Original Source", height=300)

with col2:
    suspect_text = st.text_area("📝 Suspicious Submission", height=300)

if st.button("🔍 SCAN FOR THEFT"):
    if original_text and suspect_text:
        with st.spinner("Analyzing Semantic Fingerprints..."):
            similarity = check_plagiarism(original_text, suspect_text)

        st.divider()

        if similarity > 60:
            st.error(f"🚨 HIGH SUSPICION ({similarity:.2f}%)")
            st.write("*Verdict:* Ideas are identical, words are paraphrased.")
        elif similarity > 40:
            st.warning(f"⚠️ POTENTIAL PARAPHRASING ({similarity:.2f}%)")
            st.write("*Verdict:* Partial semantic overlap detected.")
        else:
            st.success(f"✅ ORIGINAL WORK ({similarity:.2f}%)")
            st.write("*Verdict:* Completely different topics.")
    else:
        st.info("Please paste text in both boxes.")