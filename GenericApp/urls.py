from django.urls import path
from .views import GenericList
from GenericApp import views
urlpatterns = [
    path('studentLIst',views.GenericList.as_view()),
    path('StudentDetail/<int:pk>/',views.StudentDetail.as_view())
]