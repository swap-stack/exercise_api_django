from rest_framework import viewsets, generics
from api.models import ExerciseCategory, Exercise, ExerciseSet
from api.serializers import (
    ExerciseSerializer, ExerciseSetSerializer,
    ExerciseCategorySerializer, ExerciseListByCategorySerializer
    )


class ExerciseCategoryViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ExerciseCategorySerializer
    queryset = ExerciseCategory.objects.all()


class ExerciseViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class ExerciseSetViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ExerciseSetSerializer
    queryset = ExerciseSet.objects.all()


class ExerciseListByCategoryView(generics.ListAPIView):
    serializer_class = ExerciseListByCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')

        if category_id is not None:
            exercise_ids = ExerciseSet.objects.filter(category__id=category_id).prefetch_related('exercise').values_list('exercise_id')
            queryset = Exercise.objects.filter(pk__in=exercise_ids)
            return queryset
