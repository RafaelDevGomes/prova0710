from django.contrib import admin
from django.urls import path
from portal import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view)
]
