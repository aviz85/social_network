from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile_picture']

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None