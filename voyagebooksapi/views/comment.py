from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from voyagebooksapi.models import Comment, User, Post
from rest_framework.decorators import action
from rest_framework import generics

class CommentSerializer(serializers.ModelSerializer):
  """JSON serializer for comments"""
  class Meta:
    model= Comment
    fields = ( 'id', 'author', 'post', 'content', 'created_on')
    depth = 2
    
class CommentView(ViewSet):
  """comments view"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for single comment
    Returns:
      Response -- JSON serialized comment
    """
    comment = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  
  def list(self, request):
      """Handle GET requests to get all comments for post and author
      Returns:
          Response -- JSON serialized list of game types
      """
      comments = Comment.objects.all()
      
      post = request.query_params.get('postId', None)
      if post is not None:
        comments = comments.filter(post_id=post)
      serializer = CommentSerializer(comments, many=True)
      
      return Response(serializer.data)
    
  def create(self, request):
      """Handle POST operations
      Returns
          Response -- JSON serialized comment instance
      """
      author = User.objects.get(uid = request.data["author"])
      post = Post.objects.get(pk = request.data["post"])
      
      comment = Comment.objects.create(
        author = author,
        post = post,
        content = request.data["content"],
        created_on = request.data["created_on"]
      )
      serializer = CommentSerializer(comment)
      return Response(serializer.data)

  def update(self, request, pk):
    """Handle PUT requests for a comment
    Returns:
        Response -- Empty body with 204 status code
    """
    post = Post.objects.get(pk = request.data["post"])
    
    comment = Comment.objects.get(pk=pk)
    comment.content = request.data["content"]
    comment.created_on = request.data["created_on"]
    comment.post = post
    
    comment.save()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)

