from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditarPerfilForm, CambiarPasswordForm

class CambiarPasswordView(PasswordChangeView):
    form_class = CambiarPasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserEditView(generic.UpdateView):
    form_class = EditarPerfilForm
    template_name = 'registration/edit_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user