from django.contrib import admin
from api_app.models import  Post,Comment,Category


class Postadmin(admin.ModelAdmin):
    list_display = ('id','title','content','owner','created_at','updated_at')

admin.site.register(Post,Postadmin)


class Commentadmin(admin.ModelAdmin):
    list_display = ('id','owner','post','content','created_at')

admin.site.register(Comment,Commentadmin)


class Categoryadmin(admin.ModelAdmin):
    list_display = ('id','name','owner')

admin.site.register(Category,Categoryadmin)