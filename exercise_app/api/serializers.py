from unicodedata import category
from rest_framework import serializers
from api.models import ExerciseCategory, Exercise, ExerciseSet


class ExerciseCategorySerializer(serializers.ModelSerializer):
    total_exercise = serializers.SerializerMethodField('get_total_exercise')
    time = serializers.SerializerMethodField('get_total_time')
    calories = serializers.SerializerMethodField('get_total_calories')

    def get_total_exercise(self, instance):
        return ExerciseSet.objects.filter(category=instance).count()

    def get_total_time(self, instance):
        return sum(ExerciseSet.objects.filter(
            category=instance).prefetch_related(
                'exercise').values_list('exercise__time_in_second', flat=True))        

    def get_total_calories(self, instance):
        return sum(ExerciseSet.objects.filter(
            category=instance).prefetch_related(
                'exercise').values_list('exercise__calories', flat=True))

    class Meta:
        model = ExerciseCategory
        fields = (
            'id',
            'name',
            'image',
            'total_exercise',
            'time',
            'calories',
            'level',
            'description',

        )


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'


class ExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseSet
        fields = '__all__'


class ExerciseListByCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'
