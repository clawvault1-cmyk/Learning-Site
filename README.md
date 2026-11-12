# Proud Little Learners

Static website for [proudlittlelearners.com](https://proudlittlelearners.com). Pages are HTML, CSS, and JavaScript. No build step is required to open the site.

Owner launch steps, checkout URLs, and legal fill-in fields live in the private repo `clawvault1-cmyk/proud-little-learners-packs`, in `from-learning-site/LAUNCH.md`. Pack PDF generators also live there, not in this public repository.

## Open it locally

```bash
python3 -m http.server 8000
```

Then go to [http://localhost:8000/](http://localhost:8000/).

## GitHub Pages

Prefer **GitHub Actions** as the Pages source (not “Deploy from a branch”). The workflow in `.github/workflows/pages.yml` already strips leftover generator files and markdown before publishing. If Pages is still set to deploy the `main` branch from `/`, Jekyll uses `_config.yml` to keep `README.md` off the live site.
