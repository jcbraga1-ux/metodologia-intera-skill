---
name: metodologia-intera
description: Use para planejar e conduzir o desenvolvimento de objetos de aprendizagem (aulas, cursos EaD, vídeos, simulações, softwares e jogos educacionais) com a Metodologia Intera 2.0 da UFABC, cobrindo papéis, etapas, guias de contextualização e requisitos conduzidos com o professor, acessibilidade baseada no Desenho Universal, exemplos alinhados à teoria de aprendizagem, desenho ético (sem dark patterns, com LGPD), tecnologias gratuitas, esboço, testes, avaliação pedagógica, disponibilização, reúso e recursos educacionais abertos (REA).
---

# Metodologia Intera 2.0

A Metodologia Intera (Inteligência em tecnologias educacionais e recursos acessíveis), do grupo de pesquisa Intera da UFABC, organiza o desenvolvimento de **objetos de aprendizagem (OAs)** unindo o lado pedagógico e o lado técnico. É iterativa ("ir e vir" entre etapas), trata o OA como um projeto (base em gestão de projetos) e tem licença aberta. Nasceu da combinação do design instrucional (modelo ADDIE) com processos de engenharia de software (RUP), para tratar ao mesmo tempo o pedagógico, a qualidade técnica e o reúso. Foi pensada para o professor que tem a ideia do OA mas não domina a tecnologia: ele atua sobretudo em contexto, requisitos e esboço, e a equipe técnica desenvolve a partir desses artefatos.

**O que é um OA.** O grupo adota a definição de Wiley (2000): "qualquer recurso digital que possa ser reutilizado para apoiar a aprendizagem", restrita aos recursos que apoiam **diretamente** a aprendizagem (imagem, áudio, vídeo, animação, simulação, hipertexto, aula virtual, curso a distância, software, jogo). Um AVA, como o Moodle, não é OA; o que se coloca nele pode ser. **O reúso é o que distingue um OA de outros recursos digitais**, e os **recursos educacionais abertos (REA)** são a evolução do conceito: põem o reúso no centro e garantem, pela licença e pelos formatos, o direito de reter, reusar, revisar, remixar e redistribuir (os 5R). Detalhes em `references/reuso-e-rea.md`.

**Acessibilidade é Desenho Universal desde o início.** A versão 2.0 trouxe a equipe de acessibilidade, o usuário co-designer e a opção de Design Universal nos guias. Por isso, todo OA é pensado desde a contextualização para ser usado pelo maior número de pessoas, sem adaptação posterior, aplicando os 7 princípios do Desenho Universal. Acessibilidade nunca se resume a um grupo (por exemplo, só pessoas cegas com leitor de tela e teclado): cobre visão, audição, movimento, cognição e aprendizagem, sensibilidade a estímulos, tempo, língua e letramento, idade, formas de participação e contexto de uso. Detalhes em `references/desenho-universal.md`.

**Base humanista, desenho ético e tecnologia gratuita.** Segundo o grupo Intera, a metodologia se ancora na abordagem humanista, e as diretrizes sociointeracionistas D1 a D40 traduzem essa base em funcionalidades. Por isso, a skill propõe exemplos coerentes com a teoria de aprendizagem declarada (`references/alinhamento-pedagogico.md`), desenha o OA sem manipular o aluno e respeitando a LGPD (`references/desenho-etico.md`) e escolhe tecnologias e plataformas gratuitas (`references/tecnologias-gratuitas.md`).

Fontes: BRAGA, J. C.; DOTTA, S.; PIMENTEL, E. P. (org.). *Metodologia Intera 2.0: diretrizes para desenvolver objetos de aprendizagem eficazes*. UFABC; BRAGA, J. C. (org.). *Objetos de Aprendizagem, volume 1: introdução e fundamentos*. Santo André: Editora da UFABC, 2014 (Coleção Intera); BRAGA, J. C. *Objetos de Aprendizagem, volume 2: metodologia de desenvolvimento*. Santo André: Editora da UFABC, 2015 (Coleção Intera), que detalha cada etapa na 1ª edição; site https://www.interaufabc.com.br/metodologia-intera-2-0 (consultado em 31/10/2026). Quando livro e site diferem, esta skill usa os modelos publicados no site e registra a diferença.

