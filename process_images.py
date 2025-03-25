#!/usr/bin/env python3
import os
import shutil

# 源图片（使用一个已有的图片作为模板）
source_image = 'images/conquer-kingdoms.jpg'

# 需要填充的汽车游戏图片列表
car_games = [
    'turbo-race-3d.jpg',
    'race-clicker-drift-max.jpg',
    'drift-king.jpg',
    'highway-traffic.jpg',
    'traffic-jam-3d.jpg',
    'gta-simulator.jpg',
    'drift-hunters-pro.jpg',
    'stickman-gta-city-car.jpg',
    'madalin-stunt-cars-pro.jpg',
    'police-chase-drifter.jpg'
]

# 复制源图片到缺失的图片
for game in car_games:
    target_path = os.path.join('images', game)
    # 如果目标文件大小为0或非常小，替换它
    if not os.path.exists(target_path) or os.path.getsize(target_path) < 1000:
        print(f"Copying template to {target_path}")
        shutil.copy2(source_image, target_path)
    else:
        print(f"Skipping {target_path} - already has content")

print("Done processing car game images!") 