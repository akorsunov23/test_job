from django.urls import path
from .views import item_view, buy_item_view, stripe_config, main_page, order_view, buy_order_view


app_name = 'app_payment'

urlpatterns = [
	path('', main_page, name='main'),
	path('item/<int:pk>/', item_view, name='detail_item'),
	path('buy/<int:pk>/', buy_item_view, name='buy_item'),
	path('order/<int:pk>/', order_view, name='detail_order'),
	path('buy_order/<int:pk>/', buy_order_view, name='buy_order'),
	path('config/', stripe_config),

]
