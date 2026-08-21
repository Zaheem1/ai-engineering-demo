from unittest.mock import patch, MagicMock

from app.ai.release_notes import generate_release_notes


@patch("app.ai.release_notes.requests.post")
def test_generate_release_notes_returns_summary(mock_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "message": {
            "content": "Added JWT authentication and protected API routes."
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    result = generate_release_notes(
        "Add user authentication",
        "Added JWT authentication and protected API routes.",
    )

    assert result == "Added JWT authentication and protected API routes."
    mock_post.assert_called_once()


@patch("app.ai.release_notes.requests.post")
def test_generate_release_notes_sends_correct_prompt_content(mock_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "message": {"content": "Some summary."}
    }
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    generate_release_notes("My PR Title", "My PR Description")

    _, kwargs = mock_post.call_args
    sent_prompt = kwargs["json"]["messages"][0]["content"]

    assert "My PR Title" in sent_prompt
    assert "My PR Description" in sent_prompt