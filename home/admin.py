from django.contrib import admin
from .models import Post, Profile, Contact, Booking

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('user','source','destination','vacant_seats','date_of_trip','time_of_trip','price')

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','contact_no','image')

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc','time')

# class ContactAdmin(admin.ModelAdmin):
#     list_display=('name','email','phone','desc','time')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Booking)
