# Proud Little Learners

Static website for [proudlittlelearners.com](https://proudlittlelearners.com). Pages are HTML, CSS, and JavaScript. No build step is required to open the site.

Owner launch steps, checkout URLs, and legal fill-in fields are in `_internal/LAUNCH.md`. That folder is not published on the live site.

## Open it locally

```bash
python3 -m http.server 8000
```

Then go to [http://localhost:8000/](http://localhost:8000/).

## GitHub Pages

Prefer **GitHub Actions** as the Pages source (not "Deploy from a branch"). `.github/workflows/pages.yml` removes internal files before publishing. If Pages is still set to deploy the `main` branch from `/`, Jekyll will skip the `_internal` folder.

Pack PDF generators live in the private repo `clawvault1-cmyk/proud-little-learners-packs`, not in this public repository.
