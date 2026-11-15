# Metodologia Intera 2.0 – Skill

Agent Skill que conduz, também chamada de **Intera-IA**, o desenvolvimento de **objetos de aprendizagem** (aulas, cursos a distância, vídeos, simulações, softwares e jogos educacionais) com a **Metodologia Intera 2.0**, do grupo de pesquisa Intera da Universidade Federal do ABC (UFABC). Funciona com assistentes de IA compatíveis com o padrão aberto [Agent Skills](https://agentskills.io/).

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
- **Constrói o OA com o professor:** analisa os artefatos prontos, propõe um protótipo de alta fidelidade para teste e aprovação, pergunta a plataforma (ou faz em HTML completo), mantém um registro de reúso em um único .md e, ao final, oferece tutorial de uso e plano de teste.
- **Acessibilidade no OA final:** todo OA em HTML5 traz menu de acessibilidade; para H5P, a skill avisa os limites e indica os tipos de conteúdo acessíveis.
- **Prepara o OA para onde ele vai ficar:** pacote SCORM para Moodle e outros AVAs ou, sem AVA compatível, HTML5 publicado com um link para compartilhar com os alunos.
- **Em jogos, sempre o GDD:** conduz a criação passo a passo ou analisa criticamente o GDD que o professor já tiver.
- **Organiza o projeto como um acordo:** propõe o acordo do OA (escopo, não escopo, requisitos não atendidos com justificativa) e um diagnóstico opcional da turma.
- **Testa em três visões:** técnica, linguística e pedagógica, e acessibilidade, com parecer do professor e decisão de apto ou não apto; ao final, separa ajustes e mudanças para a próxima versão.
- **Sugere o repositório do grupo Intera** para guardar o código e os artefatos de forma aberta: passo a passo para publicar na organização [intera-repositorio-docente](https://github.com/intera-repositorio-docente) no GitHub, ou contato por iemtec@ufabc.edu.br.
- **Traz as diretrizes de acessibilidade do grupo Intera**, já incluídas: WCAG 2.1 em linguagem simples, MobileDU (aplicativos) e RPG-DU (jogos RPG).

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
    ├── prototipo-e-desenvolvimento.md         # protótipo, plataforma, registro de reúso, SCORM e repositório Intera
    ├── diretrizes-sociointeracionistas.md     # D1–D40
    ├── diretrizes-wcag.md                     # 78 critérios WCAG 2.1 (cópia da skill wcag-sem-complicacao)
    ├── diretrizes-mobiledu.md                 # 60 diretrizes MobileDU (cópia da skill mobiledu-diretrizes)
    ├── diretrizes-rpg-du.md                   # visão geral das 88 diretrizes RPG-DU (cópia da skill rpg-du-diretrizes)
    └── diretrizes-rpg-du-completas.md         # texto completo das 88 diretrizes RPG-DU
```

## Intera-IA e as skills separadas

Desde a versão 1.7.0, esta skill reúne as três skills de acessibilidade do grupo Intera. Elas continuam publicadas separadamente, cada uma com seu DOI, para quem quiser usar só uma delas:

| Skill separada | Versão incluída | DOI |
| --- | --- | --- |
| [wcag-sem-complicacao](https://github.com/jcbraga1-ux/wcag-sem-complicacao-skill) | 1.0.1 | [10.5281/zenodo.23837715](https://doi.org/10.5281/zenodo.23837715) |
| [mobiledu-diretrizes](https://github.com/jcbraga1-ux/mobiledu-skill) (Coletto, 2026) | 1.0.1 | [10.5281/zenodo.23809314](https://doi.org/10.5281/zenodo.23809314) |
| [rpg-du-diretrizes](https://github.com/jcbraga1-ux/rpg-du-skill) (Cunha, 2022) | 1.0.0 | [10.5281/zenodo.23836531](https://doi.org/10.5281/zenodo.23836531) |

- **Instale a Intera-IA ou as skills separadas, não as duas**, para o assistente não receber as mesmas orientações em dobro.
- **As skills separadas são a fonte.** As correções são feitas nelas, e o script [`montar-pacote.py`](montar-pacote.py) copia o conteúdo para `references/` a cada nova versão da Intera-IA. Não edite os arquivos `diretrizes-wcag.md`, `diretrizes-mobiledu.md` e `diretrizes-rpg-du*.md` à mão.

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
- COLETTO, Carlos Jair. **Diretrizes para o desenvolvimento de aplicações móveis voltadas para o Desenho Universal: a Biblioteca MobileDU**. Tese (Doutorado em Ciência da Computação). Santo André: Universidade Federal do ABC, 2026.
- CUNHA, Francinete Furtado da. **Diretrizes para o design universal de jogos educacionais digitais do tipo Role Play Games (RPG)**. Dissertação (Mestrado em Ciência da Computação). Santo André: Universidade Federal do ABC, 2022.
- W3C. **Web Content Accessibility Guidelines (WCAG) 2.1**. W3C Recommendation, 2018. https://www.w3.org/TR/WCAG21/

Quando livro e site diferem, a skill usa os modelos publicados no site e registra a diferença. Trechos que são propostas da skill, e não constam nas fontes, estão sinalizados como tal.

## Como citar

Use o botão *Cite this repository* do GitHub (arquivo [`CITATION.cff`](CITATION.cff)) e cite também o livro acima.

## Licença

Conteúdo licenciado sob [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br), a mesma licença aberta da metodologia.

## Contribuições

Sugestões e correções são bem-vindas por meio de *issues* ou *pull requests*.
