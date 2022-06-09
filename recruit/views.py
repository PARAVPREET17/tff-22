from django.shortcuts import render,HttpResponse,redirect
from .forms import RecruitmentForm
import xlwt
from .models import RecruitmentModel
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def recruit(request):
    if request.method=="POST":
        form=RecruitmentForm(request.POST or None)
        if form.is_valid():
            user=form.save()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            user.save()
            send_mail(
                    'TFF Registration Confirmation',
                    f"""

Greetings {user.name}, soon-to-be sophomore (hopefully),

This is to inform you that you have taken the first step towards becoming a member of the core team for this 'Food Gala', Thapar Food Fest(TFF), 2k22.

All the best for the upcoming rounds. 

Regards,
Team TFF'22
                        """,
                    'thaparfoodfestival22@gmail.com',
                    [email],
                )
            messages.success(request,f"Hello {name} You are successfully registered for Recruitment of TFF'22")
            redirect('recruit')
    return render(request,'recruit/recruit.html')        

def tff16(request):
    return render(request,'2016.html')

def tff17(request):
    return render(request,'2017.html')

def tff18(request):
    return render(request,'2018.html')

def tff19(request):
    return render(request,'2019.html')

def export_answers_xls(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="tffrecruitment.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Recruitment responses')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['name', 'email','phone','roll_no','branch','homecity','qualities','previous_experience','dish_describe','qualities_for_core','upcoming_event_desired']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = RecruitmentModel.objects.order_by('name').values_list('name', 'email','phone','roll_no','branch','homecity','qualities','previous_experience','dish_describe','qualities_for_core','upcoming_event_desired')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response
    else:
        return redirect('home')    