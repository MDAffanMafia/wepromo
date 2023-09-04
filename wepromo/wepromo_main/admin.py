from django.contrib import admin
from .models import Post,User,Comments,Chat
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['senderId','title','link','desc','content']
#User details module    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','userEmail','password']
#Comments on post module    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['sname','rname','comment']   
@admin.register(Chat) 
class ChatAdmin(admin.ModelAdmin):
    list_display=['senderId','senderName','receiverName','message','mainSender','community']   