from django.urls import path
from .views import ListClient 
from .views import AddClientView
from .views import GetClientView 
from .views import UpdateClientView
from .views import DeleteClientView



urlpatterns = [
    path('client-list/', ListClient.as_view()),
    path('client-add/', AddClientView.as_view()),
    path('client/<int:id>/', GetClientView.as_view()),
    path('client-update/<int:id>/', UpdateClientView.as_view()),
    path('client-delete/<int:id>/', DeleteClientView.as_view())


]
