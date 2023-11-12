from django.urls import path
from . import views

urlpatterns = [
    path('hospital_app/', views.home_view, name='home_view'),
    path('hospital_app/', views.adminclick_view, name='adminclick_view'),
    path('hospital_app/', views.doctorclick_view, name='doctorclick_view'),
    path('hospital_app/', views.patientclick_view, name='patientclick_view'),
    path('hospital_app/', views.admin_signup_view, name='admin_signup_view'),
    path('hospital_app/', views.doctor_signup_view, name='doctor_signup_view'),
    path('hospital_app/', views.patient_signup_view, name='patient_signup_view'),
    path('hospital_app/', views.is_admin, name='is_admin'),
    path('hospital_app/', views.is_doctor, name='is_doctor'),
    path('hospital_app/', views.is_patient, name='is_patient'),
    path('hospital_app/', views.afterlogin_view, name='afterlogin_view'),

]