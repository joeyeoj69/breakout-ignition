
---
title: Breakout Ignition
---

# Breakout Ignition 📈

A fully‑automated TrendSpider → Operator → IBKR pipeline that hunts
**GoNoGo Trend Pro = 2 “Strong Go”** breakouts and fires bracketed market orders.

<!-- architecture image placeholder -->
![Architecture](architecture.png)

## Components
| Layer | Tech |
|-------|------|
| Scanner | TrendSpider Advanced Scans (JSON in repo) |
| Automation | Operator task template |
| Broker | IBKR Gateway / TWS |
| Relay (optional) | Hookdeck or Pipedream |
| Docs Hosting | GitHub Pages |
