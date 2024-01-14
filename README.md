# Chatbot QAGenerate AzureOpenAI

## Demo
https://github.com/nguyenlykhanhlinh/Chatbot_QAGenerate_AzureOpenAI/assets/100570402/a98abd31-cfe9-4502-ba72-e3b7ca0b78fe

## Problem
  1. Cognitive Overload: Students often face challenges with information overload in traditional learning, impacting processing and retention.
  2. Limited Interactivity: Current educational methods lack engagement, affecting students' absorption of material.
  3. Insufficient Practice Opportunities: Without regular, targeted practice, students may struggle to internalize knowledge, hindering deeper understanding.
## Idea
>We propose the development of a chatbot, QAGenerate AzureOpenAI, designed to generate questions based on content to support student learning.

>Our primary focus is to empower students with an engaging and relevant learning tool. The chatbot will analyze documents submitted by students and generate context-specific, fitting questions. This approach aims to facilitate a deeper understanding of the document's content.

  1. Engagement: The interactive nature of the chatbot promotes active participation and sustained interest in the learning process.

  2. Document Analysis: Thorough analysis of provided documents ensures relevance in question generation.

  3. Relevance: Context-specific questions ensure that students focus on essential aspects, promoting effective learning.

## Technical Solution
### _Technologies Used_
  1. Azure OpenAI: Utilized for interacting with AI models. It harnesses powerful natural language processing capabilities to comprehend and analyze textual content, enabling the generation of relevant questions.

  2. Dotenv (python-dotenv): This library manages environment variables to enhance security and flexibility, safely storing API keys and other sensitive information required for interacting with external services.

  3. OpenAI Python Package: Employed to seamlessly communicate with the Azure OpenAI API, enhancing the precision and relevance of the questions generated.

  4. Streamlit: The library for building user interfaces for applications. Streamlit provides an intuitive and responsive interface, allowing users to interact with the chatbot, receive generated questions, and track their learning progress.

## Getting Started

### _Prerequisites_
  1. Streamlit
  2. Azure OpenAI API Key
  3. Python environment with required packages
### _Steps:_
  1. Clone the repository
  2. Set up environment variables using OpenAI
  3. Install dependencies
     ```
     pip install -r requirements.txt
     ```
  5. Start the chatbot by command
     ```
     streamlit run app.py
     ```
### _Hosted Version_
  - If you prefer not to set up locally, you can use the hosted version of QAGenerate AzureOpenAI at example-hosted-link.

## Contribute 🤝
_Team leader_ 🥇 
  - Nguyễn Lý Khánh Linh

_Member_ 🥈
  - Phan Thành Đạt
  - Phùng Bá Công
  - Đỗ Văn Hảo
