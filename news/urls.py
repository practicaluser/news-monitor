from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeywordViewSet
from .views import get_news

router = DefaultRouter()
router.register(r'keywords', KeywordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('get-news/', get_news),
]