from django.contrib import admin
from .models import Bioinfo, BusinessDetails, EmploymentDetails, Bankdetails, LoanType,OtherLoans


admin.site.register(Bioinfo)
admin.site.register(EmploymentDetails)
admin.site.register(BusinessDetails)
admin.site.register(LoanType)
admin.site.register(OtherLoans)
admin.site.register(Bankdetails)

