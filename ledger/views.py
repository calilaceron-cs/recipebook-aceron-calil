from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage


class LedgerListView(ListView):
    template_name = 'ledger/recipe_list.html'
    model = Recipe


class LedgerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'ledger/recipe_detail.html'
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    model = Recipe


class LedgerCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    login_url = '/accounts/login'
    redirect_field_name = 'next'


class ImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'ledger/add_image.html'
    login_url = '/accounts/login'
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe-detail',
            kwargs={
                'pk': self.object.recipe.pk
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
        context['form'] = RecipeImageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
            recipe_image.recipe = recipe
            recipe_image.save()
            self.object = recipe_image
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
