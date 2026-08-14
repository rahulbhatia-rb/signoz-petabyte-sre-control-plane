# Ingest Freshness Incident Playbook

1. Confirm customer-facing freshness SLO impact.
2. Inspect queue depth and collector saturation.
3. Check autoscaling and pending pods.
4. Check ClickHouse insert latency, merges, disk pressure, replication lag.
5. Isolate noisy tenants if required.
6. Roll back recent deploys when burn correlates with rollout.
7. Restore capacity headroom.
8. Capture permanent automation in the postmortem.
