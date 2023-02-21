from app_payment.models import Order, Item


def get_contex_order(pk) -> dict:
	order = Order.objects.\
		select_related('discount', 'tax').\
		prefetch_related('items').\
		only('user__username', 'items__name', 'items__price', 'discount__discount', 'tax__tax').\
		get(pk=pk)
	price = [int(item.price) for item in order.items.all()]

	if order.discount and order.tax:
		price = sum(price) - ((sum(price) * int(order.discount.discount)) / 100)
		price = price + ((price * int(order.tax.tax)) / 100)
	elif order.discount:
		price = sum(price) - ((sum(price) * int(order.discount.discount)) / 100)
	elif order.tax:
		price = sum(price) + ((sum(price) * int(order.tax.tax)) / 100)

	context = {
		'order': order,
		'all_price': price
	}
	return context


def get_context_items(pk) -> dict:
	item = Item.objects.get(pk=pk)
	context = {
		'item': item
	}
	return context


def get_items_detail(pk):
	item = Item.objects.only('name', 'price').get(pk=pk)
	return item
