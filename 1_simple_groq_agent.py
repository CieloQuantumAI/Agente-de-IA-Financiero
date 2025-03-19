from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv

import sys
import os

load_dotenv()

print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Write a 2 line poem about birds")