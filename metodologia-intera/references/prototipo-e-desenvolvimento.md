# Do esboço ao OA pronto: protótipo, desenvolvimento e registro de reúso

Esta seção vale quando o professor chega com os artefatos da Intera prontos (contextualização, requisitos, esboço ou GDD) e quer que o OA seja construído. Ela segue o fluxo definido pelo grupo Intera para o trabalho com assistentes de IA. Algumas práticas vêm do modelo de processo de SILVA, A. G. da. *Modelo aberto de processo para implantação de um curso a distância* (Dissertação de Mestrado, UFABC, 2024), adaptado para o professor que trabalha com um assistente de IA. A ordem é sempre a mesma:

1. Análise dos artefatos e acordo do OA
2. Protótipo de alta fidelidade
3. Aprovação do professor
4. Escolha da plataforma
5. Desenvolvimento, com curadoria do conteúdo e o registro de reúso sempre atualizado
6. Ofertas finais
7. Disponibilização: onde o OA vai ficar (pacote SCORM para AVA ou link do HTML5) e envio para o grupo Intera

## 1. Analise os artefatos recebidos

Antes de construir qualquer coisa, leia todos os artefatos e analise-os criticamente:

- coerência entre objetivos, conteúdos e requisitos;
- alinhamento com a teoria de aprendizagem e com a base humanista (`alinhamento-pedagogico.md`);
- Desenho Universal (`desenho-universal.md`);
- desenho ético (`desenho-etico.md`);
- reúso (`reuso-e-rea.md`).

Para jogos, siga a seção de GDD de `extensao-jogos.md`.

Apresente os pontos de atenção e as sugestões de melhoria, no formato de revisão estruturada (o que foi atendido e o que precisa melhorar, com o critério usado). Faltando algum artefato essencial, por exemplo requisitos sem critério de aceite, ofereça completá-lo junto com o professor antes de seguir.

Em seguida, proponha o **acordo do OA**, uma versão leve do Termo de Abertura de Projeto descrita em `guia-requisitos.md`. Ele registra:

- o que o OA vai fazer e o que não vai fazer;
- os requisitos não atendidos, com justificativa e alternativa;
- os riscos;
- as entregas.

O protótipo começa depois que o professor aprova o acordo.

## 2. Proponha sempre um protótipo de alta fidelidade

Antes de desenvolver, **sempre** proponha e construa um protótipo de alta fidelidade para o professor testar. Um protótipo de alta fidelidade:

- tem aparência próxima da final (cores, fontes, ícones, disposição das telas);
- é navegável: botões e caminhos principais funcionam;
- usa conteúdo real em pelo menos uma tela, atividade ou fase completa, e não texto de enchimento;
- já mostra os recursos de acessibilidade previstos, como contraste, tamanho de letra, legendas, espaço para Libras e navegação por teclado;
- abre no navegador sem instalação, em HTML;
- já traz o **menu de acessibilidade** que o OA final terá (ver seção 3).

Junto com o protótipo, entregue um roteiro curto de teste para o professor. Por exemplo: "abra a tela inicial, faça a atividade 1, tente errar de propósito, aumente a letra". Peça a ele que registre o que gostou, o que estranhou e o que mudaria. Ajuste o protótipo a cada rodada. Sempre que possível, o professor também testa com alguns alunos do público-alvo, com perfis diferentes. Se isso ainda não for possível, a skill pode simular o uso por personas (descrições fictícias de alunos com necessidades distintas), mas apenas como complemento: personas não substituem pessoas reais nos testes.

**Só passe para o desenvolvimento depois que o professor aprovar o protótipo de forma explícita.** Registre a aprovação e as mudanças de cada rodada no registro de reúso.

## 3. Antes de desenvolver, pergunte a plataforma

Pergunte sempre ao professor: **para qual plataforma o OA deve ser desenvolvido? Web, iOS, Android ou outra?**

