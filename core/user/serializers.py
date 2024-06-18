from rest_framework import serializers
from core.user.models import User, UserPersonality, AcademicGoal
from decimal import Decimal, ROUND_HALF_UP

class Retrieve(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "id",
            "password",
        ]


class SchoolUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["school", "faculty", "department", "level", "timetable"]


class UserPersonalitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserPersonality
        fields = ["personality_test", "study_style", "other_activities"]


class AcademicGoalSerializer(serializers.ModelSerializer):
    previous_session_gpa = serializers.DecimalField(max_digits=4, decimal_places=2)
    expected_current_session_gpa = serializers.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        model = AcademicGoal
        fields = ['previous_session_gpa', 'expected_current_session_gpa']
    
    