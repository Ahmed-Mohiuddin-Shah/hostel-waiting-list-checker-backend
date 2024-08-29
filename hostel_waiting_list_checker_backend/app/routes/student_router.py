from fastapi import APIRouter
from decouple import config

from ..utils.access_excel import get_excel_data

router = APIRouter()


@router.get("/student-waiting-info/{student_id}")
async def get_student_waiting_info(student_id: int):

    # Get the Excel file path from the environment variable
    excel_file_path = config("EXCEL_FILE_PATH")
    data = get_excel_data(excel_file_path)

    # Filter the data to get the student's waiting info
    student_data = [student for student in data if student["Emp ID"] == student_id]

    if not student_data:
        return {
            "status": False,
            "msg": "Student not found in the waiting list",
            "data": None,
        }

    # get the SR. # of the student
    student_sr_no = student_data[0]["SR. #"]
    student_sr_no = int(student_sr_no)

    if student_sr_no == 0:
        return {
            "status": False,
            "msg": "Student has been allotted a room",
            "data": None,
        }

    # get the student Name
    student_name = student_data[0]["Student Name"]

    # get the student's CMS ID
    student_cms_id = student_data[0]["Emp ID"]
    
    if student_cms_id is None:
        student_cms_id = "CMS ID not available"
    if student_name is None:
        student_name = "Name not available"

    return {
        "status": True,
        "msg": "Student waiting info",
        "data": {
            "student_sr_no": student_sr_no,
            "student_name": student_name,
            "student_cms_id": student_cms_id,
        },
    }
