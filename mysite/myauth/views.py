from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from .models import Profile
from django.contrib.auth.decorators import login_required, permission_required


class AboutMeView(TemplateView):
    template_name = 'myauth/about-me.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('recipe_app:recipies_list')
