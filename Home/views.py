from django.shortcuts import render
from .models import loanApplication

def loan_application(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        loan_amount = request.POST["loanamount"]
        loan_type = request.POST["loantype"]

        ob = loanApplication.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            loan_amount=loan_amount,
            loan_type=loan_type
        )
        ob.save()
        return render(request, 'success.html', {'name': name})

    return render(request, 'loan_application.html')

def home(request):
    return render(request,"home.html")
def home_loan(request):
    return render(request,"homeloan.html")

def bussiness_loan(request):
    return render(request,"bussiness_loan.html")

def personal_loan(request):
    return render(request,"personal_loan.html")
def poperty_loan(request):
    return render(request,"poperty_loan.html")
def credit(request):
    return render(request,"credit.html")
def gureenty(request):
    return render(request,"gureenty.html")
def term(request):
    return render(request,"term.html")
def bill_discount(request):
    return render(request,"bill_discount.html")
def contactus(request):
    return render(request,"contact.html")

# def emi_calculator(request):
#     if request.method=="POST":
#         p=request.POST["principal"]
#         r=request.POST["annual_rate"]
#         n=request.POST["tenure_months"]
#         monthly_rate=r/(12*100)
#         emi=(p * monthly_rate * (1 + monthly_rate)**n) / ((1 + monthly_rate)**n - 1)

#         return render(request,"emi_calculator.html",{'emi':emi})
#     return render(request,"emi_calculator.html")


from django.shortcuts import render

def emi_calculator(request):
    if request.method == "POST":
        try:
            p = float(request.POST["principal"])
            r = float(request.POST["annual_rate"])
            tenure_input = request.POST["tenure"]
            tenure_type = request.POST.get("tenure_type", "months")

            if not tenure_input:
                raise ValueError("Tenure is required.")

            # Convert years to months if needed
            if tenure_type == "years":
                n = int(float(tenure_input) * 12)
            else:
                n = int(tenure_input)

            monthly_rate = r / (12 * 100)
            
            # EMI formula
            emi = (p * monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
            emi = round(emi, 2)

            total_payment = round(emi * n, 2)
            total_interest = round(total_payment - p, 2)

            # Percentages for chart (not mandatory, but can be used)
            principal_percent = round((p / total_payment) * 100, 2)
            interest_percent = round((total_interest / total_payment) * 100, 2)

            context = {
                'emi': emi,
                'total_payment': total_payment,
                'total_interest': total_interest,
                'principal_percent': principal_percent,
                'interest_percent': interest_percent,
                'p': p,
                'r': r,
                'tenure_input': tenure_input,
                'tenure_type': tenure_type,
                'n': n
            }
            return render(request, "emi_calculator.html", context)

        except Exception:
            return render(request, "emi_calculator.html", {
                'error': 'Please enter valid numeric values for all fields.'
            })

    # GET request or first load
    return render(request, "emi_calculator.html")

