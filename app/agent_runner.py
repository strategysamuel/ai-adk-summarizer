from google import genai
from app.tools import SummarizeTool
from app.agent import SummarizerAgent
from app.config import GOOGLE_API_KEY

# Create client (NEW SDK way)
client = genai.Client(api_key=GOOGLE_API_KEY)

# Pass client to tool
tool = SummarizeTool(client)

# Create agent
agent = SummarizerAgent(client, tool)

def run_agent(input_text: str) -> str:
    return agent.run(input_text)