from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_user():
    return {"message": "get_user"}


@router.post("/register")
def register():
    return {"message": "register"}
