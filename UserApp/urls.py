from . import views


from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('',views.home),
  path('login',views.login_vw),
  path('register',views.register),
  path("homep",views.homep),

  # path('viewSubjects/<sid>/', views.viewSubjects)

 path('viewSubjects/<int:subject_id>/', views.viewSubjects, name='view_subjects'),
path('select-subject/', views.select_subject, name='select_subject'),
# path('Finish/', views.Finish, name='Finish'),
path('another-view/<int:subject_id>/', views.another_view, name='another_view'),
path('final/', views.final, name='final'),
path('logout',views.logout),  
]


