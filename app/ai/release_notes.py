import ollama


MODEL = "tinyllama:latest"


def generate_summary(pr_title, pr_description):

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

    print(
        "Generating summary... "
        "this may take a minute or two on tinyllama."
    )

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()