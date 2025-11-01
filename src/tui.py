from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from pathlib import Path
from .banner import get_banner

def render_mock_summary(pcap_path):
    console = Console()
    banner = get_banner()
    console.print(banner)
    table = Table(title="networsnifing summary")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    table.add_row("pcap file", str(pcap_path))
    table.add_row("total packets", "42")
    table.add_row("top src ip", "192.0.2.1")
    table.add_row("top dst ip", "198.51.100.2")
    table.add_row("top proto", "6 (TCP)")
    panel = Panel(Align.center(table), title="terminal")
    console.print(panel)

def main():
    p = Path("examples/sample_capture.pcap")
    render_mock_summary(p)

if __name__ == "__main__":
    main()
