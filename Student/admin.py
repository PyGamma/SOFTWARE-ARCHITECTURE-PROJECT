from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ('stu_id', 'first_name','last_name', 'b_date', 'telephone', 'gender', 'district', 'nationality')
	list_filter = ('stu_id', 'first_name','last_name', 'b_date', 'telephone', 'gender', 'district', 'nationality')

admin.site.register(Student, StudentAdmin)

# Register your models here.
