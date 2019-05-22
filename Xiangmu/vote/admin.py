from django.contrib import admin
from .models import question,choice,MyUser

# Register your models here.
admin.site.register(question)
admin.site.register(choice)
admin.site.register(MyUser)
