from django.urls import path, include
from .views import (
    List_Employee,
    Details_Employee
)
urlpatterns = [
    # Class bsed
    path("emp/", List_Employee.as_view(),name='test'),
    path("emp/<int:pk>", Details_Employee.as_view(),name='test1'),

# Function based

    # path("emp/", List_Employee,name='test'),
    # path("emp/<int:pk>", Details_Employee,name='test1'),
]
