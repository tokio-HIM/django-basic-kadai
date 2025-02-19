from django.contrib import admin
from django.urls import path
from crud.views import ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('crud/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
