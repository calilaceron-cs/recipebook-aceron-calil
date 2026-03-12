from django.urls import path

from .views import (
    LedgerListView,
    LedgerDetailView,
    LedgerCreateView,
    ImageUploadView
)

urlpatterns = [
    path('recipe/<int:pk>/add_image', ImageUploadView.as_view(), name='image-add'),
    path('recipe/add', LedgerCreateView.as_view(), name='recipe-add'),
    path('recipes/list', LedgerListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', LedgerDetailView.as_view(), name='recipe-detail'),
]

app_name = 'ledger'
