# Etapas de Arquitetura a Ambiente e Padrões

Fonte: site Intera, Metodologia 2.0 › Etapas e › Artefatos (31/10/2026); livro *Metodologia Intera 2.0*, cap. 1.

## Arquitetura (esboço do OA)

Transforma contexto e requisitos em um esboço independente de tecnologia, para que toda a equipe — inclusive o professor que não domina a tecnologia — entenda como será o OA. Também define tecnologias, padrões e componentes de reúso, e decompõe o OA em módulos.

- **Entradas:** relatório de análise de contexto; especificação de requisitos.
- **Práticas:** modelagem; divisão em componentes menores.
- **Saídas:** artefatos ligados à prática usada (o esboço).
- É iterativa: ajustes nos requisitos durante o esboço são esperados e devem ser registrados.

Não há modelo único; o tipo de esboço depende do OA (livro, Quadro 5; site, Artefatos):

| Esboço | Recomendado para | O que é | Modelo/exemplo |
| --- | --- | --- | --- |
| Mapa de atividades (mapa instrucional) | Disciplinas e cursos a distância | Ementa do curso em aulas: unidade, subunidades, objetivos específicos, conteúdo teórico, atividades a entregar e ferramentas, extras, carga horária | https://docs.google.com/document/d/15XCsWBXbHIDDNVMJHWUDJmnzCJBdwJok/edit (exemplo preenchido) |
| Sumário executivo | Cursos a distância | Lista tópica dos assuntos, organização linear | — |
| Roteiro | Aulas síncronas, videoaulas, simulações, animações | Texto detalhado de imagens, ações, falas, cenários e personagens; para aula síncrona, inclui a sequência didática | https://docs.google.com/document/d/1Q4EqSwYfnn5pCNGqfra0ZUb33QcdZ0VT/edit |
| Storyboard | Simulações e animações | Desenhos em sequência, como quadrinhos sem balões | — |
| Protótipo ou wireframe | Simulação, software, animação | Modelo funcional que destaca as funcionalidades | https://docs.google.com/document/d/1D_3AeQduUWq66OSPCsbs_tDpyzuFJ9NK/edit (formulário de solicitação audiovisual, exemplo) |
| GDD (documento de game design) | Jogos | Ver `extensao-jogos.md` | — |

### Detalhamento da Arquitetura (livro vol. 2 (BRAGA, 2015), cap. 4)

A etapa tem **três atividades**: (a) **esboço** do OA, feito pelo professor, independente de tecnologia; (b) **decomposição** do OA em componentes pequenos, independentes e reutilizáveis, com as conexões entre eles; (c) **definições técnicas** (tecnologias e padrões), feitas pela equipe técnica. O esboço evita o problema ilustrado no livro do demandante que imagina um "vestido" e recebe um "chapéu". É normal ajustar os requisitos durante o esboço; o importante é que estejam claros antes do desenvolvimento.

Detalhes práticos dos esboços:
- **Roteiro de videoaula** em quatro colunas: tipo de trecho (conceito ou exemplo), texto narrado, texto que aparece na tela, recurso digital exibido. O roteiro deve permitir que um técnico produza o vídeo sem a presença do autor.
- **Sumário executivo:** lista de tópicos em ordem linear; recomenda-se até quatro laudas.
- **Storyboard:** pode ser um desenho simples do próprio professor; muitas vezes precisa de um roteiro junto, com falas e descrições.
- **Protótipo (mockup):** modelo funcional, em papel, slides ou ferramenta de prototipação; deve ser testado e aprovado antes do desenvolvimento.
- **Mapa de atividades:** num curso, cada aula pode ser tratada como um objeto.

**Decomposição pela taxonomia de Wiley (2000):** ajuda a decidir o tamanho e a combinação dos componentes.

| Tipo | O que é | Reúso |
| --- | --- | --- |
| Fundamental | um único recurso de um só tipo de mídia (uma imagem, um texto, uma citação) | o mais alto; projetar para o maior número de contextos |
| Combinado-inédito | poucos recursos combinados (2 a 4), com uma única finalidade (ex.: mapa com rótulos; vídeo com áudio) | alto, menor que o fundamental |
| Combinado-modificável | muitos recursos combinando instrução e prática numa sequência | reusável como um todo; partes menos reaproveitáveis |
| Gerador-apresentação | lógica que monta apresentações a partir de objetos menores | alto em contextos semelhantes, baixo em contextos diferentes |
| Gerador-instrução | lógica que monta e avalia interações do aluno | alto em contextos semelhantes e diferentes |

O desafio é que cada módulo possa ser entendido de forma independente dos demais.

## Desenvolvimento

Construção do OA e de seus componentes de reúso. A técnica varia com o tipo (vídeo: gravar, decupar, editar; software: programar).

- **Entradas:** relatório de contexto; especificação de requisitos; documento de arquitetura.
- **Práticas:** variam conforme o OA.
- **Saídas:** o OA (e código-fonte, se software); práticas pedagógicas sugeridas; manual de uso para o professor; manual de uso para o aluno; instalador com OA, manuais e metadados; direitos autorais e patrimoniais.

