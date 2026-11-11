---
name: cerebro-vivo
description: Use when the user wants to turn a text, document or file (PDF, DOCX, PPTX, XLSX, CSV, HTML, Markdown…) into a "brain" — a living, interactive mind map / knowledge graph in HTML (central hub, branches and leaves, force-directed), where clicking any node opens an editable text box with the topic's content. Triggers: "turn this into a brain", "turn this PDF/file into a mind map", "interactive mind map", "knowledge graph in HTML", "living knowledge graph", "visualize this document as a brain".
---

# Cérebro Vivo (Living Brain)

Turns any text into a **living, interactive mind graph**: a central hub, branches and leaves, with continuous *force-directed* physics. Clicking any node opens a panel with an **editable text box** describing that topic. Output = **a single HTML file**, no dependencies, works offline in any browser. The UI ships in **English, Portuguese and Spanish** (language switcher in the header, English by default).

![How it works](assets/en/00-how-it-works.png)

## When to use

- The user gives a text/document/outline and wants to **see** it as an interactive mind map.
- They want to navigate a topic by areas (center → branches → leaves) instead of reading a list.
- They want a visual artifact to study, present or publish.
- They hand over a **file** (PDF, DOCX, slides, a spreadsheet…) and want it as a brain.

## Build a brain from a file (PDF, DOCX, XLSX, HTML…)

The brain is born from the clean **structure** of a document, not its raw dump. Three steps:

**1. Get the text.** If the file's content is already in context (an upload you can read), use it. Otherwise extract it:
- Prefer a matching skill when available (the `pdf`, `docx`, `pptx`, `xlsx` skills).
- Or run the bundled extractor, which handles most formats in one call:
  ```bash
  python -I scripts/extract_text.py path/to/file.pdf
  ```
  Supports `.pdf .docx .pptx .xlsx/.xlsm .csv/.tsv .html .json .md .txt` (anything else is read as plain text). Heavy formats need an optional lib — the script prints the exact `pip install` if one is missing.

**2. Condense it into a brain.** This is the important part — summarize, don't copy. Read the extracted text and decide:
- **Center** (`#`): the document's subject in 1–3 words (its title, or what it's really about).
- **Branches** (`##`): the 5–10 main sections or themes. Use the document's own headings when it has them; otherwise group related ideas. For a **spreadsheet**, branches are usually the key columns, categories, or sheet names; leaves are the notable values, groups or records — never dump every row.
- **Leaves** (`-`): the sub-topics or key items under each branch. Keep labels 1–3 words.
- **SEED**: for each node, 1–2 sentences distilled from the source so its box opens already explaining the topic.

Keep it legible: ~5–10 branches, up to ~8 leaves each. A 40-page PDF becomes a few dozen nodes, not hundreds.

**3. Build and deliver** using Mode B below (inject `SAMPLE` + `SEED` into a copy of the template), then publish or hand over the `.html`.

> Example shape for a report: `# Q3 Report` → `## Revenue` / `## Growth` / `## Risks` → leaves like `- Churn`, `- Pipeline`, each with a one-line SEED pulled from the document.

## How to deliver (2 modes)

### Mode A — Ready for the user to paste (fast)
Hand over `assets/cerebro-template.html` as-is. It is already a complete tool: the user clicks **✎ Text**, pastes content and generates the brain. Use when the user hasn't supplied a specific text yet.

### Mode B — Pre-filled with the user's content (recommended)
When the user supplied a text, **edit a copy of the template** injecting their content, and deliver it already rendering. Two edit points inside `<script>`:

1. **`const SAMPLE = \`...\`;`** — replace with the user's text in the format below.
2. **`const SEED = { ... };`** — optional dictionary `"node label": "topic description"`. Fills the text box of each node. Leave `{}` if the user will write the descriptions by hand.

Then deliver as an **artifact** (publish the HTML) or as a **.html file** for download, depending on context.

## Input format (the SAMPLE string)

```
# Central title
## First branch
- leaf
- leaf
## Second branch
- leaf
```

Parser rules (already built into the template):
- `#` → **center** (only one).
- `##` → **branch** (from the center).
- `-`, `*` or `•` → **leaf** (from the last branch).
- **Plain text** (no markers): the first line becomes the center, each following line a branch; commas / `;` / `|` on the same line become leaves of that branch.

## Filling the descriptions (SEED)

For each label that appears in the text, write 1–2 direct sentences:

```js
const SEED = {
  "Central title": "What the whole map represents, in one sentence.",
  "First branch": "What this branch covers.",
  "leaf": "Short, useful description of the topic."
};
```

Repeated labels share the same description (same meaning). Nodes without a SEED entry open an empty box with the prompt *"Write about 'topic'…"*.

## Language

The tool auto-detects `?lang=en|pt|es` in the URL and defaults to English. The header has a switcher. Only the **UI** is translated — node labels and topic text come from the user's content, so write those in the user's language.

## What the user can do with the result

- **Drag** the background (pan) and **mouse wheel** (zoom).
- **Drag a node** to reposition; **double-click** releases it back to the physics.
- **Click a node** → focuses its neighborhood and opens the **topic text box** (editable, with ‹ › to move between nodes and auto-save ✓).
- **Search** a node by name.
- **↧ PNG** exports the brain as an image.
- **✎ Text** reopens the editor to generate another brain from another text.

Text typed into the boxes is saved in the browser session (localStorage), per brain.

## Quality tips

- Keep labels **short** (1–3 words) — long labels clutter the graph.
- 5–10 branches and up to ~8 leaves per branch is the sweet spot.
- Group by logical theme; don't copy long section titles verbatim.

## Example

`examples/cyber-30-dias.html` — a cybersecurity study plan (Security+, CEH, OSCP, CISSP) already built, with every topic box filled.

![Overview](assets/en/01-overview.png)
![Topic text box](assets/en/02-topic-note.png)

---

**Translations of this README:** [Português](README.pt-BR.md) · [Español](README.es.md)
