from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .decorators import allowed_users
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import requests

from .forms import Bioinfoform, Businessdetailsform, empdetailsform, bankdetailsform, LoanTypeform, Otherloanform
from .models import  Bioinfo, BusinessDetails, EmploymentDetails, Bankdetails, LoanType, OtherLoans



def page_not_found_view(request, exception):
    return render(request, 'codechallenege/404.html', status=404)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def home(request):
	context ={
		'title': 'home page',
	}
	return render(request, 'codechallenege/home.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def userbio(request):
	if request.method == 'POST': 
		#author = Author(title='Mr')
		obj= request.user.id

		form = Bioinfoform(request.POST)
		if form.is_valid():
			name = form.cleaned_data['membership_no']
			getmembership_no = Bioinfo.objects.filter(membership_no= name).exists()
			if not getmembership_no:
				# bioinfo=form.save(commit=False)
				# bioinfo.bio = request.user.id
				# bioinfo.save()
				#form.save()
				obj = form.save(commit=False)
				obj.bio = request.user
				obj.save()
				form = Bioinfoform()
				return redirect('client_business')
			else:
				form = Bioinfoform()
				context= {'form': form, 'error':'membership No as been taken.'}
				return render(request, 'codechallenege/bioinfo.html', context)
	else:
		form = Bioinfoform()
	context ={
		'title': 'Bio info',
		'form': form
	}
	return render(request,'codechallenege/bioinfo.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def listclients(request):
	clients = Bioinfo.objects.all()
	context = {
		'title': 'list of clients',
		'users': clients
	}
	return render(request, 'codechallenege/listlclients.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updateuser(request, id):
	try:
		userobj =Bioinfo.objects.get(id =id)
		form = Bioinfoform(request.POST or None, instance= userobj)
		if form.is_valid():
			form.save()
			form= Bioinfoform()
			return redirect('list_user')
		context ={
			'userobj':userobj,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')  
	return render(request, 'codechallenege/updatedetails.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deletelient(request, id):
	try:
		deluser =Bioinfo.objects.get(id =id)
		if request.method == 'POST':
			deluser.delete()
			return redirect('list user')
		context ={
			'deluser':deluser,
			'title': 'remove client',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deleteclient.html', context)

''' seond part of the project '''
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def businessdetails(request):
	if request.method == 'POST':
		form = Businessdetailsform(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.bio = request.user
			obj.save()
			form = Businessdetailsform()
			return redirect('emp_form')
	else:
		form = Businessdetailsform()
	context ={
		'title': 'business details',
		'form': form
	}
	return render(request,'codechallenege/businessdetails.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def clientsbusiness(request):
	clientsbiz = BusinessDetails.objects.all()
	context = {
		'title': 'clients business',
		'users': clientsbiz
	}
	return render(request, 'codechallenege/clientbiz.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updatebiz(request, id):
	try:
		userobj =BusinessDetails.objects.get(id =id)
		form =  Businessdetailsform(request.POST or None, instance= userobj)
		if form.is_valid():
			form.save()
			form= Businessdetailsform()
			return redirect('list user')
		context ={
			'userobj':userobj,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/updatebiz.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deletebiz(request, id):
	try:
		delbiz =BusinessDetails.objects.get(id =id)
		if request.method == 'POST':
			delbiz.delete()
			return redirect('list user')
		context ={
			'delbiz':delbiz,
			'title': 'remove business',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deletebiz.html', context)

''' third part of the project '''


@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def employmentdetails(request):
	if request.method == 'POST':
		form = empdetailsform(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.bio = request.user
			obj.save()
			form = empdetailsform()
			return redirect('bank_form')
	else:
		form = empdetailsform()
	context ={
		'title': 'employment details',
		'form': form
	}
	return render(request,'codechallenege/employmentform.html', context)


''' think of show user his own employment details as well as loaner '''
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def showemploymentdetails(request):
	details = EmploymentDetails.objects.all()
	context = {
		'title': 'details of employment',
		'users': details
	}
	return render(request, 'codechallenege/showemp.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updateemployment(request, id):
	try:
		useremploy =EmploymentDetails.objects.get(id =id)
		form =  empdetailsform(request.POST or None, instance= useremploy)
		if form.is_valid():
			form.save()
			form= empdetailsform()
			return redirect('list user')
		context ={
			'useremploy':useremploy,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/updateemp.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deleteemp(request, id):
	try:
		delemp =EmploymentDetails.objects.get(id =id)
		if request.method == 'POST':
			delemp.delete()
			return redirect('list user')
		context ={
			'delemp':delemp,
			'title': 'delete employment',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deleteemp.html', context)


''' four part of the project '''
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def BankDetails(request):
	if request.method == 'POST':
		form = bankdetailsform(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.bio = request.user
			obj.save()
			form = bankdetailsform()
			return redirect('homepage')
	else:
		form = bankdetailsform()
	context ={
		'title': 'bank details',
		'form': form
	}
	return render(request,'codechallenege/bankform.html', context)
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def bankclient(request):
	clientsbank = Bankdetails.objects.all()
	context = {
		'title': 'bank details',
		'users': clientsbank
	}
	return render(request, 'codechallenege/bankdetails.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updateBank(request, id):
	try:
		bankobj =Bankdetails.objects.get(id =id)
		form =  bankdetailsform(request.POST or None, instance= bankobj)
		if form.is_valid():
			form.save()
			form= bankdetailsform()
			return redirect('list user')
		context ={
			'bankobj':bankobj,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/updatebank.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deletebank(request, id):
	try:
		delbank =Bankdetails.objects.get(id =id)
		if request.method == 'POST':
			delbank.delete()
			return redirect('list user')
		context ={
			'delbank':delbank,
			'title': 'remove bank details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deletebank.html', context)



''' fifth part of the project '''
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def Loanform(request):
	if request.method == 'POST':
		form = LoanTypeform(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.bio = request.user
			obj.save()
			form = LoanTypeform()
			return redirect('homepage')
	else:
		form = LoanTypeform()
	context ={
		'title': 'loan form',
		'form': form
	}
	return render(request,'codechallenege/loanform.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def loantypedetails(request):
	clientsbank = LoanType.objects.all()
	context = {
		'title': 'bank details',
		'users': clientsbank
	}
	return render(request, 'codechallenege/loandetails.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updateloan(request, id):
	try:
		loanobj =LoanType.objects.get(id =id)
		form =  LoanTypeform(request.POST or None, instance= loanobj)
		if form.is_valid():
			form.save()
			form= LoanTypeform()
			return redirect('list user')
		context ={
			'loanobj':loanobj,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/updateloan.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deleteloan(request, id):
	try:
		delloan =loandetails.objects.get(id =id)
		if request.method == 'POST':
			delloan.delete()
			return redirect('list user')
		context ={
			'delloan':delloan,
			'title': 'remove bank details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deleteloan.html', context)


''' sixth part of the project '''
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','clientuser'])
def otherform(request):
	if request.method == 'POST':
		form = Otherloanform(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.bio = request.user
			obj.save()
			form = Otherloanform()
			return redirect('homepage')
	else:
		form = Otherloanform()
		context ={
			'title': 'loan form',
			'form': form
		}
		return render(request,'codechallenege/otherform.html', context)
@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def otherdetails(request):
	clientsbank = OtherLoans.objects.all()
	context = {
		'title': 'other bank details',
		'users': clientsbank
	}
	return render(request, 'codechallenege/otherdetails.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def updateother(request, id):
	try:
		otherobj =OtherLoans.objects.get(id =id)
		form =  Otherloanform(request.POST or None, instance= otherobj)
		if form.is_valid():
			form.save()
			form= Otherloanform()
			return redirect('list user')
		context ={
			'otherobj':otherobj,
			'form': form,
			'title': 'update your details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/updateother.html', context)

@login_required(login_url='/accounts/login/')
@allowed_users(allowed_roles=['admin','webadminister'])
def deleteother(request, id):
	try:
		delother =OtherLoans.objects.get(id =id)
		if request.method == 'POST':
			delother.delete()
			return redirect('list user')
		context ={
			'delother':delother,
			'title': 'delete other  bank details',
		}
	except ObjectDoesNotExist:
		return render(request, 'codechallenege/404.html')
	return render(request, 'codechallenege/deleteother.html', context)


def moredetails(request):
	userid= request.user
	detailbio= userid.bioinfo_set.all()
	detailbank= userid.bankdetails_set.all()
	detailbiz= userid.businessdetails_set.all()
	detailemp= userid.employmentdetails_set.all()
	detaildel= userid.otherloans_set.all()
	detailloan= userid.loantype_set.all()
	context={
		'detailbank': detailbank,
		'detailbio': detailbio,
		'detailbiz': detailbiz,
		'detailemp': detailemp,
		'detaildel': detaildel,
		'detailloan':detailloan
	}
	return render(request, 'codechallenege/userdetails.html', context)
