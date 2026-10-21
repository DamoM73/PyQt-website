# PyQt Tutorials

Tutorials for building desktop GUI apps in Python with [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) and Qt Designer. Written for Year 11/12 Digital Solutions students using VS Code, GitHub Desktop and Qt Designer, and linked to the [Digital Solutions 2025](https://damom73.github.io/digital-solutions-text-2025/) text.

Live site: <https://damom73.github.io/PyQt-website/>

Students start from the [PyQt6 Boiler Plate](https://github.com/DamoM73/PyQt6-Boiler-Plate) repo and build four apps: a calculator, the Time Machine (clock, stopwatch and timer), a To Do List and a Contacts app.

## Preview the site

```
python -m pip install -r requirements.txt
zensical serve
```

Then open <http://localhost:8000>. To build the site: `zensical build --clean` (expect `No issues found`).

## Checks

- `python scripts/check_explanations.py` checks every Code explanation box against the code it explains (expect `0 issue(s) found`).

## Layout

```
zensical.toml                 site config and navigation
docs/
  index.md                    home page
  start/                      introduction and setup
  basics/                     Tutorials 1-5 (Qt Designer workflow, signals and slots)
  calculator/                 Tutorials 6-7
  time_machine/               Tutorials 8-12
  to_do/                      Tutorials 13-15
  contacts/                   Tutorials 16-17
  reference/                  boilerplate code, common errors, exercise solutions, glossary, licence
  examples/<section>/<tutorial>/stepNN/<file>.py
                              every version of every file shown on a page
  solutions/<section>/<tutorial>/exN_name.py
                              exercise solutions
  assets/                     images and GIFs
  downloads/                  mr-coder.png, alarm_sound.wav, contacts.csv
  stylesheets/extra.css       colours, callouts and code block styles
scripts/                      check_explanations.py
design/                       draw.io source for the diagrams
```

Pages include step files with `--8<-- "examples/..."` and mark new or changed lines with `hl_lines`.

## Licence

Content is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Code is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
