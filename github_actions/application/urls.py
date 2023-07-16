from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from rest_framework import routers

from application.views import QuestionViewSet

router = routers.DefaultRouter()
router.register('question', QuestionViewSet)

urlpatterns = [
    re_path(r'^',include(router.urls)),
]