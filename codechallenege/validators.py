from django.core.exceptions import ValidationError
  
#string_name.isnumeric() numbers
#first_name.isalpha() strings only
# pin.isalnum()

def onlyletters(value):
    if value.isalpha() == True:
        return  value
    else:
         raise ValidationError("only letters are allowed")

def onlyisalnum(value):
    if value.isalnum() == True:
        return  value
    else:
        raise ValidationError("only numbers and letters are allowed")


def onlyisnumeric(value):
    if value.isnumeric() == True:
        return  value
    else:
        raise ValidationError("enter numbers only")




