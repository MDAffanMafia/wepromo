from django.db import models

# Create your models here.
# For the Login field
class User(models.Model):
    name=models.CharField(max_length=200)
    userEmail=models.EmailField(max_length=200,default="shaikh3@gmail.com")
    password=models.CharField(max_length=200)

    def __str__(self):
        return "hello"
    def json(self):
        return {
            'name': self.name,
        }

# For the Comments field
class Comments(models.Model):
    sname=models.CharField(max_length=200)
    rname=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    def __str__(self):
        return self.sname

# For the post field
class Post(models.Model):
    senderId=models.IntegerField(default=23)
    title=models.CharField(max_length=200)
    link=models.URLField(max_length=200)
    desc=models.CharField(max_length=200)
    content=models.ImageField(upload_to="prodImages",default="shaikh3@gmail.com")
class Chat(models.Model):
    senderId=models.IntegerField()
    senderName=models.CharField(max_length=150)
    receiverName=models.CharField(max_length=150)
    message=models.CharField(max_length=200)
    mainSender=models.CharField(max_length=150,default="md shaikh")
    community=models.CharField(max_length=150,default="Gaming")  
    def json(self):
        return {
            'mainSender': self.mainSender,
            'message':self.message,
            'community':self.community,
        }

