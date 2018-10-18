# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!\n")

# Vamos verificar quantas linhas nós temos
print("Número de linhas: {}\n".format(len(data_list)))
# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: {}\n".format(data_list[0]))
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: {}\n".format(data_list[1]))
input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    # Vai transformar a lista para string, e passar ela para a variavel line
    line = str(data_list[i])
    # Vai inserir a string " desconhecido" nos campos vazios
    line = line.replace("''"," ").replace("  "," Desconhecido")
    # Vai remover os colchetes e aspas
    line = line.replace("[","").replace("]","").replace("'","")
    print("Linha {}: {}\n".format(i+1, line))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(20):
    # Vai transformar a lista para string, e passar ela para a variavel line
    line = str(data_list[i][-2])
    # Vai inserir a string "Desconhecido" nos campos vazios
    if(len(line) == 0):
        line = "Desconhecido"
    print("Linha {}: {}\n".format(i+1, line))


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função que adiciona as colunas(features) de uma lista em outra lista, na mesma ordem.
      Argumentos:
          data: A lista de dados (list).
          index: O indice da coluna (int).
      Retorna:
          Uma lista com os valores da coluna escolhida pelo indice 'index'
    """
    column_list = [column[index] for column in data]
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
empty = 0
column_list = column_to_list(data_list, -2)
for column in column_list:
    if column == "Male":
        male+=1
    elif column == "Female":
        female+=1
    else:
        empty += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função que conta a quantidade de cada gênero em uma lista.
      Argumentos:
          data_list: A lista de dados (list).
      Retorna:
          Uma lista com as quantidades de homem e mulher, no formato [qntd_male, qntd_female].
    """
    male = 0
    female = 0

    column_list = column_to_list(data_list, -2)
    for column in column_list:
        if column == "Male":
            male += 1
        elif column == "Female":
            female+=1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Função que determina o gênero mais popular da lista de dados.
      Argumentos:
          data_list: A lista de dados (list).
      Retorna:
          answer: gênero mais popular da lista de dados (string) podendo ser,
                  "Male" caso o masculino, "Female" caso o feminino e "Equal" caso iguais.
    """
    gender = count_gender(data_list)
    answer = ""
    if gender[0] > gender[1]:
        answer = "Male"
    elif gender[0] < gender[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")

# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_user_types(data_list):
    """
    Função que conta a quantidade de cada tipo de usuario em uma lista.
      Argumentos:
          data_list: A lista de dados (list).
      Retorna:
          Uma lista com as quantidades de usuarios, no formato [qntd_customer, qtnd_dependent, qntd_subscriber].
    """
    customer = 0
    dependent = 0
    subscriber = 0

    column_list = column_to_list(data_list, -3)
    for column in column_list:
        if column == "Customer":
            customer += 1
        elif column == "Dependent":
            dependent += 1
        else:
            subscriber += 1
    return [customer, dependent, subscriber]


user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Dependent", "Subscriber"]
quantity = count_user_types(data_list)
print("Customer:{}\nDependent:{}\nSubscriber:{}".format(quantity[0], quantity[1], quantity[2]))
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem {} campos vazios na coluna gênero.".format(empty)
print("resposta: {}\n".format(answer))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
# Transforma os elementos da list de string para int
trip_duration_list = [int(i) for i in trip_duration_list]
# Ordena lista de forma crescente
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
size = len(trip_duration_list)
soma = sum(trip_duration_list)
# Vai calcular a media e arrendondar ela
mean_trip = round(soma / size)
mean_trip = round(mean_trip)
# Vai calcular a mediana
if size % 2 == 1:
    # a variavel p vai armazenar a posiçao do elemento do meio da lista
    p = size//2
    median_trip = trip_duration_list[p]
else:
    # a variavel p1 e p2 vão armazenar as posições dos elementos do meio da lista
    p1 = size//2
    p2 = p1 - 1
    median_trip = (trip_duration_list[p1] + trip_duration_list[p2]) / 2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.


# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = "yes"

def count_items(column_list):
    """
    Função que conta a ocorrência de cada item diferente em uma lista, sem ser necessário definir os itens.
      Argumentos:
          column_list: A lista de itens (list).
      Retorna:
            item_types - os tipos diferentes de itens na lista. (list)
            count_items - quantidade de cada tipo de itens na lista. (list)
    """
    item_types = []
    count_items = []
    # Varre a lista "column_list" elemento por elemento
    for item in column_list:
        if item not in item_types:
            # Adiciona um novo tipo na lista "item_types" e cria seu corresponde na lista "count_items"
            item_types.append(item)
            count_items.append(1)
        else:
            # Incrementa o correspondente do item na lista "count_items"
            i = item_types.index(item)
            count_items[i] += 1
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
