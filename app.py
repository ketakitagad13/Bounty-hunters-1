import streamlit as st
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Viral Reel Script Writer",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Viral Reel Script Writer")
st.markdown("Turn boring topics into engaging 30-second viral reel scripts.")

# ---------------- API SETUP ----------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- USER INPUT ----------------
topic = st.text_input("Enter a boring topic:")

tone = st.selectbox(
    "Select tone:",
    ["Funny", "Motivational", "Educational", "Storytelling", "Dramatic"]
)

generate = st.button("Generate Viral Script 🚀")

# ---------------- SCRIPT GENERATION ----------------
def generate_script(topic, tone):
    prompt = f"""
You are a professional short-form content strategist.

Create a 30-second Instagram Reel script for the topic: "{topic}"

Tone: {tone}

Structure:
1. Strong hook (first 3 seconds)
2. Engaging main content
3. Clear call-to-action
4. On-screen caption suggestions
5. Music suggestion

Keep it punchy, engaging, and optimized for virality.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    return response.choices[0].message.content


# ---------------- OUTPUT ----------------
if generate and topic.strip() != "":
    with st.spinner("Crafting your viral script... ✨"):
        script = generate_script(topic, tone)

    st.success("Your Viral Script is Ready!")

    st.markdown("### 📜 Script Output")
    st.markdown(script)

elif generate:
    st.warning("Please enter a topic.")

