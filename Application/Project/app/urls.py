from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    WorkoutListView,
    WorkoutDetailView,
    WorkoutCreateView,
    WorkoutUpdateView,
    WorkoutDeleteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('Workout/', WorkoutListView.as_view(), name='Workout'),
    path('Workout/<int:pk>/', WorkoutDetailView.as_view(), name='Workout_detail'),
    path('Workout/create/', WorkoutCreateView.as_view(), name='Workout_create'),
    path('Workout/<int:pk>/edit/', WorkoutUpdateView.as_view(), name='Workout_update'),
    path('Workout/<int:pk>/delete/', WorkoutDeleteView.as_view(), name='Workout_delete'),
]
