from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api_app.views import (
    UserViewSet,
    CategoryViewSet,
    PostViewSet,
    CommentViewSet,
    LoginView,
    RegisterUserAPIView,
    ChangePasswordView,
)
router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'post',PostViewSet)
router.register(r'comment',CommentViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('log/', LoginView.as_view()),
    path('reg/',RegisterUserAPIView.as_view()),
    path('pass/<int:pk>/', ChangePasswordView.as_view()),
    #path('user/', UserList.as_view()),
    #path('user/<int:pk>/', UserDetail.as_view()),
    #path('post/', PostList.as_view()),
    #path('post/<int:pk>/', PostDetail.as_view()),
    #path('comment/', CommentList.as_view()),
    #path('comment/<int:pk>/', CommentDetail.as_view()),
    #path('categories/', CategoryList.as_view()),
    #path('categories/<int:pk>/', CategoryDetail.as_view()),
]




