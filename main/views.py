from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from main.forms import AuthUserForm, RegisterUserView, NoteForm
from django.contrib.auth.models import User

from main.models.note import Note


@login_required(login_url='/login')
def index(request):
    context = {
        'notes': Note.objects.all(),
        'private_posts': Note.objects.filter(author=request.user)

    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def edit_page(request, pk):
    form = NoteForm(instance=Note.objects.get(pk=pk))
    if request.method == 'POST':
        form = NoteForm(data=request.POST, instance=Note.objects.get(pk=pk))
        if form.is_valid():
            form_new = form.save(commit=False)
            form_new.author = request.user
            form_new.save()
    context = {
        'form': form,
        'notes': Note.objects.get(pk=pk),
        'private_posts': Note.objects.filter(author=request.user)
    }
    return render(request, 'edit_page.html', context=context)


@login_required(login_url='/login')
def detail_page(request, pk):
    context = {
        'notes': Note.objects.get(pk=pk),
        'private_posts': Note.objects.filter(author=request.user)
    }
    return render(request, 'detail_page.html', context=context)


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


def some(request):
    return HttpResponseRedirect('http://yandex.ru/')