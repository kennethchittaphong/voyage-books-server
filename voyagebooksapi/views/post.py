import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from voyagebooksapi.models import Post, User
from rest_framework.decorators import action


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'location',
                  'creation_date', 'photo_url', 'content')
        depth = 2


class PostView(ViewSet):

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        uid = request.query_params.get('user', None)
        if uid is not None:
            posts = posts.filter(user=uid)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])

        post = Post.objects.create(
            title=request.data["title"],
            photo_url=request.data["photo_url"],
            content=request.data["content"],
            location=request.data["location"],
            creation_date = datetime.date.today(),
            user=user,
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.creation_date = request.data["creation_date"]
        post.photo_url = request.data["photo_url"]
        post.content = request.data["content"]
        post.location = request.data["location"]
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)