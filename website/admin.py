from django.contrib import admin
from django.utils.html import format_html
from .models import Featured, Release, Contact, Name, YouTubeVideo, SocialPlatform, Logo, ThemeColor, Tour

class FeaturedAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable the ability to add new records
        return False

    def has_delete_permission(self, request, obj=None):
        # Disable the ability to delete the existing record
        return False
    
class LogoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'preview_image', 'is_active')
    readonly_fields = ('preview_image',)
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="350" height="50" />', obj.image.url)
        else:
            return ''
    preview_image.short_description = 'Preview'

class TourAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'background_preview', 'is_dark_text')
    actions = None  # Disable all actions

    def has_add_permission(self, request):
        # Allow adding only if there are no instances already
        return not Tour.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disable delete permission
        return False

    def background_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="200" />'.format(obj.background_image.url))
        else:
            return 'No Image'

    background_preview.allow_tags = True
    background_preview.short_description = 'Background Image'
   
    
admin.site.register(Featured, FeaturedAdmin)
admin.site.register(Release)
admin.site.register(Contact)
admin.site.register(Name)
admin.site.register(SocialPlatform)
admin.site.register(YouTubeVideo)
admin.site.register(Logo, LogoAdmin)
admin.site.register(ThemeColor)
admin.site.register(Tour, TourAdmin)

