
import streamlit as st
import random

# Page Settings
st.set_page_config(page_title="Quiz Master", page_icon="🎯")

st.title("🎯 Quiz Master")
st.write("Test your knowledge and see your score!")

# Quiz Questions
quiz_data = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "What data type stores True or False?",
            "options": ["int", "str", "bool", "list"],
            "answer": "bool"
        },
        {
            "question": "What is the output of 2 + 3 * 4?",
            "options": ["12", "10", "14", "0"],
            "answer": "14"
        }
    ],
    "Science": [
        {
            "question": "Which organ pumps blood?",
            "options": ["Brain", "Liver", "Heart", "Ear"],
            "answer": "Heart"
        },
        {
            "question": "Which planet is called the Red Planet?",
            "options": ["Jupiter", "Earth", "Sun", "Mars"],
            "answer": "Mars"
        }
    ],
    "General Knowledge": [
        {
            "question": "Which is the capital of India?",
            "options": ["Mumbai", "Delhi", "Chennai", "Goa"],
            "answer": "Delhi"
        },
        {
            "question": "Which is the smallest continent?",
            "options": ["Asia", "Africa", "Europe", "Australia"],
            "answer": "Australia"
        }
    ]
}

st.divider()

# Select Category
category = st.selectbox(
    "Choose a Quiz Category",
    list(quiz_data.keys())
)

# Number of Questions
count = st.slider(
    "Number of Questions",
    1,
    len(quiz_data[category]),
    min(3, len(quiz_data[category]))
)

# Start New Quiz
if st.button("Start New Quiz"):
    st.session_state.quiz_questions = random.sample(
        quiz_data[category], count
    )
    st.session_state.quiz_started = True
    st.session_state.quiz_submitted = False

# Display Quiz
if st.session_state.get("quiz_started", False):
    questions = st.session_state.quiz_questions

    st.subheader("📝 Answer the Questions")

    with st.form("quiz_form"):
        answers = []

        for i, q in enumerate(questions):
            st.write(f"**Q{i + 1}. {q['question']}**")

            answer = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"answer_{i}",
                index=None
            )
            answers.append(answer)

        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        score = 0

        for q, answer in zip(questions, answers):
            if answer == q["answer"]:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.quiz_submitted = True

    # Show Result
    if st.session_state.get("quiz_submitted", False):
        score = st.session_state.quiz_score

        st.success(
            f"🎉 Your Score: {score}/{len(questions)}"
        )

        for i, q in enumerate(questions):
            st.write(f"**Q{i + 1}. {q['question']}**")
            st.write(f"Correct Answer: {q['answer']}")

        if st.button("Play Again"):
            st.session_state.quiz_started = False
            st.session_state.quiz_submitted = False
            st.rerun()
