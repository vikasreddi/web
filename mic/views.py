from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import album,song
from .forms import Userform


class Indexview(generic.ListView):
    template_name = 'mic/index1.html'

    def get_queryset(self):
        return album.objects.all()


class Detailview(generic.DetailView):
     model = album
     context_object_name = 'al'
     template_name = 'mic/detail1.html'



class Albumcreate(CreateView):
    model = album
    fields = ['artist','album_tittle','genre','album_logo']


class songview(generic.ListView):
    template_name = 'mic/detail2.html'

    def get_queryset(self):
        return song.objects.all()

class albumview(generic.ListView):
    template_name = 'mic/detail3.html'

    def get_queryset(self):
        return album.objects.all()

class Userformview(View):
    form_Class =Userform
    template_name = 'mic/reg.html'
    def get(self,request):
        form =self.form_Class(None)
        return render(request,self.template_name,{'form':form})
    #process form data
    def post(self,request):
        form = self.form_Class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            #cleaned(normailzed) data
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # returns user objects if credentials are correct
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('mic:index')

        return render(request, self.template_name, {'form': form})



