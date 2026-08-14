from dataclasses import dataclass

@dataclass
class Result:
    allowed: bool
    findings: list[str]

def evaluate(spec: dict) -> Result:
    k = spec.get("kubernetes", {})
    s = spec.get("slo", {})
    i = spec.get("ingest", {})
    c = spec.get("clickhouse", {})
    checks = [
        (spec.get("owner"), "service owner is required"),
        (k.get("requests_limits") is True, "Kubernetes requests and limits are required"),
        (k.get("autoscaling") is True, "autoscaling is required"),
        (k.get("multi_az") is True, "multi-AZ scheduling is required"),
        (k.get("pdb") is True, "PodDisruptionBudget is required"),
        (i.get("backpressure") is True, "ingest backpressure is required"),
        (i.get("queue_alert") is True, "queue-depth alerting is required"),
        (i.get("capacity_headroom_percent",0) >= 30, "at least 30% ingest headroom is required"),
        (s.get("availability",0) >= 99.9, "availability SLO must be at least 99.9%"),
        (s.get("freshness_seconds",9999) <= 60, "freshness SLO must be 60 seconds or less"),
        (s.get("error_budget_policy") is True, "error-budget policy is required"),
        (c.get("replication") is True, "ClickHouse replication is required"),
        (c.get("retention_policy") is True, "ClickHouse retention policy is required"),
        (c.get("capacity_alerts") is True, "ClickHouse capacity alerts are required"),
        (set(["logs","metrics","traces"]).issubset(set(spec.get("observability",[]))), "logs, metrics, and traces are required"),
        (spec.get("tenant_isolation") is True, "tenant isolation is required"),
        (spec.get("workload_identity") is True, "workload identity is required"),
        (spec.get("managed_secrets") is True, "managed secrets are required"),
        (spec.get("progressive_delivery") is True, "progressive delivery is required"),
        (spec.get("automatic_rollback") is True, "automatic rollback is required"),
        (spec.get("runbook"), "runbook is required"),
        (spec.get("oncall_owner"), "on-call owner is required"),
        (spec.get("cost_owner"), "cost owner is required"),
    ]
    findings = [msg for ok, msg in checks if not ok]
    return Result(not findings, findings)
