from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls',namespace="products")),
    url('users/login', views.SignIn.as_view(), name='login'),
    path("users/logout",views.logout_v,name='logout' ),
    url('users/singup', views.SignUp.as_view(), name='sign_up'),
    path('profile/',views.ProfileUpdate.as_view(),name='profile')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
