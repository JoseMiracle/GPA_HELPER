from random import choice
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from core.utils import enums

class User(AbstractBaseUser, enums.BaseModelMixin):
    id = models.UUIDField(
        _("User Id"),
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    first_name = models.CharField(
        _("First Name"),
        null=True,
        blank=True,
        max_length=35
    )
    email = models.EmailField(
        _("Email"),
        null=True,
        blank=False,
        max_length=225,
        unique=True
    )
    
    google_auth_credentials = models.JSONField(
        _("auth credential for admin"), blank=True, null=True
    )
    
    school = models.CharField(
        _("User School"),
        max_length= 255,
        null= True,
        blank=True
    )
    
    faculty = models.CharField(
        _("User Faculty"),
        max_length= 255,
        null= True,
        blank=True
    )
    
    department = models.CharField(
        _("User Department"),
        max_length= 255,
        null= True,
        blank=True
    )
    
    level = models.IntegerField(
        _("User Current Level"),
        default=1
    )
    
    timetable = models.FileField(
        upload_to="gpahelper/",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


    def retrieve_auth_token(self):
        data = {}
        refresh = RefreshToken.for_user(self)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data

    def __str__(self):
        return f"<{self.first_name} - {self.email}"


""" Implementation for user and email login"""
class UserSession(enums.BaseModelMixin):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refresh = models.CharField(max_length=255, unique=True, null=True, blank=True)
    access = models.CharField(max_length=255, unique=True, null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    last_activity = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User Session"
        verbose_name_plural = "User Sessions"

    def __str__(self):
        return f"{self.user} - {self.last_activity}"



class UserPersonality(enums.BaseModelMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personality')
    personality_test = models.URLField(max_length=200)
    study_style = models.CharField(max_length=40, null=False, blank=False)
    other_activities = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}:{self.study_style}"
    

class AcademicGoal(enums.BaseModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='academic_goals')
    previous_session_gpa = models.DecimalField(max_digits=5, decimal_places=4, null=False, blank=False, default='0.00')
    expected_current_session_gpa = models.DecimalField(max_digits=5, decimal_places=4, null=False, blank=False)

    def __str__(self):
        return f"{self.user}: {self.expected_current_session_gpa}"
    
    


class UserCourse(enums.BaseModelMixin):
    """ defualt user course setup"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_courses", verbose_name=_("Course Owner"))
    semester = models.CharField(
        _("Course Semester"),
        choices=enums.SemesterType.choices(),
        default= enums.SemesterType.FIRST_SEMESTER.value,
        max_length=15
    )
    duration = models.CharField(
        _("Semester Duration"),
        choices=enums.SemesterDurationType.choices(),
        default=enums.SemesterDurationType.THREE_MONTHS.value,
        max_length=12
    )
    
    course_title = models.CharField(
        _("Course Title"),
        max_length=255,
        blank=False,
        null=False
    )
    
    course_code = models.CharField(
        _("Course Code"),
        max_length=255,
        blank=False,
        null=False
    )
    
    unit_load = models.CharField(
        _("Unit Load"),
        max_length=255,
        blank=False,
        null=False
    )
    
    knowledge = models.CharField(
        _("Course Knowledge Level"),
        choices=enums.CourseKnowledgeLevelType.choices(),
        default=enums.CourseKnowledgeLevelType.MODERATE.value,
        max_length=10
    )
    
    uploaded_course = models.FileField(
        upload_to="gpahelper/uploaded_course/",
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        
    def __str__(self):
        return f"{self.user.first_name} {self.course_code} -- {self.knowledge}"