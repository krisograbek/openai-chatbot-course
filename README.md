# GPT-4 Powered Chatbot with OpenAI API and Streamlit

This repository is designed to help you build your first chatbot using Python, OpenAI API, and Streamlit. 

This project includes a combination of text, videos, and code to guide you step-by-step from understanding Large Language Models (LLMs) to building and running a working chatbot.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

## Project Overview

This project provides a complete guide on how to build a GPT-4 powered chatbot using the OpenAI API and Streamlit. You’ll learn how to interact with the OpenAI API, understand LLM parameters, and deploy a user-friendly chatbot interface in Python.

By the end of this project, you will:

- Understand the core principles of LLMs.
- Know how to use the OpenAI API for chatbot development.
- Build an interactive chatbot using Python and Streamlit.
- Optimize responses using tokens and LLM parameters.

## Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Python 3.8+**
- **pip** (Python package installer)

You will also need an **OpenAI API Key**, which you can obtain by signing up at [OpenAI's platform](https://beta.openai.com/signup).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gpt-4-chatbot.git
   cd gpt-4-chatbot
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API Key:**

   Create a `.env` file in the root directory of the project and add your OpenAI API Key as follows:
   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

To run the chatbot locally:

1. **Run the Streamlit app:**
   ```bash
   streamlit run basic-st-app.py
   ```

2. **Start interacting with your chatbot through the browser!**

Head to `localhost:8501`...
You’ll be able to modify the chatbot's behavior through Streamlit and experiment with different GPT-4 models.

## License

This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.

