from fastapi import APIRouter

router = APIRouter()


@router.post("")
def get_tokens():
    return {"message": "get_tokens"}


@router.post("/refresh")
def refresh_token():
    return {"message": "refresh_token"}


@router.post("/blacklist")
def blacklist_token():
    return {"message": "blacklist_token"}
