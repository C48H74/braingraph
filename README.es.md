<div align="center">

<img src="assets/banner.png" alt="braingraph" width="100%" />

# 🧠 braingraph

**La forma open-source de convertir cualquier texto en un grafo mental vivo e interactivo.**

[![Stars](https://img.shields.io/github/stars/C48H74/braingraph?style=for-the-badge&logo=github&color=f5c518&label=STARS)](https://github.com/C48H74/braingraph/stargazers)
[![License](https://img.shields.io/badge/LICENSE-MIT-1f8fff?style=for-the-badge)](LICENSE)
[![PRs](https://img.shields.io/badge/PRS-WELCOME-3fb950?style=for-the-badge)](CONTRIBUTING.md)
[![Zero deps](https://img.shields.io/badge/DEPENDENCIES-ZERO-e8590c?style=for-the-badge)](#)
[![Claude Skill](https://img.shields.io/badge/CLAUDE-SKILL-8957e5?style=for-the-badge)](SKILL.md)

**[Empezar](#-empezar) · [Ejemplos](#-ejemplos) · [Cómo funciona](#%EF%B8%8F-cómo-funciona) · [Roadmap](ROADMAP.md) · [Contribuir](CONTRIBUTING.md)**

🌐 **Idiomas:** [English](README.md) · [Português](README.pt-BR.md) · Español

</div>

---

Pega un texto, un documento, un esquema — lo que sea — y `braingraph` lo convierte en un cerebro **vivo** force-directed: un hub central, ramas y hojas que respiran y se reorganizan. Haz clic en cualquier nodo y se abre una **caja de texto editable**. Un único archivo HTML. Sin build, sin servidor, sin cuenta. Funciona offline, en cualquier navegador.

## 🤔 ¿Por qué braingraph?

| Reto | braingraph |
|---|---|
| Los documentos largos son difíciles de retener | Ve toda la estructura como un grafo vivo |
| Las apps de mapas mentales piden cuenta y te atan | Un archivo HTML, cero dependencias, offline |
| Los diagramas estáticos quedan obsoletos al instante | Cada nodo tiene una caja editable, guardada al escribir |
| La mayoría de herramientas son solo en inglés | Interfaz en **EN / PT / ES** de fábrica |
| Difícil de compartir o incrustar | Un único archivo para abrir, alojar o soltar donde sea |

## ✨ Características

- 🧠 **Texto → cerebro** — `#` centro, `##` ramas, `-` hojas. O pega texto libre y se estructura solo.
- 📄 **Cualquier archivo → cerebro** — PDF, DOCX, PPTX, XLSX, CSV, HTML, Markdown: el texto se extrae y estructura automáticamente.
- 🌀 **Física viva** — layout force-directed continuo; arrastra nodos, zoom, pan, búsqueda.
- 📝 **Caja de tema por nodo** — clic en un nodo y se abre una caja editable; autoguardado, con navegación ‹ ›.
- 🌐 **Interfaz trilingüe** — inglés (por defecto), portugués, español. Selector arriba o `?lang=en|pt|es`.
- 🖼️ **Exportar PNG** — un clic para descargar el cerebro como imagen.
- 📦 **Cero dependencias** — un único `.html`. Sin build, sin CDN, sin servidor.
- ♻️ **Reutilizable** — como skill de Claude, herramienta independiente o incrustado.

## 🚀 Empezar

**1. Úsalo ya** — abre [`assets/cerebro-template.html`](assets/cerebro-template.html) en el navegador, haz clic en **✎ Texto**, pega y genera.

**2. Instalar como skill de Claude**
```bash
git clone https://github.com/C48H74/braingraph ~/.claude/skills/braingraph
```

**3. Solo pídeselo a Claude**
> "Convierte este texto en un cerebro vivo" — y pega tu contenido.

**4. Incrustar** — copia el archivo HTML único en tu sitio o en un iframe. Es self-contained.

## 📝 Formato de entrada

```
# Título central
## Primera rama
- hoja
- hoja
## Segunda rama
- hoja
```

- `#` → centro (uno solo) · `##` → rama · `-` `*` `•` → hoja
- **Texto libre**: 1ª línea = centro, cada línea siguiente = rama; las comas se vuelven hojas.

## 💡 Ejemplos

**De un esquema**
```
# Lanzamiento
## Marketing
- Landing page
- Secuencia de email
## Ingeniería
- API
- App móvil
## Ventas
- Script de demo
- Precios
```

**De texto libre**
```
Viaje de fin de semana
Sábado, museo, almuerzo, parque
Domingo, mercado, playa
```

Cada nodo abre una caja para rellenar con detalles — notas, enlaces, descripciones — guardados al escribir.

## 🖼️ Cómo funciona

![Cómo funciona](assets/es/00-how-it-works.png)

**Vista general**

![Vista general](assets/es/01-overview.png)

**Clic en un nodo → caja del tema**

![Caja del tema](assets/es/02-topic-note.png)

## 📂 Estructura

```
braingraph/
├── SKILL.md                     # la skill (cómo la usa Claude)
├── README.md / .pt-BR / .es     # docs (EN principal + traducciones)
├── ROADMAP.md
├── CONTRIBUTING.md
├── assets/
│   ├── cerebro-template.html    # la plantilla (genérica, lista para usar)
│   ├── banner.png
│   └── en|pt|es/*.png           # capturas por idioma
└── examples/
    └── cyber-30-dias.html       # ejemplo listo: plan Security+/CEH/OSCP/CISSP
```

## 🤝 Contribuir

¡PRs bienvenidos! Ver [CONTRIBUTING.md](CONTRIBUTING.md). Ideas, nuevos cerebros de ejemplo, traducciones de la interfaz y temas visuales son estupendas primeras contribuciones.

## ⭐ Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=C48H74/braingraph&type=Date)](https://star-history.com/#C48H74/braingraph&Date)

## 📄 Licencia

MIT © [C48H74](https://github.com/C48H74)
