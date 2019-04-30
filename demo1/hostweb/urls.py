from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('login/', views.login),
    path('register/', views.register),
    path('search/<int:pk>/', views.search),
    path('profile/<int:pk>/', views.profile),
    path('star/<int:pk>/', views.star),
    path('my_collections/<int:pk>/', views.my_collections),
    path('my_account/', views.my_account),
    path('buyed_resource/', views.buyed_resource),
    path('expert_home/<int:pk>', views.expert_home),
    path('add_item_list/<int:pk>/', views.add_item_list),
    path('item_cart/<int:pk>/', views.item_cart),
    path('purchase/', views.purchase),
    path('apply_for_expert/', views.apply_for_expert),
    path('has_published/', views.has_published),
    path('publish_item_application/', views.publish_item_application),
    path('U2E_pass/', views.U2E_pass),
    path('PUB_pass/', views.PUB_pass),
    path('api-test/Users/', views.User_list),
    path('api-test/resource_list/', views.resource_list),
]