
# Hookdeck Relay Setup

1. Create a **Source** in Hookdeck called *TrendSpider*.
2. Create a **Destination** pointing to your Operator endpoint (`https://<operator-host>/webhook`).
3. In Source → Destinations, set retries: 3, exponential backoff.
4. Copy the **Source URL** into TrendSpider's webhook field.
