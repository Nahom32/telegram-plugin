from rest_framework import serializers
class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    receiver = serializers.CharField()
    created_at = serializers.DateTimeField()
