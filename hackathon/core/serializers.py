from rest_framework import serializers


class RequestSenderSerializer(serializers.Serializer):
    request_sender = serializers.StringRelatedField(
        child = serializers.StringRelatedField(max_length=10000),allow_empty=False
    )