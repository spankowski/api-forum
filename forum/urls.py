from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'api/', include('speak.urls')),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', obtain_auth_token, name='auth'),
]
