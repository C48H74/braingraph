# 🗺️ Roadmap — Cérebro Vivo

Status of the project and what's planned next. Checked = shipped.

## ✅ v1.0 — Core (shipped)
- [x] Text → force-directed brain (center / branches / leaves)
- [x] Continuous physics, drag nodes, zoom, pan
- [x] Click a node → focus neighborhood + **editable topic text box**
- [x] Auto-save of topic text (localStorage, per brain)
- [x] Node search
- [x] PNG export
- [x] Markdown (`#`/`##`/`-`) **and** plain-text parsing
- [x] Trilingual UI (EN / PT / ES) with `?lang=` + switcher
- [x] Zero dependencies, single self-contained HTML file

## 🔜 v1.1 — Content & export
- [ ] Inline topic text in the input (`- SQL Injection :: description…`) so a brain is born fully filled
- [ ] Export / import **all notes** as Markdown and JSON
- [ ] "Copy brain as Markdown outline" button
- [ ] Deep links: open with a specific node focused (`#node=...`)

## 🔭 v1.2 — Visual & navigation
- [ ] Color by branch (one hue per branch) + optional dark mode
- [ ] Depth beyond leaves (sub-leaves / arbitrary nesting)
- [ ] Collapse / expand a branch
- [ ] Minimap for large brains
- [ ] Node icons / emoji per branch

## 🧠 v1.3 — Smarter brains
- [ ] Auto-summarize a long document into a brain (via Claude) before rendering
- [ ] Suggested cross-links between related leaves
- [ ] Merge two brains into a shared "atlas" view
- [ ] Per-node attachments (links, images)

## 📦 v2.0 — Distribution
- [ ] Publish to the Claude skills registries (skills.sh, openskillindex, etc.)
- [ ] Companion skill: folder of notes → brain (Obsidian-style vault)
- [ ] Theming tokens so brands can restyle it
- [ ] Optional React/standalone build

---

Ideas and requests welcome — open an issue. Maintained by [C48H74](https://github.com/C48H74).
