# AI Workstation — public learning PWA

GitHub Pages serves an anonymized software reference, educational cards, relationship diagrams and hierarchical workflows. The catalogue is extensible and independent of any live PC inventory. Missing/dashed public cards indicate tools outside the shared selection, not proof of absence from a PC.

## Local preview

```powershell
py -m http.server 8767 --bind 127.0.0.1
```

Open `http://127.0.0.1:8767/`. Modify the source, test locally, then publish the reviewed changes to `main`. The public PWA caches only known public assets. The browser can offer installation when its criteria are met.

## Private companion

Monitoring, password verification, real installed-app detection and remote access belong to a separate locally installed companion. Its source and state are deliberately excluded from this public repository. The public site does not receive a password or PC telemetry. Use the installed private application shortcut for setup and monitoring.

The local companion refreshes measurements every 5 seconds and inventory every 3 minutes. It keeps its data outside Git. It provides Argon2id password hashing, bounded sessions, CSRF protection and login throttling. Remote access is prepared through Tailscale Serve on a private network; the PC and agent must run. User setup is required before remote access is enabled.

No public server, subnet routing, exit node, SSH access or Tailscale Funnel is configured by the public site. Tailscale's open-source client and proprietary hosted coordination are distinguished in the catalogue. Headscale is a documented self-hosted alternative, requiring infrastructure and maintenance.

## Main public files

- `index.html`, `style.css`, `app.js`: base interface.
- `enhance.js`, `enhance.css`: educational cards, filters and hierarchical workflows.
- `catalog.json`: independent competency reference with licence evidence and learning steps.
- `stack.json`: original anonymized selection.
- `manifest.webmanifest`, `sw.js`, `icons/`: installable public PWA and public offline cache.
- `tests/test_public.py`: data consistency, privacy and cache checks.

## Checks

```powershell
py -m unittest discover -s tests -p test_public.py -v
node --check app.js
node --check enhance.js
node --check sw.js
```

Do not commit a password, private companion files, app listings, telemetry, runtime databases or local HTTPS hostnames. Open source, freeware, source-available software and open-weight models are different categories. Check the exact edition and licence before adopting a tool.
