from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','mobile','email','password','is_Hr','is_Admin','is_Employee')
    search_fields=('first_name','last_name','email')
    list_filter=('is_Hr','is_Admin','is_Employee')


admin.site.register(User,UserAdmin)

class EmployeeReferralAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','dob','email_id','contact','address','position','location','what_relation','experience','profile_photo','resume_upload')

admin.site.register(EmployeeReferral,EmployeeReferralAdmin)