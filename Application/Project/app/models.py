from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    muscle_group = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="exercises"
    )

    def __str__(self):
        return self.name

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="workouts",
        null=True,      # allow empty
        blank=True      # optional in forms
    )
    workout_date = models.DateField()
    duration_min = models.IntegerField()
    calories_burned = models.IntegerField()

    def __str__(self):
        if self.user:
            return f"Workout on {self.workout_date} - {self.user.username}"
        return f"Workout on {self.workout_date}"

class ExerciseLog(models.Model):
    exercise_log_id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="exercise_logs"
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="exercise_logs"
    )
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.exercise.name} ({self.sets}x{self.reps})"
