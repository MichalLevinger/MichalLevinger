from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success_page, name='success-page'),
    path('<slug:action>', views.action_page, name='action-page')
]
