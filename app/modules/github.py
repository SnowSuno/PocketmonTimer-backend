import requests
from fastapi import HTTPException

from app.core.config import settings


def get_github_commits(username: str) -> int:
    try:
        res = requests.get(
            f"https://api.github.com/search/commits?q=author:{username}",
            headers={"Authorization": f"bearer {settings.GITHUB_TOKEN}"},
        ).json()

        if "total_count" not in res:
            raise HTTPException(
                status_code=404,
                detail="No such user found"
            )

        return res["total_count"]
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
