from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200, unique=True)
    # profil_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class New(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photos = models.FileField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
