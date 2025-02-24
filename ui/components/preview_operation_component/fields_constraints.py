from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field


class FieldTypes(StrEnum):
    ENUM = 'ENUM',
    CHECKBOX = 'CHECKBOX'
    RANGE = 'RANGE'


class OperationField(BaseModel):
    field_type: FieldTypes = None
    param_name: str
    default_value: int | float | bool | StrEnum = None
    current_value: int | float | bool | StrEnum = Field(default_factory=lambda: 'default')
    min_value: Optional[int | float] = None
    max_value: Optional[int | float] = None
    step: Optional[int | float] = None
    values: Optional[StrEnum] = None

    def model_post_init(self, __context):
        self.current_value = self.default_value





