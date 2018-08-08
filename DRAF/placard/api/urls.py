from django.urls import path, re_path

from .views import (
        PlacardDetailAPIView,
        PlacardListCreateAPIView,
    )


app_name = 'placard'
urlpatterns = [
    path('', PlacardListCreateAPIView.as_view(), name='list-create'),
    re_path(r'^(?P<slug>[\w-]+)/$', PlacardDetailAPIView.as_view(), name='detail'),

]
