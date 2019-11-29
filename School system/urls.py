from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import view as local_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view()),
    path('signup/', local_view.signup),
    path('Logedin/', local_view.Logedin),
    path('admission/', local_view.admission),
    path('staff/', local_view.staff),
    path('add_admission/', local_view.add_admission),
    path('add_staff/', local_view.add_staff),
    path('ViewStudent/', local_view.ViewStudent),
    path('FlashPage/', local_view.FlashPage),
    path('ViewStaff/', local_view.ViewStaff),
   

]
