from django import template
from courses.models.currency_model import CurrencyValue
register = template.Library()


@register.simple_tag
def calculate_discount(price, discount):
    if discount is None or discount is 0:
        return format(round(price, 2), '.2f')
    else:
        return format(round(price - (price * discount * .01), 2), '.2f')


@register.simple_tag
def get_decimal(price):
    return format(round(price, 2), '.2f')


@register.filter
def currency_value(price):
    active_currency = CurrencyValue.objects.filter(status=True).first()
    if active_currency:
        value = int(active_currency.value) * price
        return f'{active_currency.symbole} {value}'
    else:
        return f'{active_currency.symbole} {price}'
