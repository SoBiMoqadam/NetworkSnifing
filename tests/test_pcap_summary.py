import pytest
from pathlib import Path
from src.pcap_summary import summarize_pcap
def test_empty_pcap(tmp_path):
    p = tmp_path / "e.pcap"
    p.write_bytes(b"")
    s = summarize_pcap(str(p), None)
    assert "Total packets" in s
