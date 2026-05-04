# Tonic App Demo

A demo module for Odoo 19 by Toni.

## Description

This module provides a simple demo model `tonic.demo` to showcase custom Odoo app
development within the Doodba framework.

## Features

- Provides `tonic.demo` model with basic fields
- Simple structure ready to extend
- Follows Odoo 19.0 conventions

## Installation

1. Clone the `tonicaodooapps` repository into your Doodba project:
   ```yaml
   # odoo/custom/src/repos.yaml
   ./tonicaodooapps:
     defaults:
       depth: $DEPTH_DEFAULT
     remotes:
       origin: https://github.com/tonica/tonicaodooapps.git
     target: origin $ODOO_VERSION
     merges:
       - origin $ODOO_VERSION
   ```

2. Enable the module in `addons.yaml`:
   ```yaml
   ./tonicaodooapps:
     - "*"
   ```

3. Run:
   ```bash
   invoke git-aggregate
   invoke img-build
   invoke start
   ```

4. Install **Tonic App Demo** from the Apps menu in Odoo.

## Usage

After installation, you can access the demo model through the Odoo shell:

```python
# -*- coding: utf-8 -*-
from odoo import models, fields

# Create a demo record
env['tonic.demo'].create({
    'name': 'Test Demo',
    'description': 'This is a demo record',
})
```

## Known issues / Roadmap

- Add views for the demo model
- Add demo data
- Add tests

## Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/tonica/tonicaodooapps/issues).

## Credits

### Author

- Toni

### Maintainer

This module is maintained by Toni.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

See [LICENSE](https://www.gnu.org/licenses/agpl-3.0-standalone.html) for details.
