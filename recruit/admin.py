from django.contrib import admin
from .models import RecruitmentModel

# Register your models here.
class RecruitmentAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','roll_no','branch')
admin.site.register(RecruitmentModel,RecruitmentAdmin)
