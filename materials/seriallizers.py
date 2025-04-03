from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import validate_video_link
from users.models import Payment, User


class LessonSerializer(ModelSerializer):
    video_link = serializers.URLField(validators=[validate_video_link])
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True,)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ("name", "description", "lesson_count", "lessons")


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
