import requests
from fastapi import HTTPException

from app.core.config import settings


def get_github_commits(username: str) -> int:
    try:
        return requests.get(
            f"https://api.github.com/search/commits?q=author:{username}",
            headers={"Authorization": f"bearer {settings.GITHUB_TOKEN}"},
        ).json()["total_count"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    # For testing
    print(get_github_commits("snowsuno"))
