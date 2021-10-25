from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    text_of_post = models.TextField(max_length=350)
    data_created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title
                             
class Like(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("post", "user",)
        index_together = ("post", "user",)

    def __str__(self):
        return str(self.post)+"---"+str(self.user) 