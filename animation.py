import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap

# 假設JSON檔案名稱為 'data1.json', 'data2.json', ..., 'dataN.json'
# 並且它們被儲存在一個字典列表 'data_list' 中
data_list = []
for i in range(1, N + 1):
    with open(f"data{i}.json", "r") as file:
        data_list.append(json.load(file))

# 定義感興趣的站點名稱
stations_of_interest = ["Station A", "Station B", "Station C"]

# 篩選感興趣的站點數據
filtered_data = []
for data in data_list:
    filtered_data.append(
        {station: data[station] for station in stations_of_interest if station in data}
    )

# 設置基礎地圖
fig = plt.figure(figsize=(10, 8))
m = Basemap(
    projection="merc",
    llcrnrlat=min_lat,
    urcrnrlat=max_lat,
    llcrnrlon=min_lon,
    urcrnrlon=max_lon,
    resolution="i",
)
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# 在地圖上繪製站點
for station_data in filtered_data:
    for station, info in station_data.items():
        x, y = m(info["longitude"], info["latitude"])
        m.plot(x, y, "bo", markersize=info["available_bikes"])


# 創建動畫函數
def animate(i):
    plt.clf()
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    station_data = filtered_data[i]
    for station, info in station_data.items():
        x, y = m(info["longitude"], info["latitude"])
        m.plot(x, y, "bo", markersize=info["available_bikes"])


# 創建動畫
ani = animation.FuncAnimation(fig, animate, frames=len(filtered_data), interval=60000)

# 將動畫保存為GIF檔案
ani.save("bike_stations.gif", writer="imagemagick")

# 注意：用戶需要根據自己的地圖調整 'min_lat', 'max_lat', 'min_lon', 'max_lon' 的值。
# 另外，'N' 應該替換為實際的JSON檔案數量。
