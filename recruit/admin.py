from django.contrib import admin
from .models import RecruitmentModel,Ardour

# Register your models here.
class RecruitmentAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','roll_no','branch')
admin.site.register(RecruitmentModel,RecruitmentAdmin)
class ArdourAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','roll_no','branch')
admin.site.register(Ardour,ArdourAdmin)
