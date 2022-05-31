
from django.contrib import admin
from .models import Profile, User
from django.contrib.auth.models import Group



# class UserAdmin(admin.ModelAdmin):
#     model = User

# admin.site.unregister(Group)
# admin.site.register(User,UserAdmin)
# admin.site.register(Profile)

# class UserAdmin(admin.ModelAdmin):
#     model = User
#     inlines = [ProfileInline]

# admin.site.unregister(User)
admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Profile)   
# admin.site.register(Profile)
# Remove: admin.site.register(Profile)  
  