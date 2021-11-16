
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from project.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('api/v1.0/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
