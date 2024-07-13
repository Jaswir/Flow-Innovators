from langflow.load import run_flow_from_json
from langflow.graph.schema import RunOutputs
from dotenv import load_dotenv
import os

# Environment Variables
load_dotenv()

TWEAKS = {
  "Prompt-THgGW": {},
  "ChatInput-4pXK9": {},
  "ChatOutput-39xM2": {},
  "OpenAIModel-WK9I0": {},
  "ParseData-AdEkx": {},
  "File-OKJZs": {}
}

result = run_flow_from_json(flow="file uploader + parser to text.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

print(result)