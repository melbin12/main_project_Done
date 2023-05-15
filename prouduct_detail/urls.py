from . import views
from django.urls import path

urlpatterns = [
      path('product_d/<int:id>',views.product_d,name='product_d'),
  ]