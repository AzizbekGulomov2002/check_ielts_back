from django.contrib import admin

# Register your models here.
from .models import IELTS

class IELTSAdmin(admin.ModelAdmin):
   
    list_display = ['family_name','first_name','candidate_number','candidate_id', 'overal', 'cefr_level']
    list_per_page = 10
    ordering = ('candidate_number','family_name','first_name','candidate_id',)
    search_fields = ['candidate_number','family_name','first_name','candidate_id',]

admin.site.register(IELTS, IELTSAdmin)


from .models import Pupil
@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']
    list_per_page = 8
    list_filter = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']
    search_fields = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']