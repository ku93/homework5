from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, object):
        return object.lesson_set.count()


    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_count',)


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