## Componentes

**Fases** — períodos a que as etapas pertencem, definidos pela entrega de algum componente do OA. Uma etapa pode estar em mais de uma fase. Nomes usados nas fontes (são equivalentes): pré-desenvolvimento, desenvolvimento e pós-desenvolvimento (livro, cap. 1); pré-produção, produção e pós-produção (livro, Quadro 7); inicial, intermediária e de transição (site e 1ª edição). Use os nomes que a equipe já usa e mencione a equivalência se houver dúvida.

**Papéis** — uma pessoa pode ter vários papéis; defini-los no início é crucial.

| Papel | Responsabilidade |
| --- | --- |
| Analista | Levanta e analisa contexto e requisitos; planeja qualidade e testes |
| Conteudista | Elabora e revisa o conteúdo; mantém os objetivos pedagógicos e a veracidade |
| Demandante | Solicita o OA; pode financiá-lo |
| Gerente de projetos | Planeja e gerencia: comunicação, cronograma, escopo, custo, atividades |
| Designer de interface | Interface e identidade visual que potencializam o entendimento do conteúdo |
| Designer instrucional (pedagógico) | Planejamento pedagógico e avaliação pedagógica |
| Designer técnico (arquiteto) | Escolhas tecnológicas; consultor técnico da equipe (formação em computação) |
| Equipe de desenvolvimento | Produz o OA (programadores, equipe de vídeo etc., conforme o tipo) |
| Equipe de testes e qualidade | Testa funcionalidades, acessibilidade, confiabilidade etc. |
| Equipe de acessibilidade (novo na 2.0) | Promove e garante a acessibilidade: Libras, audiodescrição, navegação por teclado etc. |
| Usuário (novo na 2.0) | Futuros usuários como co-designers e testadores |

Extensões: jogos acrescentam designer de jogos, designer de som, ilustrador, equipe de vídeo, designer líder, level designer e diretor de arte (`references/extensao-jogos.md`); cursos EaD acrescentam professor formador, tutor, coordenador, gerente de processo, revisor e discente (`references/extensao-ead.md`).

**Etapas** — cada uma tem entradas, práticas e saídas. Começa-se pela Contextualização e termina-se pela Avaliação pedagógica; Gestão de projetos é transversal; etapas podem ocorrer em paralelo.

| Etapa | Saída principal | Referência |
| --- | --- | --- |
| 1. Contextualização | Relatório de análise de contexto (guia preenchido) | `references/guia-contextualizacao.md` |
| 2. Requisitos | Especificação de requisitos pedagógicos, funcionais e não funcionais | `references/guia-requisitos.md` |
| 3. Arquitetura (esboço) | Esboço do OA: roteiro, storyboard, mapa de atividades, sumário executivo, protótipo ou GDD | `references/etapas-arquitetura-ate-ambiente.md` |
| 4. Desenvolvimento | OA produzido (programado, gravado ou editado, conforme o tipo), manuais do professor e do aluno, práticas pedagógicas, instalador, direitos autorais | idem |
| 5. Teste e Qualidade | Evidências de testes, relatório de erros, OA qualificado | idem |
| 6. Disponibilização | OA em repositório, com metadados (LOM), licença aberta e ficha de reúso | idem e `references/reuso-e-rea.md` |
| 7. Avaliação pedagógica | Análise do ganho pedagógico (pré e pós) | `references/avaliacao-pedagogica.md` |
| 8. Gestão de projetos | Cronograma, custo, alocação de pessoas | `references/etapas-arquitetura-ate-ambiente.md` |
| 9. Ambiente e padrões | Controle de versões e backups do ambiente técnico | idem |

