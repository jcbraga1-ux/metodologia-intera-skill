# Extensão da Metodologia Intera para jogos educacionais

Um jogo educacional é tratado como OA. A extensão mantém as 9 etapas da Intera 2.0 e adapta papéis, entradas, práticas e saídas. Recomenda-se iniciar pela Contextualização e terminar pela Avaliação, com ida e volta entre etapas.

Fontes: site Intera › Metodologia INTERA para Jogos (papéis, etapas, artefatos), consultado em 31/10/2026; livro *Metodologia Intera 2.0*, caps. 5 e 6.

## Tétrade e acessibilidade

As etapas se relacionam com a tétrade elemental de Schell: **narrativa, mecânica, tecnologia e estética**, mais **acessibilidade** em todas as etapas. Em Teste e Qualidade, Disponibilização, Avaliação e Gestão de Projetos todos os elementos têm peso igual.

## Papéis

Todos os papéis da Intera 2.0 (ver SKILL.md) e mais:

| Papel | Descrição (livro, cap. 1 Quadro 2, e site) |
| --- | --- |
| Designer de jogos (game designer) | Define pontuação, vidas, requisitos do sistema; ajuda a escolher o gênero, elementos do cenário e regras; facilita o trabalho dos outros papéis |
| Designer de som | Escolhe e cria os sons do jogo |
| Ilustrador | Produz as ilustrações e elementos visuais |
| Equipe de vídeo | Produz ou prepara vídeos do jogo, inclusive traduções em Libras |
| Designer líder | Papel listado no site (pode ser acumulado pelo ilustrador ou designer de jogos) |
| Level designer | Papel listado no site (idem) |
| Diretor de arte | Papel listado no site (idem) |
| Equipe de acessibilidade (jogos) | Profissionais de Libras, audiodescritores etc.; pensam sempre no Design Universal |

No projeto Expedição Antártica (cap. 6) atuaram também co-designers cegos e surdos, audiodescritor, tradutores de Libras e editor/produtor de vídeo.

## Entradas, práticas e saídas por etapa (site)

| Etapa | Entradas | Práticas | Saídas |
| --- | --- | --- | --- |
| Contextualização | Livros, revistas, artigos; informações sobre os jogadores; objetivos pedagógicos; guia de contextualização; cenário de uso | Entrevistas com possíveis jogadores e com as equipes; preenchimento do guia | Relatório dos dados colhidos; guia preenchido |
| Requisitos | Guia de contextualização preenchido; guia de requisitos; wireframe; arquitetura da narrativa | Análise da contextualização; reuniões com conteúdo e desenvolvimento; diagramas de atividades; casos de uso; casos de teste | Especificação de requisitos; casos de uso; decupagem |
| Arquitetura | Documento das missões; documento dos diálogos; wireframe; especificação de requisitos; relatório e guia de contextualização | Reuniões entre equipes; modelagem do jogo | GDD; pré-roteiro; arquitetura do jogo; fluxo de telas; wireframe; protocolos de testes |
| Desenvolvimento | GDD; pré-roteiro; fluxo de telas; casos de uso; wireframe; contextualização; requisitos; arquitetura | Elementos estéticos; narrativa; desenvolvimento do jogo | Sprites; cenários; elementos sonoros; narrativa; jogo; prática pedagógica; manual do professor; instalador com jogo, manuais e metadados; direitos autorais e patrimoniais |
| Teste e Qualidade | Plano de testes; protocolos; questionários; casos de teste | Testes de defeitos, usabilidade, jogabilidade, acessibilidade e conteúdo | Relatórios consolidados; evidências de testes |
| Disponibilização | Manuais de instalação, do professor e do aluno | Depósito do jogo em repositório | Jogo disponível |
| Avaliação | Jogo; manuais; instalação; práticas pedagógicas; curso; plano de avaliação | Questionário pré e pós | Análise da avaliação |
| Gestão de Projetos | Requisitos; contextualização; edital do projeto | Cronograma; estimativas; reuniões | Cronograma; custos e prestação de contas; alocação de pessoas; relatório de bolsista; formulário post-mortem |
| Ambiente e Padrões | — | Controle do ambiente técnico (versões, backups) | — |

## Acessibilidade em jogos (lições do cap. 6)

