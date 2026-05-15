# 太陽系運動模擬器（Solar System Simulator）

使用 Python 與 turtle graphics 製作的太陽系運動模擬專案，透過物件導向程式設計（OOP）與簡化萬有引力模型，模擬行星繞行太陽的運動。

---

## 專案特色

- 使用物件導向設計（OOP）
- 模擬行星公轉
- 實作基礎萬有引力運動
- 使用 turtle 製作即時動畫
- 包含太陽、行星、衛星系統

---

## 使用技術

- Python
- Turtle Graphics
- Object-Oriented Programming（OOP）
- 基礎物理模擬

---

## 專案架構

```text
Solar_System.py

├── Sun
│   ├── 儲存太陽資料
│   ├── 建立太陽圖形
│   └── 提供體積、表面積、密度等計算
│
├── Planet
│   ├── 儲存行星資料
│   ├── 設定速度與位置
│   ├── 更新行星移動
│   └── 使用 turtle 繪製行星
│
├── Moon
│   ├── 儲存衛星資料
│   ├── 模擬衛星運動
│   └── 繪製衛星軌道
│
├── SolarSystem
│   ├── 管理所有天體
│   ├── 計算萬有引力
│   ├── 更新速度與座標
│   └── 控制整體動畫
│
└── creatSSandAnimate()
    ├── 建立太陽與行星
    ├── 初始化太陽系
    ├── 執行動畫迴圈
    └── 啟動模擬


---
