# Etapa de Requisitos — guia

Objetivo: levantar o que se espera do OA (o "quê" e o "como"), unindo objetivos pedagógicos e desenvolvimento técnico. O professor deve atuar fortemente nesta etapa.

- **Entradas:** relatório de análise de contexto; guia de coleta de requisitos. (Jogos: também wireframe e arquitetura da narrativa.)
- **Práticas:** entrevistas; preenchimento de formulários; brainstorm (mapas conceituais). (Jogos: reunião com equipes de conteúdo e desenvolvimento; diagramas de atividades; casos de uso; casos de teste.)
- **Saída:** documento de especificação de requisitos. (Jogos: também casos de uso e decupagem.)

Fonte: site Intera, Metodologia 2.0 › Etapas › Requisitos e › Artefatos (31/10/2026); livro, cap. 1, Quadro 4.

## Três tipos de requisito

- **Didático-pedagógicos:** conceitos pedagógicos evidenciados no OA e a abordagem teórica que o fundamenta (ex.: OA orientado pela teoria sociointeracionista).
- **Técnicos funcionais:** funcionalidades que o OA deve ter e como são apresentadas (ex.: "o jogo deverá permitir ao usuário configurar o tamanho da letra").
- **Técnicos não funcionais:** propriedades e restrições do OA como um todo: confiabilidade, usabilidade, segurança, disponibilidade, reusabilidade, **acessibilidade**, desempenho, portabilidade, suporte/ajuda, design.

Na extensão para jogos, os requisitos se distribuem pela tétrade: narrativa (diálogos e conteúdo pedagógico), mecânica e tecnologia (plataforma, regras, funcionalidades) e estética.

## Guia de Requisitos Pedagógicos e Técnicos (modelo publicado no site)

Modelo: https://docs.google.com/document/d/19y8CqzaArEBDLAjzz99EM1L0ZEFhD8q2/edit

**Requisitos didático-pedagógicos**
- Deseja se basear em alguma teoria de aprendizagem? Qual?
- Existe material didático (livros, sites, apostilas) a aproveitar? Qual e onde está?
- Existe algum OA que sirva de base?
- Deseja trabalhar a **interatividade** do conteúdo pedagógico (o aluno vê, escuta ou responde algo)? Como?
- Deseja trabalhar a **autonomia** (iniciativa e tomada de decisão do aluno)? Como?
- Deseja trabalhar a **cooperação** (alunos trocam opiniões e trabalham coletivamente)? Como?
- Deseja trabalhar a **afetividade** (sentimentos e motivações do aluno)? Como?
- O OA deve conter outros tipos de OA? (apresentação em texto/HTML; atividades; feedback das atividades; outros)
- Outras informações pedagógicas.

**Requisitos técnicos de funcionalidade**
- Tipo de OA: imagem, vídeo, texto, animação, simulação, jogo, curso on-line.
- Quais funcionalidades o OA deve ter? (pode ser expresso por protótipo)

**Interface gráfica:** padrão de cores, fontes, estilos.

**Disponibilidade:** onde o OA ficará disponível (AVA como Moodle, sites públicos, repositórios de OA, outros).

**Acessibilidade**
- Por quais dispositivos o OA deve ser acessado (celular, computador, TV, tablet)?
- Será acessível por qualquer dispositivo com internet?
- O OA deverá ser acessível a pessoas com algum tipo de deficiência? Quais? (Na skill, a resposta parte do Desenho Universal e percorre a matriz de necessidades de `desenho-universal.md`.)

**Acesso:** professores e alunos acessam da mesma forma? Quais as diferenças? Precisa de administrador?

> Complemento proposto por esta skill, feito no bloco de Acesso: o OA precisa de login? Quais dados dos alunos serão coletados e para quê? O público inclui crianças ou adolescentes? As respostas viram requisitos de ética e privacidade (RNF-ET), conforme `desenho-etico.md`.

**Desempenho:** quantos alunos simultâneos?

**Portabilidade:** sistemas operacionais; outros dispositivos; acesso via web e necessidade de plugin.

