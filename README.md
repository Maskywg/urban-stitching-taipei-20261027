# 城市縫合：接回生活，還是換一種撕裂？

繁體中文公共空間研究專題。8個國際案例、10處台北候選與對照地點、真實授權照片、歷史回顧、交通連結圖解與批判。

- 線上：https://maskywg.github.io/urban-stitching-taipei-20261027/
- 資料檢視：2026-10-27
- 台北標記為人工整理的約略代表座標，不是工程界線、嚴重程度排名或正式問題鑑定。
- 來源與證據限制附於網頁，29筆研究及官方／營運資料；照片授權逐圖列示。
- 地圖採 Leaflet 1.9.4 與 OpenStreetMap；JS/CSS本地提供，地圖圖磚需網路。
- 網站為純靜態頁面，無帳號、追蹤碼或後端。互動觀察清單不傳送或持久保存。

## 修改

`content.py`：案例、來源與地點資料。
`build.py`：產生完整靜態 HTML，照片資料讀取 `photos.json`。
`style.css`、`app.js`：版面與互動。
`make_share.py`：以 Pillow 製作原創1200×630分享圖，目前字型路徑為macOS。

```sh
python3 build.py
python3 -m http.server 8767
```

分享設定包含 canonical、Open Graph 與 Twitter large image；若變更部署URL，需修改 build.py 的 URL 並重建。

## 授權

原創網站文字、程式與分享圖採 MIT（研究來源本身及照片除外）；照片依各作者原授權使用，見 `assets/PHOTO-CREDITS.md`。圖片畫面裁切不改變其原授權。Leaflet 採 BSD-2-Clause，見 `assets/leaflet/LICENSE`。底圖 © OpenStreetMap contributors。
