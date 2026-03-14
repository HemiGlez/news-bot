from datetime import datetime

def dt_to_str(dt: datetime) -> str:
    return dt.isoformat()

def str_to_dt(s: str) -> datetime:
    return datetime.fromisoformat(s)
