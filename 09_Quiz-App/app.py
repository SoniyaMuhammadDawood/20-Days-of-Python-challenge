import streamlit as st
import random
import time

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


all_questions = [
    {
      "question": "Which keyword is used to define a function in Python?",
      "option": ["function", "def", "define", "fun"],
      "answer": "def"
    },
    {
      "question": "What is the correct file extension for Python files?",
      "option": [".pyth", ".pt", ".py", ".pyt"],
      "answer": ".py"
    },
    {
      "question": "Which of the following is a valid variable name in Python?",
      "option": ["1name", "name_1", "name-1", "@name"],
      "answer": "name_1"
    },
    {
      "question": "What is the output of print(2 ** 3)?",
      "option": ["6", "8", "9", "5"],
      "answer": "8"
    },
    {
      "question": "Which data type is used to store text?",
      "option": ["int", "float", "str", "bool"],
      "answer": "str"
    },
    {
      "question": "What is the output of print(typeof(true))?",
      "option": ["<class 'int'>", "<class 'str'>", "<class 'bool'>", "<class 'float'>"],
      "answer": "<class 'bool'>"
    },
    {
      "question": "Which operator is used for floor division?",
      "option": ["/", "//", "%", "**"],
      "answer": "//"
    },
    {
      "question": "What is the output of len('Python')?",
      "option": ["5", "6", "7", "Error"],
      "answer": "6"
    },
    {
      "question": "Which of these is used to start a comment in Python?",
      "option": ["//", "/*", "#", "--"],
      "answer": "#"
    },
    {
      "question": "What will print(bool(0)) return?",
      "option": ["True", "False", "0", "None"],
      "answer": "False"
    },
    {
      "question": "How do you insert comments in Python code?",
      "option": ["// comment", "/* comment */", "# comment", "<!-- comment -->"],
      "answer": "# comment"
    },
    {
      "question": "What will print(10 % 3) output?",
      "option": ["3", "1", "0", "10"],
      "answer": "1"
    },
    {
      "question": "What is the correct way to create a list?",
      "option": ["list = (1,2,3)", "list = {1,2,3}", "list = [1,2,3]", "list = <1,2,3>"],
      "answer": "list = [1,2,3]"
    },
    {
      "question": "Which of the following is a Python tuple?",
      "option": ["[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "<1, 2, 3>"],
      "answer": "(1, 2, 3)"
    },
    {
      "question": "How do you start a loop in Python?",
      "option": ["for x in y:", "loop(x):", "foreach x in y:", "for (x in y)"],
      "answer": "for x in y:"
    },
    {
      "question": "What is the correct syntax for a while loop?",
      "option": ["while (x > 0)", "while x > 0:", "while x > 0 then", "do while x > 0:"],
      "answer": "while x > 0:"
    },
    {
      "question": "How do you check if a is equal to b in Python?",
      "option": ["a = b", "a == b", "a === b", "a equals b"],
      "answer": "a == b"
    },
    {
      "question": "Which built-in function returns the largest item?",
      "option": ["largest()", "max()", "maximum()", "biggest()"],
      "answer": "max()"
    },
    {
      "question": "What is the output of print('Hello' + 'World')?",
      "option": ["Hello World", "HelloWorld", "Hello+World", "Error"],
      "answer": "HelloWorld"
    },
    {
      "question": "What is the correct way to define a dictionary?",
      "option": ["d = [1: 'one']", "d = (1: 'one')", "d = {1: 'one'}", "d = <1: 'one'>"],
      "answer": "d = {1: 'one'}"
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "option": ["input()", "get()", "scanf()", "read()"],
        "answer": "input()"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "option": ["catch", "except", "error", "handle"],
        "answer": "except"
    },
    {
        "question": "What is the correct way to write a function that returns a value?",
        "option": ["function myFunc(): return 5", "def myFunc(): return 5", "define myFunc(): return 5", "fun myFunc(): return 5"],
        "answer": "def myFunc(): return 5"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "option": ["tuple", "str", "list", "int"],
        "answer": "list"
    },
    {
        "question": "What will be the output of print(type(3.14))?",
        "option": ["<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'double'>"],
        "answer": "<class 'float'>"
    }
    ]
    

# Intialize the random if none exixts in the session state.
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(all_questions)

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