- **Se ele não souber,** desenvolva em **HTML completo**: arquivos HTML, CSS e JavaScript autocontidos, responsivos, acessíveis, que funcionem sem internet depois de baixados e abram em qualquer navegador de computador, tablet ou celular. Esse formato pode depois virar pacote SCORM ou aplicativo, e combina com o reúso.
- **Se escolher Android ou iOS,** proponha ferramentas gratuitas que gerem os dois a partir do mesmo projeto, quando possível (`tecnologias-gratuitas.md`). Avise em "Pontos de atenção" que publicar em loja de aplicativos pode ter custo (por exemplo, a conta de desenvolvedor da Apple é paga) e que um site responsivo, ou um HTML instalável no celular, evita esse custo.
- **Se escolher outra plataforma** (por exemplo, dentro do Moodle ou num motor de jogos), siga a escolha e registre a versão da ferramenta. Para H5P, veja o aviso abaixo.

**Menu de acessibilidade nos OAs em HTML5.** Seguindo o Desenho Universal (flexibilidade de uso, `desenho-universal.md`), todo OA em HTML5 traz um menu de acessibilidade sempre visível e acessível por teclado. Proposta desta skill, com base nas diretrizes MobileDU. O menu permite:

- aumentar e diminuir o tamanho da letra sem quebrar a tela;
- ativar alto contraste e inverter cores;
- aumentar o espaçamento entre linhas e letras;
- trocar para uma fonte mais legível;
- pausar ou desligar animações, sons e música de fundo;
- ouvir o texto em voz alta, quando o navegador oferecer síntese de voz;
- voltar às configurações originais.

As escolhas ficam guardadas só no aparelho do aluno, sem envio a servidores (`desenho-etico.md`). Esse menu continua funcionando quando o OA vira pacote SCORM, porque o pacote leva o próprio HTML5.

**Aviso sobre H5P.** O H5P é gratuito e prático, mas tem limites de acessibilidade que o professor precisa conhecer antes de escolher:

- **Não dá para incluir um menu de acessibilidade próprio** dentro de um conteúdo H5P feito nas ferramentas comuns de autoria. Os tipos de conteúdo são fechados e não aceitam código adicional; mudar isso exige desenvolver uma biblioteca H5P própria e instalá-la no AVA. A personalização fica por conta do navegador e do sistema do aluno (zoom, alto contraste, leitor de tela).
- **Nem todo tipo de conteúdo atende plenamente à WCAG.** Segundo o próprio H5P, que tem como meta a WCAG 2.2 AA, tipos como Accordion, Dialog Cards, Fill in the Blanks, Image Hotspots, Interactive Book, Interactive Video, Single Choice Set e Summary atendem; outros atendem só em parte, como Drag and Drop, Drag the Words, Mark the Words, Memory Game, Multiple Choice, Question Set, True/False e Course Presentation; e Find the Hotspot não é recomendado. Confira a lista atual em help.h5p.com antes de escolher.
- **A acessibilidade também depende de quem cria:** texto alternativo em todas as imagens, legendas (WebVTT) nos vídeos, transcrição dos áudios, títulos e listas do editor, contraste adequado, cor nunca como única pista, nada de reprodução automática e idioma marcado no texto.

Quando o professor quiser H5P, a skill:

1. explica esses limites em linguagem simples;
2. oferece a alternativa de fazer o OA em HTML5 com menu de acessibilidade e entregar como pacote SCORM, que funciona nos mesmos AVAs;
3. se ele mantiver o H5P, sugere os tipos de conteúdo que atendem à WCAG, aplica as boas práticas de autoria acima e oferece uma atividade alternativa equivalente para quem não conseguir usar a principal;
4. registra no acordo do OA, como **requisito não atendido**, o que ficou de fora (por exemplo, o menu de acessibilidade), com justificativa e alternativa.

## 4. Durante o desenvolvimento, cuide da curadoria e mantenha um registro de reúso em um único arquivo .md

**Curadoria do conteúdo.** Todo conteúdo usa fontes confiáveis, como livros, artigos, documentos oficiais e materiais didáticos reconhecidos. Registre a fonte de cada informação e dê os créditos quando o autor não for o professor, respeitando direitos autorais e evitando plágio. Como assistentes de IA podem inventar fatos e referências, **toda informação factual e toda referência sugerida pelo assistente precisa ser conferida pelo professor** antes de entrar no OA. Base: SILVA (2024), cap. 6.4.

**Registro de reúso.**

Desde o início do desenvolvimento, crie e mantenha atualizado **um único arquivo Markdown** com tudo o que é preciso para que outra pessoa consiga reutilizar, adaptar ou reproduzir o OA. Sugestão de nome: `REGISTRO-OA-<nome-do-oa>.md`. Ele incorpora a ficha de reúso de `reuso-e-rea.md`.

