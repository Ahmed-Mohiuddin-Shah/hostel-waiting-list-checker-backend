from fastapi import APIRouter

router = APIRouter()

@router.get("/student-waiting-info/{student_id}")
async def get_student_waiting_info(student_id: int):
    return {
        "status": True,
        "msg": "Student waiting info",
        "data": 1
    }