- Acessibilidade para pessoas cegas e com baixa visão entra **desde o início**, porque está no código (navegação por teclado, mapa de teclas, leitor de tela, contraste, customização).
- Libras e audiodescrição entram **depois** que as telas estão testadas, para não refazer gravações.
- Não usar avatares de tradução automática para Libras; usar intérpretes.
- Artefatos novos: glossário em Libras, requisitos de acessibilidade por público, caso de uso acessível, mapa de teclas, roteiro de gravação em Libras, fluxo de teste para Design Universal.
- O analista é papel crítico; os testes das equipes dependem uns dos outros.
- Para diretrizes de Design Universal em jogos RPG, use a skill `rpg-du-diretrizes` (88 diretrizes, Cunha 2022), se disponível.

## Validação da extensão para jogos (artigo do grupo)

Fonte: MELLE, L. F. O.; BRAGA, J. C.; PIMENTEL, E. P.; DOTTA, S. C.; FREIBERGER-AFFONSO, S.; DOMINGUES, F. U.; KARRAS, D. P. *Metodologia INTERA ampliada e validada para o desenvolvimento de jogos educacionais* (capítulo 5, disponível no site Intera › Metodologia INTERA para Jogos › Artigo, consultado em 01/11/2026).

**Por que um jogo educacional pede mais cuidado:** comparado a um software comum, o jogo tem mecânica e narrativa, e a estética é essencial; o jogo educacional soma a isso os **elementos pedagógicos**, que são o desafio adicional de qualidade.

**Como a extensão foi construída:** (1) revisão sistemática com 13 metodologias de jogos sérios (nenhuma tratava acessibilidade de forma direta, só 4 previam a participação do jogador e a maioria planejava apenas no início); (2) incorporação à Intera do que faltava: narrativa, mecânica, estética, participação do jogador e papéis de jogos; (3) estudo de campo qualitativo de 18 meses com o *Expedição Antártica* (RPG, cerca de 40 pessoas na equipe, incluindo pessoas cegas, surdas e com deficiência cognitiva).

**O que mudou na metodologia para jogos:** fases renomeadas para pré-produção, produção e pós-produção; papéis de ilustrador, designer de som, usuários, designer de jogos, equipe de vídeo e equipe de acessibilidade (audiodescritor, tradutor de Libras); artefatos de GDD, vídeos em Libras, texto de audiodescrição, arquivos de som, caso de uso acessível, glossário em Libras e diálogos dos personagens; e, em cada etapa, como a tétrade e a acessibilidade aparecem.

**Validação com o *Jornada Jubarte*** (corrida infinita sobre a migração das baleias-jubarte entre a Antártica e o Brasil, para crianças de 7 a 12 anos, base vigotskiana, projeto InterAntar/CNPq):
- A equipe acumulou papéis, mas cada papel tinha alguém responsável. O próprio grupo registra como **limitação** a ausência de usuários desde o início e de equipe de acessibilidade.
- O guia de contextualização ajudou a manter o foco pedagógico: durante a produção, a equipe voltava a ele para conferir se os objetivos estavam sendo cumpridos.
- Os requisitos funcionais (migrar, amamentar o filhote, fugir das orcas, alimentar-se de krill) foram derivados das diretrizes sociointeracionistas (desafios de resolução de problemas, transposição de conceitos, interação com objetos do cenário, papel ativo do jogador, linguagem acessível).
- Na arquitetura, GDD e protótipo (artefatos da área de jogos, fortemente recomendados pela Intera), começando pelo *high concept*, gênero e público.
- Testes com 12 pessoas que **não** eram do público-alvo (75% de satisfação geral); o grupo registra isso como limitação e indica que a aprendizagem ainda precisa ser avaliada com crianças. Tipos de teste recomendados para jogos: funcionalidade, acessibilidade, confiabilidade técnica, usabilidade/jogabilidade e validação/aceitação.

**Como a skill usa isso:** ao montar a matriz de papéis de um jogo, aponte explicitamente a falta de usuários do público-alvo e de equipe de acessibilidade como risco (a própria validação do grupo mostra o efeito); ao final de cada etapa, compare o artefato com os objetivos do guia de contextualização; e não trate satisfação de testadores como evidência de aprendizagem.

## Exemplos de jogos do grupo Intera

