from django.urls import path
from mardikor.views import home,signup,check_user,user_login,user_logout,ishBeruvchiProfile,\
    viewProfile,change_password,advertisement,myAnnouncement,\
    update_announce,announce_details,allAnounce,about,employer,\
    allEmployers,employer_details,update_resume,search
urlpatterns = [
    path('',home,name='index-page'),
    path('signup/',signup,name='signup'),
    path('check_user/',check_user,name='check_user'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('ishberuvchi-panel/',ishBeruvchiProfile,name='ishBeruvchiProfile'),
    path('viewProfile/',viewProfile,name='viewProfile'),
    path('change_password/',change_password,name='change_password'),
    path('advertisement/',advertisement,name='advertisement'),
    path('myAnnouncement/',myAnnouncement,name='myAnnouncement'),
    path('update_announce/',update_announce,name='update_announce'),
    path('announce_details/<int:pk>',announce_details,name='announce_details'),
    path('allAnounce/',allAnounce,name='allAnounce'),
    path('about/',about,name='about'),
    path('employer/',employer,name='employer'),
    path('allEmployers/',allEmployers,name='allEmployers'),
    path('employer_details/<int:pk>',employer_details,name='employer_details'),
    path('update_resume/',update_resume,name='update_resume'),
    path('search/',search,name='search'),
]