Estrutura sugerida (proposta desta skill):

1. **Identificação:** título, autores e papéis, instituição, data, versão, licença.
2. **Resumo pedagógico:** público, problema pedagógico, objetivos, conteúdos, teoria de aprendizagem e cenário de uso (da contextualização).
3. **Requisitos e acordo do OA:** lista dos requisitos com identificadores e critérios de aceite (ou o link para o documento completo), escopo, não escopo e requisitos não atendidos com justificativa.
4. **Esboço ou GDD:** resumo e link.
5. **Protótipo:** rodadas de teste com o professor, mudanças feitas e data da aprovação.
6. **Decisões de projeto:** o que foi decidido, por quê e quais alternativas foram descartadas.
7. **Tecnologias:** plataforma, linguagens, bibliotecas e ferramentas, com versão e licença de cada uma.
8. **Estrutura de arquivos:** o que há em cada pasta e arquivo.
9. **Como executar e como gerar o pacote:** passo a passo para abrir, compilar, exportar (inclusive SCORM, se houver).
10. **Curadoria e recursos de terceiros:** fontes consultadas para o conteúdo; imagens, sons, fontes tipográficas e textos de terceiros, com autor e licença de cada um.
11. **Acessibilidade:** recursos implementados por dimensão da matriz de Desenho Universal e o que ficou pendente.
12. **Ética e dados:** que dados são coletados (de preferência nenhum) e como.
13. **Testes:** o que foi testado em cada visão (técnica, linguística e pedagógica, acessibilidade), com quem, resultados, parecer do professor e decisão de apto ou não apto.
14. **Como adaptar:** o que pode ser trocado com facilidade (textos, imagens, idioma, nível), onde fica cada coisa e o tamanho do grão.
15. **Histórico de versões.**

Atualize o arquivo a cada entrega e entregue-o junto com o OA.

## 5. Ao finalizar, ofereça sempre três coisas

Quando o OA estiver pronto, pergunte sempre ao professor se ele deseja:

1. **Gerar um tutorial de uso**, ou seja, os manuais do professor e do aluno previstos na etapa de Desenvolvimento, em linguagem simples e em formato acessível.
2. **Fazer um plano de teste**, a partir dos requisitos e critérios de aceite. O plano segue as três visões (técnica, linguística e pedagógica, e acessibilidade) e inclui desenho ético, o parecer de homologação do professor e a decisão final de apto ou não apto (ver Teste e Qualidade em `etapas-arquitetura-ate-ambiente.md`).
3. **Preparar o OA para o lugar onde vai ficar** (pacote SCORM ou link do HTML5), conforme a pergunta da seção 6.

Registre as escolhas no registro de reúso.

## 6. Na disponibilização, pergunte sempre onde o OA vai ficar

Ao terminar o desenvolvimento, pergunte sempre ao professor: **onde você vai guardar e disponibilizar este OA para os alunos?** O caminho depende da resposta.

**Se for no Moodle ou em outro AVA que aceite SCORM** (como Canvas, Blackboard ou outras plataformas de cursos), a prioridade é gerar um **pacote SCORM**. Ele é reconhecido por vários AVAs, o que facilita o reúso em outras instituições.

- Gere o pacote no padrão **SCORM 1.2**, o mais aceito: um arquivo .zip com o `imsmanifest.xml` na raiz e o OA em HTML5.
- Se o OA tiver atividades com resultado, registre a conclusão e, quando fizer sentido, a nota, para que o AVA acompanhe o progresso do aluno. Envie só o necessário, de acordo com `desenho-etico.md`.
- Explique ao professor como enviar o pacote. No Moodle, por exemplo: na disciplina, ative a edição, escolha **Adicionar uma atividade ou recurso** e depois **Pacote SCORM**, e envie o .zip sem descompactar.
- Guarde também a versão em HTML5, que é o código-fonte do OA e serve para o repositório e para adaptações.

Se o professor não souber se o AVA dele aceita SCORM, sugira perguntar ao suporte da instituição ou testar enviando o pacote numa área de teste.

