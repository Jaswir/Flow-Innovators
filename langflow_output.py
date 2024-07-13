from langflow.load import run_flow_from_json
from langflow.graph.schema import RunOutputs
from dotenv import load_dotenv
import os

# Environment Variables
load_dotenv()


def getResponseFromLangFlow():
    message = "Backstory: the student failed the exam, 3 times. Student Experieence: I can understand the topics generally but I can't understand the mathematical formulations, my biggest challenges for the course is to understand mathematical formulations"

    response = run_flow_from_json(
        flow="Priority and Depth Agents.json",
        input_value=message,
        fallback_to_env_vars=True,  # False by default
    )

    output_text = response
    return output_text

# result = RunOutputs(getResponseFromLangFlow()[0])
result = getResponseFromLangFlow()[0].outputs[0].results['message'].text

print(type(result))
print(result)

