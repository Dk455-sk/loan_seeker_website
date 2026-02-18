from django.db import models
# Create your models here.

class loanApplication(models.Model):  
    LOAN_TYPES = [
        ('home', 'Home Loan'),
        ('personal', 'Personal Loan'),
        ('car', 'Car Loan'),
        ('business', 'Business Loan'),
        ('property', 'Loan Against Property'),
    ]
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)       
    email = models.CharField(max_length=70)
    mobile = models.CharField(max_length=25)      
    loan_type = models.CharField(max_length=30, choices=LOAN_TYPES)
    loan_amount = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.regid}-{self.name} - {self.loan_type} - {self.loan_amount}"



