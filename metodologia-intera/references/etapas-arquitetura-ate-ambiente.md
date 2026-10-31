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

## Desenvolvimento

Construção do OA e de seus componentes de reúso. A técnica varia com o tipo (vídeo: gravar, decupar, editar; software: programar).

- **Entradas:** relatório de contexto; especificação de requisitos; documento de arquitetura.
- **Práticas:** variam conforme o OA.
- **Saídas:** o OA (e código-fonte, se software); práticas pedagógicas sugeridas; manual de uso para o professor; manual de uso para o aluno; instalador com OA, manuais e metadados; direitos autorais e patrimoniais.

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

**Como a skill conduz:** monte o plano de testes a partir da especificação (um caso de teste por RF/RA, com critério de aceite); para acessibilidade, use o conjunto de diretrizes definido nos requisitos (WCAG/e-MAG, MobileDU ou RPG-DU) e recomende testes com pessoas com deficiência do público-alvo, não só com a equipe; registre o perfil e o número de testadores.

## Disponibilização

Publicação do OA, da documentação de uso e da instalação em repositório, de preferência um repositório de objetos de aprendizagem com metadados no padrão **LOM**.

- **Entradas:** OA/curso; manual de instalação; manual de uso do professor; manual de uso do aluno.
- **Prática:** depósito em repositório de objetos de aprendizagem.
- **Saída:** objeto disponível para reúso.

**Como a skill conduz:** gere a ficha de metadados (título, descrição, autores, idioma, público, nível, área/disciplina, objetivos, tipo de recurso, formato, requisitos técnicos, recursos de acessibilidade, licença, data, versão, palavras-chave) e um README; quando o OA for software ou material aberto, sugira repositório com versionamento e DOI (ex.: GitHub + Zenodo).

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
