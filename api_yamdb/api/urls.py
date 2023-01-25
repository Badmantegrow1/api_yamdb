from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, GenreViewSet, CommentViewSet,
                       ReviewViewSet, TitleViewSet, UsersViewSet)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet
)
router.register('titles', TitleViewSet)
router.register('users', UsersViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet
)


urlpatterns = [
    path('v1/', include(router.urls)),
]
