from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from rest_framework import serializers

from placard.models import Placard

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'username',  
            'first_name',
            'last_name',
            'email'
            ]
    

class PlacardSerializer(serializers.ModelSerializer):
    url             = serializers.HyperlinkedIdentityField(
                            view_name='api-placards:detail',
                            lookup_field='slug'
                            )
    user            = UserSerializer(read_only=True)
    publish         = serializers.DateField(default=timezone.now())
    owner           = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Placard
        fields = [
            'url',
            'slug',
            'user',
            'title',
            'content',
            'draft',
            'publish',
            'updated',
            'owner',
            'timestamp',
        ]
    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
        return False


