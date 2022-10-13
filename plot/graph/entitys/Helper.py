import locale

class Helper:
    
    def moeda(self, valor):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(valor, grouping=True, symbol=None)
        return "R$ " + valor
           
           
    def quantidade(self, qtd):
        return '{0:,}'.format(qtd).replace(',','.')