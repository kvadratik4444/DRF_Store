from django.urls import path
from .views import IndexAPIView, AboutAPIView

app_name = 'main'

urlpatterns = [
    path('', IndexAPIView.as_view(), name='index'),
    path('about/', AboutAPIView.as_view(), name='about'),
]
