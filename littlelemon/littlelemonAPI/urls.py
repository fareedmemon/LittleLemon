from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register('tables', views.BookingViewSet, basename='tables')

urlpatterns = [
    path('booking/', include(router.urls)),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-auth-token/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
