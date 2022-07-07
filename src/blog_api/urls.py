from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostDetail, PostList, PostSearch, PostListDetailFilter
app_name = "blog_api"


# router = DefaultRouter()
# router.register('', PostList, basename='post')

# urlpatterns = router.urls



urlpatterns = [
    path('posts/', PostDetail.as_view(), name="detail-create"),
    path('search/', PostListDetailFilter.as_view(), name="post-search"),
    # path('<int:pk>/update/', PostUpdate.as_view(), name="update-create"),
]
