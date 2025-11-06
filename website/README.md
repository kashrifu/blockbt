# BlockBT Website Deployment Guide

This website can be deployed to various platforms. Here are the options:

## Option 1: GitHub Pages (Recommended)

1. **Create a `gh-pages` branch:**
   ```bash
   git checkout -b gh-pages
   git push origin gh-pages
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from `gh-pages` branch
   - Your site will be live at: `https://yourusername.github.io/blockbt/`

## Option 2: Netlify

1. **Drag and drop:**
   - Go to [netlify.com](https://netlify.com)
   - Drag the `website/` folder to Netlify
   - Site is live instantly

2. **Or connect GitHub:**
   - Connect your repository
   - Build command: (none needed for static site)
   - Publish directory: `website/`

## Option 3: Vercel

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   cd website
   vercel
   ```

## Local Development

Serve locally:
```bash
cd website
python -m http.server 8000
# Open http://localhost:8000
```

