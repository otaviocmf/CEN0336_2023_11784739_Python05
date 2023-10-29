# 1) Construa um dicionário de suas coisas favoritas.
fav_dict = {
    'livro': 'Indústria Cultural',
    'som': 'The Doors - Strange Days',
    'árvore': 'Kapok'
}

# 2) Print o seu livro favorito.
print(fav_dict['livro'])

# 3) Print o seu livro favorito, mas use uma variável na chave.
fav_thing = 'livro'
print(fav_dict[fav_thing])

# 4) Agora print a sua árvore favorita.
print(fav_dict['árvore'])

# 5) Adicione o seu "organismo" favorito ao dicionário. 
# Faça com que "organismo" seja o novo valor da chave fav_thing.
fav_thing = 'organismo'
fav_dict[fav_thing] = 'Ostra Japonesa'  # Exemplo de organismo favorito.
print(fav_dict[fav_thing])

# 6) Obtenha um valor da linha de comando para fav_thing e print o valor desse item do dicionário. 
print("\nOpções disponíveis:")
for chave in fav_dict:
    print(chave)
fav_thing = input("Qual das opções acima você quer saber? ")
if fav_thing in fav_dict:
    print(fav_dict[fav_thing])
else:
    print("Opção inválida!")

# 7) Altere o valor do seu organismo favorito.
fav_dict['organismo'] = 'Lince Ibérico'  # Alterando para outro exemplo de organismo favorito.
print("\nOrganismo favorito atualizado:", fav_dict['organismo'])

# 8) Obtenha fav_thing da linha de comando e um novo valor para essa chave. 
# Altere o valor com o valor inserido pelo usuário.
fav_thing = input("Para qual favorito você gostaria de atualizar o valor? (ex: livro, som, árvore, organismo) ")
if fav_thing in fav_dict:
    novo_valor = input(f"Digite o novo valor para {fav_thing}: ")
    fav_dict[fav_thing] = novo_valor
    print(f"Valor atualizado para {fav_thing}:", fav_dict[fav_thing])
else:
    print("Opção inválida!")

# 9) Use um loop for para imprimir cada chave e valor do dicionário.
for chave, valor in fav_dict.items():
    print(f"{chave}: {valor}")


