#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import locale


# In[ ]:


locale.setlocale(locale.LC_MONETARY, '')


# In[ ]:


valor_em_real_formatado = locale.currency(6783643)
print(valor_em_real_formatado)


# In[ ]:


faturamento_mensal_por_estado = ({
     'SP':[6783643],
     'RJ' :[3667866],
     'MG':[2922988],
     'ES':[2716548],
     'OUTROS':[1984953]   
               })

df = pd.DataFrame(faturamento_mensal_por_estado)
print(df)


# In[ ]:


df


# In[ ]:


# percentual de representação que cada estado teve dentro do valor total mensal da distribuidora:  


# In[ ]:


# Resolução: somar o faturamento de todos os estados


# In[ ]:


# Para somar, vou criar uma lista contendo os valores de faturamento de todos os estados:

Row_list =[]
  

for rows in df.itertuples():
    
    faturamento_mensal_por_estado =[rows.SP, rows.RJ, rows.MG, rows.ES, rows.OUTROS]
      
    
    Row_list.append(faturamento_mensal_por_estado)
  

print(Row_list)


# In[ ]:


# Depois de ter criado a lista com todos os valores de faturamento, vamos somar:

soma_faturamento_todos_estados = sum(faturamento_mensal_por_estado)
soma_faturamento_todos_estados


# In[ ]:


# Com o valor da somatória obtido, agora iremos calcular o percentual de representação que cada estado teve dentro do valor total mensal :


# In[ ]:


# Percentual do estado de SP:

percentual_sp = (6783643/18075998)
format(percentual_sp, (".2f"))


# In[ ]:


# Percentual do estado do RJ:

percentual_rj = (3667866/18075998)
format(percentual_rj, (".2f"))


# In[ ]:


# Percentual do estado de MG:

percentual_mg = ((2922988/18075998)*100)
format(percentual_mg, (".2f"))


# In[ ]:


# Percentual do estado do ES:

percentual_es = ((2716548/18075998)*100)
format(percentual_es, (".2f"))


# In[ ]:


# Percentual dos outros estados:

percentual_outros = ((1984953/18075998)*100)
format(percentual_outros, (".2f"))


# In[ ]:


percentual_outros = (1984953/18075998)
percentual_outros


# In[ ]:


estado = input("digite o estado de seu interesse (opções: SP, RJ, MG, SP ou OUTROS) e saiba o percentual de faturamento da distribuidora em relação ao faturamento de todos os estados no mês:")


# In[ ]:


if (SP or sp or Sp ou sP):
    percentual = (percentual_sp);


# In[ ]:


if (RJ or rj or Rj ou rJ):
    percentual = (percentual_rj);


# In[ ]:


if (MG or mg or Mg ou mG):
    percentual = (percentual_mg);


# In[ ]:


if (OUTROS or Outros or outros):
    percentual = (percentual_outros);


# In[ ]:


print("O percentual de faturamento dentro do valor total mensal da distribuidora, no estado de {estado} é: {percentual}")


# In[ ]:


else:
    print("Dado incorreto. Favor, digite o dado corretamente,de acordo com as opções apresentadas anteriormente")
    


# In[ ]:





# In[ ]:




