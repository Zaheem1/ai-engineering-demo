from app.ai.github import get_pull_request
from app.ai.release_notes import generate_summary
from app.ai.notion import create_release_note


# Get real GitHub Pull Request
pr = get_pull_request(1)

pr_title = pr["title"]
pr_description = pr["description"]
pr_number = str(pr["number"])
pr_author = pr["author"]


# Generate only a summary with AI
summary = generate_summary(
    pr_title,
    pr_description
)


# Python controls the final structure
release_notes = f"""# Release Notes

## Summary

{summary}

## Changes

{pr_description}

## Technical Details

No technical details were provided.
"""


print("Generated Release Notes:")
print(release_notes)


# Save to Notion
create_release_note(
    title=pr_title,
    pr_number=pr_number,
    pr_author=pr_author,
    status="Testing",
    summary=summary,
    release_notes=release_notes,
    created_by="AI Release Notes Skill",
)