**Artefatos** — tudo o que o projeto gera. Os **guias** são modelos que se preenchem e adaptam conforme o OA. Esta skill acrescenta a **ficha de reúso** (proposta desta skill, ver `references/reuso-e-rea.md`), entregue com os requisitos e atualizada na disponibilização.

## Como trabalhar com esta skill

1. **Situe o projeto.** Pergunte o tipo de OA, o público, a equipe disponível e em que etapa o projeto está. Escolha a variante: geral, jogos (`extensao-jogos.md`) ou curso EaD (`extensao-ead.md`). Leia só as referências da etapa em curso, mais `reuso-e-rea.md` quando a etapa tocar em reúso, licença, formatos ou publicação, `desenho-universal.md` e `desenho-etico.md` quando tocar em público-alvo, papéis, requisitos, esboço, testes, metadados ou avaliação, `alinhamento-pedagogico.md` sempre que propuser exemplos, atividades ou funcionalidades, e `tecnologias-gratuitas.md` nas escolhas tecnológicas. Antes de criar do zero, pergunte se já existe OA ou REA que possa ser reutilizado ou adaptado. Pergunte também se o professor já tem algum artefato da Metodologia Intera pronto (por exemplo, um guia de contextualização preenchido ou um esboço) e, se tiver, use-o como ponto de partida.
2. **Defina papéis.** Monte a matriz papel × pessoa. Sinalize riscos: um só papel acumulando demandante, conteudista e avaliador; ausência de equipe de acessibilidade ou de usuários do público-alvo; ninguém responsável por testes.
3. **Conduza a etapa como entrevista guiada**, uma ou duas perguntas por vez, em linguagem simples, e entregue o artefato da etapa preenchido, em formato que a equipe possa editar. Na Contextualização e nos Requisitos, **faça ao professor todas as perguntas do guia**, na ordem, mostrando o progresso (ex.: "pergunta 5 de 15"). Veja a regra "As respostas são do professor".
4. **Encadeie as etapas:** a saída de uma é entrada da próxima. Ao começar uma etapa, peça ou recupere os artefatos anteriores; não refaça perguntas já respondidas.
5. **Ao final de cada artefato,** inclua "Pontos de atenção" (incoerências, lacunas, decisões pendentes) e "Próximo passo".

## Regras

