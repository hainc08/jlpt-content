"""Kiểm tra dữ liệu Kanji (kanji/<app>.json) — GitHub Actions tự chạy mỗi lần push.

App chỉ nhận một file khi: đọc được JSON, có ≥ 20 chữ, không trùng chữ, không trùng nghĩa,
mỗi chữ có Hán Việt, nghĩa và ít nhất một cách đọc (On hoặc Kun). File sai sẽ bị app bỏ qua.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent


def main():
    errors = []
    files = sorted(ROOT.glob("*.json"))
    seen_all = {}
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            items = data["kanji"]
        except Exception as e:  # noqa: BLE001
            errors.append(f"{f.name}: JSON lỗi hoặc thiếu 'kanji' — {e}")
            continue
        if len(items) < 20:
            errors.append(f"{f.name}: chỉ có {len(items)} chữ (cần ≥ 20)")
        chars, meanings = {}, {}
        for i, k in enumerate(items, 1):
            where = f"{f.name} dòng #{i} ({k.get('char', '?')})"
            for key in ("char", "hanViet", "meaning"):
                if not str(k.get(key, "")).strip():
                    errors.append(f"{where}: thiếu '{key}'")
            if not (str(k.get("on", "")).strip() or str(k.get("kun", "")).strip()):
                errors.append(f"{where}: cần ít nhất 'on' hoặc 'kun'")
            c, m = k.get("char"), str(k.get("meaning", "")).strip()
            if c in chars:
                errors.append(f"{where}: trùng chữ với #{chars[c]}")
            chars[c] = i
            if m in meanings:
                errors.append(f"{where}: trùng nghĩa '{m}' với #{meanings[m]} (quiz cần nghĩa khác nhau)")
            meanings[m] = i
            if c in seen_all and seen_all[c] != f.name:
                print(f"CẢNH BÁO: {where}: chữ đã có trong {seen_all[c]}")
            seen_all.setdefault(c, f.name)
        print(f"{f.name}: {len(items)} chữ")
    for e in errors:
        print("LỖI:", e)
    if errors:
        sys.exit(1)
    print("OK — dữ liệu Kanji hợp lệ")


if __name__ == "__main__":
    main()
