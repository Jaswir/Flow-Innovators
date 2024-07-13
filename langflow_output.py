from langflow.load import run_flow_from_json
from langflow.graph.schema import RunOutputs
from dotenv import load_dotenv
import os

# Environment Variables
load_dotenv()


def getResponseFromLangFlow(question):
    response = run_flow_from_json(
        flow="Priority and Depth Agents.json",
        input_value=question,
        fallback_to_env_vars=True,  # False by default
    )

    output_text = response[0].outputs[0].results['message'].text
    return output_text

# result = RunOutputs(getResponseFromLangFlow()[0])
# result = getResponseFromLangFlow()[0].outputs[0].results['message'].text

# print(type(result))
# print(result)

