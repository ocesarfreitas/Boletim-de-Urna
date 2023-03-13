import pandas as pd
import basedosdados as bd
import numpy as np


from funs_tse import extract_data, candidatos, tabela, partidos, tabela_filiacao

df_eleicao = extract_data("GO",2016,'Municipal')
candidatos_df = candidatos(df_eleicao, "'GO'", "2016",'Municipal')
tabela(candidatos_df, 'GO', '2016','Municipal')

