from django.urls import path
from . import views

urlpatterns=[
path('recruit/',views.recruit,name='recruit'),
path('',views.home,name='home'),
path('tff16/',views.tff16,name='tff16'),
path('tff17/',views.tff17,name='tff17'),
path('tff18/',views.tff18,name='tff18'),
path('tff19/',views.tff19,name='tff19'),
path('export/',views.export_answers_xls,name='export'),
]