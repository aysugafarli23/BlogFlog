from django.urls import path
from .views import *

app_name ='homeapi'

urlpatterns = [
    path('create/', CreateBlogView.as_view(), name='apicreate'),
    path('list/', ListBlogView.as_view() , name='apilist'),
    path('detail/<pk>', RetrieveBlogView.as_view(), name='apidetail'),
    path('update/<pk>', UpdateBlogView.as_view(), name='apiupdate'),
    path('delete/<pk>', DeleteBlogView.as_view(), name='apidelete'),
]
