# CliffsAP & QuickStudy 普生高頻核心公式與定律速查

**典藏檔案**：`Biolo(CliffsAP)_muya.pdf` & `qsbiology-1572227419.pdf`
**核心價值**：整理普通生物學中必須掌握的定量方程式、物理化學常數與快速判讀定律，專供高中資優培訓、生奧初賽與大考計算題命題參考。

---

## 一、水勢與滲透壓公式 (Water Potential)

$$\Psi = \Psi_s + \Psi_p$$

- **溶質勢 (Solute Potential, $\Psi_s$)**：
  $$\Psi_s = -iCRT$$
  - $i$：電離常數（蔗糖 $i = 1$；$\text{NaCl}$ $i = 2$）。
  - $C$：體積莫耳濃度 ($\text{mol/L}$)。
  - $R$：壓力氣體常數 ($0.00831\text{ liter}\cdot\text{bar}/(\text{mol}\cdot\text{K})$ 或 $0.00831\text{ MPa}\cdot\text{L}/(\text{mol}\cdot\text{K})$)。
  - $T$：絕對溫度 ($\text{K} = ^\circ\text{C} + 273$)。
- **純水水勢標準**：開放容器中純水 $\Psi_s = 0, \Psi_p = 0 \implies \Psi = 0$。加入溶質後 $\Psi_s$ 必為負值。
- **水流方向判斷**：水永遠自**高水勢處（較少負值）流向低水勢處（較多負值）**。

---

## 二、哈溫平衡數理方程式 (Hardy-Weinberg Equilibrium)

在二倍體雙等位基因 ($A$ 與 $a$) 族群中：

- **等位基因頻率公式**：
  $$p + q = 1$$
  - $p$：顯性等位基因 $A$ 之頻率。
  - $q$：隱性等位基因 $a$ 之頻率。
- **基因型頻率公式**：
  $$p^2 + 2pq + q^2 = 1$$
  - $p^2$：同型合子顯性 ($AA$) 頻率。
  - $2pq$：異型合子 ($Aa$) 頻率。
  - $q^2$：同型合子隱性 ($aa$) 頻率。
- **速算訣竅**：題目若給予隱性表現型個體比例，先開根號求出 $q = \sqrt{\text{隱性頻率}}$，再求 $p = 1 - q$，最後計算帶因者（雜合子）頻率 $2pq$。

---

## 三、生物能量學與 Gibbs 自由能 (Bioenergetics)

$$\Delta G = \Delta H - T\Delta S$$

- **自發性判據**：
  - $\Delta G < 0$：放能反應 (Exergonic)，反應可自發進行。
  - $\Delta G > 0$：吸能反應 (Endergonic)，需偶聯外在能量才能進行。
  - $\Delta G = 0$：系統達到動態平衡。
- **標準自由能與平衡常數關聯**：
  $$\Delta G^\circ = -RT \ln K_{\text{eq}}$$

---

## 四、族群增長動態模型 (Population Growth Dynamics)

- **指數增長 (Exponential Growth)**（資源無限）：
  $$\frac{dN}{dt} = r_{\max} N$$
- **邏輯斯增長 (Logistic Growth)**（受環境容納量 $K$ 制約）：
  $$\frac{dN}{dt} = r_{\max} N \left(\frac{K - N}{K}\right)$$
  - 族群最大總增長速率點：出現在拐點 $N = \frac{K}{2}$ 處。
  - 當 $N \rightarrow K$ 時，$\frac{dN}{dt} \rightarrow 0$。

---

## 五、生理學常用物理化學公式

- **Nernst 方程式 (單一離子平衡膜電位)**：
  $$E_{\text{ion}} = \frac{61.5}{z} \log_{10} \frac{[\text{ion}]_{\text{outside}}}{[\text{ion}]_{\text{inside}}} \quad (\text{mV at } 37^\circ\text{C})$$
- **呼吸商 (Respiratory Quotient, $RQ$)**：
  $$RQ = \frac{\text{釋放的 } \text{CO}_2 \text{ 體積}}{\text{吸收的 } \text{O}_2 \text{ 體積}}$$
  - 醣類燃燒：$RQ = 1.0$（$\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \rightarrow 6\text{CO}_2 + 6\text{H}_2\text{O}$）
  - 脂質燃燒：$RQ \approx 0.7$
  - 蛋白質燃燒：$RQ \approx 0.8$
- **溫度係數 ($Q_{10}$)**：溫度每上升 $10^\circ\text{C}$ 反應速率的倍數：
  $$Q_{10} = \left(\frac{R_2}{R_1}\right)^{\frac{10}{T_2 - T_1}}$$
