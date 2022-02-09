from django.db import models


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self) -> str:
        return str(self.name)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ExerciseCategory, on_delete=models.SET_NULL, null=True)
    category_name = models.CharField(max_length=255)
    time_in_second = models.IntegerField()
    calories = models.IntegerField()
    repeat_count = models.IntegerField()
    image = models.ImageField()
    url = models.URLField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class ExerciseSet(models.Model):
    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return str(self.category_name)
