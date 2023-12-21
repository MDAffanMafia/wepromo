from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms_main import SignUp
from wepromo_main.models import  Comments,User,Post,Chat
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    ff=SignUp()
    print(request.session.get('user_id'))
    currentSession=request.session.get('user_id')
    return render(request,'index.html',{'curSession':currentSession})
def signup(request):
    if request.method=='POST':
        username=request.POST['first_name']+" "+request.POST['last_name']
        email=request.POST['user_email']
        password=request.POST['password']
        print(username)
        print(password)
        new_user=User(name=username,userEmail=email,password=password)
        new_user.save()

    return render(request,'signup.html')   
def login(request):
    if request.method=='POST':
        print("hello")
        allUser=User.objects.all()
        username=request.POST['username']
        password=request.POST['password']
        h=False
        for user in allUser:
            if user.name==username:
                if user.password==password:
                    print("got it")
                    request.session['user_id']=user.id
                    request.session['user_name']=user.name
                    h=True
                    break
        if h==True:
            h=False
            return redirect('/')
        else:
            return redirect('/login')
    return render(request,'login.html')
def group(request):
    if request.method=='POST':
         senderName=request.session.get('user_name')
         mainSender=request.session.get('user_name')
         message=request.POST['message']
         community=request.POST['community']
         sendId=request.session.get('user_id')
         newchat=Chat( senderId=sendId,senderName=senderName,receiverName="mudassir",message=message,mainSender=mainSender, community=community)
         newchat.save()
    user=User.objects.all()
    us=request.session.get('user_name')
    print(us,"the user name")
    chat=Chat.objects.filter(senderName=us)
    print(chat)
    currentSession=request.session.get('user_name')
    return render(request,'group.html',{'user_dis':user,'user_name':currentSession,'user_chat':chat})
def addContent(request):
    return render(request,'addContent.html')
def comment(request):

    return render(request,'comment.html')
def rank(request):
    return render(request,'rank.html')
def userFeed(request):
    comment=Comments.objects.all()
    posts=Post.objects.all()
    postone=Post.objects.filter(pk=1)
    print(postone ,"this is the value")
    count=0
    for po in posts:
        count+=1
    print("the row count".count)    
    currentSession=request.session.get('user_id')
    return render(request,'userFeed.html',{'comm':comment,'currSession':currentSession,'post':posts})    

def addPost(request):
    if request.method=='POST':
       senderId=request.session.get('user_id') 
       title=request.POST['title']
       link=request.POST['link']
       desc=request.POST['desc']
       content=request.FILES.get('myfile')   
       mcontent=content
       new_post=Post(senderId=senderId,title=title,link=link,desc=desc,content=mcontent)
       new_post.save()
       return redirect('userFeed')
    return render(request,'addPost.html')
def logout(request):

    del request.session['user_id']
    return redirect('/')

        