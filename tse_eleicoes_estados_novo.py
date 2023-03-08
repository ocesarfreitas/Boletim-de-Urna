import pandas as pd
import basedosdados as bd
import numpy as np
from funs_tse import extract_data, candidatos, tabela, partidos, partidos2, tabela_filiacao

lista_uf =['SP']
    
for uf in lista_uf:
    df_eleicao = extract_data(f"{uf}")
    candidatos_df = candidatos(df_eleicao, f"'{uf}'", "2022")
    tabela(candidatos_df, f'{uf}', '2022')
    df_partidos = partidos2(candidatos_df, f"'{uf}'")
    tabela_filiacao(df_partidos, f"{uf}", "2022")
    