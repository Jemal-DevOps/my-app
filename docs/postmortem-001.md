# Post-Mortem Report — Incident 001
**Date:** 2026-05-20  
**Severity:** P2 — Elevated Error Rate  
**Duration:** 12 minutes (simulated)  
**Author:** Jemal DevOps  
**Status:** Resolved

---

## Summary
A spike in HTTP 404 errors was detected on the myapp service,
triggering the High Error Rate alert in Grafana. The alert fired
after the error rate exceeded 0.1 req/s for 1 minute. Root cause
was traffic hitting a non-existent endpoint `/nonexistent`.
No data loss occurred.

---

## Timeline
| Time | Event |
|---|---|
| 00:00 | Traffic spike begins, mix of valid and invalid requests |
| 00:01 | Error rate crosses 0.1 req/s threshold |
| 00:02 | Grafana alert fires — High Error Rate rule triggered |
| 00:04 | Engineer investigates Grafana dashboard |
| 00:06 | Prometheus query confirms 404s from `/nonexistent` endpoint |
| 00:10 | Root cause identified — invalid endpoint in traffic pattern |
| 00:12 | Traffic normalised, alert resolved |

---

## Root Cause
HTTP requests were being sent to `/nonexistent` which has no
registered route in the Flask application. Flask returns 404
for unregistered routes. The error rate alert correctly
identified the degradation within 2 minutes of onset.

---

## What Went Well
- Alert fired within 2 minutes of threshold breach
- Grafana dashboard made root cause immediately visible
- Prometheus metrics clearly separated 200 vs non-200 responses
- Pipeline continued deploying normally throughout the incident

---

## What Could Be Improved
- Add request logging to capture full request paths for faster diagnosis
- Set up Alertmanager to route alerts to Slack for faster response
- Add scrape interval reduction during incidents for finer granularity
- Consider rate limiting to protect against traffic spikes

---

## Action Items
| Action | Owner | Priority |
|---|---|---|
| Add structured JSON logging to Flask app | Jemal | High |
| Configure Alertmanager Slack integration | Jemal | Medium |
| Add request path label to Prometheus metrics | Jemal | Medium |
| Write runbook for error rate alerts | Jemal | Low |

---

## Metrics During Incident
- Peak error rate: ~0.4 req/s
- Affected endpoint: `/nonexistent`
- Successful requests unaffected: 100%
- MTTD (Mean Time To Detect): 2 minutes
- MTTR (Mean Time To Resolve): 12 minutes

---

## Lessons Learned
Monitoring without alerting is just data. The value of this
observability stack is not the dashboards — it is the 2-minute
MTTD. In a production system processing thousands of requests,
detecting degradation in 2 minutes instead of hours directly
translates to reduced customer impact and revenue protection.
