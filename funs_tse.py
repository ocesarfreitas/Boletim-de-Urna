import pandas as pd
import basedosdados as bd
import numpy as np

def RA_funs(NM_BAIRRO):
 if NM_BAIRRO == 'AGUAS CLARAS - TAGUATINGA SUL':
  return 'Águas Claras'
 if NM_BAIRRO == 'ARAPOANGA':
  return 'Planaltina'
 if NM_BAIRRO == 'AREA OCTOGONAL SUL':
  return 'Octogonal/Sudoeste'
 if NM_BAIRRO == 'ASSENTAMENTO DO AREAL (ÁGUAS cLARAS)':
  return 'Arniqueiras'
 if NM_BAIRRO == 'BRAZLANDIA':
  return 'Brazlândia'
 if NM_BAIRRO == 'ASA NORTE':
  return 'Plano Piloto'
 if NM_BAIRRO == 'ASA SUL':
  return 'Plano Piloto'
 if NM_BAIRRO == 'CANDANGOLANDIA':
  return 'Candangolândia'
 if NM_BAIRRO == 'CEILANDIA NORTE':
  return 'Ceilândia' 
 if NM_BAIRRO == 'CEILANDIA SUL':
  return 'Ceilândia'
 if NM_BAIRRO == 'CIDADE NOVA':
  return 'Gama'
 if NM_BAIRRO == 'COLÔNIA AGRÍCOLA VICENTE PIRES':
  return 'Vicente Pires'
 if NM_BAIRRO == 'CRUZEIRO NOVO':
  return 'Cruzeiro'
 if NM_BAIRRO == 'CRUZEIRO VELHO':
  return 'Cruzeiro'
 if NM_BAIRRO == "ESTANCIA MESTRE D'ARMAS":
  return 'Planaltina'
 if NM_BAIRRO == 'GRANJA DO TORTO':
  return 'Lago Norte'
 if NM_BAIRRO == 'GUARA I':
  return 'Guará'
 if NM_BAIRRO == 'GUARA II':
  return 'Guará'
 if NM_BAIRRO == 'ITAPOÃ':
  return 'Itapoã'
 if NM_BAIRRO == 'JARDIM BOTÂNICO':
  return 'Jardim Botânico'
 if NM_BAIRRO == 'JARDIM RORIZ':
  return 'Planaltina'
 if NM_BAIRRO == 'LAGO NORTE':
  return 'Lago Norte' 
 if NM_BAIRRO == 'LAGO SUL':
  return 'Lago Sul'
 if NM_BAIRRO == 'N.R.ALEX. GUSMAO':
  return 'Brazlândia' 
 if NM_BAIRRO == 'NORTE (AGUAS CLARAS)':
  return 'Águas Claras'
 if NM_BAIRRO == 'NUCLEO BANDEIRANTE':
  return 'Núcleo Bandeirante' 
 if NM_BAIRRO == 'NÚCLEO RURAL CÓRREGO DO ARROZAL':
  return 'Planaltina'
 if NM_BAIRRO == 'NÚCLEO RURAL DO GAMA':
  return 'Gama'
 if NM_BAIRRO == 'PARANOÁ':
  return 'Paranoá'
 if NM_BAIRRO == 'PLANALTINA':
  return 'Planaltina'
 if NM_BAIRRO == 'RECANTO DAS EMAS':
  return 'Recanto das Emas'
 if NM_BAIRRO == 'RESIDENCIAL SANTOS DUMONT':
  return 'Santa Maria'
 if NM_BAIRRO == 'RIACHO FUNDO':
  return 'Riacho Fundo I'
 if NM_BAIRRO == 'RIACHO FUNDO II':
  return 'Riacho Fundo II'
 if NM_BAIRRO == 'SAMAMBAIA':
  return 'Samambaia'
 if NM_BAIRRO == 'SAMAMBAIA NORTE':
  return 'Samambaia'
 if NM_BAIRRO == 'SAMAMBAIA SUL':
  return 'Samambaia'
 if NM_BAIRRO == 'SANTA MARIA':
  return 'Santa Maria'
 if NM_BAIRRO == 'SAO SEBASTIAO':
  return 'São Sebastião'
 if NM_BAIRRO == 'SETOR CENTRAL':
  return 'Gama'
 if NM_BAIRRO == 'SETOR LESTE':
  return 'Gama'
 if NM_BAIRRO == 'SETOR OESTE':
  return 'Gama'
 if NM_BAIRRO == 'SETOR DE INDUSTRIAS GRAFICAS':
  return 'Octogonal/Sudoeste'
 if NM_BAIRRO == 'SETOR MILITAR COMPLEMENTAR':
  return 'Plano Piloto'
 if NM_BAIRRO == 'SETOR MILITAR URBANO':
  return 'Plano Piloto'
 if NM_BAIRRO == 'SETOR NORTE':
  return 'Gama'
 if NM_BAIRRO == 'SETOR RESIDENCIAL LESTE':
  return 'Planaltina'
 if NM_BAIRRO == 'SETOR SUDOESTE':
  return 'Octogonal/Sudoeste'
 if NM_BAIRRO == 'SETOR SUL':
  return 'Gama'
 if NM_BAIRRO == 'SETOR TRADICIONAL':
  return 'Ceilândia'
 if NM_BAIRRO == 'SETOR VEREDAS':
  return 'Brazlândia'
 if NM_BAIRRO == 'SOBRADINHO':
  return 'Sobradinho I'
 if NM_BAIRRO == 'SOBRADINHO II':
  return 'Sobradinho II'
 if NM_BAIRRO == 'SUL (AGUAS CLARAS)':
  return 'Águas Claras'
 if NM_BAIRRO == 'TAGUATINGA CENTRO':
  return 'Taguatinga'
 if NM_BAIRRO == 'TAGUATINGA NORTE':
  return 'Taguatinga'
 if NM_BAIRRO == 'TAGUATINGA SUL':
  return 'Taguatinga'
 if NM_BAIRRO == 'TAQUARI':
  return 'Lago Norte'
 if NM_BAIRRO == 'VALE DO AMANHECER':
  return 'Planaltina'
 if NM_BAIRRO == 'VARJÃO':
  return 'Varjão'
 if NM_BAIRRO == 'VILA ESTRUTURAL':
  return 'SCIA/Estrutural'
 if NM_BAIRRO == 'VILA SAO JOSE':
  return 'Brazlândia'
 if NM_BAIRRO == 'ZONA INDUSTRIAL':
  return 'Guará'
 if NM_BAIRRO == 'ZONA RURAL':
  return 'Candangolândia'

def zonas_df(NR_ZONA):
    if NR_ZONA == 1:
        return 'Asa Sul'
    if NR_ZONA == 2:
        return 'Paranoá, Varjão, Itapoã, Lago Norte'
    if NR_ZONA == 3:
        return 'Taguatinga'
    if NR_ZONA == 4:
        return 'Santa Maria'
    if NR_ZONA == 5:
        return 'Sobradinho'
    if NR_ZONA == 6:
        return 'Planaltina'
    if NR_ZONA == 8:
        return 'Ceilândia Centro'
    if NR_ZONA == 9:
        return 'Guará'
    if NR_ZONA == 10:
        return 'Núcleo Bandeirante, Riacho Fundo, Park Way, Candangolândia'
    if NR_ZONA == 11:
        return 'Cruzeiro, Sudoeste, Octogonal'
    if NR_ZONA == 13:
        return 'Samambaia'
    if NR_ZONA == 14:
        return 'Asa Norte'
    if NR_ZONA == 15:
        return 'Águas Claras'
    if NR_ZONA == 16:
        return 'Ceilândia Norte, Brazlândia'
    if NR_ZONA == 17:
        return 'Gama'
    if NR_ZONA == 18:
        return 'Lago Sul, Jardim Botânico, São Sebastião'
    if NR_ZONA == 19:
        return 'Taguatinga'
    if NR_ZONA == 20:
        return 'Ceilândia Sul'
    if NR_ZONA == 21:
        return 'Recanto das Emas'

def extract_data(UF, ano, tipo_eleicao):
    filename = f'Microdados UF/{ano}/{ano}_{UF}.csv'
    # Lendo a base de dados 
    df = pd.read_csv(filename, sep=';', encoding = 'iso-8859-1')
    df_bairros = pd.read_csv("Microdados UF/eleitorado_local_votacao_2022.csv", sep=';',
                          encoding = 'iso-8859-1', 
                          usecols=['SG_UF','CD_MUNICIPIO','NM_MUNICIPIO','NR_ZONA','NR_SECAO','NM_BAIRRO'])
    df_partidos = pd.read_csv("Microdados UF/partidos políticos.csv", sep=';',
                          encoding = 'iso-8859-1')
    if tipo_eleicao == 'Municipal':
        # Bairros Eleições
        df_bairros = df_bairros[df_bairros['SG_UF'] == f'{UF}']
        df = df.merge(df_bairros, on=['NR_ZONA','SG_UF','NR_SECAO','CD_MUNICIPIO'], how='left').fillna('Não identificado')
        # Lista selecionando colunas
        cols_select = ['ANO_ELEICAO','NR_TURNO','SG_UF','CD_MUNICIPIO','DS_CARGO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS','NM_BAIRRO']
        df_lim = df[cols_select]
        
        # Tratamento inicial
        df_lim = df_lim[df_lim['NM_VOTAVEL'] != 'VOTO NULO']
        df_lim = df_lim[df_lim['NM_VOTAVEL'] != 'VOTO BRANCO']
        df_lim['NR_PARTIDO'] = df['NR_VOTAVEL'].astype(str).str[:2].astype(int)
        df_lim = df_lim.merge(df_partidos, on='NR_PARTIDO', how='left').fillna('Extintos')

        # Tratamento final
        df_lim = df_lim.groupby(['ANO_ELEICAO','NR_TURNO','SG_UF','NM_BAIRRO','CD_MUNICIPIO','DS_CARGO','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum"}).reset_index()
        df_lim["NM_VOTAVEL"] = df_lim["NM_VOTAVEL"].apply(lambda x: x.title())
        df_lim['NM_VOTAVEL'] = df_lim['NM_VOTAVEL'].str.replace('ª', '.')
        if (df_lim['NR_TURNO'] == 2).any():
            mask = (df_lim['DS_CARGO'] == 'Prefeito') & (df_lim['NR_TURNO'] == 1)
            df_lim = df_lim.loc[~mask, :]   
        else:
            pass
        return df_lim
    else:
        if UF == 'DF':
            # Definindo RAs        
            df_bairros = df_bairros[df_bairros['SG_UF'] == 'DF']
            df_bairros["RA"] = df_bairros["NM_BAIRRO"].apply(lambda x: RA_funs(x))
            df = df.merge(df_bairros, on=['NR_ZONA','SG_UF','NR_SECAO','SQ_CANDIDATO','CD_MUNICIPIO'], how='left')
            
            # Lista selecionando colunas
            cols_select = ['ANO_ELEICAO','NR_TURNO','SG_UF','RA','CD_MUNICIPIO','DS_CARGO','SQ_CANDIDATO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS']
            df_lim = df[cols_select]
            
            # Tratamento inicial
            df_lim = df_lim[df_lim['SQ_CANDIDATO'] != -1]
            df_lim['NR_PARTIDO'] = df['NR_VOTAVEL'].astype(str).str[:2].astype(int)
            df_lim = df_lim.merge(df_partidos, on='NR_PARTIDO', how='left')
            
            # Tratamento final
            df_lim = df_lim.groupby(['ANO_ELEICAO', 'NR_TURNO', 'SG_UF', 'RA', 'DS_CARGO','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum"}).reset_index()
            df_lim["NM_VOTAVEL"] = df_lim["NM_VOTAVEL"].apply(lambda x: x.title())
            df_lim['NM_VOTAVEL'] = df_lim['NM_VOTAVEL'].str.replace('ª', '.')
        else:
            # Lista selecionando colunas
            cols_select = ['ANO_ELEICAO','NR_TURNO','SG_UF','CD_MUNICIPIO','DS_CARGO','SQ_CANDIDATO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS']
            df_lim = df[cols_select]
            
            # Tratamento inicial
            df_lim = df_lim[df_lim['SQ_CANDIDATO'] != -1]
            df_lim['NR_PARTIDO'] = df['NR_VOTAVEL'].astype(str).str[:2].astype(int)
            df_lim = df_lim.merge(df_partidos, on='NR_PARTIDO', how='left')

            # Tratamento final
            df_lim = df_lim.groupby(['ANO_ELEICAO','NR_TURNO','SG_UF','CD_MUNICIPIO','DS_CARGO','NM_VOTAVEL','SG_PARTIDO']).agg({'QT_VOTOS': "sum"}).reset_index()
            df_lim["NM_VOTAVEL"] = df_lim["NM_VOTAVEL"].apply(lambda x: x.title())
            df_lim['NM_VOTAVEL'] = df_lim['NM_VOTAVEL'].str.replace('ª', '.')    
            
            if (df_lim['NR_TURNO'] == 2).any():
                mask = (df_lim['DS_CARGO'] == 'GOVERNADOR') & (df_lim['NR_TURNO'] == 1)
                df_lim = df_lim.loc[~mask, :]   
            else:
                pass
            return df_lim

def candidatos(df, UF, ano, tipo_eleicao):  
    # Project ID google cloud 
    project_id = 'ivory-volt-354818'
    # Candidatos: nomes
    base = '`basedosdados.br_tse_eleicoes.candidatos`'
    var = ('ano,sigla_uf,cpf,titulo_eleitoral,nome,sequencial,cargo,ocupacao,data_nascimento,idade,instrucao,sigla_uf_nascimento,municipio_nascimento,nome_urna')
    query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF} AND ano = {ano}"
    candidatos_nomes = bd.read_sql(query=query,billing_project_id=project_id)
    # Candidatos: eleitos
    base = '`basedosdados.br_tse_eleicoes.resultados_candidato`'
    var = ('ano,sequencial_candidato AS sequencial,cargo,resultado')
    query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF} AND ano = {ano} AND resultado != 'nao eleito'"
    candidatos_eleito = bd.read_sql(query=query,billing_project_id=project_id)
    # Tratamento da base
    candidatos = candidatos_nomes.merge(candidatos_eleito, on=['sequencial','ano','cargo'], how='inner')
    candidatos["cargo"] = candidatos["cargo"].apply(lambda x: x.title())
    candidatos["instrucao"] = candidatos["instrucao"].astype(str).apply(lambda x: x.title())
    candidatos["ocupacao"] = candidatos["ocupacao"].astype(str).apply(lambda x: x.title())
    candidatos["resultado"] = candidatos["resultado"].astype(str).apply(lambda x: x.title())
    candidatos_completo = candidatos.merge(df, left_on="nome", right_on="NM_VOTAVEL", how = 'left')
    if tipo_eleicao == 'Municipal':
        # Cidades
        base = '`basedosdados.br_bd_diretorios_brasil.municipio`'
        var = ('id_municipio_tse AS CD_MUNICIPIO,nome AS NM_MUNICIPIO')
        query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF}"
        cidades = bd.read_sql(query=query,billing_project_id=project_id)
        cidades['CD_MUNICIPIO'] = cidades['CD_MUNICIPIO'].astype(np.float64)
        candidatos_completo = candidatos_completo.merge(cidades, on="CD_MUNICIPIO", how = 'left')
        # Dados por bairro
        select_col = ['ano', 'sigla_uf','NM_MUNICIPIO','NM_BAIRRO','cpf','titulo_eleitoral','cargo','nome','nome_urna',
                      'SG_PARTIDO','data_nascimento','instrucao','ocupacao','CD_MUNICIPIO',
                      'sigla_uf_nascimento','municipio_nascimento','resultado','NR_TURNO',
                      'QT_VOTOS']
        candidatos_completo = candidatos_completo[select_col]
        candidatos_completo['QT_VALIDOS'] = candidatos_completo.groupby(['NM_BAIRRO','cargo'])['QT_VOTOS'].transform('sum')
        candidatos_completo = candidatos_completo.rename(columns={
            "ano": "Ano","sigla_uf": "UF",'NM_MUNICIPIO':'Município',"NM_BAIRRO":"Bairro","cpf":"CPF",
            "titulo_eleitoral":"Título Eleitoral",'cargo':'Cargo','nome':'Nome Completo', 'nome_urna':'Nome Campanha',
            'SG_PARTIDO':'Partido','data_nascimento':'Data Nascimento','instrucao':'Instrução',
            'ocupacao':'Ocupação','sigla_uf_nascimento':'UF Nascimento',
            'municipio_nascimento':'Município Nascimento','resultado':'Resultado',
            'NR_TURNO':'Turno','QT_VOTOS':'Votos Nominais','QT_VALIDOS':'Votos Válidos'})
        # Votos Relativos
        candidatos_completo['Votos Relativos'] = candidatos_completo['Votos Nominais']/candidatos_completo['Votos Válidos']
        # Alterando data
        candidatos_completo["Data Nascimento"] = pd.to_datetime(candidatos_completo["Data Nascimento"])
        candidatos_completo["Data Nascimento"] = candidatos_completo["Data Nascimento"].dt.strftime("%d/%m/%Y")
        return candidatos_completo 
    else: 
        if UF == "'DF'":
            # Dados por RA
            select_col = ['ano', 'sigla_uf','RA','cpf','titulo_eleitoral','cargo','nome','nome_urna',
                          'SG_PARTIDO','data_nascimento','instrucao','ocupacao',
                          'sigla_uf_nascimento','municipio_nascimento','resultado','NR_TURNO',
                          'QT_VOTOS']
            candidatos_completo = candidatos_completo[select_col]
            candidatos_completo['QT_VALIDOS'] = candidatos_completo.groupby(['RA','cargo'])['QT_VOTOS'].transform('sum')
            candidatos_completo = candidatos_completo.rename(columns={
                "ano": "Ano","sigla_uf": "UF","RA":"Região Administrativa","cpf":"CPF",
                "titulo_eleitoral":"Título Eleitoral",'cargo':'Cargo','nome':'Nome Completo', 'nome_urna':'Nome Campanha',
                'SG_PARTIDO':'Partido','data_nascimento':'Data Nascimento','instrucao':'Instrução',
                'ocupacao':'Ocupação','sigla_uf_nascimento':'UF Nascimento',
                'municipio_nascimento':'Município Nascimento','resultado':'Resultado',
                'NR_TURNO':'Turno','QT_VOTOS':'Votos Nominais','QT_VALIDOS':'Votos Válidos'})
            # Votos Relativos
            candidatos_completo['Votos Relativos'] = candidatos_completo['Votos Nominais']/candidatos_completo['Votos Válidos']
            # Alterando data
            candidatos_completo["Data Nascimento"] = pd.to_datetime(candidatos_completo["Data Nascimento"])
            candidatos_completo["Data Nascimento"] = candidatos_completo["Data Nascimento"].dt.strftime("%d/%m/%Y")
            return candidatos_completo 
        else:
            # Cidades
            base = '`basedosdados.br_bd_diretorios_brasil.municipio`'
            var = ('id_municipio_tse AS CD_MUNICIPIO,nome AS NM_MUNICIPIO')
            query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF}"
            cidades = bd.read_sql(query=query,billing_project_id=project_id)
            cidades['CD_MUNICIPIO'] = cidades['CD_MUNICIPIO'].astype(np.float64)
            candidatos_completo = candidatos_completo.merge(cidades, on="CD_MUNICIPIO", how = 'left')
            # Tratamento 
            select_col = ['ano', 'sigla_uf','NM_MUNICIPIO','cpf','titulo_eleitoral','cargo','nome','nome_urna',
                          'SG_PARTIDO','data_nascimento','instrucao','ocupacao',
                          'sigla_uf_nascimento','municipio_nascimento','resultado','NR_TURNO',
                          'QT_VOTOS']
            candidatos_completo = candidatos_completo[select_col]
            candidatos_completo['QT_VALIDOS'] = candidatos_completo.groupby(['NM_MUNICIPIO','cargo'])['QT_VOTOS'].transform('sum')
            candidatos_completo = candidatos_completo.rename(columns={
                "ano": "Ano","sigla_uf":"UF",'NM_MUNICIPIO':'Município',"cpf":"CPF",
                "titulo_eleitoral":"Título Eleitoral",'cargo':'Cargo','nome':'Nome Completo',
                'nome_urna':'Nome Campanha','SG_PARTIDO':'Partido','data_nascimento':'Data Nascimento',
                'instrucao':'Instrução','ocupacao':'Ocupação','sigla_uf_nascimento':'UF Nascimento',
                'municipio_nascimento':'Município Nascimento','resultado':'Resultado',
                'NR_TURNO':'Turno','QT_VOTOS':'Votos Nominais','QT_VALIDOS':'Votos Válidos'})
            # Votos Relativos
            candidatos_completo['Votos Relativos'] = candidatos_completo['Votos Nominais']/candidatos_completo['Votos Válidos']
            # Alterando data
            candidatos_completo["Data Nascimento"] = pd.to_datetime(candidatos_completo["Data Nascimento"])
            candidatos_completo["Data Nascimento"] = candidatos_completo["Data Nascimento"].dt.strftime("%d/%m/%Y")
        return candidatos_completo 
    
def tabela(df, UF, ano, tipo_eleicao):
    # Nomes das tabelas
    header_names = [{'header': df.columns[x]} for x in range(df.shape[1])]
    if tipo_eleicao == 'Municipal':
        # Separando dfs
        df_vereador = df[df['Cargo'] == "Vereador"]
        df_prefeito = df[df['Cargo'] == "Prefeito"]

        # Criando espaço da tabela
        writer = pd.ExcelWriter(f'{ano}/{UF} - Eleições {ano}.xlsx', engine='xlsxwriter')
        # Criando tabelas
        workbook  = writer.book
        df_vereador.to_excel(writer, sheet_name='Vereador', index=False)
        vereador = writer.sheets['Vereador']
        # Add a percent number format.
        percent_format = workbook.add_format({'num_format': '0.00%'})
        # Apply the number format to Grade column.
        vereador.set_column('U:U', None, percent_format)
        end_0 = len(df_vereador) + 1
        end_1 = len(df_vereador.columns) - 1
        vereador.add_table(0,0,end_0,end_1, {'columns': header_names})  
        ## Federal 
        df_prefeito.to_excel(writer, sheet_name='Prefeito', index=False)
        prefeito = writer.sheets['Prefeito']
        # Add a percent number format.
        percent_format = workbook.add_format({'num_format': '0.00%'})
        # Apply the number format to Grade column.
        prefeito.set_column('U:U', None, percent_format)
        end_0 = len(df_prefeito) + 1
        end_1 = len(df_prefeito.columns) - 1
        prefeito.add_table(0,0,end_0,end_1, {'columns': header_names})
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
    else:
        # Separando dfs
        df_estadual = df[df['Cargo'] == "Deputado Estadual"]
        df_distrital = df[df['Cargo'] == "Deputado Distrital"]
        df_federal = df[df['Cargo'] == "Deputado Federal"]
        df_senado = df[df['Cargo'] == "Senador"]
        df_governo = df[df['Cargo'] == "Governador"]
        # Criando espaço da tabela
        writer = pd.ExcelWriter(f'{ano}/{UF} - Eleições {ano}.xlsx', engine='xlsxwriter')
        if UF == 'DF':
            # Criando tabelas
            workbook  = writer.book
            df_distrital.to_excel(writer, sheet_name='Distrital', index=False)
            distrital = writer.sheets['Distrital']
            # Add a percent number format.
            percent_format = workbook.add_format({'num_format': '0.00%'})
            # Apply the number format to Grade column.
            distrital.set_column('S:S', None, percent_format)
            end_0 = len(df_distrital) + 1
            end_1 = len(df_distrital.columns) - 1
            distrital.add_table(0,0,end_0,end_1, {'columns': header_names})
        else:
            # Criando tabelas
            workbook  = writer.book
            df_estadual.to_excel(writer, sheet_name='Estadual', index=False)
            estadual = writer.sheets['Estadual']
            # Add a percent number format.
            percent_format = workbook.add_format({'num_format': '0.00%'})
            # Apply the number format to Grade column.
            estadual.set_column('S:S', None, percent_format)
            end_0 = len(df_estadual) + 1
            end_1 = len(df_estadual.columns) - 1
            estadual.add_table(0,0,end_0,end_1, {'columns': header_names})  
        ## Federal 
        df_federal.to_excel(writer, sheet_name='Federal', index=False)
        federal = writer.sheets['Federal']
        # Add a percent number format.
        percent_format = workbook.add_format({'num_format': '0.00%'})
        # Apply the number format to Grade column.
        federal.set_column('S:S', None, percent_format)
        end_0 = len(df_federal) + 1
        end_1 = len(df_federal.columns) - 1
        federal.add_table(0,0,end_0,end_1, {'columns': header_names})
        #### Senado
        df_senado.to_excel(writer, sheet_name='Senado', index=False)
        senado = writer.sheets['Senado']
        # Add a percent number format.
        percent_format = workbook.add_format({'num_format': '0.00%'})
        # Apply the number format to Grade column.
        senado.set_column('S:S', None, percent_format)
        end_0 = len(df_senado) + 1
        end_1 = len(df_senado.columns) - 1
        senado.add_table(0,0,end_0,end_1, {'columns': header_names})
        #### Governo
        df_governo.to_excel(writer, sheet_name='Governo', index=False)
        governo = writer.sheets['Governo']
        # Add a percent number format.
        percent_format = workbook.add_format({'num_format': '0.00%'})
        # Apply the number format to Grade column.
        governo.set_column('S:S', None, percent_format)
        end_0 = len(df_governo) + 1
        end_1 = len(df_governo.columns) - 1
        governo.add_table(0,0,end_0,end_1, {'columns': header_names})
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

def partidos(df,UF):
    # Project ID google cloud 
    project_id = 'ivory-volt-354818'
    # Candidatos: nomes
    base = '`basedosdados.br_tse_filiacao_partidaria.microdados`'
    var = ('titulo_eleitoral,data_filiacao,data_desfiliacao,sigla_uf,sigla_partido')
    query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF} AND data_filiacao >= '1980-01-01'"
    candidatos_filicao = bd.read_sql(query=query,billing_project_id=project_id)

    df_candidatos = df

    lista_eleitos = df_candidatos[['Título Eleitoral','Nome Completo','Nome Campanha','Cargo','CPF']]

    candidatos_filicao = candidatos_filicao.merge(lista_eleitos, left_on='titulo_eleitoral', right_on='Título Eleitoral')


    candidatos_filicao = candidatos_filicao.rename(columns={
        "sigla_partido": "Partido","data_filiacao": "Data Filiação",
        "data_desfiliacao":"Data Desfiliação"})

    var = ['Cargo','CPF','Nome Completo','Nome Campanha','Partido','Data Filiação','Data Desfiliação']
    candidatos_filicao = candidatos_filicao[var]
    candidatos_filicao = candidatos_filicao.drop_duplicates()
    
    candidatos_filicao["Data Filiação"] = candidatos_filicao["Data Filiação"].astype(str).str.split('-', n=1, expand=True).iloc[:,0].str.extract('(\d{4})')
    candidatos_filicao["Data Desfiliação"] = candidatos_filicao["Data Desfiliação"].astype(str).str.split('-', n=1, expand=True).iloc[:,0].str.extract('(\d{4})')

    candidatos_filicao["Data Filiação"] = pd.to_numeric(candidatos_filicao["Data Filiação"], errors='coerce', downcast='integer')
    candidatos_filicao["Data Desfiliação"] = pd.to_numeric(candidatos_filicao["Data Desfiliação"], errors='coerce', downcast='integer')

    return candidatos_filicao   

