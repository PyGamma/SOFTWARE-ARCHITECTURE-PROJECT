from django.contrib import admin
from .models import Staff

class StudentAdmin(admin.ModelAdmin):
	list_display = ('staff_id', 'first_name','last_name', 'b_date', 'telephone', 'gender', 'district', 'nationality')
	list_filter = ('staff_id', 'first_name','last_name', 'b_date', 'telephone', 'gender', 'district', 'nationality')

# Register your models here.
admin.site.register(Staff, StudentAdmin)