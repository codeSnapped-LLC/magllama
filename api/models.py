from pydantic import BaseModel
from datetime import datetime

class ScanMetadata(BaseModel):
    scan_date: datetime
    result: str