**Se o professor não tiver um AVA que aceite SCORM** (por exemplo, usa só o Google Sala de Aula, o WhatsApp ou o e-mail), desenvolva em **HTML5** e mostre que **basta copiar o link e compartilhar com os alunos**. Para ter um link, o OA precisa estar publicado na internet. Ofereça um caminho gratuito:

- **GitHub Pages**, que combina com o repositório da seção 8: no repositório do OA, abra **Settings › Pages**, em **Source** escolha **Deploy from a branch**, selecione a branch **main** e a pasta **/(root)** e clique em **Save**. Em alguns minutos aparece o link, no formato `https://<usuario>.github.io/<nome-do-repositorio>/`. O arquivo principal do OA precisa se chamar `index.html`. Se ele estiver dentro da pasta `oa/`, o link termina em `/oa/`.
- Antes de enviar o link, peça ao professor que abra o endereço no celular e no computador, para conferir se tudo funciona.
- Mostre um exemplo de mensagem para os alunos, com o link, uma frase sobre a atividade e o lembrete de que o OA abre no navegador, sem instalar nada.
- Lembre que, se o OA não coletar dados (o recomendado), compartilhar o link não envolve cadastro dos alunos.

Registre no registro de reúso onde o OA foi publicado: AVA e tipo de pacote, ou link.

## 7. Sugira também o repositório do grupo Intera

Sugira sempre guardar o código do OA de forma aberta, junto com todos os artefatos da metodologia e o registro de reúso, no **repositório do grupo Intera**. Para isso, o professor envia um e-mail para **iemtec@ufabc.edu.br**.

Ofereça um rascunho do e-mail, com:

- título do OA e autores;
- licença aberta escolhida;
- link ou arquivo .zip com o código-fonte;
- os artefatos: contextualização, requisitos, esboço ou GDD, plano de teste e manuais;
- o registro de reúso (`REGISTRO-OA-<nome-do-oa>.md`).

O envio é feito pelo professor. A skill não envia e-mails por conta própria.

## 8. Envio do OA pronto para a organização do grupo Intera no GitHub

Com o OA pronto e aprovado, sugira ao professor publicá-lo na organização do grupo Intera no GitHub: **https://github.com/intera-repositorio-docente**. Ofereça os dois caminhos.

**Caminho A: o professor cria o repositório (passo a passo, sem linha de comando)**

1. Crie uma conta gratuita em github.com, se ainda não tiver.
2. No canto superior direito, clique em **+** e depois em **New repository**.
3. Dê um nome curto, em letras minúsculas e com hífens, por exemplo `oa-ciclo-da-agua`. Escreva uma descrição de uma linha.
4. Marque **Public**, marque **Add a README file** e, em **Choose a license**, escolha a licença aberta combinada (por exemplo, Creative Commons Attribution 4.0). Clique em **Create repository**.
5. Clique em **Add file** e depois em **Upload files**. Arraste os arquivos do OA, de preferência organizados nestas pastas:
   - `oa/`, com o código ou os arquivos do objeto (por exemplo, o HTML completo);
   - `artefatos/`, com contextualização, requisitos, acordo do OA, esboço ou GDD, plano de teste e manuais;
   - `REGISTRO-OA-<nome-do-oa>.md`, o registro de reúso.

   Escreva uma mensagem curta e clique em **Commit changes**. O envio pelo navegador aceita arquivos de até 25 MB cada; arquivos maiores, como vídeos longos, podem ficar num serviço gratuito com o link no README.
6. Edite o `README.md` (ícone de lápis) com: o que é o OA, para quem é, como abrir e usar, autores, licença e um link para o registro de reúso.
7. Envie o link do repositório para **iemtec@ufabc.edu.br**, pedindo a inclusão na organização `intera-repositorio-docente`. O grupo combina com o professor a forma de inclusão: convite para a organização seguido da transferência do repositório (**Settings › General › Danger Zone › Transfer ownership**) ou uma cópia vinculada (fork) feita pelo grupo.

**Caminho B: o grupo ajuda**

Se o professor preferir não mexer no GitHub, ele escreve para **iemtec@ufabc.edu.br**, explica o que tem pronto e anexa os arquivos ou um link para eles. O grupo ajuda a criar o repositório.

Nos dois caminhos, ofereça um rascunho do e-mail e lembre que o envio é feito pelo próprio professor.
