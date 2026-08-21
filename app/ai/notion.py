import os

from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")


def create_skill(
    name,
    version,
    status,
    owner,
    input_data,
    output_data,
    description,
):
    response = notion.pages.create(
        parent={
            "database_id": database_id
        },
        properties={
            "Skill Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Version": {
                "rich_text": [
                    {
                        "text": {
                            "content": version
                        }
                    }
                ]
            },
            "Status": {
                "select": {
                    "name": status
                }
            },
            "Owner": {
                "rich_text": [
                    {
                        "text": {
                            "content": owner
                        }
                    }
                ]
            },
            "Input": {
                "rich_text": [
                    {
                        "text": {
                            "content": input_data
                        }
                    }
                ]
            },
            "Output": {
                "rich_text": [
                    {
                        "text": {
                            "content": output_data
                        }
                    }
                ]
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
        },
    )

    print("Skill created successfully!")
    print("Page ID:", response["id"])


def create_release_note(
    title,
    pr_number,
    pr_author,
    status,
    summary,
    release_notes,
    created_by,
):
    response = notion.pages.create(
        parent={
            "database_id": os.getenv("RELEASE_NOTES_DATABASE_ID")
        },
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "PR Number": {
                "rich_text": [
                    {
                        "text": {
                            "content": pr_number
                        }
                    }
                ]
            },
            "PR Author": {
                "rich_text": [
                    {
                        "text": {
                            "content": pr_author
                        }
                    }
                ]
            },
            "Status": {
                "select": {
                    "name": status
                }
            },
            "Summary": {
                "rich_text": [
                    {
                        "text": {
                            "content": summary
                        }
                    }
                ]
            },
            "Release Notes": {
                "rich_text": [
                    {
                        "text": {
                            "content": release_notes[:2000]
                        }
                    }
                ]
            },
            "Created By": {
                "rich_text": [
                    {
                        "text": {
                            "content": created_by
                        }
                    }
                ]
            },
        },
    )

    print("Release note created successfully!")
    print("Page ID:", response["id"])


if __name__ == "__main__":
    create_skill(
        name="Generate Release Notes",
        version="1.0.0",
        status="Testing",
        owner="Zaheem",
        input_data="GitHub PR title and description",
        output_data="Markdown release notes",
        description="Generates concise release notes from GitHub pull request information.",
    )

    create_release_note(
        title="Add user authentication",
        pr_number="PR-001",
        pr_author="Zaheem",
        status="Testing",
        summary="Added authentication functionality.",
        release_notes="""
# Release Notes

## Feature

Add user authentication

## Description

Added JWT authentication and protected API routes.
""",
        created_by="AI Release Notes Skill",
    )