from django.urls import path
from basicapp import views

app_name = 'basicapp'
urlpatterns = [
    path(r'', views.form_name_view, name='form-page'),
    path(r'sign_up', views.form_signUp_view, name="form-sign-up"),
]
