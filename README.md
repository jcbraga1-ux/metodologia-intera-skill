# Metodologia Intera 2.0 – Skill

Agent Skill que conduz o desenvolvimento de **objetos de aprendizagem** (aulas, cursos a distância, vídeos, simulações, softwares e jogos educacionais) com a **Metodologia Intera 2.0**, do grupo de pesquisa Intera da Universidade Federal do ABC (UFABC). Funciona com assistentes de IA compatíveis com o padrão aberto [Agent Skills](https://agentskills.io/).

## O que a skill faz

- **Situa o projeto:** identifica o tipo de objeto, a etapa em que ele está e a variante da metodologia (geral, jogos ou cursos EaD).
- **Define papéis:** monta a matriz papel × pessoa e aponta riscos, como a falta de equipe de acessibilidade.
- **Conduz os guias como entrevista:** contextualização, requisitos, esboço, testes, avaliação pedagógica, disponibilização e gestão, entregando cada artefato preenchido com pontos de atenção.
- **Transforma requisitos pedagógicos em funcionalidades testáveis**, inclusive com as diretrizes sociointeracionistas D1–D40 para jogos.
- **Coloca o reúso no centro:** reutiliza antes de criar, escreve requisitos de reúso, orienta sobre recursos educacionais abertos (REA), os 5R e licenças Creative Commons, e entrega uma ficha de reúso.
- **Conduz os guias com o professor:** faz todas as perguntas dos guias de contextualização e de requisitos, sem responder por ele, e registra as questões em aberto.
- **Parte do Desenho Universal desde o início:** a acessibilidade cobre visão, audição, movimento, cognição e aprendizagem, língua e letramento, entre outras dimensões, e não um único público.
- **Propõe exemplos alinhados à teoria de aprendizagem**, sem contradizer a base humanista da Intera, e usa as diretrizes sociointeracionistas D1–D40 em jogos e atividades gamificadas.
- **Cuida do desenho ético:** evita dark patterns e segue a LGPD e, para crianças e adolescentes, o ECA Digital.
- **Escolhe tecnologias gratuitas**, de preferência de código aberto.
- **Trata acessibilidade com diretrizes** e trabalha junto com as skills [WCAG sem complicação](https://github.com/jcbraga1-ux/wcag-sem-complicacao-skill), [MobileDU](https://github.com/jcbraga1-ux/mobiledu-skill) e [RPG-DU](https://github.com/jcbraga1-ux/rpg-du-skill).

## Conteúdo

```
metodologia-intera/
├── SKILL.md                                   # papéis, fases, etapas, modo de uso e regras
└── references/
    ├── guia-contextualizacao.md               # guias geral e de jogos
    ├── guia-requisitos.md                     # guia de requisitos pedagógicos e técnicos
    ├── etapas-arquitetura-ate-ambiente.md     # esboço, desenvolvimento, testes, disponibilização, gestão
    ├── avaliacao-pedagogica.md                # plano de avaliação pré e pós
    ├── extensao-jogos.md                      # papéis, etapas e GDD para jogos
    ├── extensao-ead.md                        # processo BPM para cursos a distância
    ├── reuso-e-rea.md                         # definição de OA, reúso, REA, 5R, licenças, ficha de reúso
    ├── desenho-universal.md                   # acessibilidade desde o início: princípios do DU e matriz de necessidades
    ├── alinhamento-pedagogico.md              # base humanista, coerência dos exemplos com a teoria de aprendizagem
    ├── desenho-etico.md                       # dark patterns, LGPD e ECA Digital
    ├── tecnologias-gratuitas.md               # critérios e exemplos de ferramentas gratuitas
    └── diretrizes-sociointeracionistas.md     # D1–D40
```

## Como instalar

A skill é a pasta [`metodologia-intera/`](metodologia-intera/).

- **Claude e Gemini:** baixe o arquivo `metodologia-intera.zip` na página de [Releases](../../releases), em *Assets*, e envie sem mudar o nome do arquivo (o Gemini exige que o nome do .zip seja igual ao nome da skill). No Claude, envie em *Configurações › Capacidades › Skills*; no Gemini, na página de *Skills*, opção de enviar arquivo. O mesmo arquivo serve para os dois.
- **Ferramentas que leem skills de uma pasta (como Claude Code):** copie a pasta `metodologia-intera` para o diretório de skills da ferramenta (no Claude Code, `~/.claude/skills/`).

Depois de instalada, basta pedir em linguagem natural, por exemplo: *“Quero desenvolver um jogo de frações para o 6º ano usando a metodologia Intera.”*

## Fontes

- BRAGA, Juliana Cristina; DOTTA, Silvia; PIMENTEL, Edson Pinheiro (org.). **Metodologia Intera 2.0: diretrizes para desenvolver objetos de aprendizagem eficazes**. Santo André: UFABC.
- BRAGA, Juliana Cristina (org.). **Objetos de Aprendizagem, volume 1: introdução e fundamentos**. Santo André: Editora da UFABC, 2014. (Coleção Intera). ISBN 978-85-68576-03-8.
- BRAGA, Juliana Cristina. **Objetos de Aprendizagem, volume 2: metodologia de desenvolvimento**. Santo André: Editora da UFABC, 2015. (Coleção Intera). ISBN 978-85-68576-04-5.
- Site do grupo Intera: https://www.interaufabc.com.br/metodologia-intera-2-0 (guias e artefatos consultados em 31/10/2026).

Quando livro e site diferem, a skill usa os modelos publicados no site e registra a diferença. Trechos que são propostas da skill, e não constam nas fontes, estão sinalizados como tal.

## Como citar

Use o botão *Cite this repository* do GitHub (arquivo [`CITATION.cff`](CITATION.cff)) e cite também o livro acima.

## Licença

Conteúdo licenciado sob [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br), a mesma licença aberta da metodologia.

## Contribuições

Sugestões e correções são bem-vindas por meio de *issues* ou *pull requests*.
