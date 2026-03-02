#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))
from app.services.excel_logic_parser import parse_workbook


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: extract_excel_logic.py <workbook.xlsx>")
    parsed = parse_workbook(sys.argv[1])
    print(json.dumps(parsed, indent=2, default=str))


if __name__ == "__main__":
    main()
