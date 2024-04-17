from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
]

admin.site.site_header = 'Frokedal.com Admin'
admin.site.site_title = 'Frokedal.com'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
