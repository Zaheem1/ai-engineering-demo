def generate_release_notes(commits: list[str]) -> str:
    """
    Turn a list of commit messages into simple, human-readable
    release notes. Replace this with an actual LLM call as needed.
    """
    if not commits:
        return "No changes in this release."

    bullet_points = "\n".join(f"- {commit.strip()}" for commit in commits)
    return f"## Release Notes\n\n{bullet_points}"
