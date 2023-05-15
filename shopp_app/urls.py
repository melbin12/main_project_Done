from django.contrib import admin
from django.urls import path,include
from django.urls import path
from grower import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [ 
    path('category_page/<int:id>',views.category_page,name='category_page'),
    path('category_page1/<int:id>',views.category_page1,name='category_page1'),
    
    
]