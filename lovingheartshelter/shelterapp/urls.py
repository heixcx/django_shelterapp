from django.urls import path
from . import views

# URLs of Shelterapp
urlpatterns = [
    path('', views.index, name='index'), # Home page
    path('adopt_animals/', views.animals, name='animals'), # Adopt page
    path('adopt_animals/<int:id>/', views.animal_detail, name='animal_detail'), # Animal detail page
    path('login/', views.login, name='login'), # Login page
    path('register/', views.register), # Signup page
    path('logout/', views.logout), 
    path('my/', views.mypage, name='mypage'), # User's personal page
	path('my/apply/', views.create_new, name='create'), # Adoption application create view
    path('my/<int:id>/', views.view_application, name='view'), # Adoption application info view
    path('my/<int:id>/update/', views.update_application, name='update'), # Adoption application edit view
]