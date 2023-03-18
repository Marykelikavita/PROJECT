from django.urls import path
from . import views


urlpatterns = [
    
    path('index/', views.index, name='index_page'),
    path('', views.landing_page, name='landing_page'),
    path('predictions/results', views.results_page, name='results_page'),
    path('visualizations/', views.visualizations, name='visualizations'),
]