### Detalhamento do Desenvolvimento (livro vol. 2 (BRAGA, 2015), cap. 5)

- Quanto mais planejado o OA antes do desenvolvimento (contexto, requisitos e esboço), maior a qualidade e o reúso. O demandante e o conteudista atuam sobretudo no início e no fim desta etapa.
- Os **componentes de reúso** fazem parte do desenvolvimento: manual do usuário, instruções de instalação e **guia de edição** (como outra pessoa pode alterar o OA).
- **Ferramentas de autoria gratuitas** permitem que o próprio professor produza OAs simples; o livro (2015) cita Xerte, CourseLab, Ardora e HagáQuê. Confira se continuam disponíveis antes de recomendar e prefira ferramentas que exportem em formatos abertos ou SCORM.
- **Padrões:** o único padrão formal do IEEE LTSC para OAs é o de metadados **LOM**; para cursos on-line são usados **SCORM** (ADL) e o empacotamento **IMS Content Package**; o **W3C** define os padrões da web. **Empacote** o OA quando ele tiver vários itens (páginas, vídeos, atividades), para que seja distribuído e reutilizado como uma unidade; um item único, como uma imagem, não precisa de pacote.

## Teste e Qualidade

Valida características técnicas (incluindo acessibilidade e usabilidade) e parte das pedagógicas. Recomenda-se testar desde o esboço, não só no final.

- **Entradas:** especificação de requisitos; casos de teste; cenários de teste; plano de testes.
- **Saídas:** evidências de testes; relatório de erros; OA testado e qualificado.

Tipos de teste e questões orientadoras (site e livro):

| Tipo | Questão orientadora |
| --- | --- |
| Funcionalidade | Todos os requisitos funcionais foram atendidos? |
| Acessibilidade | O OA pode ser acessado em diferentes contextos, por diversos usuários e dispositivos? É compatível com leitores de tela? |
| Confiabilidade técnica | As funcionalidades apresentam algum defeito? |
| Confiabilidade pedagógica / Conteúdo | O OA está alinhado aos objetivos pedagógicos e às teorias de aprendizagem definidas? |
| Precisão | O OA gera resultados precisos e dentro do esperado? |
| Portabilidade | Funciona em diferentes sistemas, AVAs e dispositivos? |
| Instalação | É fácil de instalar? O manual de instalação é adequado? |
| Interoperabilidade | Exporta dados para outros sistemas, quando necessário? |
| Usabilidade | É fácil de usar? Tem ajuda adequada ao aluno e ao professor? |
| Manutenibilidade | Pode ser corrigido, atualizado e alterado com facilidade? |
| Eficiência | Recursos e tempos de uso são compatíveis com o desempenho esperado? |
| Disponibilidade | Está indexado e em repositório adequado? É fácil localizar e acessar? |
| Segurança | Protege contra acessos indevidos (ex.: aluno ver notas de outros)? |

A página de Artefatos também recomenda, em resumo: testes funcionais, de usabilidade e de experiência do usuário. Para jogos, somam-se jogabilidade e conteúdo; para cursos EaD, checklist de qualidade e checklist de acessibilidade e-MAG.

**Como a skill conduz:** monte o plano de testes a partir da especificação (um caso de teste por RF/RA, com critério de aceite); para acessibilidade, use o conjunto de diretrizes definido nos requisitos (WCAG/e-MAG, MobileDU ou RPG-DU) e recomende testes com pessoas com deficiência do público-alvo, de perfis diferentes (não só com a equipe e não só com um tipo de deficiência); registre o perfil e o número de testadores e quais dimensões da matriz de `desenho-universal.md` foram testadas.

### Detalhamento de Teste e Qualidade (livro vol. 2 (BRAGA, 2015), cap. 6)

- **Dois objetivos:** testes de **validação** (o OA faz o que foi proposto?) e testes de **defeito** (encontrar erros antes do uso com alunos). Em OA, corrigir erros inclui o conteúdo pedagógico, não só o técnico.
- **Quando testar:** durante o desenvolvimento (ainda em esboço), ao final do desenvolvimento e antes do uso efetivo. "Não se pode testar a qualidade se ela não estiver lá": o teste melhora, mas quem garante a qualidade é o processo.
- **O que os testes conferem:** o contexto idealizado × o real (outras realidades tecnológicas, números de usuários, plataformas); se o conteúdo está correto e completo; se todos os requisitos foram implementados; as características de OA, **em especial a reusabilidade**; a arquitetura.
- **Ciclo de vida dos testes:** planejamento (estratégia e plano de testes, sem antecipar soluções), preparação (ambiente, equipamentos, artefatos, pessoas), execução (registrar e corrigir erros) e entrega (histórico, soluções, características finais e documentação arquivada).
- **Testes com usuários** (alunos e professores do público-alvo) são fortemente recomendados: a equipe não reproduz o contexto real (ex.: um jogo para crianças de 9 anos precisa ser testado com crianças dessa idade).
- **Testes de conteúdo**, com especialistas e usuários: o conteúdo está correto, completo, atualizado e adequado ao público? A perspectiva é consistente? Exemplos, exercícios e feedback são realistas? A abordagem pedagógica e as estratégias instrucionais são coerentes com a teoria adotada?
- **Artefatos de teste do livro:** *plano de testes* (tipo de teste, fase, responsável); *evidência de teste* (captura de tela com o erro marcado); *checklist* (item, atende, não atende, corrigido); *caso de teste* (passo, valor de entrada, ação, resultado esperado, erro encontrado, evidência). A quantidade de testes cresce com a complexidade do OA (uma animação precisa de menos testes que um software).