- ***O Mistério da Iluminária*** (RPG sobre energia e problemas socioambientais, com base na educação ambiental crítica; Nishida, Braga, Monteforte e Benassi; UAB/Capes; 2º lugar na Mostra de Software do CBIE 2014). Página: https://www.interaufabc.com.br/jogos-educacionais. Do ponto de vista do reúso, observe que o instalador é um .exe para Windows hospedado em serviço de terceiros: isso limita a portabilidade e a durabilidade, duas das dificuldades de reúso descritas em `reuso-e-rea.md`.
- ***Expedição Antártica*** (RPG com ciência cidadã, desenvolvido com co-designers com deficiência) e ***Jornada Jubarte*** (corrida infinita), descritos acima.

## Guia para o documento de game design (GDD)

Modelo: https://docs.google.com/document/d/105q2GiSmPaFgAhsXC67-aagzY4DZAokb/edit · Exemplos (pasta): https://drive.google.com/drive/folders/1PZsP2wQRFXGqS0XF2uIqT1IM4rdWGRbN

1. **Gênero:** ação, adivinhação, aventura, corrida, estratégia, puzzle, quiz, RPG, roll-and-move, simulação (pode combinar ou usar outra classificação).
2. **Plataforma:** desktop, rede, console, dispositivos móveis.
3. **Interação:** singleplayer, multiplayer, multigrupos.
4. **Regras:** restrições que orientam o jogador; nem complexas demais, nem simples demais.
5. **Mecânica:** ações do personagem e como são executadas (ex.: teclado para correr, saltar).
6. **Narrativa:** enredo, época, lugar, relações entre personagens; linear ou não linear; interativa ou não (ferramenta sugerida: Twine).
7. **Elementos da narrativa:** personagens (nome, tipo — jogador, adversário, máquina — e ações), artefatos (objetos com que o jogador interage e que valem pontos), cenários.

Referência do guia: ROGERS, S. *Level Up: um guia para o design de grandes jogos*.

**Como a skill conduz:** em todo jogo, sugira sempre criar o GDD. Conduza o professor passo a passo, uma seção por vez, na ordem do guia acima, e preencha a partir da contextualização e dos requisitos. Se o professor já trouxer um GDD, analise-o criticamente: alinhamento à teoria declarada e às diretrizes D1–D40, Desenho Universal, dark patterns, coerência com os requisitos. Proponha melhorias antes de seguir para o protótipo (`prototipo-e-desenvolvimento.md`). Em ambos os casos, ao final, faça uma checagem de consistência: público e idade iguais em todo o documento; personagens e NPCs com os mesmos nomes; número de níveis × progressão de desafio; regras de pontuação que fecham (máximo, descontos); cada requisito aparece em alguma mecânica ou tela; acessibilidade prevista em cada elemento da tétrade.

## Diretrizes sociointeracionistas

Em todos os jogos, use `diretrizes-sociointeracionistas.md` (D1–D40) para transformar objetivos pedagógicos em funcionalidades, conferindo a coerência com a teoria declarada (`alinhamento-pedagogico.md`). Mecânicas, recompensas e progressão também passam pela checagem de dark patterns de `desenho-etico.md`; caixas de recompensa são proibidas em jogos para crianças e adolescentes. Para escolher a ferramenta de desenvolvimento, veja `tecnologias-gratuitas.md`.

## Artefatos publicados (site › Artefatos Jogos)

| Etapa | Guia | Exemplo |
| --- | --- | --- |
| Contextualização | https://docs.google.com/document/d/12aRjA62LQdTkzgl6hKg8A-Ls-X5pzNwKDQFtP7lMS6k/edit | https://docs.google.com/document/d/1xMk0R9BXLhYFP4dsAMGlzfS0xd4usZ0uP01mPvFlgRc/edit |
| Requisitos | (o link do site aponta para o guia de aulas síncronas; use `guia-requisitos.md`) | https://docs.google.com/document/d/1igb_MoMLjK2oS5VPw2wfa7qSldol9EYLnljaJB5DYq0/edit |
| Arquitetura (GDD) | https://docs.google.com/document/d/105q2GiSmPaFgAhsXC67-aagzY4DZAokb/edit | https://drive.google.com/drive/folders/1PZsP2wQRFXGqS0XF2uIqT1IM4rdWGRbN |
| Desenvolvimento | https://drive.google.com/drive/u/0/folders/1YFdpVTBWcaOFiomIA3vIWG5vTEAdcOuJ | idem |
| Gestão de Projetos | https://drive.google.com/drive/u/0/folders/1A_aYlTaIg_7nlK2bfnzjHRkuy60g2Czq | idem |
