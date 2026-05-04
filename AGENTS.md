# AGENTS.md

Odoo 19 custom apps repository. Modules live at repo root.

## Modules

- `tonicapp_demo` - Demo module with `tonic.demo` model
- `tonicapp_lens_memoria` - Photo fonds management (Lens Memory)

## Module structure

Each module: `__manifest__.py`, `__init__.py`, `models/`, `views/`, `security/`, `tests/`

Import pattern: `from odoo import models, fields`

## Development (Doodba)

Requires Doodba framework. Commands from repo root:

```
invoke git-aggregate  # Pull modules into Doodba
invoke img-build      # Build Odoo image
invoke start          # Start Odoo instance
```

Install modules via Apps menu in Odoo UI after deployment.

## Notes

- Modules were renamed from `tonicappdemo` → `tonicapp_demo`
- Odoo 19.0 targeted (`$ODOO_VERSION` in Doodba config)
- No CI workflows configured yet
