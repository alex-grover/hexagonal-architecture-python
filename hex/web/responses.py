from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class ErrorResponse:
    status: int
    title: str
    detail: str
    path: str
    timestamp: datetime = datetime.now()
