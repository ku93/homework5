from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView,
                             SubscriptionAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson-retrieve"),
    path("lesson/<int:pk>/edit/", LessonUpdateApiView.as_view(), name="lesson-update"),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson-destroy"
    ),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson-create"),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
]

urlpatterns += router.urls
