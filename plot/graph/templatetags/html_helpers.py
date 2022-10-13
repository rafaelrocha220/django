from django import template
import locale

register = template.Library()

@register.filter(name='currency')
def currency(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol=None)
    return "R$ " + valor