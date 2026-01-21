from sentence_transformers import SentenceTransformer, util

# Load model (first time may take 1–2 minutes)
model = SentenceTransformer('all-MiniLM-L6-v2')

def check_similarity(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return float(score[0][0]) * 100

# Test cases
text_a = "The sky is blue."
text_b = "The color of the atmosphere is azure."

text_c = "The sky is blue."
text_d = "I like eating apples."

print("Test 1 similarity:", check_similarity(text_a, text_b))
print("Test 2 similarity:", check_similarity(text_c, text_d))