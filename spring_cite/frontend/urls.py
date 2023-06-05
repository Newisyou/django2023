from django.urls import path
from backend import views as bv
from auth_clicker import views as av

urlpatterns = [
    path('call_click/', bv.call_click),
]