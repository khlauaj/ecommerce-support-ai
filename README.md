# ecommerce-support-ai

# Landed (working name)

**Know the true cost of anything you see on an overseas site — before you buy.**

Paste a product page or screenshot from any overseas store, and get an instant landed-cost estimate: item price, domestic shipping, forwarding fee, duties and VAT. Add several items to one cart and see how consolidating them cuts the shipping cost per item.

---

## The problem

UK shoppers who want products from Japan or China usually can't buy them directly. Local stores carry a small selection of overseas goods, so shoppers turn to proxy-buying services or parcel forwarders.

The friction comes in three layers:

1. **Can't read it.** Product pages are in Japanese or Chinese, with specs buried in descriptions.
2. **Can't calculate it.** Many pages don't list packaged dimensions or weight. Even when they do, most shoppers don't know how volumetric weight works.
3. **Don't know the total.** Item price + domestic shipping + forwarding fee + duties and VAT + service fees. Shoppers have to leave the product page, open a forwarder's calculator, and estimate inputs they don't have.

Every step between "I want this" and "I know what it really costs" is a point where shoppers give up.

## Who it's for (MVP)

UK-based shoppers buying from **[Decide: Japan or China]** marketplaces through a parcel forwarder.

## Evidence

- [Add: what you observed about this problem during your time in cross-border logistics]
- [Add: findings from user interviews, Week 2]

## How it works: AI understands, code calculates

| Step | Done by | Why |
|---|---|---|
| Extract product name, price, specs from page or screenshot | AI | Messy, multilingual, unstructured input |
| Estimate packaged dimensions and weight when missing, with a range | AI | Requires judgement about product type and packaging |
| Flag prohibited or restricted items (batteries, liquids, etc.) | AI, verified by rules | Protects users and the business |
| Calculate volumetric weight, forwarding fee, duties and VAT | Code | Deterministic rules; must be exact and auditable |
| Calculate consolidation savings across cart items | Code | Deterministic |

## Non-AI alternatives

- **Forwarders' own calculators:** accurate if you know the weight and dimensions, but most shoppers don't.
- **Proxy-buying platforms:** handle purchasing end to end, but each covers a limited set of source sites or countries.

## MVP scope

| In | Out |
|---|---|
| One source market | Multiple source countries |
| One forwarder with a public rate table: **[Decide]** | Comparing multiple forwarders |
| Input via pasted page content or screenshot | Browser extension, automatic scraping |
| Landed-cost estimate shown as a range | Guaranteed quotes |
| Cart with consolidation savings | Real checkout and payment |
| Prohibited-item flags | Customs paperwork |

## Success metrics

**Estimate quality** (core — this is what earns user trust)
- Weight and dimension estimation error vs. actual specs
- Share of landed-cost estimates within ±10% of the actual cost — target set after baseline

**User value**
- Time from seeing a product to knowing its landed cost

**Demand validation**
- Number of user interviews completed
- Waitlist sign-ups after launch

## Hypotheses to validate

1. Cost uncertainty is a main reason shoppers abandon overseas purchases.
2. An estimate shown as a range is accurate enough for shoppers to make a buying decision.
3. Showing consolidation savings increases the number of items per order.

## Risks

- **Counterfeit and prohibited goods:** flag high-risk items from day one.
- **Estimate liability:** always show a range and a clear disclaimer; never present an estimate as a quote.
- **Rate changes:** forwarder rate tables must be versioned and easy to update.

## Roadmap

- **Week 2:** build the extraction → estimation → calculation pipeline; run user interviews
- **Week 3:** build an eval set from real product pages with known specs; iterate on estimation accuracy
- **Week 4:** landing page, waitlist, launch write-up

## Long-term vision

Remove the information barrier to overseas shopping, so anyone can buy from any overseas site as easily as a local one.

The same engine can serve businesses: a landed-cost estimation API for forwarders and cross-border platforms.
