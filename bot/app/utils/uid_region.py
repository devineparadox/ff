def region_from_uid(uid: str) -> str:
    """Infer region from UID using pattern heuristics.
    Replace with real mapping from your own research.
    """
    try:
        n = int(uid)
    except ValueError:
        return "unknown"
    # Demo ranges (PLACEHOLDER). Replace with your own mapping.
    if 10000000 <= n < 20000000:
        return "sg"
    if 20000000 <= n < 30000000:
        return "ind"
    if 30000000 <= n < 40000000:
        return "br"
    return "unknown"
