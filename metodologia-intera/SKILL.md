---
name: "metodologia-intera"
description: "Use para planejar e conduzir o desenvolvimento de objetos de aprendizagem (aulas, cursos EaD, vídeos, simulações, softwares e jogos educacionais) com a Metodologia Intera 2.0 da UFABC: papéis, etapas, guias de contextualização e requisitos, esboço, testes, avaliação pedagógica e disponibilização."
---

# Metodologia Intera 2.0

A Metodologia Intera (Inteligência em tecnologias educacionais e recursos acessíveis), do grupo de pesquisa Intera da UFABC, organiza o desenvolvimento de **objetos de aprendizagem (OAs)** — qualquer conteúdo digital reutilizável para aprendizagem, de uma aula virtual a um jogo — unindo o lado pedagógico e o lado técnico. É iterativa ("ir e vir" entre etapas), trata o OA como um projeto (base em gestão de projetos) e tem licença aberta.

Fontes: BRAGA, J. C.; DOTTA, S.; PIMENTEL, E. P. (org.). *Metodologia Intera 2.0: diretrizes para desenvolver objetos de aprendizagem eficazes*. UFABC; site https://www.interaufabc.com.br/metodologia-intera-2-0 (consultado em 31/10/2026). Quando livro e site diferem, esta skill usa os modelos publicados no site e registra a diferença.

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
| 4. Desenvolvimento | OA, manuais do professor e do aluno, práticas pedagógicas, instalador, direitos autorais | idem |
| 5. Teste e Qualidade | Evidências de testes, relatório de erros, OA qualificado | idem |
| 6. Disponibilização | OA em repositório, com metadados (LOM) | idem |
| 7. Avaliação pedagógica | Análise do ganho pedagógico (pré e pós) | `references/avaliacao-pedagogica.md` |
| 8. Gestão de projetos | Cronograma, custo, alocação de pessoas | `references/etapas-arquitetura-ate-ambiente.md` |
| 9. Ambiente e padrões | Controle de versões e backups do ambiente técnico | idem |

**Artefatos** — tudo o que o projeto gera. Os **guias** são modelos que se preenchem e adaptam conforme o OA.

## Como trabalhar com esta skill

1. **Situe o projeto.** Pergunte o tipo de OA, o público, a equipe disponível e em que etapa o projeto está. Escolha a variante: geral, jogos (`extensao-jogos.md`) ou curso EaD (`extensao-ead.md`). Leia só as referências da etapa em curso.
2. **Defina papéis.** Monte a matriz papel × pessoa. Sinalize riscos: um só papel acumulando demandante, conteudista e avaliador; ausência de equipe de acessibilidade ou de usuários do público-alvo; ninguém responsável por testes.
3. **Conduza a etapa como entrevista guiada**, uma ou duas perguntas por vez, em linguagem simples, e entregue o artefato da etapa preenchido, em formato que a equipe possa editar.
4. **Encadeie as etapas:** a saída de uma é entrada da próxima. Ao começar uma etapa, peça ou recupere os artefatos anteriores; não refaça perguntas já respondidas.
5. **Ao final de cada artefato,** inclua "Pontos de atenção" (incoerências, lacunas, decisões pendentes) e "Próximo passo".

## Regras

- **Acessibilidade não é dispositivo.** "Celular e computador", "Play Store" ou "na internet" respondem a disponibilidade/portabilidade. Acessibilidade exige: quais públicos com deficiência, se haverá co-designers com deficiência, qual conjunto de diretrizes e nível-alvo, e como será testado. Diretrizes por tipo de OA: WCAG ou e-MAG (web e cursos EaD), MobileDU (apps móveis), RPG-DU (jogos RPG). Se as skills `wcag-sem-complicacao`, `mobiledu-diretrizes` ou `rpg-du-diretrizes` estiverem disponíveis, use-as.
- **Requisito pedagógico vira funcionalidade testável.** Para cada objetivo pedagógico, proponha requisitos funcionais com critério de aceite. Para jogos de base sociointeracionista, use `references/diretrizes-sociointeracionistas.md` (D1–D40).
- **Avaliação pedagógica tem plano.** Mesmo que não seja aplicada no projeto, entregue o plano (dimensão avaliada, pré e pós alinhados aos objetivos) e registre a decisão.
- **Fidelidade às fontes.** Não invente papéis, etapas, guias ou diretrizes. Quando propuser algo que não está no livro nem no site (ex.: formato de requisito com critério de aceite, checagens de consistência), diga que é uma proposta desta skill.
- **Ética.** Lembre consentimento para gravar, publicar imagens ou coletar dados de alunos, especialmente menores, e use "pessoa com deficiência".

## Validação da metodologia (quando o objetivo for pesquisa)

Se a pessoa estiver aplicando a Intera para validá-la, ajude a registrar: quais etapas, papéis e artefatos foram usados e quais não (e por quê); perfil e número de participantes; resultados e limitações em seções separadas; e a diferença entre relato de aplicação e validação com critérios e dados.
