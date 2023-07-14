from rest_framework import serializers
class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=255)
    phone=serializers.CharField(max_length=255)
    