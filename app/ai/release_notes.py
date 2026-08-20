def generate_release_notes(pr_title, pr_description):
    return f"""
# Release Notes

## Feature

{pr_title}

## Description

{pr_description}
"""


if __name__ == "__main__":
    title = "Add user authentication"
    description = "Added JWT authentication and protected API routes."

    notes = generate_release_notes(title, description)

    print(notes)