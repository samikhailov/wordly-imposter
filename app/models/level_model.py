from enum import Enum

from pydantic import BaseModel


class ProgressType(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class LetterType(str, Enum):
    MATCH = "MATCH"
    EXIST = "EXIST"
    MISS = "MISS"


class LevelModel(BaseModel):
    id: int
    progress: ProgressType
    words: list[list[str, LetterType]]


class LevelsModelResponse(BaseModel):
    __root__: list[LevelModel]
