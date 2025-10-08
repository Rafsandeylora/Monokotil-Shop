from django.urls import path
from main.views import (
    show_main, show_product,
    register, login_user, logout_user, 
    create_product_ajax, delete_product_ajax, get_product_json,
    register_ajax, login_ajax,
    show_xml, show_json, show_xml_by_id, show_json_by_id,edit_product_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    
    path('product/<int:id>/', show_product, name='show_product'),
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
 
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_product_ajax, name='create_product_ajax'),
    path('delete-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('edit-ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),

   
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:product_id>/', show_xml_by_id, name='show_xml_by_id'), 
    path('json/<int:product_id>/', show_json_by_id, name='show_json_by_id'),
]