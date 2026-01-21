# 🔥 PlagiarismProof

*PlagiarismProof* is an AI-based semantic plagiarism detection tool that identifies paraphrased content by comparing meaning rather than exact words.

Traditional plagiarism checkers rely on keyword matching. Our solution uses transformer-based sentence embeddings to detect copied ideas even when vocabulary is changed.

---

## 🚀 Features
- Detects paraphrased plagiarism  
- Compares semantic meaning instead of exact words  
- Displays similarity percentage with clear verdict  
- Simple and clean web interface  

---

## 🧠 How It Works
1. User inputs:
   - Original text  
   - Suspicious submission  
2. Both texts are converted into *sentence embeddings* using a pre-trained *Sentence Transformer*  
3. *Cosine Similarity* is calculated between embeddings  
4. Based on similarity score, a verdict is displayed:
   - High similarity → Paraphrasing detected  
   - Low similarity → Original content  

---

## 🛠️ Tech Stack
- *Python*
- *Sentence Transformers*
- *Cosine Similarity*
- *Streamlit*
- *VS Code*

---

## 🖥️ How to Run Locally

```bash
# Activate virtual environment
venv\Scripts\activate

# Run the app
streamlit run app.py

The app will open at:
http://localhost:8501

🎯 Use Cases
Academic institutions
Faculty assignment evaluation
Detecting AI-assisted paraphrasing
Promoting originality in student submissions

📌 Note
This project uses a pre-trained model and focuses on practical application.

Team
Code Alchemists
Smt. Indira Gandhi College of Engineering
Hackathon: Multiverse of Tech 2026
