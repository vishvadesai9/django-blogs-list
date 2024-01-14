from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogs_app.views import BlogsView, index, detail


router = DefaultRouter()
router.register(r'blogs', BlogsView)
urlpatterns = [
    path("api/", include(router.urls)),
    path("", index, name="index"),
    path('<int:post_id>/', detail, name="detail")
]
