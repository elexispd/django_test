
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_login, name="login"),
    path('secure', views.dashboard, name="dashboard"),
    # path('admin/create_staff', views.create_staff, name="create_staff"),
    path('patients/all_patients', views.get_patients, name="get_patients"),
    path('register_staff', views.register_staff, name="register_staff"),
]
