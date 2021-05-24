print('"Bem vindo à Casa de Câmbio Muito Dinheiro"')

nome = input('Qual é o seu nome? ')

real = float (input('Quanto você deseja converter para dólar ou para euro? R$'))

dolar = real / 5.37

euro = real / 6.53

taxa = 10 / 100

print('Considerando a taxa de câmbio de 10%, ', nome, 'você poderá comprar com R${:.2f} o valor de US${:.2f} e de €{:.2f}'.format(real, dolar * (1-taxa), euro * (1-taxa)))

print('Segue detalhamento abaixo:')

print('Dólar: US$ ', dolar)
print('Desconto da Taxa de Câmbio: US$ ', dolar * taxa)
print('Valor com desconto: US$ ', dolar * (1-taxa))

print('Euro: € ', euro)
print('Desconto da Taxa de Câmbio: € ', euro * taxa)
print('Valor com desconto: € ', euro * (1-taxa))

print('Obrigada, pela preferencia', nome, '!')
