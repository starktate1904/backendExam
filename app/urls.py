from django.contrib import admin
from django.urls import path
from .. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard ,name='dashboard'), 
    path('register/',views.register, name = 'register'),
    path('',views.login, name= 'login'),
    path('logout/',views.logout_user, name= 'logout'),
    path('library/',views.library, name= 'library'),
    path('courses/',views.courses, name= 'courses'),
    path('transport/',views.transport, name= 'transport'),
    path('students/',views.students, name= 'students'),
    path('delete-student/<str:email>/',views.deleteStudent, name= "delete-student"),
    path('edit-student/<str:email>/',views.editStudent, name= "edit-student"),
    path('saveeditstaff/',views.saveEditStudent, name= "saveeditstudent"),
    path('enrollstudents/',views.registerStudent, name= "enrollstudents"),
    path('teachers/',views.teachers, name= 'teachers'),
    path('profile/',views.profile, name= 'profile'),
    path('staff/',views.staff, name= "staff"),
     path('addstaff/',views.addStaff, name = 'addstaff'),
    path('deletestaff/<int:id>/',views.deleteStaff, name= "deletestaff"),
    path('editstaff/<int:id>/',views.editStaff, name= "editstaff"),
    path('saveeditstaff/',views.saveEditStaff, name= "saveeditstaff"),]