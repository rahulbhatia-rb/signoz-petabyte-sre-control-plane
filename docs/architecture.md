# Architecture Notes

Key platform signals: ingest queue depth, telemetry freshness, p95/p99 ingest latency, dropped telemetry, error-budget burn, ClickHouse disk/merge pressure, query latency, node/pod saturation, rollout health.

Failure modes modeled:
1. Burst exceeds collector/queue capacity.
2. HPA reacts too slowly.
3. ClickHouse saturation hurts freshness.
4. Noisy tenant creates contention.
5. Cluster upgrade disrupts stateful workloads.
6. Bad rollout raises latency without obvious errors.
7. Replication lag increases recovery risk.
8. Alert storms create on-call fatigue.
