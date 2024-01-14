Chatbot QAGenerate AzureOpenAI
Problem
Cognitive Overload: Students often face challenges with information overload in traditional learning, impacting processing and retention.

Limited Interactivity: Current educational methods lack engagement, affecting students' absorption of material.

Insufficient Practice Opportunities: Without regular, targeted practice, students may struggle to internalize knowledge, hindering deeper understanding.

Idea
We propose the development of a chatbot, QAGenerate AzureOpenAI, designed to generate questions based on content to support student learning.

Our primary focus is to empower students with an engaging and relevant learning tool. The chatbot will analyze documents submitted by students and generate context-specific, fitting questions. This approach aims to facilitate a deeper understanding of the document's content.

Engagement: The interactive nature of the chatbot promotes active participation and sustained interest in the learning process.

Document Analysis: Thorough analysis of provided documents ensures relevance in question generation.

Relevance: Context-specific questions ensure that students focus on essential aspects, promoting effective learning.

Technical Solution
Technologies Used:
Azure OpenAI: Utilized for interacting with AI models. It harnesses powerful natural language processing capabilities to comprehend and analyze textual content, enabling the generation of relevant questions.

Dotenv (python-dotenv): This library manages environment variables to enhance security and flexibility, safely storing API keys and other sensitive information required for interacting with external services.

OpenAI Python Package: Employed to seamlessly communicate with the Azure OpenAI API, enhancing the precision and relevance of the questions generated.

Streamlit: The library for building user interfaces for applications. Streamlit provides an intuitive and responsive interface, allowing users to interact with the chatbot, receive generated questions, and track their learning progress.

Getting Started
Prerequisites:
Node.js v18
Azure OpenAI API Key
Python environment with required packages installed
Steps:
Clone the repository
Set up environment variables using Dotenv
Install dependencies: npm install
Run the application: npm run dev
Visit http://localhost:3000 to interact with the chatbot
Hosted Version
If you prefer not to set up locally, you can use the hosted version of QAGenerate AzureOpenAI at example-hosted-link.

Contribute 🤝
We welcome contributions to enhance and improve QAGenerate AzureOpenAI. Feel free to open issues or submit pull requests.

Open Issues
Open Pull Requests
License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Community
Join the Discord community at Community Discord Link to get support with setting up and using QAGenerate AzureOpenAI.
