import argparse
import sys
from collections import Counter
from scapy.all import rdpcap, IP, TCP, UDP

def summarize_pcap(path, max_packets):
    packets = rdpcap(path, count=max_packets) if max_packets else rdpcap(path)
    total = len(packets)
    proto_counter = Counter()
    src_counter = Counter()
    dst_counter = Counter()
    sport_counter = Counter()
    dport_counter = Counter()
    sizes = []
    for p in packets:
        sizes.append(len(p))
        if IP in p:
            src_counter[p[IP].src] += 1
            dst_counter[p[IP].dst] += 1
            proto_counter[p[IP].proto] += 1
        if TCP in p:
            sport_counter[p[TCP].sport] += 1
            dport_counter[p[TCP].dport] += 1
        elif UDP in p:
            sport_counter[p[UDP].sport] += 1
            dport_counter[p[UDP].dport] += 1
    out_lines = []
    out_lines.append(f"PCAP summary for: {path}")
    out_lines.append(f"Total packets: {total}")
    if total == 0:
        return "\n".join(out_lines)
    out_lines.append("")
    out_lines.append("Top 10 source IPs:")
    for ip, cnt in src_counter.most_common(10):
        out_lines.append(f"  {ip}: {cnt}")
    out_lines.append("")
    out_lines.append("Top 10 destination IPs:")
    for ip, cnt in dst_counter.most_common(10):
        out_lines.append(f"  {ip}: {cnt}")
    out_lines.append("")
    out_lines.append("Top protocols (number):")
    for proto, cnt in proto_counter.most_common(10):
        out_lines.append(f"  {proto}: {cnt}")
    out_lines.append("")
    out_lines.append("Top destination ports:")
    for port, cnt in dport_counter.most_common(10):
        out_lines.append(f"  {port}: {cnt}")
    out_lines.append("")
    out_lines.append(f"Packet size: min={min(sizes) if sizes else 0} max={max(sizes) if sizes else 0} avg={sum(sizes)/len(sizes) if sizes else 0:.2f}")
    return "\n".join(out_lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pcap", nargs=1)
    parser.add_argument("--max", type=int, default=0)
    args = parser.parse_args()
    path = args.pcap[0]
    max_packets = args.max if args.max > 0 else None
    summary = summarize_pcap(path, max_packets)
    print(summary)

if __name__ == "__main__":
    main()
