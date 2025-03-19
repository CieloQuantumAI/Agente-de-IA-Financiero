from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

import sys
import os

load_dotenv()


print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    #model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."],
    #debug_mode=True
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")