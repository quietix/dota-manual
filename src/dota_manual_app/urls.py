from django.urls import path

import dota_manual_app.views
from .views import HomePageView
from django.conf.urls.static import static  # new
from server import settings

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("juggernaut", dota_manual_app.views.send_file),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
