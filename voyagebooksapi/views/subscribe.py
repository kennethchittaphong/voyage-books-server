from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from voyagebooksapi.models import User, Subscribe


class SubscribeView(ViewSet):
    """Follow View"""
    def retrieve(self, request, pk):
        try:
            subscribe = Subscribe.objects.get(pk=pk)
            serializer = SubscribeSerializer(subscribe)
            return Response(serializer.data)
        except Subscribe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        subscribes = Subscribe.objects.all()
        subscriber = self.request.query_params.get("subscriber_id", None)
        subscribed = self.request.query_params.get("subscribed_id", None)
        if subscriber:
            subscribes = subscribes.filter(subscriber=subscriber)
        if subscribed and subscriber is not None:
            subscribes = subscribes.filter(subscriber=subscriber, subscribed=subscribed)
        serializer = SubscribeSerializer(subscribes, many=True)
        return Response(serializer.data)

    def create(self, request):
        subscriber = User.objects.get(id=request.data["subscriber_id"])
        subscribed = User.objects.get(id=request.data["subscribed_id"])
        subscribe = Subscribe.objects.create(
            subscriber = subscriber,
            subscribed = subscribed
          )
        serializer = SubscribeSerializer(subscribe)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Handle DELETE requests for a single follow"""
        subscribe = Subscribe.objects.get(pk=pk)
        subscribe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SubscribeSerializer(serializers.ModelSerializer):
    """serializer for follows"""
    class Meta:
        model = Subscribe
        depth = 1
        fields = ('id', 'subscriber', 'subscribed')