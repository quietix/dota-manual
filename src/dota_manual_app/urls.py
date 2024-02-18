from django.urls import path
from .views import HomePageView
from django.conf.urls.static import static  # new
from server import settings

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
