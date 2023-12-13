from django.urls import path
from . import views
urlpatterns = [
     path('quality',views.showQuality),
    path('quality/change',views.changeQuality),
    path('privacy',views.showPrivacy),
    path('privacy/change',views.changePrivacy),
]