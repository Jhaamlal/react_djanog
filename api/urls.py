from django.urls import path, include
from django.views.generic.base import View
from rest_framework import views

from django.urls import path
from rest_framework import routers
from .views import article_details, article_list

from .views import ArticleList, ArticalDetails, ArticleViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('articles', ArticleViewSet, basename='article')
router.register('user', UserViewSet, basename='Users')

urlpatterns = [
    path('api/', include(router.urls))


    # Function base Views
    # path('articles/', article_list, name='article'),
    # path('articles/<pk>', article_details, name='artical_details'),

    # Class Base views
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>', ArticalDetails.as_view())

    # ClassbaseViewset


]
