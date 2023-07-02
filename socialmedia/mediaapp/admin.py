from django.contrib import admin

from .models import Users,Profile,Post,Like,Comment,Tag,Follow,Message,Group

admin.site.register(Users)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Message)
admin.site.register(Group)

