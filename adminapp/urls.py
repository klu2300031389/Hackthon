from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import user_activity_list
from django.conf import settings
from django.conf.urls.static import static
app_name='adminapp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projecthomepage/', views.projecthomepage, name='projecthomepage'),
    path('user_list/', views.user_list, name='user_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', LogoutView.as_view(next_page='adminapp:homepage'), name='logout'),
    path('UserLoginPage/', views.UserLoginPageCall, name='UserLoginPage'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('courses/add/', views.add_course, name='add_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('courses/edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='adminapp/UserLoginPage.html'), name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('assessments/', views.assessment_list, name='assessment_list'),
    path('assessments/add/', views.add_assessment, name='add_assessment'),
    path('assessments/edit/<int:assessment_id>/', views.edit_assessment, name='edit_assessment'),
    path('assessments/delete/<int:assessment_id>/', views.delete_assessment, name='delete_assessment'),
    path('results/', views.view_results, name='view_results'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('search_users/', views.search_users, name='search_users'),
    path('search_courses/', views.search_course, name='search_courses'),
    path('export_users_csv/', views.export_users_csv, name='export_users_csv'),
    path('export_users_excel/', views.export_users_excel, name='export_users_excel'),
    path('export_courses_csv/', views.export_courses_csv, name='export_courses_csv'),
    path('export_courses_excel/', views.export_courses_excel, name='export_courses_excel'),
    path('user_activity_list', user_activity_list, name='user_activity_list'),
    path('users/', views.users_list, name='users_list'),
    path('assign_courses/', views.assign_course, name='assign_course'),
    path('assigned_courses/', views.assigned_courses, name='assigned_courses'),
    path('track_progress/', views.track_progress, name='track_progress'),
    path('track_progress/edit/<int:progress_id>/', views.edit_progress, name='edit_progress'),
    path('track_progress/delete/<int:progress_id>/', views.delete_progress, name='delete_progress'),
    path('issue-certificate/', views.issue_certificate, name='issue_certificate'),
    path('generate-certificate/<int:progress_id>/', views.generate_certificate, name='generate_certificate'),
    path('feedback/', views.view_feedback, name='view_feedback'),
    path('courses/<int:course_id>/resources/', views.get_course_resources, name='get_course_resources'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

