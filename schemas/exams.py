from pydantic import BaseModel,Field
from datetime import datetime

class ExamBase(BaseModel):
    group__id: int = Field(description="ID of the group that will take exam")
    teacher_id: int = Field(description="ID of the teacher")
    duration: float = Field(ge=1, le=600,description="Exam duration")
    start_time: datetime = Field(description="Start time of the exam")
    end_time: datetime = Field(description="End time of the exam")
    
class ExamGet(ExamBase):
    id: int = Field()
    
class ExamCreate(ExamBase):
    pass