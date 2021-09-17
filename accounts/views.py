from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import userupdateform
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
        	try:
        		username = form.cleaned_data['username']
        		user= User.objects.get(username=username)
        		context= {'form': form, 'error':'username as been taken.'}
        		return render(request, 'accounts/sign_up.html', context)
        	except User.DoesNotExist:
        		user = form.save()
        	login(request,user)
        	group = Group.objects.get(name='clientuser')
        	user.groups.add(group)
        	return redirect('login')
    context['form']=form
    return render(request,'accounts/sign_up.html',context)



def updateprofile(request, ):
	if request.method =='POST':
		form= userupdateform(request.POST, instance= request.user)
		if form.is_valid():
			try:
				email = form.cleaned_data['email']
				user= User.objects.get(email=email)
				context= {'form': form, }
				return render(request, 'accounts/edit_profile.html', context)
			except User.DoesNotExist:
				user = form.save()
		return redirect('homepage')
	else:
		form= userupdateform(instance= request.user)
	context ={
		'form':form,
		'error':'username as been taken.'
	}
	return render(request, 'accounts/edit_profile.html', context)

