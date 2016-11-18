from django.shortcuts import render

# Create your views here.
from .models import Snippets
from django.shortcuts import render
from django.views.generic import ListView

class SnippetListView(ListView):
    model = Snippets

    def get_context_data(self, **kwargs):

        context = super(SnippetListView, self).get_context_data(**kwargs)
        context['snippets'] = Snippets.objects.all()
        return context