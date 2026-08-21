from release_notes import generate_release_notes
from notion import create_release_note


# Simulated GitHub Pull Request
pr_title = "Add user authentication"

pr_description = """
Added JWT authentication.
Added login API.
Added protected routes.
"""

pr_number = "PR-001"
pr_author = "Zaheem"


# Step 1: Generate release notes
release_notes = generate_release_notes(
    pr_title,
    pr_description
)

print("Generated Release Notes:")
print(release_notes)


# Step 2: Save the result to Notion
create_release_note(
    title=pr_title,
    pr_number=pr_number,
    pr_author=pr_author,
    status="Testing",
    summary="Added user authentication functionality.",
    release_notes=release_notes,
    created_by="AI Release Notes Skill",
)