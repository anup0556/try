from django.contrib import admin
from django.contrib.auth.models import Group,User
from.models import profile

# Register your models here.
admin.site.unregister(Group)
class profileInline(admin.StackedInline):
    model=profile

class useradmin(admin.ModelAdmin):
         model=User
fields=["username"] 
inlines=[profileInline]      

admin.site.unregister(User)
admin.site.register(User,useradmin)
#admin.site.register(profile)