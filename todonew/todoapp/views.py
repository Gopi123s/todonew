from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,UpdateView,DeleteView,DetailView,CreateView,FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# authentication packages
from django.contrib.auth import login,logout,mixins
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def home(request):
#     return HttpResponse('hiiii')

class Custumlogin(LoginView):
    template_name='todoapp/login.html'
    redirect_authenticated_user=True
    # success_url=reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
    
class Register(FormView):
    template_name='todoapp/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        if user :
            login(self.request,user)
        return super(Register,self).form_valid(form)

# def logoutfunc(request):
#     logout(request)
#     return redirect('home')

class Alltask(LoginRequiredMixin,ListView):
    model=Task
    template_name='todoapp/home.html'
    context_object_name='all_task'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['all_task']=context['all_task'].filter(user=self.request.user)
        context['count']=context['all_task'].filter(complete=False).count()

        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['all_task']=context['all_task'].filter(title__icontains=search_input)
            # title__startwith to check if its start with this query


        context['search_input']=search_input

        return context
        # return super().get_context_data(**kwargs)


class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name='todoapp/taskdetail.html'
    context_object_name='task_detail'

class Addtask(LoginRequiredMixin,CreateView):
    model=Task
    template_name='todoapp/addtask.html'
    success_url=reverse_lazy('home')
    fields=['title','description','complete']

    def form_valid(self, form):
        # to select it as itself
        form.instance.user=self.request.user
        return super(Addtask,self).form_valid(form)

class EditTask(LoginRequiredMixin,UpdateView):
    model=Task
    template_name='todoapp/edittask.html'
    fields=['title','description','complete']
    success_url=reverse_lazy('home')

class Deletetask(LoginRequiredMixin,DeleteView):
    model=Task
    template_name='todoapp/deletetask.html'
    success_url=reverse_lazy('home')

def updatemark(request,pk):
    obk=Task.objects.get(id=pk)
    if obk.complete==True:
        obk.complete=False
    else:
        obk.complete=True
    obk.save()
    return redirect ('home')

