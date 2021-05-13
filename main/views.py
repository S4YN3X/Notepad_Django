from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import AuthUserForm, RegisterUserView, NoteForm
from django.contrib.auth.models import User

from main.models.note import Note


def index(request):
    form = NoteForm(initial={'text': 'first_value'})
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)


class BlLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url


class BlRegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserView
    success_url = reverse_lazy('index')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class BlLogoutView(LogoutView):
    next_page = reverse_lazy('index')
