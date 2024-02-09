from pydantic import BaseModel
from typing import List, Optional

class ArrayRequest(BaseModel):
    array: List[int]
    algorithms: List[str]
    k: Optional[int] = None    