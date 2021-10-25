from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .serializer import LikeSerializer, PostSerializer
from .models import Post, Like
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser 
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # dodanie dekoratora @method_decorator(login_required) sprawia, iż użytkownik niezalogowany jest w stanie przeglądać oceny
    # natomiast nie jest w stanie sam zagłosować/ przeniesiony zostaje na stronę logowanie (to do)
    @action(detail=True, methods=['POST'])
    @method_decorator(login_required) 
    def like_post(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            rating = Like.objects.get(user=user.id, post=post.id)
            rating.save()
            serializers = LikeSerializer(rating, many=False)
            response = {'message': 'Like updated', 'result': serializers.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            rating = Like.objects.create(user=user, post=post)
            serializers = LikeSerializer(rating, many=False)
            response = {'message': 'Dislike created', 'result': serializers.data}
            return Response(response, status=status.HTTP_200_OK)
 

    def get_queryset(self):
        queryset = Post.objects.all()
        tmp = queryset.order_by('-data_created')
        return tmp

    @method_decorator(login_required) 
    def update(self, request, pk, *args, **kwargs):
        user = request.user
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        post = Post.objects.get(id=pk)
        if post.user == user.id:
            post.title = body['title']
            post.text_of_post = body['text_of_post']
            post.save()
            messege = 'Post Updated'
        else: 
            messege = "You can't update this post"   
        response = {'message': messege}
        return Response(response, status=status.HTTP_200_OK)
    
    @method_decorator(login_required) 
    def create(self, request, *args, **kwargs):
        user = request.user
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        post = Post()
        post.user = user
        post.title = body['title']
        post.text_of_post = body['text_of_post']
        post.save()
        response = {'message': 'Created new post'}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    @method_decorator(login_required) 
    def post_remove(self, request, pk):
        item = Post.objects.get(pk=pk)
        if request.user == item.user:
            Post.objects.filter(id=pk).delete()
            response = {'message': 'Delated'}
            return Response(response, status=status.HTTP_200_OK)
        else:     
            response = {'message': 'Not your post'}
            return Response(response, status=status.HTTP_200_OK)