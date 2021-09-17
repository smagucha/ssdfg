from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codechallenege.urls')),
    path('', include('accounts.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset_form.html"),
     name ='reset_password'),
    path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name ='accounts/password_reset_confirm.html'),),
    path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = "codechallenege.views.page_not_found_view"
