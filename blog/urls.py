
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rianablog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] 