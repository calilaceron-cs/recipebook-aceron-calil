from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import Recipe


class LedgerListView(ListView):
    template_name = 'ledger/recipe_list.html'
    model = Recipe
    queryset = Recipe.objects.all()


class LedgerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'ledger/recipe_detail.html'
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    model = Recipe

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Recipe, pk=pk_)
