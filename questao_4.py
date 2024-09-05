#!/usr/bin/env python
# coding: utf-8

# In[93]:


# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np


# In[94]:


# Declarando os tipos das variáveis
SP = "SP"
RJ = "RJ"
MG = "MG"
ES = "ES"
OUTROS = "OUTROS"

percentual = 0.0
percentual_sp = float
percentual_rj = float
percentual_mg = float
percentual_outros = float
soma_faturamento_todos_estados = float


# In[95]:


# Especificando os dados do faturamento em cada estado

faturamento_mensal_por_estado = ({
     'SP':[6783643],
     'RJ' :[3667866],
     'MG':[2922988],
     'ES':[2716548],
     'OUTROS':[1984953]   
               })
# Gerando um DataFrame
df = pd.DataFrame(faturamento_mensal_por_estado)
print(df)


# In[96]:


# Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora:
# Resolução: primeiramente, vamos somar o faturamento de todos os estados
# Para somar, vamos criar uma lista contendo os valores de faturamento de todos os estados:

Row_list =[]
  

for rows in df.itertuples():
    
    faturamento_mensal_por_estado =[rows.SP, rows.RJ, rows.MG, rows.ES, rows.OUTROS]
      
    
    Row_list.append(faturamento_mensal_por_estado)
  

print(Row_list)


# In[97]:


# Depois de ter criado a lista com todos os valores de faturamento, vamos somar:

soma_faturamento_todos_estados = sum(faturamento_mensal_por_estado)
soma_faturamento_todos_estados


# In[98]:


# Com o valor da somatória obtido, agora vamos calcular o percentual de representação que cada estado teve em relação ao valor total mensal :


# In[99]:


# Percentual do estado de SP:

SP = 6783643
TOTAL = 18075998
percentual_sp = (6783643/18075998)
percentual_sp


# In[100]:


percentual_sp_formatado = "{:.2f}".format(percentual_sp)
percentual_sp_formatado


# In[101]:


percentual_sp_formatado_final = 0.38*100
percentual_sp_formatado_final


# In[102]:


# Percentual do estado do RJ:

RJ = 3667866
TOTAL = 18075998
percentual_rj = (3667866/18075998)
percentual_rj


# In[103]:


percentual_rj_formatado = "{:.2f}".format(percentual_rj)
percentual_rj_formatado


# In[104]:


percentual_rj_formatado_final = 0.20*100
percentual_rj_formatado_final


# In[105]:


# Percentual do estado de MG:

MG = 2922988
TOTAL = 18075998
percentual_mg = (2922988/18075998)
percentual_mg


# In[106]:


percentual_mg_formatado = "{:.2f}".format(percentual_mg)
percentual_mg_formatado


# In[107]:


percentual_mg_formatado_final = 0.16*100
percentual_mg_formatado_final


# In[108]:


# Percentual do estado do ES:

ES = 2716548
TOTAL = 18075998
percentual_es = float(2716548/18075998)
percentual_es


# In[109]:


percentual_es_formatado = "{:.2f}".format(percentual_es)
percentual_es_formatado


# In[110]:


percentual_es_formatado_final = 0.15*100
percentual_es_formatado_final


# In[111]:


# Percentual dos outros estados:

OUTROS = 1984953
TOTAL = 18075998
percentual_outros = (1984953/18075998)
percentual_outros


# In[112]:


percentual_outros_formatado = "{:.2f}".format(percentual_outros)
percentual_outros_formatado


# In[113]:


percentual_outros_formatado_final =0.11*100
percentual_outros_formatado_final


# In[114]:


# Desenvolvendo o programa para o usuário descobrir o percentual de cada estado


# In[115]:


estado = input("digite o estado de seu interesse (opções: SP, RJ, MG, SP ou OUTROS) e saiba o percentual de faturamento da distribuidora em relação ao faturamento de todos os estados no mês:")


# In[116]:


print(estado)


# In[117]:


if estado == "SP":
    percentual = 38.0


# In[118]:


if estado == "RJ":
    percentual = 20.0


# In[119]:


if estado == "MG":
    percentual = 16.0


# In[120]:


if estado == "ES":
    percentual = 15.0


# In[121]:


if estado == "OUTROS":
    percentual = 11.0


# In[122]:


# Resposta final
print(f"O percentual de faturamento em relação ao faturamento total mensal distribuidora, no estado de {estado} é {percentual}")


# In[ ]:




