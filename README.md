# SigNoz Petabyte-Scale SRE Control Plane

A SigNoz-specific proof-of-work for the Senior Site Reliability Engineer role, focused on Kubernetes failure modes under load, bursty ingest, ClickHouse reliability/cost, OpenTelemetry dogfooding, SLO/error-budget automation, multi-tenant safety, capacity planning, and small-team operability.

## Core idea
Make reliability policy executable.

```text
OTel telemetry -> collectors -> burst/backpressure gate -> ClickHouse -> SLO/error-budget engine
                                                        -> capacity / rollback / incident signals
```

## What this POC models
- Kubernetes requests/limits, autoscaling, PDBs, multi-AZ
- burst handling, queue-depth alerts, capacity headroom
- telemetry freshness and availability SLOs
- ClickHouse replication, retention, capacity alerts
- logs + metrics + traces for SigNoz itself
- tenant isolation, workload identity, managed secrets
- progressive delivery + automatic rollback
- on-call ownership, runbooks, and cost ownership

## Why this maps to SigNoz
The interesting failures are not basic deployment failures. They are cases where ingest spikes outrun scaling, one tenant hurts others, ClickHouse saturation degrades freshness, upgrades interact badly with stateful workloads, or a rollout raises p95 latency without obvious 5xx errors.

## Repository
- `src/signoz_sre/gate.py` — executable readiness gate
- `examples/production-ingest.json` — safe contract
- `examples/unsafe-ingest.json` — deliberately unsafe contract
- `tests/test_gate.py` — validation tests
- `docs/architecture.md` — failure modes and design notes
- `docs/incident-playbook.md` — example ingest incident workflow

## Run
```bash
python -m pytest -q
```

## 30 / 60 / 90 direction
**0-30:** map ingest/Kubernetes/ClickHouse failure modes, SLOs, burn rates, alert quality, upgrade/rollback paths.

**31-60:** standardize readiness contracts, burst/capacity signals, progressive delivery, restore/failover drills.

**61-90:** automate capacity forecasting, harden tenant isolation, optimize ClickHouse hotspots, make upgrades boring and repeatable.

## Candidate
Rahul H Bhatia — Cloud / Platform / SRE Engineering

- LinkedIn: https://www.linkedin.com/in/rahul-h-bhatia/
- Portfolio: https://rahulhbhatia.vercel.app
- AWS badges: https://www.credly.com/users/rahul-h-bhatia/badges

## Disclaimer
Independent proof-of-work based only on the public role description; not SigNoz private architecture.