def partidos2(df, UF):
    # Project ID google cloud 
    project_id = 'ivory-volt-354818'
    
    # Candidatos: nomes
    base = '`basedosdados.br_tse_filiacao_partidaria.microdados`'
    var = ('titulo_eleitoral,data_filiacao,data_desfiliacao,sigla_uf,sigla_partido')
    query = f"SELECT {var} FROM {base} WHERE sigla_uf = {UF} AND data_filiacao >= '1980-01-01'"
    candidatos_filicao = bd.read_sql(query=query, billing_project_id=project_id)

    # Select only the necessary columns from df
    df_candidatos = df[['Título Eleitoral', 'Nome Completo', 'Nome Campanha', 'Cargo', 'CPF']]

    # Merge the two DataFrames and drop duplicates
    candidatos_filicao = candidatos_filicao.merge(df_candidatos, left_on='titulo_eleitoral', right_on='Título Eleitoral')
    candidatos_filicao.drop_duplicates(subset=['Cargo', 'CPF', 'Nome Completo', 'Nome Campanha', 'Partido', 'Data Filiação', 'Data Desfiliação'], keep='first', inplace=True)

    # Extract the year from the date columns
    candidatos_filicao['Data Filiação'] = pd.to_datetime(candidatos_filicao['Data Filiação']).dt.year
    candidatos_filicao['Data Desfiliação'] = pd.to_datetime(candidatos_filicao['Data Desfiliação']).dt.year

    return candidatos_filicao

