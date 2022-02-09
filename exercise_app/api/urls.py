from api.views import ExerciseCategoryViewset, ExerciseListByCategoryView, ExerciseSetViewset, ExerciseViewset
from rest_framework.routers import DefaultRouter
from rest_framework.urls import path


router = DefaultRouter()
router.register(
    'get_set_by_category', ExerciseCategoryViewset, basename='get_by_category')
router.register('get_by_exercise', ExerciseViewset, basename='get_by_exercise')
router.register('get_by_set', ExerciseSetViewset, basename='get_by_set')

urlpatterns = [
    path(
        'getexercisebycategory',
        ExerciseListByCategoryView.as_view()),
]

urlpatterns += router.urls
