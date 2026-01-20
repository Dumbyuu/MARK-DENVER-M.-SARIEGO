from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class WorkoutListView(ListView):
    model = Workout
    template_name = 'app/Workout_list.html'
    context_object_name = 'workouts'

class WorkoutDetailView(DetailView):
    model = Workout
    context_object_name = 'Workout'
    template_name = 'app/Workout_detail.html'

class WorkoutCreateView(CreateView):
    model = Workout
    fields = ['workout_date', 'duration_min', 'calories_burned']
    template_name = 'app/Workout_create.html'
    success_url = reverse_lazy('Workout')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ['workout_date', 'duration_min', 'calories_burned']
    template_name = 'app/Workout_update.html'
    success_url = reverse_lazy('Workout')

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = 'app/Workout_delete.html'
    success_url = reverse_lazy('home')