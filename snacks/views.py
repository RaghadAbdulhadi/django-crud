from django.shortcuts import render
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    TemplateView,
                                )
from .models import Snack

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class SnackListView(ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snack

class SnackCreateView(CreateView):
    template_name = "snacks_create.html"
    model = Snack
    fields = "__all__"

class SnackUpdateView(UpdateView):
    template_name = "snacks_update.html"
    model = Snack
    fields = ['title', 'description', 'quantity']

class SnackDeleteView(DeleteView):
    template_name = "snacks_delete.html"
    model = Snack
    success_url = "/"
