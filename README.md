# YouBike 歷史站點流量分析工具

使用本工具可以查詢個別 YouBike 站點歷史車輛數量變化，透過一目了然的視覺化數據，了解並預測在什麼時間會無車可借、什麼時間無位可還車。

![screenshot](demo.gif)

## 如何使用

設定 cron jobs 讓電腦或伺服器每分鐘下載一份所有 YouBike 站點的即時數據

```bash
* * * * * cd ~/youbike-data-analysis && python download.py
```

列出單一站點歷史紀錄

```bash
 python analysis.py --name "公館站(2號出口)"
```
