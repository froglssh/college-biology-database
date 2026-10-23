# 大學生物資料庫 (College Biology Academic Database)

> **資料庫定位**：本資料庫專門依據 `/Users/froglssh/Library/CloudStorage/GoogleDrive-frog@lssh.tp.edu.tw/我的雲端硬碟/04生物教學/bio` 資料夾中典藏之**世界經典大學生物學、動物學、生物化學、數理生物學與生命科學百科全書**系統性整編而成。
>
> ⚠️ **嚴格隔離規範（防難度污染）**：
> 本資料庫匯聚了大學乃至研究所層級的精細生物化學代謝途徑、動物比較解剖學胚層特徵、數理生物學微分動力學模型與前沿生物物理學機制。**本資料庫必須嚴格獨立管理，嚴禁與「高中生物知識庫」混合，亦不可直接用於高中常態段考出題**，以免試題嚴重超標、挫傷學生學習熱忱！

---

## 一、館藏文獻盤點與五大核心學術庫

本資料庫全面整合了 `04生物教學/bio` 資料夾中的 15+ 部重要學術專著，分為五大專業子庫：

```
大學生物資料庫/
├── 01_普通生物學核心庫/         # 綜合性普生經典與探究導向教材
├── 02_動物學與生物多樣性庫/     # 大學動物學、無脊椎動物學與比較解剖
├── 03_生物化學與分子生理庫/     # 權威生物化學、酵素動力學與生殖生理
├── 04_數理生物學與科研方法庫/   # 數理建模、生物物理與科學證據評估
├── 05_MacMillan生物科學百科索引/ # 全套 4 冊生命科學百科辭典與科學家專題
├── 108課綱高中教學對接與防超綱指南.md # 雙向課綱對照與命題安全邊界
└── search_college_bio_db.py     # 跨書跨學科終端機檢索工具
```

### 五大子庫館藏對應書目

| 子庫編號與名稱 | 涵蓋經典書目（檔案名稱） | 核心學術特色 |
|---|---|---|
| **01 普通生物學核心庫** | • **Campbell Biology (12th Edition)** (含 7.2MB 全文字版 `txt` 及完整 PDF)<br>• **Raven & Johnson's Biology (6th Edition)**<br>• **Discover Biology (2nd Edition - Cain et al.)**<br>• **Biology: Science for Life (Belk & Borden)**<br>• **CliffsAP Biology** & **QuickStudy Biology** | 普生跨領域通論、植物演化特色、情境式探究實作題材、AP 生物核心考點速查。 |
| **02 動物學與生物多樣性庫** | • **Zoology (5th Edition - Miller & Harley)**<br>• **Animal Diversity (Cleveland Hickman et al.)**<br>• **ZOOLOGI INVERTEBRATA** | 動物界各門系統發生樹、胚胎發育（原口/後口、體腔演化）、無脊椎動物解剖構造、脊椎動物器官系統比較。 |
| **03 生物化學與分子生理庫** | • **生物化學 (第五版) (王鏡岩/朱聖庚)**<br>• **生殖生物學（簡體版）**<br>• **Under the Knife** (解剖手術史) | 酵素動力學（Michaelis-Menten）、代謝反應步驟與能量計量、配子發生與胚胎誘導、生殖內分泌軸。 |
| **04 數理生物學與科研方法庫** | • **Mathematical Biology I & II (3rd Ed - J.D. Murray)**<br>• **Special Topics in Biological Physics**<br>• **How Science Works: Evaluating Evidence in Biology & Medicine** | 族群生態微分方程、傳染病 SIR 模型、生物物理膜通道與分子馬達、假說演繹與臨床試驗統計偏誤分析。 |
| **05 MacMillan生物科學百科索引** | • **Gale / MacMillan Reference Biology (全 4 冊 Vol 1~4 及合訂本, Richard Robinson 主編)** | 數千條生命科學權威名詞辭典、跨學科概念解析、重要生物醫學科學家傳記與科學史。 |

---

## 二、四大應用情境與教學賦能

1. **高中生物教師深度備課（深挖學理本質）**：
   - 告別「高中課本點到為止」的含糊解釋，例如：深入理解酵素競爭型與非競爭型抑制劑對 $K_m$ 與 $V_{\max}$ 的真實生化本質、植物維管束在 Raven 演化樹中的形成機制、原口動物與後口動物在囊胚孔命運與卵裂方式的決定性差異。
2. **高中探究與實作／校訂必修課程設計（真實情境命題）**：
   - 參考 Belk & Borden 的 *Biology: Science for Life*，將真實生活議題（如「抗生素抗藥性檢測」、「運動員肥胖與飲食代謝」、「法醫 DNA 鑑定與親子血緣評估」）轉化為高中探究學習單與校內素養評量試題。
3. **生物奧林匹亞 (IBO) 與學科能力競賽培訓（競賽選手學術底座）**：
   - 生奧考綱大量涉及動物各門解剖特徵（Hickman & Miller-Harley）、精確生物化學途徑（王鏡岩生化）、以及遺傳與生態數理計算（Murray 數理模型），本庫為培訓選手提供了頂級的學術查考依據。
4. **高中科展專題研究輔導（定量建模與科研論證）**：
   - 指導學生利用 J.D. Murray 的數理模型進行微生物生長曲線擬合、以 *How Science Works* 指導實驗組對照組之雙盲設計、統計顯著性檢定與避免偽陽性/偽陰性陷阱。

---

## 三、快速檢索工具使用方法

資料庫內建專屬檢索程式 `search_college_bio_db.py`，支援跨書、跨領域快速檢索：

```bash
# 1. 關鍵字快速檢索（例如：酵素動力學、原口動物、SIR模型、水勢）
python3 search_college_bio_db.py -q "酵素動力學"

# 2. 依子庫模組篩選（例如：02 動物學庫）
python3 search_college_bio_db.py -m 2 -q "體腔"

# 3. 依特定教材名稱篩選（例如：Campbell, Raven, Miller-Harley, Murray）
python3 search_college_bio_db.py --book "Campbell" -q "光反應"

# 4. 依高中 108 課綱對應模組檢索（例如：選修生物I、選修生物II、探究實作）
python3 search_college_bio_db.py --curriculum "選修生物II"
```

---

## 四、資料庫位置與同步維護

- **本機工作區路徑**：
  [`/Users/froglssh/Documents/知識庫管理/大學生物資料庫`](file:///Users/froglssh/Documents/知識庫管理/大學生物資料庫)
- **Google Drive 獨立存放路徑**：
  [`/Users/froglssh/Library/CloudStorage/GoogleDrive-frog@lssh.tp.edu.tw/我的雲端硬碟/04生物教學/bio/大學生物資料庫`](file:///Users/froglssh/Library/CloudStorage/GoogleDrive-frog@lssh.tp.edu.tw/我的雲端硬碟/04生物教學/bio/大學生物資料庫)
