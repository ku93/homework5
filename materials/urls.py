from tkinter.font import names

from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urls import app_name

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/edit/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_destroy"
    ),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
]

urlpatterns += router.urls
