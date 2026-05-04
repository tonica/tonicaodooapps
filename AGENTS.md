# AGENTS.md

Odoo 19 custom apps repository. Modules live at repo root (not nested in addons/).

## Module structure

Each module: `__manifest__.py`, `__init__.py`, `models/`, `views/`, `security/`, `tests/`

Import pattern: `from odoo import models, fields`

## Development (Doodba)

Requires Doodba framework. Commands from repo root (not module dirs):

```
invoke git-aggregate  # Pull modules into Doodba
invoke img-build      # Build Odoo image
invoke start          # Start Odoo instance
```

Install modules via Apps menu in Odoo UI after deployment.

## Known quirks

- `lens_memoria` was recently flattened from `addons/lens_memoria/lens_memoria` to repo root
- Module directories contain stub dirs (`models/`, `tests/`, etc.) that may be empty
- No CI workflows configured yet (`.github/workflows/` empty)
- Odoo 19.0 targeted (`$ODOO_VERSION` in Doodba config)
