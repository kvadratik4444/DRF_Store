from goods import views
from django.urls import path
from .views import CatalogAPIView, ProductAPIView

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', CatalogAPIView.as_view(), name='catalog'),
    path('product/<slug:slug>/', ProductAPIView.as_view(), name='product'),
]