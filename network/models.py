from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    following = models.ManyToManyField("self", blank=True, related_name='followers', symmetrical=False)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, blank=True, related_name="likes")

    def __str__(self):
        return f"{self.author} posted {self.content}"

    def likes(self):
        """Returns total number of likes on post"""
        return self.liked_by.all().count()

    class Meta: 
        # Orders posts by most recent first, by default
        ordering = ['-created_at']