from django.db import models
from .validators import onlyletters, onlyisalnum,onlyisnumeric
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission




new_group1, created = Group.objects.get_or_create(name ='clientuser')
new_group2, created = Group.objects.get_or_create(name ='webadminister')

ct = ContentType.objects.get_for_model(User)


# permission = Permission.objects.create(
# 	codename ='add_bankdetails',name ='can add bank details', 
# 	# codename ='add_bioinfo',name ='can add bioinfo',
# 	# codename ='add_business_details',name ='can add business details',
# 	# codename ='add_employment_details',name ='can add employment details',
# 	# codename ='add_loan_type',name ='can add loan type',
# 	# codename ='add_other_loans',name ='can add other others',
# content_type = ct)



# can add bioinfo
# can_add_business_details
# can_add_employment_details
# can_add_loan_type
# can_add_bank_details
# new_group1.permissions.add(permission)


class Bioinfo(models.Model):
	No ='No'
	Yes = 'yes'

	single = 'single'
	married = 'married'
	window = 'window'
	other = 'other'

	Owned =(
		(No, 'No'),
  		(Yes, 'yes'),
	)

	Marry=(
		(single, 'single'),
		(married,'married'),
		(window, 'window'),
		(other, 'other')
		)
	
	membership_no = models.PositiveIntegerField()
	first_name = models.CharField(max_length= 50, validators= [onlyletters])
	middle_name = models.CharField(max_length= 50, validators= [onlyletters])
	last_name = models.CharField(max_length= 50, validators= [onlyletters])
	DateOfBirth = models.DateField()
	Homeaddress = models.CharField(max_length= 50, validators= [onlyletters])
	OffieNumber= models.PositiveIntegerField()
	mobile_no = models.CharField(max_length=12,)
	Pin_no = models.CharField(max_length= 50, validators= [onlyisalnum])
	Email = models.EmailField(max_length=100, )
	physical_add = models.CharField(max_length = 100, validators= [onlyletters])
	town = models.CharField(max_length = 100, validators= [onlyletters])
	estate = models.CharField(max_length = 100, validators= [onlyletters])
	house_no = models.CharField(max_length= 100, validators= [onlyisalnum])
	livedthrere=  models.CharField(max_length = 100,validators=[onlyisnumeric])
	Houseowned = models.CharField(max_length=3, choices=Owned,)
	martial_status =models.CharField(max_length=7, choices=Marry,)
	No_dependents = models.PositiveIntegerField()
	bio = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return (self.first_name +"   "+self.middle_name)

	class Meta:
		verbose_name_plural = "Bioinfo"


# client to fill if he/she runs a business
class BusinessDetails(models.Model):
	typeofbusiness = models.CharField(max_length = 100, validators= [onlyletters])
	yrsoperation = models.PositiveIntegerField()
	Businessincome = models.PositiveIntegerField()
	bio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "BusinessDetails"
	def __str__(self):
		return self.typeofbusiness

# client to fill if employe
class EmploymentDetails(models.Model):
	
	Permanent ='Peranent'
	Casual = 'casual'
	Contract = 'Contract'
	terms =(
		(Permanent ,'Peranent'),
		(Casual , 'casual'),
		(Contract, 'Contract'),
		)

	employer= models.CharField(max_length = 100, validators= [onlyletters])
	physical_add = models.CharField(max_length= 100 )
	designation = models.CharField (max_length=100)
	employmenterms= models.CharField(max_length=9, choices=terms,)
	bio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "EmploymentDetails"

	

class Bankdetails(models.Model):
	account_name = models.CharField(max_length= 100)
	acount_no = models.PositiveIntegerField()
	Bank = models.CharField(max_length= 100, validators= [onlyletters])
	branch = models.CharField(max_length= 100)
	bio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "bankdetails"

class LoanType(models.Model):
	Normal = 'normal'
	Development = 'Development' 
	Emergency = 'Emergency'
	school_fee = 'school fee'
	typeloan =(
		(Normal ,'normal'),
		(Development , 'Development'),
		(Development ,'Development'),
		(school_fee , 'school fee'),
		)
	loan = models.CharField(max_length =16, choices = typeloan)
	Purposeofloan=models.TextField()
	amountapplied = models.PositiveIntegerField()
	bio = models.ForeignKey(User, on_delete=models.CASCADE)


class OtherLoans(models.Model):
	bank = models.CharField(max_length = 100, validators= [onlyletters])
	amount_advanced = models.PositiveIntegerField()
	date_granted = models.DateField()
	Repayment_period = models.PositiveIntegerField()
	Outstanding_balance = models.PositiveIntegerField()
	bio = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "OtherLoans"





# codechallenege bankdetails can add_bankdetails
# codechallenege bioinfo can add_bioinfo
# codechallenege business details can add_business_details
# codechallenege employment details can add_employment_details
# codechallenege loan type can add_loan_type
# codechallenege bank details can add_bank_details
# can_add_bankdetails
# can_add_bioinfo
# can_add_business_details
# can_add_employment_details
# can_add_loan_type
# can_add_bank_details