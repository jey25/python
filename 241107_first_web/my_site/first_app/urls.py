from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view),
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.new_view)
]
