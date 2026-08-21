def validate_release_notes(
    release_notes,
    pr_title,
    pr_description
):
    source_text = (
        pr_title + " " + pr_description
    ).lower()

    suspicious_phrases = [
        "resolved a bug",
        "fixed a bug",
        "updated the code",
        "new feature",
        "api",
        "database",
        "framework",
        "function",
        "class",
    ]

    for phrase in suspicious_phrases:
        if phrase in release_notes.lower():
            if phrase not in source_text:
                return False

    return True