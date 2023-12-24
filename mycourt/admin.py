from django.contrib import admin
from .models import Client,CaseType,AddCase,NextListening,InterimOrder,CaseFile,AdvocateProfile ,RespondentAdvocate,Rules

# Register your models here.
admin.site.register(Client)
admin.site.register(AdvocateProfile)
admin.site.register(CaseType)
admin.site.register(CaseFile)
admin.site.register(Rules)
admin.site.register(RespondentAdvocate)
admin.site.register(AddCase)
admin.site.register(NextListening)
admin.site.register(InterimOrder)