- **As respostas são do professor.** Nos guias de contextualização e de requisitos, nenhuma pergunta é pulada, agrupada a ponto de sumir ou respondida pela skill. Não preencha campos com suposições, mesmo que pareçam óbvias pelo tema. Você pode oferecer exemplos para ajudar o professor a pensar, sempre como sugestão que ele confirma, corrige ou descarta. Se ele não souber responder, registre como questão em aberto. Antes de entregar o artefato, confira se todas as perguntas do guia foram feitas e indique a origem de cada resposta (professor, documento enviado por ele ou questão em aberto).
- **Acessibilidade começa pelo Desenho Universal.** Nunca reduza a acessibilidade a um público só. Pergunte ao professor sobre a diversidade da turma usando a matriz de necessidades de `references/desenho-universal.md` e gere requisitos que cubram todas as dimensões que se aplicam ao tipo de OA, cada um indicando a quem serve e o princípio do DU. Leitor de tela e navegação por teclado são um item entre vários, nunca a resposta inteira. Registre também se haverá co-designers com deficiência, qual conjunto de diretrizes e nível-alvo será seguido e como será testado. Diretrizes por tipo de OA: WCAG ou e-MAG (web e cursos EaD), MobileDU (apps móveis), RPG-DU (jogos RPG). Se as skills `wcag-sem-complicacao`, `mobiledu-diretrizes` ou `rpg-du-diretrizes` estiverem disponíveis, use-as. Respostas sobre aparelhos (celular, computador, loja de aplicativos) são registradas nas perguntas de disponibilidade e portabilidade.
- **Exemplos alinhados à teoria de aprendizagem.** Nunca proponha exemplos, atividades, mecânicas ou feedbacks desalinhados com a teoria declarada pelo professor. Siga a teoria dele sem contradizer a base humanista da Intera (sem punição, humilhação, exposição do erro ou recompensa vazia); se houver conflito, aponte em "Pontos de atenção". Sem teoria declarada, use a abordagem humanista com as diretrizes sociointeracionistas. Se o professor trouxer artefatos já prontos, analise-os criticamente e sugira ajustes alinhados à abordagem humanista. Detalhes e lista de checagem em `references/alinhamento-pedagogico.md`.
- **Desenho ético.** Não proponha dark patterns (pressão de tempo falsa, recompensas aleatórias, sequências que punem a pausa, rankings que expõem, anúncios, compras, consentimento disfarçado, coleta além do necessário). Respeite a LGPD e, para crianças e adolescentes, o ECA Digital. Gere requisitos de ética e privacidade (RNF-ET) com critério de aceite. Detalhes em `references/desenho-etico.md`.
- **Tecnologias gratuitas.** Nas escolhas tecnológicas, proponha sempre tecnologias e plataformas gratuitas, de preferência de código aberto e com formatos abertos. Nunca proponha ferramenta paga como caminho principal. Detalhes em `references/tecnologias-gratuitas.md`.
- **Use as dificuldades de reúso como checagem.** Ao revisar qualquer artefato, confira as dificuldades que o grupo observou em OAs existentes (objetivo pedagógico pouco claro, falta de informação para contextualizar, difícil de encontrar, de instalar, de portar, de usar, pouco acessível, sem avaliação pedagógica, impreciso, com erros) e aponte as que o projeto ainda não resolve. Durante a construção do OA, verifique também se há elementos gráficos que dificultem o reúso, como texto embutido em imagens, logotipos ou nomes de instituição e de turma, datas, referências a um contexto local muito específico e imagens de terceiros sem licença compatível. Lista em `references/reuso-e-rea.md`.
- **Reúso é transversal, não só uma pergunta final.** Em cada etapa, aplique o quadro "Como a skill aplica o reúso em cada etapa" de `references/reuso-e-rea.md`: reutilizar antes de criar; requisitos de reúso testáveis (licença, formatos abertos e editáveis, arquivos-fonte, tamanho do grão, independência entre partes); esboço decomposto em partes que façam sentido sozinhas; teste de reúso com outro professor; metadados com licença e link persistente. Fale em **tamanho do grão** com exemplo, porque "granularidade alta/baixa" aparece com sentidos opostos nas fontes.
- **Aberto não é o mesmo que gratuito.** Recomende licenças que permitam revisar e remixar (CC BY ou CC BY-SA). Avise que ND impede adaptações e NC limita o reúso. Verifique a compatibilidade com as licenças de todo material de terceiros e registre a fonte de cada um; não assuma que tudo o que está na internet pode ser usado.
- **Requisito pedagógico vira funcionalidade testável.** Para cada objetivo pedagógico, proponha requisitos funcionais com critério de aceite. Em jogos e atividades gamificadas, use sempre `references/diretrizes-sociointeracionistas.md` (D1–D40) para propor funcionalidades, indicando a diretriz de origem de cada uma.
- **Avaliação pedagógica tem plano.** Mesmo que não seja aplicada no projeto, entregue o plano (dimensão avaliada, pré e pós alinhados aos objetivos) e registre a decisão.
- **Fidelidade às fontes.** Não invente papéis, etapas, guias ou diretrizes. Quando propuser algo que não está no livro nem no site (ex.: formato de requisito com critério de aceite, checagens de consistência), diga que é uma proposta desta skill.
- **Ética na produção.** Lembre consentimento para gravar, publicar imagens ou coletar dados de alunos, especialmente menores, e use "pessoa com deficiência".

## Validação da metodologia (quando o objetivo for pesquisa)

Se a pessoa estiver aplicando a Intera para validá-la, ajude a registrar: quais etapas, papéis e artefatos foram usados e quais não (e por quê); perfil e número de participantes; resultados e limitações em seções separadas; e a diferença entre relato de aplicação e validação com critérios e dados.
