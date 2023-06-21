from django.urls import path
from .views import index_html

urlpatterns = [
    path('', index_html, name='index_html')
]
