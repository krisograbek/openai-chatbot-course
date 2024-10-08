# GPT-4 Powered Chatbot with OpenAI API and Streamlit

This repository serves as a practical companion to [this online course](https://krisograbek.gumroad.com/l/aichatbot) for building your first AI Chatbot.

I highly recommend checking the course because it is designed to help you build your first chatbot using Python, OpenAI API, and Streamlit. 
It includes a combination of text, videos, and code to guide you step-by-step from understanding Large Language Models (LLMs) to building and running a working chatbot.

**You can access the full course [here](https://krisograbek.gumroad.com/l/aichatbot)**.

### Here's what we're building:

![GPT4oChatbotSmall](https://github.com/user-attachments/assets/db704f99-2163-48f4-a3da-3bbc28ce7542)


## Table of Contents


1. [Project Overview](#project-overview)
2. [File Descriptions](#file-descriptions)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [License](#license)

## Project Overview

This project provides a complete guide on how to build a GPT-4 powered chatbot using the OpenAI API and Streamlit. You’ll learn how to interact with the OpenAI API, understand LLM parameters, and deploy a user-friendly chatbot interface in Python.

By the end of this project, you will:

- Understand the core principles of LLMs.
- Know how to use the OpenAI API for chatbot development.
- Build an interactive chatbot using Python and Streamlit.
- Optimize responses using tokens and LLM parameters.

## File Descriptions
Inside, you'll find 3 notebooks and 3 Python scripts with OpenAI API and Streamlit.

### Notebooks
- **[openai-api-tutorial.ipynb](./openai-api-tutorial.ipynb)**: A beginner-friendly notebook that guides users through interacting with the OpenAI API, including generating responses and streaming output.
- **[api-tutorial-new.ipynb](./api-tutorial-new.ipynb)** (_Part 3 in the course_): A Jupyter notebook demonstrating how to interact with the OpenAI API, including making API requests and processing responses.
- **[token-tutorial.ipynb](./token-tutorial.ipynb)** (_Part 4 in the course_): A tutorial notebook explaining how tokens work in OpenAI models, including how to count tokens and use tokenizers.


### Python Scripts
- **[basic-st-app.py](./basic-st-app.py)** (_Part 5 in the course_): The simplest Streamlit app file for running calling OpenAI API using Streamlits basic elements.
- **[simplest_chatbot.py](./simplest_chatbot.py)** (_Part 5 in the course_): A minimal example of a chatbot implementation using the OpenAI API and Streamlit. You'll do OpenAI API calls but the chatbot itself won't work as expected.
- **[chatbot.py](./chatbot.py)** (_Part 5 in the course_): Core chatbot logic, using the OpenAI API to generate responses and stream real-time output back to the user.


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
   streamlit run chatbot.py
   ```

2. **Start interacting with your chatbot through the browser!**

Head to `localhost:8501` and you'll be able to use your own chatbot!

## License

This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.

