from django.contrib import admin
from  .models import user
# Register your models here.

# admin.site.register(user)

@admin.register(user)
class userAdmin(admin.ModelAdmin):
      list = ('id', 'name', 'email', 'password')



