from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Snippet
    fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
  snippet = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

  class Meta:
    model = User
    fields = ('id', 'username', 'snippet')
