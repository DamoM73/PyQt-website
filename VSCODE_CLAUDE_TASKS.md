# Tasks for Claude in VS Code

These tasks finish the Zensical rework of *PyQt Tutorials*. They couldn't be done from Cowork, which can only create and overwrite files in this folder. It can't delete files, run git, access GitHub or write inside `.github/`.

The site went live on 21 October 2026: `zensical` was merged into `main`, and the old Sphinx site is tagged `v1-sphinx`. All work now happens on `main`; pushing to `main` deploys the site. Check with Damien before each task marked **Confirm first**. Report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.67 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Audience:** Year 11/12 Digital Solutions students using VS Code, GitHub Desktop and Qt Designer (the standalone installer from build-system.fman.io). Students clone `DamoM73/PyQt6-Boiler-Plate`, fork it on their first push, and build every app in that repo. Pages link to the Digital Solutions 2025 text (`https://damom73.github.io/digital-solutions-text-2025/<slug>`, slug = file name without its number, `_` → `-`).
- **Structure:** Home (`docs/index.md`); Getting Started (`docs/start/`: introduction, setup); Qt Designer Basics (`docs/basics/01_creating_apps.md` to `05_signals_slots.md`); Calculator (`docs/calculator/06_create.md`, `07_refine.md`); Time Machine (`docs/time_machine/08_ui.md` to `12_timer.md`); To Do List (`docs/to_do/13_ui.md` to `15_advanced.md`); Contacts (`docs/contacts/16_ui.md`, `17_app.md`); Reference (`docs/reference/`: boilerplate, common_errors, solutions, glossary, licence).
- **Two boilerplates:** Tutorials 1–7 use the `pyuic6` boilerplate (`main_window.py`, widgets through `self.ui.`); Tutorial 9 creates `loadui_boilerplate.py` with `uic.loadUi`, used from then on (widgets straight on `self`).
- **Examples:** each app is built up across its tutorials. Every version of a file shown on a page is a snippet file at `docs/examples/<section>/<tutorial>/stepNN/<file>.py`. Pages include them with `--8<-- "examples/..."` inside ```` ```python linenums="1" hl_lines="..." title="calculator.py" ````; `hl_lines` marks new or changed lines. Long files are shown as line ranges, for example `--8<-- "examples/calculator/07_refine/step10/calculator.py:124:128"` with `linenums="124"`; `hl_lines` still counts from 1 in those blocks. When a page says to repeat a change for several buttons, a collapsed `??? tip "Check your code"` shows the whole file with no highlights.
- **Solutions:** `docs/solutions/<section>/<tutorial>/exN_name.py`, shown on `docs/reference/solutions.md` with `hl_lines` marking the changes from the tutorial's final code. Qt Designer tutorials have open design exercises with no solutions. There's no student download zip; students build every file themselves.
- **Checks:** `python scripts/check_explanations.py` confirms every Code explanation line number matches its snippet. When a code block has `hl_lines`, only highlighted code lines need explaining; comment lines are never referenced. Expect `0 issue(s) found`.
- **Tested in Cowork:** every tutorial's final code and every solution was run headless (PyQt 6.11, `QT_QPA_PLATFORM=offscreen`) with scripted clicks and stubbed dialogs, using the `.ui` files from `PyQt6-website-tutorials`. Every error message on the site was produced by breaking a copy of the code and running it.
- **Fixes made beyond the old site:** `add_clicked`/`divide_clicked` checked `self.equation == "."` instead of `self.equation[-1] == "."`; the leading-zero rule is now applied to digits 1–9 (the old code only fixed 9, so `5+08=` crashed); `multipy_clicked` renamed `multiply_clicked`; stopwatch Reset now refreshes the display; Contacts skips the CSV header row when opening and writes it when saving (the old site's table showed the header as a contact); the calculator UI is saved as `calculator.ui` (was `tutorial_06.ui`) and the To Do controller is `to_do_list.py` (was `to_do_app.py`); typos and the "three layouts"/four-listed and "For the first button" ×4 errors fixed. Bugs kept as exercises: `=` on an empty or unfinished equation (T7), timer starting from zero and spin boxes above 23/59/59 (T12), delete with no confirmation (T14), invalid JSON crash (T15).
- **Colour scheme:** olive bronze `#6B5B12` (header, tabs, light-mode links and headings; 6.7:1 with white text), `#8A7A2E` (primary light, decorative only), pale gold `#EDE3B0` (active and hovered tab 5.2:1 on the banner, dark-mode headings and accent), light blue `#8AB4F8` (dark-mode links). Set in `docs/stylesheets/extra.css`. It's different from the micro:bit (navy), Lego Spike (magenta), Turtle (teal), Deepest Dungeon (burnt orange) and Space Rescue (charcoal) banners.
- **Callouts:** six types, the same on all of Damien's tutorial sites:
    - `!!! learn "In this tutorial we will learn"` (tutorials) or `"On this page we will learn"` (other pages): amber, target icon, directly under the title. There are no videos.
    - `!!! terms "Terminology"`: grey, open book icon, straight after `learn`. `docs/reference/glossary.md` is generated from these callouts (84 terms); regenerate it if a callout changes.
    - `!!! primm "PRIMM"`: green, flask icon, after each change students run
    - `??? note "Code explanation"`: purple, `</>` icon, collapsed, after each snippet
    - `!!! tip "Title"`: light blue, light bulb icon, every other aside (including "Digital Solutions link" tips)
    - `!!! warning "Title"`: hot pink, triangle alert icon
