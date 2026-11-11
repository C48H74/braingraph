# Contributing to braingraph

Thanks for wanting to help! braingraph is a single self-contained HTML tool plus a Claude skill — easy to hack on.

## Ways to contribute

- 🌱 **New example brains** — add a ready-made `.html` to `examples/` on any topic.
- 🌐 **UI translations** — add a language to the `I18N` object in `assets/cerebro-template.html`.
- 🎨 **Visual themes** — color-by-branch, dark mode, new layouts.
- 🐛 **Bug fixes** and small UX improvements.
- 📝 **Docs** — improve the README or its translations.

## How to submit (5 steps)

1. **Fork** the repo.
2. **Create a branch**: `git checkout -b my-change`.
3. **Make your change.** Keep the tool dependency-free and a single file.
4. **Test** by opening the HTML in a browser (desktop + mobile width).
5. **Open a pull request** describing what you changed and why.

## Ground rules

- No external dependencies, no build step — it must stay one self-contained `.html`.
- Keep the black & white aesthetic unless you're intentionally proposing a theme.
- Match the existing input format (`#` / `##` / `-`).
- Be kind in reviews. First-time contributors welcome.

## Adding a language

In `assets/cerebro-template.html`, find the `I18N` object and add a key (e.g. `fr`) with the same fields as `en`/`pt`/`es`. Add the option to the `<select id="lang">` and you're done.

## License

By contributing, you agree your contributions are licensed under the [MIT License](LICENSE).
