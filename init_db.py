import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facebook_simulation.settings')
django.setup()
from facebook.models import Post,Status,Friends,Friend_req,Round,Ready
from users.models import Profile
from django.contrib.auth.models import User
from users.models import AllLogin


users = ['UserA','UserB','UserC','UserD','UserE']
status = ['I like Pizza','Hello World','What is coronavirus www.coronavirus.com','What is the meaning of life']
profile_pic = ['img_A','img_B','img_C','img_D','img_E']
# must do first after change db!
def init_friends():
    allusers = User.objects.all()
    for i in users:
        user = allusers.filter(username=i).first()
        f = Friends(userid_id=user.id,myfriends=[])
        f.save()

# must do first after change db!
def init_friends_requst():
    allusers = User.objects.all()
    for i in users:
        user1 = allusers.filter(username=i)
        f = Friend_req(userid_id=user1.id,myfriends_req=[])
        f.save()


def init_status():

    for i in status:
        s = Status(status=i,has_link=False)
        s.save()

def delete_like():
    pass


def delete_friends():
    friends1 = Friends.objects.filter(userid_id=1).first()
    friends2 = Friends.objects.filter(userid_id=2).first()
    friends3 = Friends.objects.filter(userid_id=3).first()
    friends4 = Friends.objects.filter(userid_id=4).first()
    friends5 = Friends.objects.filter(userid_id=5).first()
    friends6 = Friends.objects.filter(userid_id=6).first()
    friends1.myfriends.clear()
    friends2.myfriends.clear()
    friends3.myfriends.clear()
    friends4.myfriends.clear()
    friends5.myfriends.clear()
    friends6.myfriends.clear()

    friends1.myfriends.append(1)
    friends1.myfriends.append(2)
    friends2.myfriends.append(2)
    friends2.myfriends.append(1)
    friends3.myfriends.append(3)
    friends4.myfriends.append(4)
    friends5.myfriends.append(5)
    friends6.myfriends.append(6)


    friends1.save()
    friends2.save()
    friends3.save()
    friends4.save()
    friends5.save()
    friends6.save()

def delete_friend_req():
    friends1 = Friend_req.objects.filter(userid_id=1).first()
    friends2 = Friend_req.objects.filter(userid_id=2).first()
    friends3 = Friend_req.objects.filter(userid_id=3).first()
    friends4 = Friend_req.objects.filter(userid_id=4).first()
    friends5 = Friend_req.objects.filter(userid_id=5).first()
    friends6 = Friend_req.objects.filter(userid_id=6).first()


    friends1.myfriends_req.clear()
    friends2.myfriends_req.clear()
    friends3.myfriends_req.clear()
    friends4.myfriends_req.clear()
    friends5.myfriends_req.clear()
    friends6.myfriends_req.clear()

    friends1.myfriends_req.append(3)
    friends3.myfriends_req.append(1)
    friends1.save()
    friends2.save()
    friends3.save()
    friends4.save()
    friends5.save()
    friends6.save()

def delete_all_rounds():
    Round.objects.all().delete()

def delete_all_posts():
    Post.objects.all().delete()

def delete_all_likes():
    Post.likes.through.objects.all().delete()

def logout_all():
    AllLogin.objects.all().delete()    

def unReady_all():
    Ready.objects.all().delete()    

if __name__ == "__main__":
    # init_friends()
    # init_friends_requst()

    delete_all_rounds()
    delete_all_posts()    
    # delete_all_likes()
    delete_friend_req()
    delete_friends()
    # logout_all()
    unReady_all()
    # init_status()