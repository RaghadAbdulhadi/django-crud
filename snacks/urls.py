from django.urls import path
from .views import (HomeView,
                    SnackListView,
                    SnackCreateView,
                    SnackDetailView,
                    SnackUpdateView,
                    SnackDeleteView,
                    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snacks_list/', SnackListView.as_view(), name='snacks_list'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('<int:pk>', SnackDetailView.as_view(), name='detail_snack'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name='delete_snack'),
]