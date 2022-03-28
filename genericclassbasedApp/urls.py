from django.urls import path
# from .views import GenericLists
from genericclassbasedApp import views
urlpatterns = [
    path('studentLIst',views.GenericLists.as_view()),
    path('GenericDetail/<int:pk>/',views.GenericDetail.as_view())
]