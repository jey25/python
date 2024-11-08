from django.urls import path
from . import views

urlpatterns = [
    path('<topic>/', views.new_view)
]
