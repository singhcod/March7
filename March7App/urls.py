from django.urls import path
from .views import StudentList
from March7App import views
urlpatterns = [
    path('studentLIst',views.StudentList.as_view()),
    path('StudentDetail/<int:pk>/',views.StudentDetail.as_view())
]