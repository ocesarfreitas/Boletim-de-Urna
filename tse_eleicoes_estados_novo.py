import pandas as pd
import basedosdados as bd
import numpy as np
from funs_tse import extract_data, candidatos, tabela

lista_uf =['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 
           'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 
           'SC', 'SP', 'SE', 'TO', 'DF']
    
for uf in lista_uf:
    df_eleicao = extract_data(f"Microdados UF/{uf}_2022.csv")
    candidatos_df = candidatos(df_eleicao, f"'{uf}'", "2022")
    tabela(candidatos_df, f'{uf}', '2022')
