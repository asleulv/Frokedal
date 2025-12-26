from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from website import views

# Define the media and static routes FIRST
dev_patterns = []
if settings.DEBUG:
    dev_patterns = [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns = dev_patterns + [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
]

admin.site.site_header = 'Frokedal.com Admin'
admin.site.site_title = 'Frokedal.com'