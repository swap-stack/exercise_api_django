from django.contrib import admin
from api.models import Exercise, ExerciseCategory, ExerciseSet


admin.site.register(Exercise)
admin.site.register(ExerciseCategory)
admin.site.register(ExerciseSet)
