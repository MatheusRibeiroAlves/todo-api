from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class taskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description:Optional[str] = Field(None, max_length=500)
    
class taskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None
    
class taskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    
class config:
    from_attributes = True
    