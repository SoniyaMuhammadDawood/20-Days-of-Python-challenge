import streamlit as st
import random
import time
import json

st.markdown(
    """
    <style>
    /* Main Page Background */
    .stApp {
        background-color: #CDE990; 
    }
    
    /* Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #AACB73;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("About the Quiz App 🧩")
st.sidebar.markdown("""
Welcome to the **Quiz App**! 🧠  
Test your knowledge of **Python programming** by answering random multiple-choice questions.

✅ **One question at a time**  
❌ **Instant feedback on wrong answers**  
🔄 **Questions refresh automatically**

**Good luck, and have fun!** 🤗
""")


# Load questions from JSON
with open("questions.json", "r") as file:
    all_questions = json.load(file)

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "asked_questions" not in st.session_state:
    st.session_state.asked_questions = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "answered" not in st.session_state:
    st.session_state.answered = False

# Select a new question if needed
if len(st.session_state.asked_questions) < len(all_questions):
    if st.session_state.current_question is None or st.session_state.answered:
        remaining_questions = [q for q in all_questions if q not in st.session_state.asked_questions]
        st.session_state.current_question = random.choice(remaining_questions)
        st.session_state.answered = False
else:
    st.balloons()  # 🎈 Streamlit built-in celebration animation
    st.title("🎉 Quiz Completed!")
    st.subheader("Great job!")
    st.success(f"Your total score is: **{st.session_state.score}** out of **{len(all_questions)}**.")
    st.markdown("Thanks for playing the quiz!🚀")
    st.stop()


# Show question
question = st.session_state.current_question
st.title("📝 Quiz App✨")
st.subheader(question["question"])
selected_option = st.selectbox("**Choose your answer**", question["option"], key="answer")

if st.button("**Submit answer**") and not st.session_state.answered:
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
        time.sleep(2)
    else:
        st.error("❌ Incorrect! Correct answer is " + question["answer"])
        time.sleep(5)

    st.session_state.asked_questions.append(question)
    st.session_state.answered = True
    st.session_state.current_question = None
    st.rerun()