**Licenciamento e direitos** (no modelo aparece repetido o título "Requisitos de Portabilidade"): licença (ver https://br.creativecommons.org/); a quem pertencerá o copyright.

**Reúso:** granularidade, agregação e reusabilidade do OA.

> Para conduzir este bloco, use `reuso-e-rea.md`: transforme as respostas em requisitos não funcionais de reúso testáveis (licença aberta, formatos editáveis, arquivos-fonte entregues, tamanho do grão, independência entre partes, compatibilidade de licenças de terceiros) e preencha a ficha de reúso. Na pergunta de licença, explique os 5R e o efeito de cada licença Creative Commons.

## Detalhamento da etapa (livro vol. 2, cap. 3)

Fonte: BRAGA, J. C. *Objetos de Aprendizagem, volume 2: metodologia de desenvolvimento*. Santo André: Editora da UFABC, 2015 (Coleção Intera), cap. 3 (Braga; Kelly).

**Para que serve a etapa:** chegar a um acordo com o demandante sobre o que o OA deve fazer; dar à equipe uma compreensão clara do OA; servir de base para planejar as iterações e **estimar custo e prazo**; preparar o esboço; e ser o elo entre o técnico e o pedagógico. O documento de especificação circula por toda a equipe como um **"acordo"** e deve estar em linguagem natural. O professor demandante preenche e o analista revisa; é normal completá-lo em várias rodadas.

**De onde vêm os requisitos:** de qualquer pessoa que ajude a entender o OA (o "requisitante": demandante, coordenador, professores, alunos do público-alvo), de documentos (ementa, apostila, texto de referência) e de **OAs já existentes** usados como base. O livro aponta como erro mais comum avançar com requisitos incompletos ou mal coletados.

**Técnicas de levantamento** (adaptado de Courage e Baxter, 2005):

| Técnica | Quando usar | Cuidado |
| --- | --- | --- |
| Entrevistas | OA com vários tipos de usuário; entrevista com o professor idealizador | exige preparo do entrevistador e tempo |
| Questionários | muitos usuários, baixo custo, sem contato presencial | quem elabora precisa conhecer os objetivos da etapa |
| Grupos de foco | equipe reunida para discutir o OA | rever requisitos e testes com frequência |
| Brainstorming | 2 a 10 pessoas buscando ideias novas | gerenciar prazo e foco pedagógico |
| Estudos de campo | grupo com interesses em comum | idem questionários |

**Subcategorias de requisitos não funcionais, com exemplos do livro:**

- *Confiabilidade:* veracidade do conteúdo; exatidão dos exercícios; nível de detalhe apropriado.
- *Usabilidade:* itens relacionados próximos; áudio para descrever gráficos; apoio à navegação; linguagem acessível; ajuda disponível.
- *Acesso:* perfis distintos (ex.: aluno não vê a área do professor; professor vê a do aluno; dados de notas armazenados com segurança).
- *Disponibilidade:* OA depositado em repositório especializado, com metadados.
- *Reusabilidade:* conteúdo organizado para ser desmembrado em mais de uma unidade (ex.: "os conceitos de desvio condicional simples e composto podem ser apresentados juntos ou separados"; "o OA poderá ser dividido em pelo menos três pequenos objetos, usados juntos ou separados").
- *Acessibilidade:* ex.: "todas as funcionalidades deverão ser lidas por leitores de tela". É um exemplo do livro para um público; na skill, ele entra junto com requisitos para as demais dimensões do Desenho Universal (`desenho-universal.md`).
- *Desempenho:* número de usuários simultâneos e tempo de resposta.
- *Portabilidade:* navegadores, AVAs, sistemas e dispositivos.
- *Ajuda e documentação:* manual de instalação, guia do professor, guia do aluno.
- *Design de interface:* ex.: mesmas fontes e cores do site da instituição.
- *Licenciamento e direitos autorais:* licença, titular do copyright, avisos legais e restrições.

**Requisitos pedagógicos de cursos EaD:** o livro organiza um exemplo pelos três pilares da EaD: **estruturação** (AVA, objetivos e critérios claros em cada aula, atividades com feedback), **autonomia do aluno** (vídeos que podem ser revistos, aulas assíncronas) e **diálogo** (prazos de resposta a dúvidas, feedback individual dos tutores, fóruns e webconferência).

## Exemplos publicados

- Aulas síncronas: https://docs.google.com/document/d/1TCLozxVqbfMYPYZTWeB0-XWe0RXeMosQ/edit
- Simulação: https://docs.google.com/document/d/1UmlRAoGSmGd9ZI6uZ1TtJT-ZlfnIvLW_/edit
- Animação: https://docs.google.com/document/d/1HEjDea4eH0v9zqFaaQ0nwg4wTc1c9Y5O/edit
- Jogo (Jornada da Jubarte): https://docs.google.com/document/d/1igb_MoMLjK2oS5VPw2wfa7qSldol9EYLnljaJB5DYq0/edit

## Como a skill conduz esta etapa

1. Leia o relatório de contexto (ou pergunte por ele). Quando uma pergunta do guia de requisitos já tiver sido respondida na contextualização, mostre a resposta registrada e peça ao professor que confirme ou atualize, em vez de perguntar do zero.
2. **Faça ao professor todas as perguntas do guia**, bloco por bloco e na ordem: didático-pedagógicos, funcionalidade, interface gráfica, disponibilidade, acessibilidade, acesso, desempenho, portabilidade, licenciamento e direitos, e reúso. Nenhuma pergunta é pulada nem respondida pela skill; quando o professor não souber (por exemplo, número de alunos simultâneos ou sistema operacional), ofereça opções como sugestão, explique em linguagem simples e registre como questão em aberto se continuar sem resposta. Mostre o progresso por bloco. As perguntas técnicas que o professor não domina podem ser encaminhadas ao designer técnico, mas ficam registradas no documento.
3. Para cada objetivo pedagógico, proponha requisitos pedagógicos e **transforme-os em requisitos funcionais testáveis** — este é o maior desafio apontado pelo próprio livro. Todo exemplo e todo requisito precisa ser coerente com a teoria de aprendizagem registrada na contextualização (`alinhamento-pedagogico.md`). Em jogos e atividades gamificadas, use sempre `diretrizes-sociointeracionistas.md` (D1–D40) e indique a diretriz de origem de cada RF.
4. **Acessibilidade com Desenho Universal**, em quatro camadas (separe sempre):
   - premissa de Desenho Universal (`desenho-universal.md`): o OA é desenhado para todas as pessoas; os requisitos cobrem todas as dimensões da matriz de necessidades que se aplicam ao tipo de OA, e não um único público;
   - dispositivos e plataformas (pergunta de portabilidade/disponibilidade);
   - necessidades da turma registradas na contextualização e co-designers com perfis diversos (papel Usuário, equipe de acessibilidade);
   - conjunto de diretrizes e nível-alvo: WCAG (AA como meta comum) ou e-MAG para web e cursos EaD; MobileDU para apps; RPG-DU para jogos. Se as skills `wcag-sem-complicacao`, `mobiledu-diretrizes` ou `rpg-du-diretrizes` estiverem disponíveis, use-as para gerar os requisitos de acessibilidade.
   Cada RA informa a quem serve (dimensão da matriz), o princípio do DU e a diretriz de origem. Os requisitos pedagógicos também seguem o DU: mais de uma forma de apresentar o conteúdo, de participar e de mostrar o que aprendeu. Leitor de tela e teclado são um item entre vários; um conjunto de RA que só atende pessoas cegas está incompleto.
5. Entregue o **documento de especificação de requisitos** com identificadores: RP-xx (pedagógicos), RF-xx (funcionais), RNF-xx (não funcionais), RA-xx (acessibilidade). Cada RF/RA com origem (objetivo, diretriz ou critério) e **critério de aceite**. Inclua um anexo com **todas as perguntas do guia e as respostas do professor**, indicando a origem de cada resposta.
   **Ética e privacidade:** gere requisitos RNF-ET (sem dark patterns, coleta mínima, LGPD e, para crianças e adolescentes, ECA Digital), cada um com critério de aceite, conforme `desenho-etico.md`. **Tecnologia:** nos requisitos de portabilidade e disponibilidade, proponha plataformas gratuitas (`tecnologias-gratuitas.md`).
6. Antes de entregar, confira: todas as perguntas foram feitas? Alguma resposta foi escrita pela skill sem confirmação? Os RA cobrem todas as dimensões da matriz que se aplicam? Liste as questões em aberto e as decisões que dependem do demandante.
