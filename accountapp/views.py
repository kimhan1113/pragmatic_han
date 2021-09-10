from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from django.contrib.auth.decorators import login_required
from django.forms import GenericIPAddressField, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.models import HelloWorld
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

has_ownership = [account_ownership_required, login_required]

# Create your views here.

# vscode는 classview 상속받을 떄 generic으로 찾자!!!

# 함수만 된다 즉 클래스 함수(메소드)에서는 안됨!!
# 기존 코드는 다 주석으로 남겨둔다!!

# @login_required
def hello_world(request):

    # if request.user.is_authenticated:

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    # else:
    #     return HttpResponseRedirect(reverse('accountapp:login'))
    # return HttpResponse('Hello world!')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

    # def form_valid(self, form):
    #     temp_profile = form.save(commit=False)
    #     temp_profile.user = self.request.user
    #     temp_profile.save()
    #     return super().form_valid(form)

@method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
class AccountDetailView(DetailView):
    model = User
    template_name = "accountapp/detail.html"
    context_object_name = 'target_user'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'







