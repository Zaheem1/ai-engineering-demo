from app.ai.release_notes import generate_release_notes


def test_generate_release_notes_empty():
    assert generate_release_notes([]) == "No changes in this release."


def test_generate_release_notes_with_commits():
    commits = ["Fix login bug", "Add dark mode"]
    result = generate_release_notes(commits)

    assert "## Release Notes" in result
    assert "- Fix login bug" in result
    assert "- Add dark mode" in result
