from django.urls import path

from .views import LedgerListView, LedgerDetailView

urlpatterns = [
    path('recipes/list', LedgerListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', LedgerDetailView.as_view(), name="recipe-detail"),
]

app_name = "ledger"