- **Code blocks:** grey border on every code block; error messages use ```` ``` { .text .error linenums="1" } ```` (red border and text), followed by a line-by-line breakdown.
- **Writing style:** Australian English, written for Year 11/12, in Damien's inclusive "we" voice. Code explanations are `- **line n** → full sentence ending in a full stop.`, grouping routine lines (`lines 30–32` → a docstring…) and saying why. Qt Designer steps from Tutorial 6 on are grouped with property tables. Coding tutorials end with a **Commit and push** section, then `## Exercises` phrased as questions. Testing tables use the Digital Solutions format `Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action`.
- **Rework plan:** the audit and plan are in Damien's Claude project as `claude/PyQt-website_rework_plan.md`, with progress in `claude/PyQt-website_progress.md`.

## 1. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 5), so nothing is lost. Show Damien this list before deleting anything:

- root pages: `index.md`, `01_introduction.md` to `19_tutorial_17.md`
- Sphinx files: `conf.py`, `Makefile`, `make.bat`, `build/`, and `_build/` if it exists
- old content folder: `assets/` (the images in use were copied to `docs/assets/`, the downloads to `docs/downloads/`, and `diagrams.drawio` to `design/`). The code screenshots in `assets/img/07`–`19` were replaced by real code and weren't copied.
- `assets/.$diagrams.drawio.bkp` (draw.io backup, removed with `assets/`)
- notes: `topics.md` (an old list of callout texts) and `notes.md` (its two items, documentation links and extension activities, are now on the pages)

Keep `README.md`, `todo.md` (Damien's own task list), `LICENSE`, `.gitignore`, `.gitattributes` (if present), `requirements.txt`, `zensical.toml`, `VSCODE_CLAUDE_TASKS.md`, `docs/`, `scripts/`, `design/` and `.github/`.

Before deleting, search the repo to confirm nothing in `docs/`, `scripts/` or `zensical.toml` references these files. Then run `zensical build --clean`.

## 2. Replace the deploy workflow

Delete `.github/workflows/write_to_gh_pages.yml` and create `.github/workflows/deploy.yml` with the workflow below. It builds with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 3. Check assumptions that couldn't be tested in Cowork

1. **Qt Designer installer:** check <https://build-system.fman.io/qt-designer-download> still offers Windows and macOS installers, and that its Qt Designer opens and saves `.ui` files that PyQt6's `uic.loadUi` and `pyuic6` accept. If the page is gone, report it to Damien; don't pick a replacement yourself.
2. **`pyuic6 -x`:** confirm the option still exists in the current PyQt6 (`pyuic6 --help`).
3. **VS Code steps:** **Python: Create Environment** → **Venv** → tick `requirements.txt`, and that VS Code adds a `.gitignore` inside `.venv`. The PyQt6 Boiler Plate repo has no `.gitignore`; tell Damien if `.venv` shows up in GitHub Desktop's changes (see `todo.md`).
4. **Fonts:** the calculator uses Consolas (Windows) and suggests SF Mono or Menlo on macOS.
5. Run every final step file against Damien's `.ui` files in `C:\GitHub\PyQt6-website-tutorials` if PyQt6 is installed (copy the `.ui` files and `alarm_sound.wav` next to a copy of each step file and run it), and report any errors.

## 4. Final checks

1. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
2. Run `zensical build --clean`. Expected: `No issues found`.
3. Check every external link in `docs/` returns a working page (python.org, git-scm.com, GitHub Desktop, VS Code Marketplace, build-system.fman.io, doc.qt.io, riverbankcomputing.com, pythonguis.com, w3schools.com, the Digital Solutions 2025 text, Creative Commons, gnu.org). Report broken ones to Damien rather than guessing replacements.
4. Spell-check the pages for Australian English. Leave American spellings in code, Qt names (`Initialize` in the boilerplate docstring, `QColor`, `alignment` values) and quoted UI text as they are.
5. Commit to `zensical` and push.

## 5. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: **Settings** → **Pages** → **Source**, or `gh api -X PUT repos/DamoM73/PyQt-website/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that <https://damom73.github.io/PyQt-website/> shows the new site.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**
6. From now on, all work happens on `main`. Update the intro of this file to say so.

## Tasks for Damien (not for Claude)

These are also in `todo.md`, which Damien keeps up to date. Don't delete or edit it unless he asks.

- Work through each tutorial in Qt Designer and VS Code, checking the grouped Qt Designer steps (Tutorial 6 on) are clear enough without one click per line.
- Check the GIFs still match the current Qt Designer, GitHub Desktop and VS Code screens.
- Check the alarm sound plays on Windows and macOS.
- Decide whether to add a `.gitignore` to the PyQt6 Boiler Plate repo, and whether its README should match the new Setup page.
