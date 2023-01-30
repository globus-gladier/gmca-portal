from django.urls import path
from gmca_portal import views


urlpatterns = [
    path('exampleview/', views.example_view, name='exampleview')
]
