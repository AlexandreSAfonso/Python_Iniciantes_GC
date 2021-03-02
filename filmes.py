### Variaveis

NomeDoFilme = "Star Wars"
AnoDoFilme = 219
NotaDoFilme = 7.4
FilmeDisponivel = True

print(NomeDoFilme, AnoDoFilme, NotaDoFilme, FilmeDisponivel, sep='\n') 

#sep= o que deve colocar como separador, '\n' separador de linha 
#end= define o que deve ser impresso ao final de todos.

NomeDoFilme = input("Qual o nome do filme: ")
AnoDoFilme =  input("Qual o ano do filme: ")
NotaDoFilme = input("Qual a nota do filme: ")
#trocar o tipo de dados novo tipo parenteses 
NotaDoFilme2 = float(NotaDoFilme)
FilmeDisponivel = False
print(NomeDoFilme, AnoDoFilme, NotaDoFilme, FilmeDisponivel, sep='\n') 

#type mostra o tipo de dados
print(type(NotaDoFilme))
print(type(NotaDoFilme2))

#Estrutura de Decisão
if FilmeDisponivel:
    print(NomeDoFilme, AnoDoFilme, NotaDoFilme, FilmeDisponivel, sep='\n') 
else:
    print("Filme não está disponível!")

# Lista 
ListaDeFilme = ['Star Wars', '1917', 'Forde vs Ferrary', 'Batman Beguins', 'Coringa', 'Juumanji']
print (ListaDeFilme)
print (type(ListaDeFilme))
#Mostrar posição da lista
print (ListaDeFilme[1])
#adicionar um item à Lista
ListaDeFilme.append('Connan')
print (ListaDeFilme)
print (len(ListaDeFilme))
#remover intens
ListaDeFilme.remove('Star Wars')
print (ListaDeFilme)
print (len(ListaDeFilme))

#laços e repetições
ListaDeDesejosDeFilmes=[]
for numero in range(6):
    ListaDeDesejosDeFilmes.append(input("Qual o nome do filme: "))
print(ListaDeDesejosDeFilmes)

#exibir linha por linha
for filmeAtual in ListaDeDesejosDeFilmes:
    print(filmeAtual)

#por posições
for filmeAtual in range(len(ListaDeDesejosDeFilmes)):
    print(filmeAtual, ' ',ListaDeDesejosDeFilmes[filmeAtual])
