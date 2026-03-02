from django.urls import path

from .views import LedgerListView, LedgerDetailView

urlpatterns = [
    path('recipes/list', LedgerListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>', LedgerDetailView.as_view(), name="recipe-detail"),
]

app_name = "ledger"
