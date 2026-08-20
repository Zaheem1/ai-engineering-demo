from fastapi import APIRouter

from app.ai.release_notes import generate_release_notes

router = APIRouter()


@router.post("/release-notes")
async def release_notes_endpoint(commits: list[str]):
    """Generate release notes from a list of commit messages."""
    notes = generate_release_notes(commits)
    return {"release_notes": notes}
