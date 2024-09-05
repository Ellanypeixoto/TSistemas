#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas necessárias


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# Carregando a base de dados da tabela de faturamento anual
df = pd.read_excel('faturamento.xlsx')
df


# In[4]:


# Mês escolhido: setembro.
setembro = df['setembro']
display(setembro)


# In[5]:


# usando a função describe() para nos fornecer algumas estatísticas necessárias para a nossa resposta:


# In[6]:


# Obtendo o menor valor de faturamento ocorrido em um dia do mês de setembro
setembro.min()


# In[7]:


# Obtendo o maior valor de faturamento ocorrido em um dia do mês
setembro.max()


# In[8]:


# Obtendo o número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# Resposta: 

setembro = df['setembro']
display(setembro)


# In[9]:


# tratando os dados, fazendo a filtragem, excluindo as listas desnecessárias ( "NaN" ):
setembro2 = setembro.dropna(axis=0)
setembro2


# In[10]:


# Transformando o dataframe em uma lista com todos os valores de faturamento - mês setembro:
list(setembro2)


# In[11]:


# Para obter a quantidade de valores acima da média mensal, eu preciso:
# Somar todos os valores da lista e dividir pela quantidade de valores da lista

# Somando todos os valores da lista:
valores_faturamento_setembro = [100.0, 500.0, 200.0]

somatoria_valores_faturamento_mensal = sum(valores_faturamento_setembro)
somatoria_valores_faturamento_mensal


# In[12]:


# Contando a quantidade de valores na lista:
valores_faturamento_setembro = [100.0, 500.0, 200.0]

quantidade_de_valores = (len(valores_faturamento_setembro))
quantidade_de_valores


# In[13]:


# Calculando o valor da média do faturamento - mês setembro:

valores_faturamento_setembro = [100.0, 500.0, 200.0]

valores = [int(val) for val in valores_faturamento_setembro]

media = sum(valores_faturamento_setembro) / len(valores_faturamento_setembro)
print(media)


# In[14]:


# Agora, vamos filtrar na lista os valores de faturamento que estão acima da média (acima do valor 266.66)
def lista_acima_media(numero):
    return numero >= 266

valores_faturamento_setembro = [100.0, 500.0, 200.0]
resultado = list(filter(lista_acima_media, valores_faturamento_setembro))

print(resultado)


# In[15]:


# Contando a quantidade de valores na lista cujo faturamento são acima da média (acima de 266)
len(resultado)


# In[16]:


print("Respostas finais:")
print(f"O menor valor de faturamento ocorrido em um dia do mês de setembro foi {setembro.min()}")
print(f"O maior valor de faturamento ocorrido em um dia do mês de setembro foi {setembro.max()}")
print(f"O número de dias no mês de setembro em que o valor de faturamento diário foi superior à média mensal foi {len(resultado)}.")

