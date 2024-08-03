from django.urls import path,include
from . import views
# create router
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',viewset=views.CompanyViewSet)
router.register(r'departments', viewset=views.DepartmentViewSet)
router.register(r'employees', viewset=views.EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls))
]
