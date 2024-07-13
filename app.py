from langflow.load import run_flow_from_json

question = input("Enter your question: ")

result = run_flow_from_json(flow="example.json",
                            input_value=question,
                            fallback_to_env_vars=True)

print(result)
