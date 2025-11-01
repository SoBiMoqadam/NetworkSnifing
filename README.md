# networsnifing

A safe, educational toolkit for offline network traffic analysis and a small terminal-style UI mockup.
This project analyzes `.pcap` files only and does not capture live traffic.

Quick start
1. Clone the repo
2. Create virtualenv and install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run a summary
python -m src.pcap_summary examples/sample_capture.pcap

Legal & Ethical
Only analyze pcap files you have explicit permission to use.


Banner demo image: terminal_with_banner.png

Run the TUI demo:

```bash
python -m src.tui
```
