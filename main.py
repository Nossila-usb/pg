calcular_pg = lambda x: x*2

numeros = [1,2,3,4,5,6,7,8,9]

# usanfos a função map para gerar uma lista de progressão geometrica
pg = list(map(calcular_pg, numeros))

# exibe a tela da lista
for i in pg:
    print(i)
