#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
大學生物資料庫 (College Biology Academic Database) - 跨書跨庫快速檢索工具
依據 /Users/froglssh/Library/CloudStorage/GoogleDrive-frog@lssh.tp.edu.tw/我的雲端硬碟/04生物教學/bio
典藏之世界經典大學生物教材建立
"""
import os, sys, argparse, re

DB_DIR = os.path.dirname(os.path.abspath(__file__))

MODULE_MAP = {
    1: ("01_普通生物學核心庫", "普生核心庫 (Campbell 12th, Raven, Science for Life, CliffsAP)"),
    2: ("02_動物學與生物多樣性庫", "動物學庫 (Miller-Harley Zoology, Hickman Animal Diversity)"),
    3: ("03_生物化學與分子生理庫", "生化分子生理庫 (王鏡岩《生物化學》, 生殖生物學)"),
    4: ("04_數理生物學與科研方法庫", "數理生物與科研方法 (J.D. Murray, Biological Physics, How Science Works)"),
    5: ("05_MacMillan生物科學百科索引", "MacMillan 百科全書 (Richard Robinson Vol 1-4)")
}

def scan_markdown_files(target_dir):
    files = []
    for root, dirs, filenames in os.walk(target_dir):
        for f in filenames:
            if f.endswith(".md"):
                files.append(os.path.join(root, f))
    return files

def search_database(query="", module_filter=None, book_filter="", curriculum_filter=""):
    print("\n" + "=" * 65)
    print(" 🔍 大學生物資料庫 (College Biology Database) 檢索結果")
    if query: print(f" 關鍵字: '{query}'")
    if module_filter: print(f" 子庫篩選: Module {module_filter} - {MODULE_MAP[module_filter][1]}")
    if book_filter: print(f" 典藏書目: '{book_filter}'")
    if curriculum_filter: print(f" 高中課綱對接: '{curriculum_filter}'")
    print("=" * 65 + "\n")

    target_dirs = []
    if module_filter and module_filter in MODULE_MAP:
        target_dirs.append(os.path.join(DB_DIR, MODULE_MAP[module_filter][0]))
    else:
        for m in MODULE_MAP:
            target_dirs.append(os.path.join(DB_DIR, MODULE_MAP[m][0]))
        target_dirs.append(DB_DIR)  # Also include root guidance files

    matched_sections = 0

    for d in target_dirs:
        md_files = scan_markdown_files(d)
        for filepath in md_files:
            rel_path = os.path.relpath(filepath, DB_DIR)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue

            # Check book filter
            if book_filter and book_filter.lower() not in text.lower() and book_filter.lower() not in rel_path.lower():
                continue

            # Check curriculum filter
            if curriculum_filter and curriculum_filter.lower() not in text.lower():
                continue

            # Search in sections (split by ## or ###)
            sections = re.split(r'\n(?=#{1,3}\s)', text)
            file_printed = False

            for sec in sections:
                if not sec.strip():
                    continue
                header = sec.strip().split("\n")[0]
                
                # Check match
                q_match = True
                if query:
                    q_lower = query.lower()
                    if q_lower not in sec.lower():
                        q_match = False

                if q_match:
                    if not file_printed:
                        print(f"📘 檔案路徑: {rel_path}")
                        print("-" * 65)
                        file_printed = True

                    matched_sections += 1
                    print(f"▶ {header}")
                    lines = sec.strip().split("\n")[1:8]
                    for l in lines:
                        if l.strip():
                            print(f"   {l.strip()[:110]}")
                    print("   ...\n")

    if matched_sections == 0:
        print("❌ 未找到相符的知識條目。建議嘗試更寬鬆的關鍵字或取消篩選。")
    else:
        print(f"✅ 共檢索出 {matched_sections} 個相符的核心機制或教學對應區塊。\n")

def main():
    parser = argparse.ArgumentParser(description="大學生物資料庫快速檢索工具 (College Biology Academic DB)")
    parser.add_argument("-q", "--query", type=str, default="", help="關鍵字檢索 (例如: 米氏常數, 逆流倍增, 羊膜卵, SIR模型)")
    parser.add_argument("-m", "--module", type=int, choices=range(1, 6), default=None, help="依子庫模組篩選 (1: 普生, 2: 動物學, 3: 生化, 4: 數理生物, 5: 百科)")
    parser.add_argument("-b", "--book", type=str, default="", help="依教材名稱篩選 (例如: Campbell, Raven, Miller-Harley, 王鏡岩, Murray)")
    parser.add_argument("-c", "--curriculum", type=str, default="", help="依高中課綱對應模組篩選 (例如: 必修生物, 選修生物I, 選修生物II, 選修生物III, 探究實作)")

    args = parser.parse_args()

    if not args.query and args.module is None and not args.book and not args.curriculum:
        print("提示：請輸入檢索關鍵字或篩選參數。範例：")
        print("  python3 search_college_bio_db.py -q '酵素動力學'")
        print("  python3 search_college_bio_db.py -m 2 -q '體腔'")
        print("  python3 search_college_bio_db.py -c '選修生物I'")
        print("  python3 search_college_bio_db.py --book 'Murray'\n")
        search_database(query="水勢")
        return

    search_database(query=args.query, module_filter=args.module, book_filter=args.book, curriculum_filter=args.curriculum)

if __name__ == "__main__":
    main()
