from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'todo/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'todo/item_detail.html'
