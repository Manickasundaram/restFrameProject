from rest_framework import serializers
from .models import restFramePost


class postSerializers(serializers.ModelSerializer):

    class Meta:
        model=restFramePost
        fields='__all__'