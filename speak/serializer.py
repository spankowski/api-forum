from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Like, Post

# Serializers define the API representation.
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','post','user',)

class PostSerializer(serializers.ModelSerializer):
    likes_amount = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id','title','text_of_post','data_created','likes_amount','user')

    def get_likes_amount(self, obj):
        amount = Like.objects.all()
        filter_amount = amount.filter(post=obj.id)
        average_rating = len(filter_amount)
        return average_rating
                
                                        



