from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

"""
This time we've used the ModelViewSet class in order to get the complete set of default read and write operations.

Notice that we've also used the @action decorator to create a custom action, named highlight. This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.

Custom actions which use the @action decorator will respond to GET requests by default. We can use the methods argument if we wanted an action that responded to POST requests.

The URLs for custom actions by default depend on the method name itself. If you want to change the way url should be constructed, you can include url_path as a decorator keyword argument.

"""

class SnippetViewSet(viewsets.ModelViewSet):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

  @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
  def highlight(self, request, *args, **kwargs):
    snippet = self.get_object()
    return Response(snippet.highlighted)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'user': reverse('user-list', request=request, format=format),
    'snippets': reverse('snippet-list', request=request, format=format),
  })
