import stripe

from django.views.decorators.csrf import csrf_exempt
from djangoProject import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .utils import get_contex_order, get_items_detail, get_context_items


def main_page(request: HttpRequest) -> HttpResponse:
	return HttpResponse('Payment was successful!')


def item_view(request: HttpRequest, pk) -> HttpResponse:
	return render(request, 'app_payment/item.html', context=get_context_items(pk=pk))


def order_view(request: HttpRequest, pk) -> HttpResponse:
	return render(request, 'app_payment/order.html', context=get_contex_order(pk=pk))


@csrf_exempt
def stripe_config(request: HttpRequest) -> JsonResponse:
	if request.method == 'GET':
		return JsonResponse({'publicKey': settings.STRIPE_API_KEY_PUBLISHABLE}, safe=False)


@csrf_exempt
def buy_item_view(request: HttpRequest, pk) -> JsonResponse:
	if request.method == 'GET':
		stripe.api_key = settings.STRIPE_API_KEY_SECRET
		try:
			checkout_session = stripe.checkout.Session.create(
				success_url='http://127.0.0.1:8000/',
				payment_method_types=['card'],
				mode='payment',
				line_items=[
					{
						"price_data": {
							"currency": "rub",
							"product_data": {"name": get_items_detail(pk).name},
							"unit_amount": int(get_items_detail(pk).price) * 100,
						},
						"quantity": 1,
					},
				]
			)
			return JsonResponse({'sessionId': checkout_session['id']})
		except Exception as e:
			return JsonResponse({'error': str(e)})


@csrf_exempt
def buy_order_view(request: HttpRequest, pk) -> JsonResponse:
	if request.method == 'GET':
		stripe.api_key = settings.STRIPE_API_KEY_SECRET
		order = get_contex_order(pk).get('order')
		discount = order.discount
		tax = order.tax
		try:
			checkout_session = stripe.checkout.Session.create(
				success_url='http://127.0.0.1:8000/',
				payment_method_types=['card'],
				mode='payment',
				line_items=[
					{
						"price_data": {
							"currency": "rub",
							"product_data": {
								"name": get_items_detail(pk).name,
								"description": f'С учётом {discount}% скидки и {tax or 0}% НДС'
							},
							"unit_amount": int(get_contex_order(pk).get('all_price')) * 100,
						},
						"quantity": 1,
						}
				]
			)
			return JsonResponse({'sessionId': checkout_session['id']})
		except Exception as e:
			return JsonResponse({'error': str(e)})
