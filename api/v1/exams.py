from fastapi import APIRouter
from schemas.exams import ExamGet,datetime

api_router=APIRouter(prefix='/exams')

exams: dict[int,ExamGet]={1: ExamGet(id=1,
                                     group__id=1,
                                     teacher_id=1,
                                     duration=10,
                                     start_time=datetime(2026,3,16,19,0,0),
                                     end_time=datetime(2026,3,16,21,0,0))}

@api_router.get('/',response_model=list[ExamGet])
def get_exams():
    return list(exams.values())