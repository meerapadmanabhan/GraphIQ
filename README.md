# GraphIQ

GraphIQ is an AI-powered chatbot developed using **Streamlit** and **LangGraph**.  
It integrates multiple tools to enhance user interaction and can be run both locally and deployed for broader access.

<img width="155" height="333" alt="output" src="https://github.com/user-attachments/assets/e83d8ccb-aba1-4832-b7be-03132977704c" />

---

## Features

- **Multi-Tool Integration**: Seamlessly combines various tools to provide comprehensive responses.
- **Interactive Interface**: Built with Streamlit for a user-friendly experience.
- **Flexible Deployment**: Supports both local execution and cloud deployment.
- **Modular Design**: Easily extendable with additional tools and functionalities.

---

## Tech Stack & Tools

GraphIQ uses the following tools and frameworks:

- **Python** – Core programming language
- **Streamlit** – For building interactive web interfaces
- **LangGraph** – To orchestrate multiple tools and manage chatbot states
- **Jupyter Notebook** – For interactive experimentation and testing
- **.env files** – For secure configuration of API keys and environment variables
- **Git & GitHub** – Version control and code hosting

---

### External Knowledge Sources

- **ArXiv** – Provides access to academic research papers; used by GraphIQ to fetch scientific and technical information for queries.
- **Wikipedia** – A general-purpose knowledge source; used to answer factual questions and provide detailed explanations.
- **Talivy** – Acts as a real-time web data provider.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**

```bash
git clone https://github.com/meerapadmanabhan/GraphIQ.git
cd GraphIQ
```


2. **Set Up a Virtual Environment**

```bash
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate
```
3. **Install Dependencies**
```bash
   pip install -r requirements.txt
```
4. **Running Locally**
```bash
   streamlit run app.py
```
