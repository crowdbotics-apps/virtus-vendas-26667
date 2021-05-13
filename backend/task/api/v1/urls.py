from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, TaskViewSet, RatingViewSet, TaskTransactionViewSet

router = DefaultRouter()
router.register("message", MessageViewSet)
router.register("task", TaskViewSet)
router.register("tasktransaction", TaskTransactionViewSet)
router.register("rating", RatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
