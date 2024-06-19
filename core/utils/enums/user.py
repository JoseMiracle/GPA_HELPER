from .base import BaseEnum

class SemesterType(BaseEnum):
    """ Semester Choices """
    FIRST_SEMESTER = "FIRST SEMESTER"
    SECOND_SEMESTER = "SECOND SEMESTER"
    

class SemesterDurationType(BaseEnum):
    """ Semester Duration """
    ONE_MONTH = "ONE MONTH"
    TWO_MONTHS = "TWO MONTHS"
    THREE_MONTHS = "THREE MONTHS"
    FOUR_MONTHS = "FOUR MONTHS"
    FIVE_MONTHS = "FIVE MONTHS"
    SIX_MONTHS = "SIX MONTHS"
    

class CourseKnowledgeLevelType(BaseEnum):
    EASY = "EASY"
    MODERATE = "MODERATE"
    HARD = "HARD"
    