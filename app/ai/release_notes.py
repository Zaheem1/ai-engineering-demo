import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL = os.getenv("OLLAMA_MODEL", "tinyllama:latest")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")


def generate_release_notes(pr_title, pr_description):
    prompt = f"""
Summarize the following GitHub Pull Request in ONE sentence.

Title:
{pr_title}

Description:
{pr_description}

Use ONLY the information provided above.
Do not add facts.
Do not mention code, APIs, functions, bugs, frameworks, or technologies
unless they are explicitly mentioned.
Return only the one-sentence summary.
"""

    print("Generating release notes... this may take a minute or two on tinyllama.")

    response = requests.post(
        f"{OLLAMA_HOST}/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()
    data = response.json()

    return data["message"]["content"].strip()


if __name__ == "__main__":
    title = "Add authentication helper"

    description = """
    Added authentication helper functionality.

    Changes:
    - Added authentication helper
    - Added authentication validation
    - Improved authentication flow
    """

    notes = generate_release_notes(
        title,
        description
    )

    print(notes)