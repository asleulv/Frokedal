from .models import Logo, ThemeColor

def active_logo(request):
    active_logo = Logo.objects.filter(is_active=True).first()
    return {'active_logo': active_logo}

def active_theme_color(request):
    active_theme_color = ThemeColor.objects.filter(is_active=True).first()
    return {'active_theme_color': active_theme_color}