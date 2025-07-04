import pandas as pd

DEFAULT_NUMBER = 0
DEFAULT_NUMBER_UNNAPLICABLE = 99
DEFAULT_STRING_UNNAPLICABLE = "<None>"

def transform_R025(df):
    df["R025"] = df["R025"].apply(lambda x: "00" if x in ("99","00") else x)
    df['R025'] = df['R025'].replace("<None>", "00")
    df = df.astype({'R025': int})
    return df

def transform_C008(df):
    # C008 - 000 a 130	age (years)
    df = df.astype({'C008': int})
    return df

def transform_C009(df):
    # C009 - Cor ou raça
    df = df.astype({'C009': 'category'})
    return df

def transform_R010(df):
    # R010 - Has the woman had a hysterectomy?
    df['R010'] = df['R010'].apply(lambda x: 1 if x == "1" else (0 if x == "2" else DEFAULT_NUMBER_UNNAPLICABLE))
    df = df.astype({'R010': int})
    return df

def transform_R011(df):
    # R011 - Segundo o médico, qual o motivo da retirada do útero?
    df = df.astype({'R011': 'category'})
    return df

def transform_R012(df):
    # R012 - Age when removed the uterus - default to 0
    df['R012'] = df['R012'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'R012': int})
    return df

def transform_W00101(df):
    # W00101 - # Peso - 1ª pesagem (em kg)
    df['W00101'] = df['W00101'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00101': float})
    return df

def transform_W00102(df):
    # W00102 - # Peso - 2ª pesagem (em kg)
    df['W00102'] = df['W00102'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00102': float})
    return df

def transform_W00103(df):
    # W00103 - # Peso - Final (em kg)
    df['W00103'] = df['W00103'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00103': float})
    return df

def transform_W00201(df):
    # W00201 - # Altura - 1ª medição (em cm)
    df['W00201'] = df['W00201'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00201': float})
    return df

def transform_W00202(df):
    # W00202 - # Altura - 2ª medição (em cm)
    df['W00202'] = df['W00202'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00202': float})
    return df

def transform_W00203(df):
    # W00203 - # Altura - Final (em cm)
    df['W00203'] = df['W00203'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'W00203': float})
    return df

def transform_P00103(df):
    # P00103 - Peso - Informado (em kg)
    df['P00103'] = df['P00103'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P00103': float})
    return df

def transform_P00104(df):
    # P00104 - Peso - Final (em kg)
    df['P00104'] = df['P00104'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P00104': float})
    return df

def transform_P00403(df):
    # P00403 - Altura - Informada (em cm)
    df['P00403'] = df['P00403'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P00403': int})
    return df

def transform_P00404(df):
    # P00404 - Altura - Final (em cm)
    df['P00404'] = df['P00404'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P00404': int})
    return df

def transform_P00901(df):
    # P00901 - Em quantos dias da semana, o(a) Sr(a) costuma comer pelo menos um tipo de verdura ou legume (sem contar batata, mandioca, cará ou inhame) como alface, tomate, couve, cenoura, chuchu, berinjela, abobrinha?
    df['P00901'] = df['P00901'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P00901': int})
    return df

def transform_P01101(df):
    # P01101 - Em quantos dias da semana o(a) Sr(a) costuma comer carne vermelha (boi, porco, cabrito, bode, ovelha etc.)?
    df['P01101'] = df['P01101'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P01101': int})
    return df

def transform_P013(df):
    # P013 - Em quantos dias da semana o(a) Sr(a) costuma comer frango/galinha?
    df['P013'] = df['P013'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P013': int})
    return df

def transform_P015(df):
    # P015 - Em quantos dias da semana o(a) Sr(a) costuma comer peixe?
    df['P015'] = df['P015'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P015': int})
    return df

def transform_P035(df):
    # P035 - Quantos dias por semana o(a) Sr(a) costuma (costumava) praticar exercício físico ou esporte?
    df['P035'] = df['P035'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P035': int})
    return df

def transform_P027(df):
    # P027 - Com que frequência o(a) Sr(a) costuma consumir alguma bebida alcoólica?
    df['P027'] = df['P027'].apply(lambda x: 1 if x == "2" or x == "3" else 0)
    df = df.astype({'P027': int})
    return df

def transform_P050(df):
    # P050 - Atualmente, o(a) Sr(a) fuma algum produto do tabaco?
    df['P050'] = df['P050'].apply(lambda x: 1 if x == "1" or x == "2" else 0)
    df = df.astype({'P050': int})
    return df

def transform_P05401(df):
    # P05402 - Quantidade de cigarros
    # Sum all tobacco product quantities into P05402
    tobacco_columns = ['P05402', 'P05405', 'P05408', 'P05411', 'P05414', 'P05417', 'P05421', 'P05801']
    columns_to_drop = [ col for col in tobacco_columns if 'P05402' not in col ]
    
    # Replace <None> values with 0 for all tobacco columns
    for col in tobacco_columns:
        if col in df.columns:
            df[col] = df[col].replace("<None>", 0)
            df[col] = df[col].replace("99", 0)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Sum all tobacco product quantities into P05402
    df['P05402'] = df[tobacco_columns].sum(axis=1)
    df = df.astype({'P05402': int})

    # Drop the individual tobacco columns since we've summed them into P05402
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    return df

def transform_P05901(df):
    # P05901 - Número de anos que parou de fumar
    df['P05901'] = df['P05901'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P05901': int})
    return df

def transform_P05902(df):
    # P05902 - Número de meses que parou de fumar
    df['P05902'] = df['P05902'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'P05902': int})
    return df

def transform_J038(df):
    # J038 - Nos últimos 12 meses, quantas vezes ___ esteve internado(a)
    df['J038'] = df['J038'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'J038': int})
    return df

def transform_Q003(df):
    # Q003 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de hipertensão arterial (pressão alta)?
    df['Q003'] = df['Q003'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q003': int})
    return df

def transform_Q031(df):
    # Q031 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de diabetes?
    df['Q031'] = df['Q031'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q031': int})
    return df

def transform_Q061(df):
    # Q061 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de colesterol alto?
    df['Q061'] = df['Q061'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q061': int})
    return df

def transform_Q064(df):
    # Q064 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de doença do coração?
    df['Q064'] = df['Q064'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q064': int})
    return df

def transform_Q070(df):
    # Q070 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de derrame (AVC)?
    df['Q070'] = df['Q070'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q070': int})
    return df

def transform_Q075(df):
    # Q075 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de asma?
    df['Q075'] = df['Q075'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q075': int})
    return df

def transform_Q080(df):
    # Q080 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de artrite ou reumatismo?
    df['Q080'] = df['Q080'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q080': int})
    return df

def transform_Q085(df):
    # Q085 - Que idade o(a) Sr(a) tinha quando começou o problema na coluna?
    df['Q085'] = df['Q085'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q085': int})
    return df

def transform_Q09301(df):
    # Q09301 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de depressão?
    df['Q09301'] = df['Q09301'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q09301': int})
    return df

def transform_Q111(df):
    # Q111 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de doença mental?
    df['Q111'] = df['Q111'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q111': int})
    return df

def transform_Q11701(df):
    # Q11701 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico dessa(s) doença(s) no pulmão?
    df['Q11701'] = df['Q11701'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q11701': int})
    return df

def transform_Q125(df):
    # Q125 - Que idade o(a) Sr(a) tinha no primeiro diagnóstico de insuficiência renal crônica?
    df['Q125'] = df['Q125'].replace("<None>", DEFAULT_NUMBER)
    df = df.astype({'Q125': int})
    return df

def transform_Q00201(df):
    # Q00201 - Algum médico já lhe deu o diagnóstico de hipertensão arterial (pressão alta)?
    df['Q00201'] = df['Q00201'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q00201': int})
    return df

def transform_Q03001(df):
    # Q03001 - Algum médico já lhe deu o diagnóstico de diabetes?
    df['Q03001'] = df['Q03001'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q03001': int})
    return df

def transform_Q060(df):
    # Q060 - Algum médico já lhe deu o diagnóstico de colesterol alto?
    df['Q060'] = df['Q060'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q060': int})
    return df

def transform_Q06306(df):
    # Q06306 - Algum médico já lhe deu o diagnóstico de doença do coração?
    df['Q06306'] = df['Q06306'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q06306': int})
    return df

def transform_Q068(df):
    # Q068 - Algum médico já lhe deu o diagnóstico de derrame (AVC)?
    df['Q068'] = df['Q068'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q068': int})
    return df

def transform_Q074(df):
    # Q074 - Algum médico já lhe deu o diagnóstico de asma?
    df['Q074'] = df['Q074'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q074': int})
    return df

def transform_Q079(df):
    # Q079 - Algum médico já lhe deu o diagnóstico de artrite ou reumatismo?
    df['Q079'] = df['Q079'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q079': int})
    return df   

def transform_Q084(df):
    # Q084 - Algum médico já lhe deu o diagnóstico de depressão?
    df['Q084'] = df['Q084'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q084': int})
    return df   

def transform_Q092(df):
    # Q092 - Algum médico já lhe deu o diagnóstico de doença mental?
    df['Q092'] = df['Q092'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q092': int})
    return df   

def transform_Q11604(df):
    # Q11604 - Algum médico já lhe deu o diagnóstico de doença no pulmão?
    df['Q11604'] = df['Q11604'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q11604': int})
    return df   

def transform_Q120(df):
    # Q120 - Algum médico já lhe deu o diagnóstico de doença renal?
    df['Q120'] = df['Q120'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q120': int})
    return df   

def transform_Q124(df):
    # Q124 - Algum médico já lhe deu o diagnóstico de doença no coração?
    df['Q124'] = df['Q124'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'Q124': int})
    return df   

def transform_R028(df):
    # R028 - A sra já entrou na menopausa?
    df['R028'] = df['R028'].apply(lambda x: 1 if x == "1" else 0)
    df = df.astype({'R028': int})
    return df