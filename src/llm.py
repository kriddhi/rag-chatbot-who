import subprocess

def generate_response(prompt):
    full_prompt = f"""
You are World Health Organization Assist, a helpful and professional healthcare knowledge assistant.
Be clear, structured, and concise. Be as detailed as possible when answering the prompt. 

{prompt}
"""

    result = subprocess.run(
        ["ollama", "run", "gemma3"],
        input=full_prompt.encode(),
        stdout=subprocess.PIPE
    )

    return result.stdout.decode()
