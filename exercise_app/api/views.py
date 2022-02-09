from unicodedata import category
from rest_framework import viewsets, generics
from api.models import ExerciseCategory, Exercise, ExerciseSet
from api.serializers import ExerciseCategorySerializer, ExerciseListByCategorySerializer, ExerciseSerializer, ExerciseSetSerializer


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
        queryset = Exercise.objects.all()
        category_id = self.request.query_params.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category__id=category_id)
            print(queryset)
        return queryset
