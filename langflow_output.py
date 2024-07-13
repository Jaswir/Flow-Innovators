from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-jmUEb": {},
  "Prompt-zYCPB": {},
  "ChatOutput-ULViL": {},
  "OpenAIModel-Wg3K9": {}
}

result = run_flow_from_json(flow="Priorities_Agent.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

print(result)