from django.urls import path, include
from backend import views as bv
from auth_clicker import views as av

urlpatterns = [
    path('call_click/', bv.call_click),
    path('logout/', av.logout)
]