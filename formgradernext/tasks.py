from nbgrader.apps import AutogradeApp
from nbgrader.coursedir import CourseDirectory

from .scheduler import scheduler_logger


def autograde_assignment(course_id: str, assignment_id:str = None, student_id:str = None):
    """
    Autogrades an assignment (submitted by the student and collected by the instructor).

    Args:
        course_id (str): the course id which is equivalent to the course name.
        assignment_id (str, optional): the assignment id which is equivalent to the assignment name. Defaults to None.
        student_id (str, optional): the student id which is equivalent to the student name. Defaults to None.
    """
    job_info = (
        f"course_id={course_id}, assignment_id={assignment_id}, student_id={student_id}"
    )
    scheduler_logger.info(f"Initialize autograding app for {job_info}")
    app = AutogradeApp()
    app.log = scheduler_logger
    app.coursedir = CourseDirectory()
    if course_id is not None:
        app.coursedir.course_id = course_id
    if assignment_id is not None:
        app.coursedir.assignment_id = assignment_id
    if student_id is not None:
        app.coursedir.student_id = student_id
    scheduler_logger.info(f"Starting autograding for {job_info}")
    app.start()
    scheduler_logger.info(f"Completed autograding for {job_info}")
