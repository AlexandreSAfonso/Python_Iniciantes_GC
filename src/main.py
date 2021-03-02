import classes

batman = classes.Filmes('Batman', 'ChristoPher Nolan', '2008', 'Ação, Policia, Suspense')


print(batman.titulo, batman.autor, batman.ano, batman.genero, batman.assistido, batman.favorito, sep='\n' )

batman.assistir()
batman.favoritar()
print(batman.titulo, batman.autor, batman.ano, batman.genero, batman.assistido, batman.favorito, sep='\n' )
batman.favoritar()
print(batman.mostrar(), sep='\n')
batman = classes.Filmes.cadastrar('Batman2', 'ChristoPher Nola2', '20082', 'Ação, Policia, Suspense, 2')
print(batman.jsonificar(), sep='\n')




