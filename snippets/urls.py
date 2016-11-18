from django.conf.urls import url

from .views import SnippetListView


urlpatterns = [
    url(r'^$', SnippetListView.as_view(), name='snippets-list'),
]
