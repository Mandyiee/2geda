from django.urls import path
from . import views
urlpatterns = [
     path('audio/quality',views.showAudio),
    path('audio/quality/change',views.changeAudio),
    path('video/quality',views.showVideo),
    path('video/quality/change',views.changeVideo),
]
