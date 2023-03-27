from fastapi import APIRouter

from app.models.level_model import LevelsModelResponse, LevelModel, ProgressType, LetterType

router = APIRouter()

in_progress_level = LevelModel(
    id=1,
    progress=ProgressType.IN_PROGRESS,
    words=[
        ["п", LetterType.MISS],
        ["о", LetterType.EXIST],
        ["л", LetterType.MATCH],
        ["к", LetterType.MISS],
        ["а", LetterType.MISS],
    ],
)


@router.get("")
def get_levels(limit: int = 10, offset: int = 0) -> LevelsModelResponse:
    return LevelsModelResponse(__root__=[in_progress_level.copy(update={"id": i}) for i in range(1, limit + 1)])


@router.get("/{id}")
def get_level(id) -> LevelModel:
    return in_progress_level.copy(update={"id": id})


@router.post("/{id}/word")
def send_word(id):
    return {"id": id}
