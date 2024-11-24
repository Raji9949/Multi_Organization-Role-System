from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Organization, CustomUser
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserCreationForm



class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = 'organization/organization_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Organization.objects.all()
        return Organization.objects.filter(is_main=False)

class OrganizationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Organization
    fields = ['name', 'address', 'is_main']
    template_name = 'organization/organization_form.html'

    def test_func(self):
        return self.request.user.is_superuser


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return CustomUser.objects.filter(organization=self.request.user.organization)

class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    fields = ['username', 'email', 'role']
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)

@login_required
def assign_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.user.role != 'Admin' or user.organization != request.user.organization:
        return redirect('home')  # Permission denied

    if request.method == 'POST':
        role_name = request.POST.get('role')
        if role_name:
            user.role = role_name
            user.save()
            return redirect('user-list')

    return render(request, 'roles/assign_role.html', {'user': user})

def create_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, current_user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = CustomUserCreationForm(current_user=request.user)

    return render(request, 'users/user_form.html', {'form': form})