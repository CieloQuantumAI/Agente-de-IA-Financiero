from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()

# Define the Web Agent
web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    #model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources"],
)

# Define the Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    #model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."],
)

# Create the agent team
agent_team = Agent(
    team=[web_agent, finance_agent],
    #model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

# Run the query
agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
