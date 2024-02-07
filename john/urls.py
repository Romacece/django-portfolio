from django.urls import path
from . import views
from .views import download_pdf


urlpatterns = [
    path('', views.index, name='index'),
    path('download-pdf/<int:portfolio_id>/', download_pdf, name='download_pdf'),
    
]