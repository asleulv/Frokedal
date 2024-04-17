from django.db import models
from colorfield.fields import ColorField

# Website design elements
class Logo(models.Model):
    image = models.ImageField(upload_to='images/logos/')
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            Logo.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Logo {self.pk}"
    
class ThemeColor(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FFFFFF')
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_active:
            ThemeColor.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class TourManager(models.Manager):
    def get_or_create_singleton(self):
        tour, created = self.get_or_create(pk=1)
        return tour

class Tour(models.Model):
    background_image = models.ImageField(upload_to='images/tour_backgrounds/')
    is_dark_text = models.BooleanField(default=True)

    objects = TourManager()

    def __str__(self):
        return "Tour Background"

# Featurred model
class Featured(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=50)
    button_url = models.URLField()
    featured_image = models.ImageField(upload_to='images/featured_images/')
    background_image = models.ImageField(upload_to='images/background_images/')
    is_dark_text = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Releases model
class Release(models.Model):
    FORMAT_CHOICES = [
        ('LP', 'LP'),
        ('EP', 'EP'),
        ('Single', 'Single'),
    ]

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    artwork = models.ImageField(upload_to='images/release_artwork/', blank=True)
    spotify_url = models.URLField(blank=True)
    bandcamp_url = models.URLField(blank=True)
    buy_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

# Contact model
class Contact(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Name(models.Model):
    contact = models.ForeignKey(Contact, related_name='names', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class SocialPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome class name (e.g., 'fab fa-facebook')")

    def __str__(self):
        return self.name

# Youtube model  
class YouTubeVideo(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title