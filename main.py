import os
from openai import AzureOpenAI
from dotenv import dotenv_values, find_dotenv, load_dotenv
import streamlit as st

load_dotenv(find_dotenv())

# Create AzureOpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Streamlit app
st.title("Azure OpenAI Quiz App")

# User input for text content
initial_text_content = st.text_area("Enter the initial text content:")

# Initialize session_state if it doesn't exist
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []

# Check if the user has entered text content
if initial_text_content and st.button("Generate Questions"):
    # Generate 10 multiple-choice questions and answers based on the entered text content
    for i in range(10):
        response = client.chat.completions.create(
            model="GPT35TURBO",
            messages=[
                {"role": "system", "content": "You are a quiz assistant."},
                {"role": "user", "content": f"Generate a multiple-choice question {i + 1} based on the following text:\n{initial_text_content}"}
            ]
        )

        # Extract the assistant's response from the user's message
        question = response.choices[0].message.content

        response2 = client.chat.completions.create(
            model="GPT35TURBO",
            messages=[
                {"role": "system", "content": "You are a quiz assistant."},
                {"role": "user", "content": f"Base on multiple-choice {question} {i + 1} and the following text:\n{initial_text_content} give me the correct answer A, B, C or D"}
            ]
        )
        correct_answer_input = response2.choices[0].message.content

        # Extract the correct answer from the list of answer choices
        correct_answer = next((choice for choice in ['A', 'B', 'C', 'D'] if choice in correct_answer_input), None)

        # Generate four random answer choices (A, B, C, D)
        answer_choices = ['A', 'B', 'C', 'D']

        # Shuffle the answer choices to randomize the order
        import random
        random.shuffle(answer_choices)

        # Create a dictionary to store question, answer choices, and correct answer
        quiz_item = {
            "question": question,
            "answer_choices": answer_choices,
            "correct_answer": correct_answer,
        }

        st.session_state.quiz_data.append(quiz_item)

# Display questions and answer choices
for i, quiz_item in enumerate(st.session_state.quiz_data):
    expander = st.expander(f"Question {i + 1}")
    expander.write(quiz_item["question"])

    # Display answer choices as radio buttons
    selected_answer = expander.radio("Select an answer:", quiz_item["answer_choices"], key=f"answer_{i}")

    if expander.button("Show Answer", key=f"show_answer_{i}"):
        # Check if the selected answer is correct
        is_correct = (selected_answer == quiz_item["correct_answer"])
        expander.write(f"Your selected answer: {selected_answer}")
        expander.write(f"Correct Answer: {quiz_item['correct_answer']}")
        expander.write(f"Result: {'Correct! ' + chr(0x1F389) if is_correct else 'Incorrect! ' + chr(0x1F61F)}")
