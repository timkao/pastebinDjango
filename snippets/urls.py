from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, UserList, UserDetail, api_root

urlpatterns = [
  path('snippets/', SnippetList.as_view()),
  path('snippets/<int:pk>', SnippetDetail.as_view()),
  path('users/', UserList.as_view()),
  path('users/<int:pk>', UserDetail.as_view()),
  path('', api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)