## Disponibilização

Publicação do OA, da documentação de uso e da instalação em repositório, de preferência um repositório de objetos de aprendizagem com metadados no padrão **LOM**.

- **Entradas:** OA/curso; manual de instalação; manual de uso do professor; manual de uso do aluno.
- **Prática:** depósito em repositório de objetos de aprendizagem.
- **Saída:** objeto disponível para reúso.

**Como a skill conduz:** gere a ficha de metadados (título, descrição, autores, idioma, público, nível, área/disciplina, objetivos, tipo de recurso, formato, requisitos técnicos, recursos de acessibilidade, licença, data, versão, palavras-chave) e um README; quando o OA for software ou material aberto, sugira repositório com versionamento e DOI (ex.: GitHub + Zenodo). Inclua na ficha a licença e os 5R que ela permite, o tamanho do grão, os formatos entregues e o link para os arquivos-fonte, e atualize a ficha de reúso (`reuso-e-rea.md`). Prefira repositórios especializados em OA ou REA, que guardam também as informações pedagógicas, e links persistentes.

### Detalhamento da Disponibilização (livro vol. 2 (BRAGA, 2015), cap. 7)

Uma disponibilização inadequada causa: OA que ninguém encontra (e **retrabalho**, quando outro professor cria de novo algo que já existe), busca difícil por falta de metadados, direitos autorais obscuros e OAs sem avaliação de qualidade.

**Características desejáveis de um repositório de OA (ROA):** disponível 24 horas; busca interna por características técnicas e pedagógicas; indexado por buscadores externos; persistência (o OA não se perde); usabilidade; acessibilidade; metadados técnicos e pedagógicos; reputação (avaliação pelos usuários); respeito ao direito autoral; gestão de conteúdo e de versões; acesso à documentação de ajuda; **acesso às práticas pedagógicas** já realizadas com o OA.

**Direitos autorais (Lei 9.610/98):** direitos **morais** (autoria; intransferíveis e irrenunciáveis) e **patrimoniais** (exploração econômica; podem ser cedidos ou licenciados). O depósito deve deixar ambos explícitos.

**Metadados:** o autor preenche as informações técnicas e pedagógicas; o repositório gera o arquivo de metadados.
- *Dublin Core:* 15 elementos opcionais e repetíveis (título, criador, assunto, descrição, editor, colaborador, data, tipo, formato, identificador, fonte, idioma, relação, cobertura, direitos). Simples e genérico.
- *IEEE LOM:* 9 categorias (geral, ciclo de vida, meta-metadados, técnica, educacional, direitos, relação, anotação, classificação). Completo, mas extenso. A categoria educacional traz tipo e nível de interatividade, tipo de recurso, densidade semântica, papel do usuário, contexto, faixa etária, dificuldade e tempo típico de aprendizagem.
- *OBAA:* proposta brasileira (UFRGS e Unisinos) baseada no LOM, com categorias adicionais de **acessibilidade** e segmentação.

**Tipos de repositório:** local (guarda OA e metadados), remoto ou referatório (só metadados e link) e misto. Alguns repositórios citados no livro (como o BIOE) avaliam o OA por especialistas antes de publicar; confira se continuam ativos.

## Avaliação pedagógica

Ver `avaliacao-pedagogica.md`.

## Gestão de Projetos (transversal)

Perpassa todo o projeto: custos, cronograma e pessoas.

- **Entradas:** especificação de requisitos; relatório de contextualização. (Jogos: também edital do projeto.)
- **Práticas:** técnicas de cronograma e de estimativa de tempo (ex.: PMBOK). (Jogos: reuniões.)
- **Saídas:** cronograma; custo; alocação de pessoas por atividade. (Jogos: também prestação de contas, relatório de atividade de bolsista e formulário post-mortem.)

**Como a skill conduz:** proponha a matriz papel × pessoa (uma pessoa pode ter vários papéis; sinalize acúmulos arriscados, como demandante = conteudista = avaliador, e a ausência de equipe de acessibilidade e de usuários) e um cronograma por etapa, lembrando que as etapas se sobrepõem.

## Ambiente e Padrões

Controla o ambiente técnico de desenvolvimento: backups, controle de versões e, no EaD, ambientes de desenvolvimento, homologação e produção.
