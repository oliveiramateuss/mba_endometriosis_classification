def get_feature_scope():

    scope = []
    # MÓDULO V – ANO DE REFERÊNCIA
    modulo_v = [
        { "V0020" : "ano_ref" } # Ano de referencia
    ]
    scope.append(modulo_v)

    # MÓDULO C – CARACTERÍSTICAS GERAIS DOS MORADORES
    modulo_c = [
        { "C008" : "idade_morador" }, # Idade do morador
        { "C009" : "cor_raca" } # Cor ou raça
    ]
    scope.append(modulo_c)

    # Módulo R - Saúde da Mulher (Para mulheres de 15 anos ou mais de idade)
    modulo_r = [
        { 'R00101': 'exame_preventivo' }, # Exame preventivo
        { 'R010': 'retirada_utero' }, # Submetida a cirurgia para retirada do útero
        { 'R011': 'motivo_retirada_utero' }, # Motivo da retirada do útero
        { 'R012': 'idade_cirurgia' }, # Idade na cirurgia
        { 'R025': 'idade_primeira_menstruacao' }, # Idade primeira menstruação
        { 'R028': 'menopausa' }, # Menopausa
        { 'R031': 'relacoes_sexuais_12_meses' }, # Relações sexuais últimos 12 meses
        { 'R034': 'metodo_evitar_gravidez' }, # Método evitar gravidez
        { 'R037': 'tratamento_engravidar' } # Tratamento para engravidar
    ]
    scope.append(modulo_r)

    # Módulo S - Atendimento Pré-Natal  (Para mulheres de 15 anos ou mais de idade)
    modulo_s = [
        { 'S065': 'gravidez' } # Alguma vez ficou grávida
    ]
    scope.append(modulo_s)

    # Módulo Y - Atividade sexual (Para pessoas de 18 anos ou mais de idade)
    modulo_y = [
        { 'Y002': 'relacoes_sexuais' } # Relações sexuais últimos 12 meses
    ]
    scope.append(modulo_y)

    # Módulo H - Atendimento médico (Para pessoas de 18 anos ou mais de idade)
    modulo_h = [
        { 'H001': 'ultima_consulta_medica' }, # Última consulta médica
        { 'H003': 'motivo_consulta' } # Motivo da consulta
    ]
    scope.append(modulo_h)

    # MÓDULO W - ANTROPOMETRIA
    modulo_w = [
        { 'W001': 'antropometria' }, # Antropometria
        { 'W00101': 'peso_1' }, # Peso 1ª pesagem
        { 'W00102': 'peso_2' }, # Peso 2ª pesagem
        { 'W00103': 'peso_final' }, # Peso final
        { 'W00201': 'altura_1' }, # Altura 1ª medição
        { 'W00202': 'altura_2' }, # Altura 2ª medição
        { 'W00203': 'altura_final' } # Altura final
    ]
    scope.append(modulo_w)

    # Módulo P - Estilos de vida
    modulo_p = [
        { 'P00102': 'sabe_peso' }, # Sabe seu peso
        { 'P00103': 'peso_informado' }, # Peso informado
        { 'P00104': 'peso_final' }, # Peso final
        { 'P00402': 'sabe_altura' }, # Sabe sua altura
        { 'P00403': 'altura_informada' }, # Altura informada
        { 'P00404': 'altura_final' }, # Altura final
        { 'P00901': 'consumo_verduras' }, # Consumo de verduras
        { 'P01101': 'consumo_carne_vermelha' }, # Consumo de carne vermelha
        { 'P013': 'consumo_frango' }, # Consumo de frango
        { 'P015': 'consumo_peixe' }, # Consumo de peixe
        { 'P027': 'consumo_alcool' }, # Consumo de álcool
        { 'P034': 'exercicio_fisico' }, # Exercício físico
        { 'P035': 'frequencia_exercicio' }, # Frequência de exercício
        { 'P050': 'fuma_atualmente' }, # Fuma atualmente
        { 'P051': 'fumou_passado_diariamente' }, # Fumou no passado diariamente
        { 'P052': 'fumou_passado' }, # Fumou no passado
        { 'P053': 'idade_comecou_fumar' }, # Idade começou a fumar
        { 'P05402': 'quantidade_cigarros' }, # Quantidade de cigarros
        { 'P05405': 'quantidade_cigarros_palha' }, # Quantidade de cigarros de palha
        { 'P05408': 'quantidade_cigarros_cravo' }, # Quantidade de cigarros de cravo
        { 'P05411': 'quantidade_cachimbos' }, # Quantidade de cachimbos
        { 'P05414': 'quantidade_charutos' }, # Quantidade de charutos
        { 'P05417': 'quantidade_narguile' }, # Quantidade de narguilé
        { 'P05421': 'quantidade_outros' }, # Quantidade de outros
        { 'P05801': 'quantidade_cigarros_passado' } # Quantidade de cigarros no passado
    ]
    scope.append(modulo_p)

    # Módulo J - Utilização de serviços de saúde 
    modulo_j = [
        { 'J001': 'estado_saude' }, # Estado de saúde
        { 'J00101': 'estado_saude_bem_estar' }, # Estado de saúde e bem-estar
        { 'J007': 'diagnostico_doenca_cronica' }, # Diagnóstico de doença crônica
        { 'J01101': 'ultima_consulta_medica' }, # Última consulta médica
        { 'J014': 'procurou_atendimento' }, # Procurou atendimento
        { 'J01502': 'motivo_procurou_atendimento' }, # Motivo procurou atendimento
        { 'J02702': 'principal_atendimento' }, # Principal atendimento
        { 'J038': 'internacoes_12_meses' }, # Internações últimos 12 meses
        { 'J039': 'principal_atendimento_internacao' } # Principal atendimento na internação
    ]
    scope.append(modulo_j)

    # Módulo M - Características do trabalho e apoio social
    modulo_m = [
        { 'M01601': 'frequencia_atividades' } # Frequência de atividades
    ]
    scope.append(modulo_m)

    # Módulo N - Percepção do estado de saúde 
    modulo_n = [
        { 'N001': 'avaliacao_saude' }, # Avaliação da saúde
        { 'N00101': 'avaliacao_saude_bem_estar' } # Avaliação da saúde e bem-estar
    ]
    scope.append(modulo_n)

    # Módulo Q - Doenças crônicas
    modulo_q = [
        { 'Q00201': 'diagnostico_hipertensao' }, # Diagnóstico de hipertensão
        { 'Q003': 'idade_diagnostico_hipertensao' }, # Idade diagnóstico hipertensão
        { 'Q03001': 'diagnostico_diabetes' }, # Diagnóstico de diabetes
        { 'Q031': 'idade_diagnostico_diabetes' }, # Idade diagnóstico diabetes
        { 'Q060': 'diagnostico_colesterol' }, # Diagnóstico de colesterol
        { 'Q061': 'idade_diagnostico_colesterol' }, # Idade diagnóstico colesterol
        { 'Q06306': 'diagnostico_doenca_coracao' }, # Diagnóstico de doença do coração
        { 'Q064': 'idade_diagnostico_coracao' }, # Idade diagnóstico coração
        { 'Q068': 'diagnostico_derrame' }, # Diagnóstico de derrame
        { 'Q070': 'idade_diagnostico_derrame' }, # Idade diagnóstico derrame
        { 'Q074': 'diagnostico_asma' }, # Diagnóstico de asma
        { 'Q075': 'idade_diagnostico_asma' }, # Idade diagnóstico asma
        { 'Q079': 'diagnostico_artrite' }, # Diagnóstico de artrite
        { 'Q080': 'idade_diagnostico_artrite' }, # Idade diagnóstico artrite
        { 'Q084': 'problema_coluna' }, # Problema crônico de coluna
        { 'Q085': 'idade_problema_coluna' }, # Idade problema coluna
        { 'Q092': 'diagnostico_depressao' }, # Diagnóstico de depressão
        { 'Q09301': 'idade_diagnostico_depressao' }, # Idade diagnóstico depressão
        { 'Q11006': 'diagnostico_outra_doenca_mental' }, # Diagnóstico de outra doença mental
        { 'Q111': 'idade_diagnostico_mental' }, # Idade diagnóstico mental
        { 'Q11604': 'diagnostico_doenca_pulmao' }, # Diagnóstico de doença no pulmão
        { 'Q11701': 'idade_diagnostico_pulmao' }, # Idade diagnóstico pulmão
        { 'Q120': 'diagnostico_cancer' }, # Diagnóstico de câncer
        { 'Q12102': 'diagnostico_cancer_pele' }, # Diagnóstico de câncer de pele
        { 'Q12104': 'diagnostico_cancer_pulmao' }, # Diagnóstico de câncer de pulmão
        { 'Q12105': 'diagnostico_cancer_intestino' }, # Diagnóstico de câncer de intestino
        { 'Q12106': 'diagnostico_cancer_estomago' }, # Diagnóstico de câncer de estômago
        { 'Q12107': 'diagnostico_cancer_mama' }, # Diagnóstico de câncer de mama
        { 'Q12108': 'diagnostico_cancer_colo_utero' }, # Diagnóstico de câncer de colo do útero
        { 'Q121010': 'diagnostico_cancer_boca' }, # Diagnóstico de câncer de boca
        { 'Q121011': 'diagnostico_cancer_bexiga' }, # Diagnóstico de câncer de bexiga
        { 'Q121012': 'diagnostico_cancer_linfoma' }, # Diagnóstico de linfoma
        { 'Q121013': 'diagnostico_cancer_cerebro' }, # Diagnóstico de câncer de cérebro
        { 'Q121014': 'diagnostico_cancer_ovario' }, # Diagnóstico de câncer de ovário
        { 'Q121015': 'diagnostico_cancer_tireoide' }, # Diagnóstico de câncer de tireoide
        { 'Q12201': 'diagnostico_cancer_outro' }, # Diagnóstico de outro câncer
        { 'Q124': 'diagnostico_insuficiencia_renal' }, # Diagnóstico de insuficiência renal
        { 'Q125': 'idade_diagnostico_renal' }, # Idade diagnóstico renal
        { 'Q128': 'diagnostico_outra_doenca_cronica' } # Diagnóstico de outra doença crônica
    ]
    scope.append(modulo_q)

    # modulo_v = [
    #     { "V0020" : "ano_ref" } # Ano de referencia
    # ]
    # scope.append(modulo_v)

    # # Módulo R - Saúde da Mulher (Para mulheres de 15 anos ou mais de idade)
    # modulo_r = [
    #     { 'R00101': 'Quando foi a última vez que a Sra fez exame preventivo para câncer de colo do útero' },
    #     { 'R011': 'Segundo o médico, qual o motivo da retirada do útero? (3 = endometriose)' },
    #     { 'R012': 'Que idade a sra tinha quando foi submetida à cirurgia?' },
    #     { 'R025': 'Com que idade a sra ficou menstruada pela primeira vez?' },
    #     { 'R031': 'Nos últimos 12 meses, a sra teve relações sexuais?' },
    #     { 'R034': 'A sra usa algum método para evitar a gravidez atualmente?' },
    #     { 'R037': 'A sra e/ou seu companheiro já fizeram ou fazem algum tratamento para engravidar?' }
    # ]
    # scope.append(modulo_r)

    # # Módulo S - Atendimento Pré-Natal  (Para mulheres de 15 anos ou mais de idade)
    # modulo_s = [
    #     { 'S065': 'Alguma vez ficou grávida, mesmo que a gravidez não tenha chegado até o final?' }
    # ]
    # scope.append(modulo_s)

    # # Módulo Y - Atividade sexual (Para pessoas de 18 anos ou mais de idade)
    # modulo_y = [
    #     { 'Y002': 'Nos últimos doze meses teve relações sexuais?' }
    # ]
    # scope.append(modulo_y)

    # # Módulo H - Atendimento médico (Para pessoas de 18 anos ou mais de idade)
    # modulo_h = [
    #     { 'H001': 'Quando foi a última vez que o(a) sr(a) consultou com um(a) médico(a)?' },
    #     { 'H003': 'Por qual motivo o(a) sr(a) precisou consultar com um(a) médico(a)?' }
    # ]
    # scope.append(modulo_h)

    # # MÓDULO W - ANTROPOMETRIA
    # modulo_w = [
    #     { 'W001': 'Antropometria aferida do morador selecionado' },
    #     { 'W00101': 'Peso - 1ª pesagem (em kg)' },
    #     { 'W00102': 'Peso - 2ª pesagem (em kg)' },
    #     { 'W00103': 'Peso - Final (em kg)' },
    #     { 'W00201': 'Altura - 1ª medição (em cm)' },
    #     { 'W00202': 'Altura - 2ª medição (em cm)' },
    #     { 'W00203': 'Altura - Final (em cm)' }
    # ]
    # scope.append(modulo_w)

    # Módulo P - Estilos de vida
    # modulo_p = [
    #     { 'P00102': 'O(A) Sr(a) sabe seu peso?' },
    #     { 'P00103': 'Peso - Informado (em kg)' },
    #     { 'P00104': 'Peso - Final (em kg)' },
    #     { 'P00402': 'O(A) Sr(a) sabe sua altura?' },
    #     { 'P00403': 'Altura - Informada (em cm)' },
    #     { 'P00404': 'Altura - Final (em cm)' },
    #     { 'P00901': 'Em quantos dias da semana, o(a) Sr(a) costuma comer pelo menos um tipo de verdura ou legume (sem contar batata, mandioca, cará ou inhame) como alface, tomate, couve, cenoura, chuchu, berinjela, abobrinha?' },
    #     { 'P01101': 'Em quantos dias da semana o(a) Sr(a) costuma comer carne vermelha (boi, porco, cabrito, bode, ovelha etc.)?' },
    #     { 'P013': 'Em quantos dias da semana o(a) Sr(a) costuma comer frango/galinha?' },
    #     { 'P015': 'Em quantos dias da semana o(a) Sr(a) costuma comer peixe?' },
    #     { 'P027': 'Com que frequência o(a) Sr(a) costuma consumir alguma bebida alcoólica?' },
    #     { 'P034': 'Nos últimos três meses, o(a) Sr(a) praticou algum tipo de exercício físico ou esporte?' },
    #     { 'P035': 'Quantos dias por semana o(a) Sr(a) costuma (costumava) praticar exercício físico ou esporte?' },
    #     { 'P050': 'Atualmente, o(a) Sr(a) fuma algum produto do tabaco?' },
    #     { 'P051': 'E no passado, o(a) Sr(a) fumou algum produto do tabaco diariamente?' },
    #     { 'P052': 'E no passado, o(a) Sr(a) fumou algum produto do tabaco?' },
    #     { 'P053': 'Que idade o(a) Sr(a) tinha quando começou a fumar produto de tabaco diariamente?' },
    #     { 'P05401': 'Em média, quanto fuma por dia ou por semana Cigarros industrializados' },
    #     { 'P05404': 'Em média, quanto fuma por dia ou por semana Cigarros de palha ou enrolados a mão?' },
    #     { 'P05407': 'Em média, quanto fuma por dia ou por semana Cigarros de cravo ou de Bali?' },
    #     { 'P05410': 'Em média, quanto fuma por dia ou por semana Cachimbos (considere cachimbos cheios)?' },
    #     { 'P05413': 'Em média, quanto fuma por dia ou por semana Charutos ou cigarrilhas?' },
    #     { 'P05416': 'Em média, quanto fuma por dia ou por semana Narguilé (sessões)?' },
    #     { 'P05419': 'Em média, quanto fuma por dia ou por semana Outro' },
    #     { 'P058': 'Em média, quantos cigarros industrializados o(a) Sr(a) fumava por dia ou por semana?' }
    # ]
    # scope.append(modulo_p)

    # # Módulo  J - Utilização de serviços de saúde 
    # modulo_j = [
    #     { 'J001': 'De um modo geral, como é o estado de saúde de________' },
    #     { 'J00101': 'Considerando saúde como um estado de bem-estar físico e mental, e não somente a ausência de doenças, como é o estado de saúde de _____________?' },
    #     { 'J007': 'Algum médico já deu o diagnóstico de alguma doença crônica, física ou mental, ou doença de longa duração (de mais de 6 meses de duração) a ___' },
    #     { 'J01101': 'Quando ____ consultou um médico pela última vez' },
    #     { 'J014': 'Nas duas últimas semanas, ___ procurou algum lugar, serviço ou profissional de saúde para atendimento relacionado à própria saúde' },
    #     { 'J01502': 'Qual foi o motivo principal pelo qual ___ procurou atendimento relacionado à própria saúde nas duas últimas semanas' },
    #     { 'J02702': 'Qual foi o principal atendimento de saúde que ___ recebeu?' },
    #     { 'J038': 'Nos últimos 12 meses, quantas vezes ___ esteve internado(a)' },
    #     { 'J039': 'Qual foi o principal atendimento de saúde que ___recebeu quando esteve internado(a) (pela última vez) nos doze últimos meses' }
    # ]
    # scope.append(modulo_j)

    # # Módulo M - Características do trabalho e apoio social
    # modulo_m = [
    #     { 'M01601': 'Nos últimos doze meses, com que frequência o(a) Sr(a) se reuniu com outras pessoas para prática de atividades esportivas, exercícios físicos, recreativos ou artísticos' }
    # ]
    # scope.append(modulo_m)

    # # Módulo N - Percepção do estado de saúde 
    # modulo_n = [
    #     { 'N001': 'Em geral, como o(a) Sr(a) avalia a sua saúde' },
    #     { 'N00101': 'Considerando saúde como um estado de bem-estar físico e mental, e não somente a ausência de doenças, como você avalia o seu estado de saúde?' }
    # ]
    # scope.append(modulo_n)

    # # Módulo Q - Doenças crônicas
    # modulo_q = [
    #     { 'Q00201': 'Algum médico já lhe deu o diagnóstico de hipertensão arterial (pressão alta)?' },
    #     { 'Q003': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de hipertensão arterial (pressão alta)?' },
    #     { 'Q03001': 'Algum médico já lhe deu o diagnóstico de diabetes?' },
    #     { 'Q031': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de diabetes?' },
    #     { 'Q060': 'Algum médico já lhe deu o diagnóstico de colesterol alto?' },
    #     { 'Q061': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de colesterol alto?' },
    #     { 'Q06306': 'Algum médico já lhe deu o diagnóstico de uma doença do coração, tal como infarto, angina, insuficiência cardíaca ou outra?' },
    #     { 'Q064': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de doença do coração?' },
    #     { 'Q068': 'Algum médico já lhe deu o diagnóstico de derrame (AVC)?' },
    #     { 'Q070': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de derrame (AVC)?' },
    #     { 'Q074': 'Algum médico já lhe deu o diagnóstico de asma?' },
    #     { 'Q075': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de asma?' },
    #     { 'Q079': 'Algum médico já lhe deu o diagnóstico de artrite ou reumatismo?' },
    #     { 'Q080': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de artrite ou reumatismo?' },
    #     { 'Q084': 'O(a) Sr(a) tem algum problema crônico de coluna, como dor crônica nas costas ou no pescoço, lombalgia, dor ciática, problemas nas vértebras ou disco?' },
    #     { 'Q085': 'Que idade o(a) Sr(a) tinha quando começou o problema na coluna?' },
    #     { 'Q092': 'Algum médico ou profissional de saúde mental (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de depressão?' },
    #     { 'Q09301': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de depressão?' },
    #     { 'Q11006': 'Algum médico ou profissional de saúde (como psiquiatra ou psicólogo) já lhe deu o diagnóstico de outra doença mental, como transtorno de ansiedade, síndrome do pânico, esquizofrenia, transtorno bipolar, psicose ou TOC (Transtorno Obsessivo Compulsivo) etc?' },
    #     { 'Q111': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de doença mental?' },
    #     { 'Q11604': 'Algum médico já lhe deu o diagnóstico de alguma outra doença crônica no pulmão, tais como enfisema pulmonar, bronquite crônica ou DPOC (Doença Pulmonar Obstrutiva Crônica)?' },
    #     { 'Q11701': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico dessa(s) doença(s) no pulmão?' },
    #     { 'Q120': 'Algum médico já lhe deu diagnóstico de câncer?' },
    #     { 'Q12102': 'Foi um diagnóstico de câncer de pele?' },
    #     { 'Q12104': 'Diagnóstico de outro câncer? Pulmão' },
    #     { 'Q12105': 'Diagnóstico de outro câncer? Cólon e reto (intestino)' },
    #     { 'Q12106': 'Diagnóstico de outro câncer? Estômago' },
    #     { 'Q12107': 'Diagnóstico de outro câncer? Mama (só para mulheres)' },
    #     { 'Q12108': 'Diagnóstico de outro câncer? Colo do útero (só para mulheres)' },
    #     { 'Q121010': 'Diagnóstico de outro câncer? Boca, Orofaringe ou Laringe' },
    #     { 'Q121011': 'Diagnóstico de outro câncer? Bexiga' },
    #     { 'Q121012': 'Diagnóstico de outro câncer? Linfoma ou leucemia' },
    #     { 'Q121013': 'Diagnóstico de outro câncer? Cerebro' },
    #     { 'Q121014': 'Diagnóstico de outro câncer? Ovário (só para mulheres)' },
    #     { 'Q121015': 'Diagnóstico de outro câncer? Tireoide' },
    #     { 'Q12201': 'Diagnóstico de câncer de outro cancer?' },
    #     { 'Q124': 'Algum médico já lhe deu o diagnóstico de insuficiência renal crônica?' },
    #     { 'Q125': 'Que idade o(a) Sr(a) tinha no primeiro diagnóstico de insuficiência renal crônica?' },
    #     { 'Q128': 'Algum médico já lhe deu algum diagnóstico de outra doença crônica (física ou mental) ou doença de longa duração (de mais de 6 meses de duração)?' }
    # ]
    # scope.append(modulo_q)

    return scope
