from django.contrib.auth.models import User
from django.forms import ModelForm

class userupdateform(ModelForm):
	class Meta:
		model = User
		fields =['username', 'first_name', 'last_name', 'email']


	# def clean_email(self): 
	# 	email = self.cleaned_data.get('email')
	# 	if (email == ""):
	# 		raise forms.ValidationError('This field cannot be left blank')
	# 	else:
	# 		for instance in User.objects.all():
	# 			if instance.email == email:
	# 				raise forms.ValidationError(email , ' is already added')
	# 			return email



	