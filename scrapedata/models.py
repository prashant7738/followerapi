from django.db import models

# Create your models here.

class FacebookFollower(models.Model):
    page_name = models.CharField(max_length=100)
    followers = models.IntegerField()
    scraped_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.page_name} - {self.followers}"