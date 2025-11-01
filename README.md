# Network-Snifing

**Networsnifing** is a lightweight and educational toolkit for **offline network traffic analysis**.  
It lets you read `.pcap` files, summarize network packets, and visualize data through a clean, terminal-style interface.  
This project is meant for learning, security labs, and research — it does **not** capture live traffic.

---

## Features
- Analyze `.pcap` files offline (no live sniffing)
- View top IPs, ports, and protocol usage
- Simple TUI (terminal-based user interface) for quick summaries
- Modular Python code (easy to extend)
- Works on Linux, macOS, and Windows

---

## Project Structure
```
networsnifing/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ src/
│  ├─ pcap_summary.py       → analyzes pcap files
│  ├─ tui.py                → terminal interface
│  ├─ banner.py             → ASCII banner for UI
│  └─ utils.py
├─ examples/
│  ├─ sample_capture.pcap   → sample test file
│  └─ demo.md
├─ docs/
│  └─ how_to_use.md
└─ tests/
   └─ test_pcap_summary.py
```

---

## Installation
Clone the repository and set up your Python environment:

```bash
git clone https://github.com/yourusername/networsnifing.git
cd networsnifing

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Example Usage

### 1. Analyze a `.pcap` file
```bash
python -m src.pcap_summary examples/sample_capture.pcap
```

Sample output:
```
PCAP summary for: examples/sample_capture.pcap
Total packets: 42

Top 10 source IPs:
  192.0.2.1: 10

Top 10 destination IPs:
  198.51.100.2: 8

Top protocols (number):
  6: 30

Top destination ports:
  80: 25
  443: 10

Packet size: min=60 max=1514 avg=415.37
```

---

### 2. Run the Terminal UI
You can also visualize results in a **terminal-style interface**:

```bash
python -m src.tui
```

This will display the ASCII banner and a summary table directly in your console.

---

## Preview
You can place your terminal screenshot or banner image here 👇  
(replace the file name once you upload it to the repo)

![Terminal Preview](./terminal_with_banner.png)

---

## Sample Code Snippet

You can easily use `pcap_summary` as a module in your own scripts:

```python
from src.pcap_summary import summarize_pcap

result = summarize_pcap("examples/sample_capture.pcap", max_packets=100)
print(result)
```

This lets you integrate packet analysis directly into your own Python projects or automation scripts.

---

## Legal & Ethical Notice
This toolkit is strictly for **educational and authorized** use only.  
Never use it to intercept or analyze traffic that you do not have explicit permission to capture.  
The developers assume no responsibility for misuse of the code.

---

## License
This project is licensed under the **MIT License** — feel free to use and modify it for your own experiments.

---

## Contributing
Contributions welcome: open an issue or submit a pull request. Please add tests for new features and keep code style consistent.
