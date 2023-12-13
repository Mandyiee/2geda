from django.urls import path
from . import views
urlpatterns = [
     path('quality',views.showQuality),
    path('quality/change',views.changeQuality),
    path('download',views.showDownload),
    path('download/change',views.changeDownload),
]