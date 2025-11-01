from collections import defaultdict

def extract_flows(packets):
    flows = defaultdict(list)
    for p in packets:
        try:
            ip = p['IP']
            key = (ip.src, ip.dst, p.payload.name if hasattr(p, 'payload') else 'raw')
            flows[key].append(p)
        except Exception:
            continue
    return flows

def flow_durations(flows):
    durations = {}
    for k, pkts in flows.items():
        times = [getattr(p, 'time', None) for p in pkts]
        times = [t for t in times if t is not None]
        if not times:
            durations[k] = 0
        else:
            durations[k] = max(times) - min(times)
    return durations
