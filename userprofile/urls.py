from django.urls import path
from . import views
urlpatterns = [
    path('change',views.changeProfile),
    path('create',views.createProfile),
    path('1',views.showProfile)
]
