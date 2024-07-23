from readline import redisplay
import pandas as pd

#Criando um dataFrame do zero : Não é muito usual, melhor criar a partir de um dicionário do Python
#datarame = pd.DataFrame()

#Criando um dicionario
vendas = {'data': ['15/02/2021', '16/02/2021'],
         'valor':[500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
         }

#Criando um df a partir de um dicionario
vendas_df = pd.DataFrame(vendas)
#print(vendas_df)

#importando a partir de uma base de dados (Planilha_pneus.xls)
pneus_df = pd.read_excel("Planilha_pneus.xlsx")
#print(pneus_df)

#importando a partir de uma base de dados (circuits.csv)
circuits_df = pd.read_csv("circuits.csv")
print(circuits_df.head(10)) #10 primeiros
#print(circuits_df.tail(5)) #5 ulimos
#print(circuits_df.shape) #Mostra quantas linhas e quantas colunas tem na tabela
#print(circuits_df.describe()) #Media das coisas

#Editar o dataframe
nome = circuits_df['circuitRef']
#print(nome) #Uma coluna nao se caracteriza como dataframe

# Método .loc[linhas, colunas]
# - Pegar Uma linha
print(circuits_df.loc[10:5])
# - Pegar todas as linhas (devem corresponder uma condicao)
print(circuits_df.loc[circuits_df["circuitRef"] == "monaco"])
# - Pegar várias linhas e colunas usando loc
monacoDf = circuits_df.loc[circuits_df["circuitRef"] == "monaco", ["location", "country"]]
print(monacoDf)
# - Pegar um valor específico
print(circuits_df.loc[5, "name"])

#Adicionar uma coluna
 # - A partir de uma coluna que existe
circuits_df['nome'] = circuits_df['name']
print(circuits_df)
 # - Criar uma coluna com valor padrao
circuits_df.loc[:, 'preco_ingreco'] = 0
print(circuits_df)

#Adicionar linha

#Excluir linha e coluna
circuits_df = circuits_df.drop("preco_ingreco", axis=1) #eixo da coluna = 1 e eixo da linha é 0
print(circuits_df)

#Valores Vazios
circuits_df = circuits_df.dropna(how='all')

#Deletar linhas que possuem pelo menos 1 valor vazio
circuits_df = circuits_df.dropna()

#Preencher valores vazios
# - Preencher com a média da coluna
#circuits_df['tabela'] = circuits_df['tabela'].fillna()

#Calcular indicadores
# - Value Counts : Conta quantos valores tem
# - Group by : Agrupar as infos

#Mesclar dataframes (merge)
