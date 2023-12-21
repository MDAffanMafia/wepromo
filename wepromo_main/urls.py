from django.urls import path
from wepromo_main import views
print("that is for url")
urlpatterns = [
    path('',views.index,name='index'),
    path('userFeed',views.userFeed,name='userFeed'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('addContent',views.addContent,name='addContent'),
    path('rank',views.rank,name='rank'),
    path('comment',views.comment,name='comment'),
    path('addPost',views.addPost,name='addPost'),
    path('logout',views.logout,name="logout"),
    path('group',views.group,name='group'),   
   
]
