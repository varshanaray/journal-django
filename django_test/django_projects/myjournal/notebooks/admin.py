from django.contrib import admin

# Register your models here.
from .models import Notebk, Page ,Login
""" Register the models. 
This code imports the models and then calls admin.site.register to register each of them. """
# admin.site.register(Login)
# admin.site.register(Notebk)
# admin.site.register(Page)

# Define the admin class
class NotebkAdmin(admin.ModelAdmin):
    list_display = ('title','description')

# Register the admin class with the associated model
admin.site.register(Notebk, NotebkAdmin)

# Register the Admin classes for Login using the decorator
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Page using the decorator
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass