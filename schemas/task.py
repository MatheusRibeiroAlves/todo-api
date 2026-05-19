from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class taskCreate(BaseModel):
    title: str
    description:Optional[str] = None
    
class taskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    
class taskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    
class config:
    from_attributes = True
    