from django.urls import path,include
from viewset_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employees',views.ViewSetView)

urlpatterns = [
    path('',include(router.urls))
]