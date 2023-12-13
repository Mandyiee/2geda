from django.urls import path
from . import views
urlpatterns = [
    path('myfeeds',views.showMyFeed),
    path('otherfeeds',views.showOtherFeed),
    path('tagging',views.showTagging),
    path('myfeeds/change',views.changeMyFeed),
    path('otherfeeds/change',views.changeOtherFeed),
    path('tagging/change',views.changeTagging),
]

