from django.shortcuts import render
from .models import Featured, Release, Contact, Tour, SocialPlatform
from datetime import datetime

def home(request):
    featured = Featured.objects.first()
    social_platforms = SocialPlatform.objects.all() 
    releases = Release.objects.order_by('-release_date')  
    tour = Tour.objects.first() 
    contact = Contact.objects.all()  
    current_year = datetime.now().year

    return render(request, 'home.html', {'featured': featured, 'social_platforms': social_platforms, 'releases': releases, 'contact': contact, 'year': current_year, 'tour': tour})
