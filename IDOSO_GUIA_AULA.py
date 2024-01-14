import streamlit as st
import pandas as pd 
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import numpy as np 

##### DADOS  ####
idoso=pd.read_csv('idoso.csv')

variaveis=['IND_MAIOR2A_BEBIDA_ADOCADA', 'IND_MAIOR2A_FRUTA',
       'IND_MAIOR2A_3_REFEICOES_DIA', 'IND_MAIOR2A_VERDURA_LEGUME',
       'IND_MAIOR2A_REFEICAO_TV', 'IND_MAIOR2A_HAMBURGR_EMBUTIDO',
       'IND_MAIOR2A_BISCOITO_RECHEADO', 'IND_MAIOR2A_MACARRAO_INSTANTAN',
       'IND_MAIOR2A_FEIJAO', 'SEXO']
variaveis=variaveis+['CLASSE']
idoso=idoso[variaveis]

X=idoso.drop('CLASSE',axis=1)
y=idoso['CLASSE']
rfc=RandomForestClassifier(random_state=42)
rfc.fit(X,y)

#### Predições####


with st.sidebar:
        
        bedida=int(st.checkbox('Bebida adocicada?'))
        fruta=int(st.checkbox('Come frutas?'))
        refeicao=int(st.checkbox('Faz pelo menos 3 refeeções diárias?'))
        verdura=int(st.checkbox('Come verduras/legumes?'))
        tv=int(st.checkbox('Come assitindo TV?'))
        hamburguer=int(st.checkbox('Come hamburguer?'))
        biscoito=int(st.checkbox('Come biscoitos?'))
        macarrao=int(st.checkbox('Come macarrão instantâneo?'))
        feijao=int(st.checkbox('Come feijão?'))
        sexo=int(st.checkbox('Você é um homem?'))
        
        valor=[np.array([bedida,fruta,refeicao,verdura,tv,hamburguer,biscoito,macarrao,feijao,sexo])]
        
        

st.title('Descubra se você vai aumentar o seu peso!')
st.write('Selecione ao lado sua configuração')

if st.button('Executar algoritmo'):
        predicao=rfc.predict(valor)[0]
        if sexo==1:
              
                if predicao==0:
                        st.title('Você NÃO tem risco de aumentar seu peso')
                        st.image('HOMEM_MAGRO.png', caption='FUTURO SAUDÁVEL!')
                if predicao==1:
                        st.title('Você corre o risco de aumentar seu peso')
                        st.image('HOMEM_GORDO.png', caption='VOCÊ CORRE RISCO DE SAÚDE!')
                
        if sexo==0:
                if predicao==0:
                        st.title('Você NÃO tem risco de aumentar seu peso')
                        st.image('MULHER_MAGRA.png', caption='FUTURO SAUDÁVEL!')
                if predicao==1:
                        st.title('Você corre o risco de aumentar seu peso')
                        st.image('MULHER_GORDA.png', caption='VOCÊ CORRE RISCO DE SAÚDE!')

        
        
 


