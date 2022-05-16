from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditarUsuarioForm, EditarPerfilForm, CambiarPasswordForm
from django.views.generic import ListView, DetailView
from .models import  Perfil
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from noticias.models import Noticia

class MostrarPaginaPerfilView(DetailView):
    model = Perfil
    template_name = 'registration/perfil_usuario.html'

    def get_context_data(self, **kwargs):
        usuarios = Perfil.objects.all()
        context = super(MostrarPaginaPerfilView, self).get_context_data(**kwargs)

        pagina_usuario = get_object_or_404(Perfil, id=self.kwargs['pk'])
        context['pagina_usuario'] = pagina_usuario
        context['noticias_recientes'] = Noticia.objects.filter(autor_id=self.kwargs['pk']).order_by('-fecha_publicacion')[0:4]
        return context


class CambiarPasswordView(PasswordChangeView):
    form_class = CambiarPasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

'''
class UserEditView(generic.UpdateView):
    form_class = EditarUsuarioForm
    template_name = 'registration/edit_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
'''

@login_required
def UserEditView(request):
    if request.method == 'POST':
        usuario_form = EditarUsuarioForm(request.POST, instance=request.user)
        perfil_form = EditarPerfilForm(request.POST, request.FILES, instance=request.user.perfil)

        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            messages.success(request, '¡Tu perfil se ha actualizado correctamente!')
            return redirect('mostrar_perfil_usuario', pk=request.user.id)
    else:
        usuario_form = EditarUsuarioForm(instance=request.user)
        perfil_form = EditarPerfilForm(instance=request.user.perfil)

    return render(request, 'registration/edit_perfil.html', {'usuario_form': usuario_form, 'perfil_form': perfil_form})




class SobreNosotrosView(ListView):
    model = Perfil
    template_name = 'sobre_nosotros.html'