def tabela_filiacao(df, UF, ano):
    # Nomes das tabelas
    header_names = [{'header': df.columns[x]} for x in range(df.shape[1])]
    # Separando dfs
    df_estadual = df[df['Cargo'] == "Deputado Estadual"]
    df_distrital = df[df['Cargo'] == "Deputado Distrital"]
    df_federal = df[df['Cargo'] == "Deputado Federal"]
    df_senado = df[df['Cargo'] == "Senador"]
    df_governo = df[df['Cargo'] == "Governador"]
    # Criando espaço da tabela
    writer = pd.ExcelWriter(f'Filiação Partidária/ {UF} - Filiação (Eleitos {ano}).xlsx', engine='xlsxwriter')
    if UF == 'DF':
        # Criando tabelas
        df_distrital.to_excel(writer, sheet_name='Distrital', index=False)
        distrital = writer.sheets['Distrital']
        end_0 = len(df_distrital) + 1
        end_1 = len(df_distrital.columns) - 1
        distrital.add_table(0,0,end_0,end_1, {'columns': header_names})
    else:
        # Criando tabelas
        df_estadual.to_excel(writer, sheet_name='Estadual', index=False)
        estadual = writer.sheets['Estadual']
        end_0 = len(df_estadual) + 1
        end_1 = len(df_estadual.columns) - 1
        estadual.add_table(0,0,end_0,end_1, {'columns': header_names})  
    ## Federal 
    df_federal.to_excel(writer, sheet_name='Federal', index=False)
    federal = writer.sheets['Federal']
    end_0 = len(df_federal) + 1
    end_1 = len(df_federal.columns) - 1
    federal.add_table(0,0,end_0,end_1, {'columns': header_names})
    #### Senado
    df_senado.to_excel(writer, sheet_name='Senado', index=False)
    senado = writer.sheets['Senado']
    end_0 = len(df_senado) + 1
    end_1 = len(df_senado.columns) - 1
    senado.add_table(0,0,end_0,end_1, {'columns': header_names})
    #### Governo
    df_governo.to_excel(writer, sheet_name='Governo', index=False)
    governo = writer.sheets['Governo']
    end_0 = len(df_governo) + 1
    end_1 = len(df_governo.columns) - 1
    governo.add_table(0,0,end_0,end_1, {'columns': header_names})

    writer.save()