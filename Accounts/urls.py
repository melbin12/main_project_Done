from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index'), 
    path('category/',views.category,name='category'), 
    # path('category1/<int:id>',views.category1,name='category1'), 
    path('logout/',views.logout,name='logout'), 
    path('address/', views.address, name='address'),
    path('profile/', views.profile, name='profile'),
    # path('e_profile/', views.e_profile, name='e_profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('de_addres/<int:id>/',views.de_addres,name='de_addres'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('wether/', views.wether, name='wether'),
    
]