
# Breakout Ignition 🚀

Automated “Strong Go” breakout system using **TrendSpider**, **Operator**, and **Interactive Brokers**.

> **Goal:** Detect high‑probability bullish breakouts (GoNoGo Trend Pro = 2) and fire bracket‑protected market orders within < 500 ms via Operator.

## Quick Start

```bash
# 1 – fork/clone
git clone https://github.com/<your‑handle>/breakout‑ignition.git
cd breakout‑ignition

# 2 – install dev helpers
python -m venv .venv && source .venv/bin/activate
pip install -r tests/requirements.txt

# 3 – copy secrets template
cp operator/secrets_template.env operator/.env

# 4 – push to GitHub
git add . && git commit -m "Initial commit" && git push origin main
```

See each folder’s README for component‑specific docs.  
Not investment advice; use at your own risk.

## Directory Guide

| Folder | What’s inside |
|--------|---------------|
| **trendspider/** | JSON exports for the Daily & 30‑min scans + usage tips. |
| **operator/** | The Operator task template, environment variables, install steps. |
| **relay/** | Example configs for Hookdeck & Pipedream if direct webhooks are blocked. |
| **docs/** | Markdown site served via GitHub Pages (auto‑deployed by `.github/workflows/pages.yml`). |
| **tests/** | Python script to replay a webhook event for smoke‑testing Operator. |
