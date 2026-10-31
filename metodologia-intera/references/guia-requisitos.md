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
- O OA deverá ser acessível a pessoas com algum tipo de deficiência? Quais?

**Acesso:** professores e alunos acessam da mesma forma? Quais as diferenças? Precisa de administrador?

**Desempenho:** quantos alunos simultâneos?

**Portabilidade:** sistemas operacionais; outros dispositivos; acesso via web e necessidade de plugin.

**Licenciamento e direitos** (no modelo aparece repetido o título "Requisitos de Portabilidade"): licença (ver https://br.creativecommons.org/); a quem pertencerá o copyright.

**Reúso:** granularidade, agregação e reusabilidade do OA.

## Exemplos publicados

- Aulas síncronas: https://docs.google.com/document/d/1TCLozxVqbfMYPYZTWeB0-XWe0RXeMosQ/edit
- Simulação: https://docs.google.com/document/d/1UmlRAoGSmGd9ZI6uZ1TtJT-ZlfnIvLW_/edit
- Animação: https://docs.google.com/document/d/1HEjDea4eH0v9zqFaaQ0nwg4wTc1c9Y5O/edit
- Jogo (Jornada da Jubarte): https://docs.google.com/document/d/1igb_MoMLjK2oS5VPw2wfa7qSldol9EYLnljaJB5DYq0/edit

## Como a skill conduz esta etapa

1. Leia o relatório de contexto (ou pergunte por ele). Não repita perguntas já respondidas.
2. Conduza o guia por blocos. Para cada objetivo pedagógico, proponha requisitos pedagógicos e **transforme-os em requisitos funcionais testáveis** — este é o maior desafio apontado pelo próprio livro. Para jogos, use `diretrizes-sociointeracionistas.md` (D1–D40).
3. **Acessibilidade em três camadas** (separe sempre):
   - dispositivos e plataformas (pergunta de portabilidade/disponibilidade);
   - público com deficiência e se haverá co-designers com deficiência (papel Usuário, equipe de acessibilidade);
   - conjunto de diretrizes e nível-alvo: WCAG (AA como meta comum) ou e-MAG para web e cursos EaD; MobileDU para apps; RPG-DU para jogos. Se as skills `wcag-sem-complicacao`, `mobiledu-diretrizes` ou `rpg-du-diretrizes` estiverem disponíveis, use-as para gerar os requisitos de acessibilidade.
4. Entregue o **documento de especificação de requisitos** com identificadores: RP-xx (pedagógicos), RF-xx (funcionais), RNF-xx (não funcionais), RA-xx (acessibilidade). Cada RF/RA com origem (objetivo, diretriz ou critério) e **critério de aceite**.
5. Liste as questões em aberto e as decisões que dependem do demandante.
