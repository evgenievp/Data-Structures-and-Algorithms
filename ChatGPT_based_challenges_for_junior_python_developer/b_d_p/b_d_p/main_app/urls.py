from django.urls import path
from b_d_p.main_app import views

urlpatterns = (
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
)
