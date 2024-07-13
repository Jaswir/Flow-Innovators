from langflow.load import run_flow_from_json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

question = input("Enter your question: ")

result = run_flow_from_json(flow="Priority and Depth Agents.json", # You can adjust this to your flow file name
                            input_value=question,
                            fallback_to_env_vars=True)

print(result[0].outputs[0].results)
