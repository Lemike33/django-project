
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userViews.open_to_main_page, name='start_page'),
    path('reg/', userViews.open_to_registration_page, name='reg'),
    path('profile/', userViews.open_to_profile_page, name='profile'),
    path('links/', userViews.CreateLinkView.as_view(), name='links'),
    path('about', include('resume.urls')),

    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
