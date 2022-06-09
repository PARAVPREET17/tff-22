from django import forms
from .models import RecruitmentModel

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model=RecruitmentModel
        fields=['name', 'email','phone','roll_no','branch','homecity','qualities','previous_experience','dish_describe','qualities_for_core','upcoming_event_desired']