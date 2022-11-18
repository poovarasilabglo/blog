from django.urls import path,include
from api_app.views import * 
from api_app import views

urlpatterns = [

    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),


]