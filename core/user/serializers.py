from rest_framework import serializers
from core.user.models import User


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
