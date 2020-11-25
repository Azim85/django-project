from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class RelatedNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'relations'
        
    def __str__(self):
        return f"{self.text[:50]}..."      
