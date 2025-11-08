from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('save-url/', views.save_image_url, name='save_image_url'),
    path('',views.index_view,name="home"),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('formfilling/', views.formfilling, name="formfilling"),
    path('edit/<int:id>/', views.edit_view, name='edit'),
    path('profile/',views.profileedit, name="profileedit"),
    path('menu/',views.menubar,name="manubar"),
    path('order/', views.order_view, name='orders')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)