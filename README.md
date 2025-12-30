# Finance AI Agent

An experimental **AI-powered finance and web research agent system** built with the **Phi framework**, **Groq / OpenAI models**, and real-time data tools like **Yahoo Finance** and **DuckDuckGo**.

This project demonstrates:

* A **simple LLM agent**
* A **dedicated finance analysis agent**
* A **multi-agent team** that collaborates to combine financial data with real-time web research

---

## 🔧 Tech Stack

* **Python 3.9+**
* **Phi Agents** (`phi.agent.Agent`)
* **LLM Providers**:

  * Groq (`llama-3.3-70b-versatile`)
  * OpenAI (`gpt-4o`)
* **Tools**:

  * Yahoo Finance (`YFinanceTools`)
  * DuckDuckGo Search
  * Newspaper4k (optional news extraction)
* **Environment Management**: `python-dotenv`

---

## 📁 Project Structure

```
.
├── 1_simple_groq_agent.py     # Minimal Groq-powered LLM agent
├── 2_finance_agent.py         # Finance-focused AI agent using Yahoo Finance
├── 3_agent_teams.py           # Multi-agent team (Web + Finance)
├── .env                       # API keys (not committed)
└── README.md
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

Install dependencies:

```
pip install phi-ai python-dotenv yfinance duckduckgo-search newspaper4k
```

---

## 🚀 Scripts Overview

### 1️⃣ Simple Groq Agent

**File:** `1_simple_groq_agent.py`

A minimal example showing how to:

* Load environment variables
* Initialize a Groq-powered LLM agent
* Send a prompt and receive a response

**Example Prompt:**

> Write a 2 line poem about birds

This is ideal for validating your setup and API keys.

---

### 2️⃣ Finance AI Agent

**File:** `2_finance_agent.py`

A specialized **financial analysis agent** that:

* Uses Yahoo Finance data
* Retrieves:

  * Stock prices
  * Analyst recommendations
  * Company fundamentals
* Formats results using **tables**

**Example Use Case:**

> Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA

This agent is optimized for **equity research and market comparison tasks**.

---

### 3️⃣ Multi-Agent Team (Web + Finance)

**File:** `3_agent_teams.py`

Demonstrates **agent collaboration** using a team-based architecture:

#### Agents Included:

* **Web Agent**

  * Searches the web using DuckDuckGo
  * Always includes sources

* **Finance Agent**

  * Pulls structured financial data from Yahoo Finance
  * Displays results in tables

* **Agent Team**

  * Routes tasks to the appropriate agent
  * Merges financial data with recent news

**Example Query:**

> Summarize analyst recommendations and share the latest news for NVDA

This pattern is powerful for **investment research, due diligence, and market intelligence tools**.

---

## 🧠 Key Concepts Demonstrated

* Tool-augmented LLMs
* Real-time financial data retrieval
* Multi-agent orchestration
* Structured outputs with markdown tables
* Model switching between Groq and OpenAI

---

## 🛠️ Customization Ideas

* Add SEC filing analysis
* Plug in vector databases for RAG
* Deploy as a FastAPI or Streamlit app
* Schedule agents for daily market summaries
* Add portfolio-level analytics

---

## ⚠️ Disclaimer

This project is for **educational and experimental purposes only**. It does **not** constitute financial advice.

---

## 👤 Author

Built by **Cielo / Andromeda AI**

Focused on AI agents, automation, and real-world business intelligence.

