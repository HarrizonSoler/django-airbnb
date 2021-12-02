import django
from django.contrib.auth import authenticate, login, logout
from django.db.models import fields
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm, SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

class SignIn(LoginView):
    template_name = 'accounts/login.html'

def logout_v(request):
    logout(request)
    return redirect('login')

class SignUp(CreateView):
    model = Profile
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/products')

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
    form_class=ProfileForm
    success_url = reverse_lazy('profile')
    template_name='accounts/update_profile_form.html'

    def get_object(self):
        try:
           return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Profile.objects.create(user=self.request.user)



