# 🧠 Cérebro Vivo

> Uma **Claude Skill** que transforma qualquer texto num grafo mental **vivo e interativo** em HTML — hub central, ramos e folhas, física *force-directed*. Clique em qualquer bolinha e abre uma **caixa de texto editável** com o conteúdo do tema.

**Zero dependências · um único arquivo `.html` · funciona offline em qualquer navegador.**

![Como funciona](assets/04-como-funciona.png)

---

## ✨ O que faz

- Converte texto (markdown ou texto solto) num **cérebro** navegável: `# centro`, `## ramos`, `- folhas`.
- **Física contínua** (force-directed): os nós respiram, você arrasta, dá zoom e busca.
- **Clique numa bolinha → caixa de texto do tema**, editável, com salvamento automático e navegação ‹ ›.
- Exporta **PNG**. Reabre o editor pra montar outro cérebro a qualquer momento.

---

## 🖼️ Como é visualmente

**Visão geral** — o grafo inteiro, estilo preto & branco:

![Visão geral](assets/01-overview.png)

**Clique num ramo** — foca a vizinhança e abre a caixa do tema:

![Caixa do tema — ramo](assets/02-ramo-nota.png)

**Clique numa folha** — mesma caixa, pra qualquer nó:

![Caixa do tema — folha](assets/03-folha-nota.png)

**Editor** — cole seu texto e gere o cérebro:

![Editor](assets/05-editor.png)

---

## 🚀 Instalar (Claude Code)

```bash
git clone https://github.com/C48H74/cerebro-vivo ~/.claude/skills/cerebro-vivo
```

Depois é só pedir ao Claude: *"transforma este texto num cérebro vivo"* e passar o conteúdo.

### Usar sem o Claude
Abra `assets/cerebro-template.html` (ou `examples/cyber-30-dias.html`) direto no navegador, clique em **✎ Texto**, cole e gere.

---

## 📝 Formato de entrada

```
# Título central
## Primeiro ramo
- folha
- folha
## Segundo ramo
- folha
```

- `#` → centro (um só) · `##` → ramo · `-` `*` `•` → folha
- **Texto solto**: 1ª linha = centro, demais = ramos; vírgulas viram folhas.

---

## 📂 Estrutura

```
cerebro-vivo/
├── SKILL.md                     # a skill (como o Claude a usa)
├── README.md
├── assets/
│   ├── cerebro-template.html    # o template (genérico, pronto pra usar)
│   └── *.png                    # imagens deste README
└── examples/
    └── cyber-30-dias.html       # exemplo pronto: plano de cyber Security+/CEH/OSCP/CISSP
```

---

## 🔧 Como a skill monta (modo populado)

O Claude edita dois pontos no `<script>` do template:

- `const SAMPLE = \`...\`;` → o texto do usuário.
- `const SEED = { "rótulo": "descrição do tema", ... };` → preenche a caixa de cada bolinha.

E entrega como artefato ou arquivo `.html`. Detalhes em [`SKILL.md`](SKILL.md).

---

## Licença

MIT © [C48H74](https://github.com/C48H74)
