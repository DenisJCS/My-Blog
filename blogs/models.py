from django.db import models

# Create your models here.
class Blogs(models.Model):
    """App where user can post his notes"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Post(models.Model):
    "Information in the post"
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'
        ordering = ['date_added']

    def __str__(self):
        """Returns string version of model"""
        return f"{self.text[:50]}..."
    