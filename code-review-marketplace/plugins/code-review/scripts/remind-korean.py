"""
PostToolUse hook: injected into Claude's context after every tool use.
Forces all responses to be written in Korean.
ASCII-only output to stay safe on cp949 (Korean Windows) consoles.
"""
print("LANGUAGE RULE: You MUST write all responses to the user in Korean. Do not respond in English.")
