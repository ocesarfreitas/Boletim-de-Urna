import pandas as pd
import basedosdados as bd
import numpy as np

df_boletim_22 = pd.read_csv("Microdados UF/PA_2022.csv", sep=';', encoding = 'iso-8859-1')

# List of column names to select
cols_select = ['ANO_ELEICAO','NR_TURNO','SG_UF','CD_MUNICIPIO','DS_CARGO_PERGUNTA',
               'SG_PARTIDO','NM_VOTAVEL','QT_COMPARECIMENTO','QT_VOTOS']

# Selecting columns using the list of column names
df_boletim_22_lim = df_boletim_22[cols_select]
df_boletim_22_lim = df_boletim_22_lim [df_boletim_22_lim['SG_PARTIDO'] != "#NULO#"]
df_boletim_22_lim = df_boletim_22_lim.groupby(['ANO_ELEICAO','NR_TURNO','SG_UF',
                                               'CD_MUNICIPIO','DS_CARGO_PERGUNTA','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum", 'QT_COMPARECIMENTO': "sum"}).reset_index()

df_boletim_22_lim["NM_VOTAVEL"] = df_boletim_22_lim["NM_VOTAVEL"].apply(lambda x: x.title())

# Candidatos: nomes
base = '`basedosdados.br_tse_eleicoes.candidatos`'
project_id = 'ivory-volt-354818'
var = ('ano,sigla_uf,cpf,nome,sequencial,cargo,ocupacao,data_nascimento,idade,instrucao,sigla_uf_nascimento,municipio_nascimento,nome_urna')
query = f"SELECT {var} FROM {base} WHERE sigla_uf = 'PA' AND ano = 2022"
candidatos_nomes = bd.read_sql(query=query,billing_project_id=project_id)

# Candidatos: eleitos
base = '`basedosdados.br_tse_eleicoes.resultados_candidato`'
project_id = 'ivory-volt-354818'
var = ('ano,sequencial_candidato AS sequencial,cargo,resultado')
query = f"SELECT {var} FROM {base} WHERE sigla_uf = 'PA' AND ano = 2022 AND resultado != 'nao eleito'"
candidatos_eleito = bd.read_sql(query=query,billing_project_id=project_id)

candidatos = candidatos_nomes.merge(candidatos_eleito, on=['sequencial','ano','cargo'], how='inner')
candidatos["cargo"] = candidatos["cargo"].apply(lambda x: x.title())
candidatos["instrucao"] = candidatos["instrucao"].astype(str).apply(lambda x: x.title())
candidatos["ocupacao"] = candidatos["ocupacao"].astype(str).apply(lambda x: x.title())
candidatos["resultado"] = candidatos["resultado"].astype(str).apply(lambda x: x.title())

candidatos_completo = candidatos.merge(df_boletim_22_lim, left_on="nome_urna", right_on="NM_VOTAVEL", how = 'left')

# Cidades
base = '`basedosdados.br_bd_diretorios_brasil.municipio`'
project_id = 'ivory-volt-354818'
var = ('id_municipio_tse AS CD_MUNICIPIO,nome AS NM_MUNICIPIO')
query = f"SELECT {var} FROM {base} WHERE sigla_uf = 'PA'"
cidades = bd.read_sql(query=query,billing_project_id=project_id)
cidades['CD_MUNICIPIO'] = cidades['CD_MUNICIPIO'].astype(np.float64)

candidatos_completo = candidatos_completo.merge(cidades, on="CD_MUNICIPIO", how = 'left')

# ------------
select_col = ['ano', 'sigla_uf','NM_MUNICIPIO','cpf','cargo','nome','nome_urna',
              'SG_PARTIDO','data_nascimento','instrucao','ocupacao',
              'sigla_uf_nascimento','municipio_nascimento','resultado','NR_TURNO',
              'QT_VOTOS', 'QT_COMPARECIMENTO']

candidatos_completo = candidatos_completo[select_col]
candidatos_completo = candidatos_completo.rename(columns={
    "ano": "Ano","sigla_uf":"UF",'NM_MUNICIPIO':'Município',"cpf":"CPF",'cargo':'Cargo','nome':'Nome Completo',
    'nome_urna':'Nome Campanha','SG_PARTIDO':'Partido','data_nascimento':'Data Nascimento',
    'instrucao':'Instrução','ocupacao':'Ocupação','sigla_uf_nascimento':'UF Nascimento',
    'municipio_nascimento':'Município Nascimento','resultado':'Resultado',
    'NR_TURNO':'Turno','QT_VOTOS':'Votos Nominais','QT_COMPARECIMENTO':'Votos Válidos'})
candidatos_completo['Votos Relativos'] = candidatos_completo['Votos Nominais']/candidatos_completo.groupby(['Município'])['Votos Nominais'].transform('sum')
# Convert the dates to datetime objects
candidatos_completo["Data Nascimento"] = pd.to_datetime(candidatos_completo["Data Nascimento"])
# Change the date format to dd/mm/yyyy
candidatos_completo["Data Nascimento"] = candidatos_completo["Data Nascimento"].dt.strftime("%d/%m/%Y")

header_names = [{'header': candidatos_completo.columns[x]} for x in range(candidatos_completo.shape[1])]

candidatos_estadual = candidatos_completo[candidatos_completo['Cargo'] == "Deputado Estadual"]
candidatos_federal = candidatos_completo[candidatos_completo['Cargo'] == "Deputado Federal"]
candidatos_senado = candidatos_completo[candidatos_completo['Cargo'] == "Senador"]
candidatos_governo = candidatos_completo[candidatos_completo['Cargo'] == "Governador"]


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('PA - Eleições 2022.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
# Get the xlsxwriter workbook and worksheet objects.

workbook  = writer.book
candidatos_estadual.to_excel(writer, sheet_name='Estadual', index=False)
distrital = writer.sheets['Estadual']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
distrital.set_column('R:R', None, percent_format)

end_0 = len(candidatos_estadual) + 1
end_1 = len(candidatos_estadual.columns) - 1

distrital.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Federal 
candidatos_federal.to_excel(writer, sheet_name='Federal', index=False)
federal = writer.sheets['Federal']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
federal.set_column('R:R', None, percent_format)

end_0 = len(candidatos_federal) + 1
end_1 = len(candidatos_federal.columns) - 1

federal.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Senado
candidatos_senado.to_excel(writer, sheet_name='Senado', index=False)
senado = writer.sheets['Senado']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
senado.set_column('R:R', None, percent_format)

end_0 = len(candidatos_senado) + 1
end_1 = len(candidatos_senado.columns) - 1

senado.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Governo
candidatos_governo.to_excel(writer, sheet_name='Governo', index=False)
governo = writer.sheets['Governo']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
governo.set_column('R:R', None, percent_format)

end_0 = len(candidatos_governo) + 1
end_1 = len(candidatos_governo.columns) - 1

governo.add_table(0,0,end_0,end_1, {'columns': header_names})


# Close the Pandas Excel writer and output the Excel file.
writer.save()
