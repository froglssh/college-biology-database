#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
大學普通生物學補充知識庫 - 快速檢索工具 (search_campbell_kb.py)
依據 Campbell Biology 13th 補充高中生物教學
"""
import os, sys, argparse, re

KB_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(KB_DIR, "01_普通生物學核心庫", "units")):
    UNITS_DIR = os.path.join(KB_DIR, "01_普通生物學核心庫", "units")
else:
    UNITS_DIR = os.path.join(KB_DIR, "units")

UNIT_FILES = {
    1: ("Unit 1 生命的化學基礎 (Ch 1-5)", "Unit01_生命的化學基礎_Ch01-05.md"),
    2: ("Unit 2 細胞生物學 (Ch 6-12)", "Unit02_細胞生物學_Ch06-12.md"),
    3: ("Unit 3 遺傳學與分子生物學 (Ch 13-21)", "Unit03_遺傳學與分子生物學_Ch13-21.md"),
    4: ("Unit 4 演化機制 (Ch 22-25)", "Unit04_演化機制_Ch22-25.md"),
    5: ("Unit 5 生命多樣性演化史 (Ch 26-34)", "Unit05_生命多樣性演化史_Ch26-34.md"),
    6: ("Unit 6 植物形態與生理 (Ch 35-39)", "Unit06_植物形態與生理_Ch35-39.md"),
    7: ("Unit 7 動物形態與生理 (Ch 40-51)", "Unit07_動物形態與生理_Ch40-51.md"),
    8: ("Unit 8 生態學與保育 (Ch 52-56)", "Unit08_生態學與保育_Ch52-56.md"),
}

CHAPTER_UNIT_MAP = {}
for ch in range(1, 6): CHAPTER_UNIT_MAP[ch] = 1
for ch in range(6, 13): CHAPTER_UNIT_MAP[ch] = 2
for ch in range(13, 22): CHAPTER_UNIT_MAP[ch] = 3
for ch in range(22, 26): CHAPTER_UNIT_MAP[ch] = 4
for ch in range(26, 35): CHAPTER_UNIT_MAP[ch] = 5
for ch in range(35, 40): CHAPTER_UNIT_MAP[ch] = 6
for ch in range(40, 52): CHAPTER_UNIT_MAP[ch] = 7
for ch in range(52, 57): CHAPTER_UNIT_MAP[ch] = 8

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def search_query(query, unit_filter=None, chapter_filter=None):
    print(f"\n=======================================================")
    print(f" 🔍 大學普生補充知識庫檢索結果")
    if query:
        print(f" 關鍵字: '{query}'")
    if unit_filter:
        print(f" 單元過濾: Unit {unit_filter}")
    if chapter_filter:
        print(f" 章節過濾: Chapter {chapter_filter}")
    print(f"=======================================================\n")

    target_units = []
    if chapter_filter and chapter_filter in CHAPTER_UNIT_MAP:
        target_units = [CHAPTER_UNIT_MAP[chapter_filter]]
    elif unit_filter and unit_filter in UNIT_FILES:
        target_units = [unit_filter]
    else:
        target_units = list(UNIT_FILES.keys())

    matches_found = 0
    for u in target_units:
        title, fname = UNIT_FILES[u]
        fpath = os.path.join(UNITS_DIR, fname)
        content = read_file(fpath)
        if not content:
            continue

        # If chapter filter, let's locate the Chapter section in the file
        sections = content.split("### ")
        unit_header = sections[0]

        matched_sections = []
        if chapter_filter:
            ch_str = f"Chapter {chapter_filter}:"
            ch_pattern = re.compile(rf"(Chapter\s+{chapter_filter}[:\s]|Concept\s+{chapter_filter}\.)", re.IGNORECASE)
            for sec in sections[1:]:
                sec_text = "### " + sec
                if ch_pattern.search(sec_text) or (query and query.lower() in sec_text.lower()):
                    matched_sections.append(sec_text)
        elif query:
            q_lower = query.lower()
            for sec in sections[1:]:
                sec_text = "### " + sec
                if q_lower in sec_text.lower():
                    matched_sections.append(sec_text)
        else:
            # Display overview
            matched_sections = [sections[1]] if len(sections) > 1 else []

        if matched_sections:
            print(f"📘 【{title}】(來源檔案: units/{fname})")
            print("-" * 55)
            for m in matched_sections:
                matches_found += 1
                lines = m.strip().split("\n")
                header = lines[0]
                print(f"▶ {header}")
                # Print preview lines highlighting query
                body_lines = [l for l in lines[1:12] if l.strip()]
                for bl in body_lines[:6]:
                    print(f"   {bl[:120]}")
                print("   ...")
                print()

    if matches_found == 0:
        print("❌ 未找到相符的知識條目。請嘗試換個關鍵字或移除過濾條件。")
    else:
        print(f"共找到 {matches_found} 個相關主題區塊。詳細機制請參閱對應 units/ Markdown 檔案。\n")

def main():
    parser = argparse.ArgumentParser(description="大學普通生物學補充知識庫檢索工具 (Campbell 13th)")
    parser.add_argument("-q", "--query", type=str, default="", help="關鍵字檢索 (例如: 光合作用, 逆流倍增, CRISPR)")
    parser.add_argument("-u", "--unit", type=int, default=None, choices=range(1, 9), help="依單元篩選 (1-8)")
    parser.add_argument("-c", "--chapter", type=int, default=None, choices=range(1, 57), help="依章節篩選 (1-56)")
    parser.add_argument("--curriculum", type=str, default="", help="依高中課綱模組篩選 (必修生物, 選修生物I, 選修生物II, 選修生物III)")

    args = parser.parse_args()

    q = args.query
    if args.curriculum:
        q = args.curriculum if not q else f"{q} {args.curriculum}"

    if not q and args.unit is None and args.chapter is None:
        print("提示：請輸入檢索關鍵字或指定單元/章節。")
        print("例如: python3 search_campbell_kb.py -q '光反應'")
        print("      python3 search_campbell_kb.py -c 9")
        print("      python3 search_campbell_kb.py -u 2\n")
        search_query("細胞呼吸")
        return

    search_query(q, unit_filter=args.unit, chapter_filter=args.chapter)

if __name__ == "__main__":
    main()
