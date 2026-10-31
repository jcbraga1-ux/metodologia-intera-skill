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

**Como a skill conduz:** preencha o GDD por seções a partir da contextualização e dos requisitos e, ao final, faça uma checagem de consistência: público e idade iguais em todo o documento; personagens e NPCs com os mesmos nomes; número de níveis × progressão de desafio; regras de pontuação que fecham (máximo, descontos); cada requisito aparece em alguma mecânica ou tela; acessibilidade prevista em cada elemento da tétrade.

## Diretrizes sociointeracionistas

Para transformar objetivos pedagógicos de base vigotskiana em funcionalidades do jogo, use `diretrizes-sociointeracionistas.md` (D1–D40).

## Artefatos publicados (site › Artefatos Jogos)

| Etapa | Guia | Exemplo |
| --- | --- | --- |
| Contextualização | https://docs.google.com/document/d/12aRjA62LQdTkzgl6hKg8A-Ls-X5pzNwKDQFtP7lMS6k/edit | https://docs.google.com/document/d/1xMk0R9BXLhYFP4dsAMGlzfS0xd4usZ0uP01mPvFlgRc/edit |
| Requisitos | (o link do site aponta para o guia de aulas síncronas; use `guia-requisitos.md`) | https://docs.google.com/document/d/1igb_MoMLjK2oS5VPw2wfa7qSldol9EYLnljaJB5DYq0/edit |
| Arquitetura (GDD) | https://docs.google.com/document/d/105q2GiSmPaFgAhsXC67-aagzY4DZAokb/edit | https://drive.google.com/drive/folders/1PZsP2wQRFXGqS0XF2uIqT1IM4rdWGRbN |
| Desenvolvimento | https://drive.google.com/drive/u/0/folders/1YFdpVTBWcaOFiomIA3vIWG5vTEAdcOuJ | idem |
| Gestão de Projetos | https://drive.google.com/drive/u/0/folders/1A_aYlTaIg_7nlK2bfnzjHRkuy60g2Czq | idem |
