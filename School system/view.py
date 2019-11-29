from django.shortcuts import render
from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from Student.models import Student
from Staff.models import Staff



def home(request):
	return render(request, 'index.html')


def Logedin(request):
	return HttpResponse('Welcome Programmer!!!') 


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		form.save()
		messages.success(request, f'User Account Created successfully')
		return render(request, 'Registration/signup.html', {'form' : form})
	else:
		form = UserCreationForm()
	return render(request, 'Registration/signup.html', {'form' : form})

def admission(request):
	return render(request, 'admission.html')

def add_admission(request):
	print("Form Data saved")
	stu_id = request.POST.get("reg_no")
	first_name = request.POST.get("First_Name")
	last_name = request.POST.get("Last_Name") 
	b_date_day = request.POST.get("Birthday_day")
	b_date_day = str(b_date_day)
	b_date_month = request.POST.get("Birthday_Month")
	b_date_month = str(b_date_month)
	b_date_year = request.POST.get("Birthday_Year")
	b_date_year = str(b_date_year)
	b_date = b_date_day + " " + b_date_month + " " + b_date_year 
	telephone = request.POST.get("Mobile_Number")
	gender = request.POST.get("Gender")
	district = request.POST.get("District")
	nationality = request.POST.get("Country")
	student_instance = Student(stu_id=stu_id, first_name=first_name, last_name=last_name, b_date= b_date,
						 telephone=telephone, gender=gender, district= district, nationality= nationality )
	student_instance.save()
	return render(request, 'admission.html')


def staff(request):
	return render(request, 'staff.html') 


def add_staff(request):
	staff_id = request.POST.get("employee_id")
	first_name = request.POST.get("First_Name")
	last_name = request.POST.get("Last_Name") 
	b_date_day = request.POST.get("Birthday_day")
	b_date_day = str(b_date_day)
	b_date_month = request.POST.get("Birthday_Month")
	b_date_month = str(b_date_month)
	b_date_year = request.POST.get("Birthday_Year")
	b_date_year = str(b_date_year)
	b_date = b_date_day + " " + b_date_month + " " + b_date_year 
	telephone = request.POST.get("Mobile_Number")
	gender = request.POST.get("Gender")
	district = request.POST.get("District")
	nationality = request.POST.get("Country")
	staff_instance = Staff(staff_id=staff_id, first_name=first_name, last_name=last_name, b_date= b_date,
						 telephone=telephone, gender=gender, district= district, nationality= nationality )
	staff_instance.save()
	return render(request, 'staff.html')


def ViewStudent(request):
	data = Student.objects.all()
	print(data)
	context= {'data': data}
	return render(request, 'studentview.html', context)


def ViewStaff(request):
	data = Staff.objects.all()
	print(data)
	context= {'data': data}
	return render(request, 'staffview.html', context)


def FlashPage(request):
	return render(request, 'panel.html')
