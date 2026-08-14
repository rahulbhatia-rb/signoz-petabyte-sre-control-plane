import json
from pathlib import Path
from src.signoz_sre.gate import evaluate

def load(name):
    return json.loads((Path(__file__).parents[1]/"examples"/name).read_text())

def test_production_passes():
    r = evaluate(load("production-ingest.json"))
    assert r.allowed and r.findings == []

def test_unsafe_fails():
    r = evaluate(load("unsafe-ingest.json"))
    assert not r.allowed and len(r.findings) >= 15
