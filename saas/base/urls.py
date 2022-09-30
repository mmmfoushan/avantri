from .views import RegisterAPI,LoginAPI
from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    #path('', RegisterAPI.as_view(), name='register'),
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),    
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('', views.jobApiOverview, name="api-overview"),
	path('jobs/', views.jobList, name="jobs"),
	path('jobs-detail/<str:pk>/', views.jobDetail, name="job-detail"),
	path('jobs-create/', views.jobCreate, name="job-create"),
	path('jobs-update/<str:pk>/', views.jobUpdate, name="job-update"),
	path('jobs-delete/<str:pk>/', views.jobDelete, name="job-delete"),
]
