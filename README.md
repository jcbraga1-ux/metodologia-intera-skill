# Metodologia Intera 2.0 – Skill

Agent Skill que conduz o desenvolvimento de **objetos de aprendizagem** (aulas, cursos a distância, vídeos, simulações, softwares e jogos educacionais) com a **Metodologia Intera 2.0**, do grupo de pesquisa Intera da Universidade Federal do ABC (UFABC). Funciona com assistentes de IA compatíveis com o padrão aberto [Agent Skills](https://agentskills.io/).

## O que a skill faz

- **Situa o projeto:** identifica o tipo de objeto, a etapa em que ele está e a variante da metodologia (geral, jogos ou cursos EaD).
- **Define papéis:** monta a matriz papel × pessoa e aponta riscos, como a falta de equipe de acessibilidade.
- **Conduz os guias como entrevista:** contextualização, requisitos, esboço, testes, avaliação pedagógica, disponibilização e gestão, entregando cada artefato preenchido com pontos de atenção.
- **Transforma requisitos pedagógicos em funcionalidades testáveis**, inclusive com as diretrizes sociointeracionistas D1–D40 para jogos.
- **Coloca o reúso no centro:** reutiliza antes de criar, escreve requisitos de reúso, orienta sobre recursos educacionais abertos (REA), os 5R e licenças Creative Commons, e entrega uma ficha de reúso.
- **Trata acessibilidade com diretrizes**, e não só com dispositivos, e trabalha junto com as skills [WCAG sem complicação](https://github.com/jcbraga1-ux/wcag-sem-complicacao-skill), [MobileDU](https://github.com/jcbraga1-ux/mobiledu-skill) e [RPG-DU](https://github.com/jcbraga1-ux/rpg-du-skill).

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
    └── diretrizes-sociointeracionistas.md     # D1–D40
```

## Como instalar

A skill é a pasta [`metodologia-intera/`](metodologia-intera/).

- **Assistentes com tela de configurações:** baixe o arquivo pronto na página de [Releases](../../releases), em *Assets*:

  | Assistente | Arquivo | Onde enviar |
  | --- | --- | --- |
  | Claude (claude.ai e app) | `metodologia-intera.zip` | *Configurações › Capacidades › Skills* |
  | Gemini (app e web) | `metodologia-intera-gemini.zip` | página de *Skills* do Gemini, opção de enviar arquivo |

  O arquivo `metodologia-intera-gemini.zip` traz o `SKILL.md` na pasta principal, como o Gemini exige, e também foi testado no Claude.
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
