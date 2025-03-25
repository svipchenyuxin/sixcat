#!/usr/bin/env python3
import os

# 需要删除并重置的汽车游戏图片列表
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

# 删除现有的图片文件
for game in car_games:
    image_path = os.path.join('images', game)
    if os.path.exists(image_path):
        print(f"删除文件: {image_path}")
        os.remove(image_path)
    
    # 创建空文件占位
    with open(image_path, 'w') as f:
        print(f"创建空文件: {image_path}")
        pass

print("已重置所有汽车游戏图片文件!") 