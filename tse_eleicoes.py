import pandas as pd
import basedosdados as bd

############################### Importando UFs ################################
df_boletim_22 = pd.read_csv("Microdados UF/DF_2022.csv", sep=';', encoding = 'iso-8859-1')
bairros = pd.read_csv("Microdados UF/eleitorado_local_votacao_2022.csv", sep=';',
                      encoding = 'iso-8859-1', 
                      usecols=['SG_UF','CD_MUNICIPIO','NM_MUNICIPIO','NR_ZONA','NR_SECAO','NM_BAIRRO'])

# List of column names to select
cols_select = ['ANO_ELEICAO', 'NR_TURNO', 'SG_UF', 'CD_MUNICIPIO', 'NR_ZONA',
               'NR_SECAO', 'DS_CARGO_PERGUNTA','SG_PARTIDO', 'NM_VOTAVEL',
               'QT_COMPARECIMENTO','QT_VOTOS']

# Selecting columns using the list of column names
df_boletim_22_lim = df_boletim_22[cols_select]
df_boletim_22_lim = df_boletim_22_lim [df_boletim_22_lim['SG_PARTIDO'] != "#NULO#"]
df_boletim_22_lim = df_boletim_22_lim.groupby(['ANO_ELEICAO', 'NR_TURNO', 'SG_UF', 'CD_MUNICIPIO', 'DS_CARGO_PERGUNTA',
                                   'NR_ZONA','NR_SECAO','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum", 'QT_COMPARECIMENTO': "sum"}).reset_index()

df_boletim_22_lim = df_boletim_22_lim.merge(bairros, on=['NR_ZONA','NR_SECAO','SG_UF', 'CD_MUNICIPIO'], how='left')
df_boletim_22_lim = df_boletim_22_lim.groupby(['ANO_ELEICAO', 'NR_TURNO', 'SG_UF', 'CD_MUNICIPIO', 'DS_CARGO_PERGUNTA',
                                   'NM_BAIRRO','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum", 'QT_COMPARECIMENTO': "sum"}).reset_index()
df_boletim_22_lim["NM_VOTAVEL"] = df_boletim_22_lim["NM_VOTAVEL"].apply(lambda x: x.title())
df_boletim_22_lim["NM_BAIRRO"] = df_boletim_22_lim["NM_BAIRRO"].apply(lambda x: x.title())

# Candidatos: nomes
base = '`basedosdados.br_tse_eleicoes.candidatos`'
project_id = 'ivory-volt-354818'
var = ('ano,sigla_uf,cpf,nome,sequencial,cargo,ocupacao,data_nascimento,idade,instrucao,sigla_uf_nascimento,municipio_nascimento,nome_urna')
query = f"SELECT {var} FROM {base} WHERE sigla_uf = 'DF' AND ano = 2022"
candidatos_nomes = bd.read_sql(query=query,billing_project_id=project_id)

# Candidatos: eleitos
base = '`basedosdados.br_tse_eleicoes.resultados_candidato`'
project_id = 'ivory-volt-354818'
var = ('ano,sequencial_candidato AS sequencial,cargo,resultado')
query = f"SELECT {var} FROM {base} WHERE sigla_uf = 'DF' AND ano = 2022"
candidatos_eleito = bd.read_sql(query=query,billing_project_id=project_id)

candidatos = candidatos_nomes.merge(candidatos_eleito, on=['sequencial','ano','cargo'], how='inner')
candidatos["cargo"] = candidatos["cargo"].apply(lambda x: x.title())
candidatos["instrucao"] = candidatos["instrucao"].apply(lambda x: x.title())
candidatos["ocupacao"] = candidatos["ocupacao"].apply(lambda x: x.title())
candidatos["resultado"] = candidatos["resultado"].apply(lambda x: x.title())

candidatos_completo = candidatos.merge(df_boletim_22_lim, left_on="nome_urna", right_on="NM_VOTAVEL", how = 'left')

select_col = ['ano', 'sigla_uf','NM_BAIRRO','cpf','cargo','nome','nome_urna',
              'SG_PARTIDO','data_nascimento','instrucao','ocupacao',
              'sigla_uf_nascimento','municipio_nascimento','resultado','NR_TURNO',
              'QT_VOTOS', 'QT_COMPARECIMENTO']

candidatos_completo = candidatos_completo[select_col]
candidatos_completo = candidatos_completo.rename(columns={
    "ano": "Ano","sigla_uf": "UF","NM_BAIRRO":"Região Administrativa",
    "cpf":"CPF",'cargo':'Cargo','nome':'Nome Completo', 'nome_urna':'Nome Campanha',
    'SG_PARTIDO':'Partido','data_nascimento':'Data Nascimento','instrucao':'Instrução',
    'ocupacao':'Ocupação','sigla_uf_nascimento':'UF Nascimento',
    'municipio_nascimento':'Município Nascimento','resultado':'Resultado',
    'NR_TURNO':'Turno','QT_VOTOS':'Votos Nominais','QT_COMPARECIMENTO':'Votos Válidos'})
candidatos_completo['Votos Relativos'] = candidatos_completo['Votos Nominais']/candidatos_completo.groupby(['Região Administrativa'])['Votos Nominais'].transform('sum')
# Convert the dates to datetime objects
candidatos_completo["Data Nascimento"] = pd.to_datetime(candidatos_completo["Data Nascimento"])
# Change the date format to dd/mm/yyyy
candidatos_completo["Data Nascimento"] = candidatos_completo["Data Nascimento"].dt.strftime("%d/%m/%Y")

header_names = [{'header': candidatos_completo.columns[x]} for x in range(candidatos_completo.shape[1])]

candidatos_distrital = candidatos_completo[candidatos_completo['Cargo'] == "Deputado Distrital"]
candidatos_federal = candidatos_completo[candidatos_completo['Cargo'] == "Deputado Federal"]
candidatos_senado = candidatos_completo[candidatos_completo['Cargo'] == "Senador"]
candidatos_governo = candidatos_completo[candidatos_completo['Cargo'] == "Governador"]


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('DF - Deputados Distritais - 2022.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
# Get the xlsxwriter workbook and worksheet objects.

workbook  = writer.book
candidatos_distrital.to_excel(writer, sheet_name='Distrital', index=False)
distrital = writer.sheets['Distrital']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
distrital.set_column('R:R', None, percent_format)

end_0 = len(candidatos_distrital) - 1
end_1 = len(candidatos_distrital.columns) - 1

distrital.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Federal 
candidatos_federal.to_excel(writer, sheet_name='Federal', index=False)
federal = writer.sheets['Federal']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
federal.set_column('R:R', None, percent_format)

end_0 = len(candidatos_federal) - 1
end_1 = len(candidatos_federal.columns) - 1

federal.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Senado
candidatos_senado.to_excel(writer, sheet_name='Senado', index=False)
senado = writer.sheets['Senado']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
senado.set_column('R:R', None, percent_format)

end_0 = len(candidatos_senado) - 1
end_1 = len(candidatos_senado.columns) - 1

senado.add_table(0,0,end_0,end_1, {'columns': header_names})

#### Governo
candidatos_governo.to_excel(writer, sheet_name='Governo', index=False)
governo = writer.sheets['Governo']
# Add a percent number format.
percent_format = workbook.add_format({'num_format': '0.00%'})

# Apply the number format to Grade column.
governo.set_column('R:R', None, percent_format)

end_0 = len(candidatos_governo) - 1
end_1 = len(candidatos_governo.columns) - 1

governo.add_table(0,0,end_0,end_1, {'columns': header_names})


# Close the Pandas Excel writer and output the Excel file.
writer.save()
