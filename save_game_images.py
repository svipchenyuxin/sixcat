#!/usr/bin/env python3
import os
import base64
import shutil

# 确保图片目录存在
if not os.path.exists('images'):
    os.makedirs('images')

# 创建一个特定图片样本 - 用于测试
def create_sample_game_image(filepath, color=(100, 100, 200)):
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # 创建一个300x300的图片
        img = Image.new('RGB', (300, 300), color=color)
        draw = ImageDraw.Draw(img)
        
        # 尝试添加文字（如果有系统字体）
        try:
            # 尝试获取系统字体
            font = ImageFont.truetype("Arial", 20)
            draw.text((100, 150), os.path.basename(filepath), fill=(255, 255, 255), font=font)
        except:
            # 如果没有字体，就画一个简单的框
            draw.rectangle([(50, 50), (250, 250)], outline=(255, 255, 255))
        
        # 保存图片
        img.save(filepath)
        print(f"创建示例图片: {filepath}")
    except ImportError:
        # 如果没有PIL库，创建一个简单的文件
        with open(filepath, 'w') as f:
            f.write("Sample game image placeholder")
        print(f"创建简单占位图: {filepath}")

# 检查并创建游戏图片
def ensure_game_image(filename, sample_color=(100, 150, 250)):
    filepath = os.path.join('images', filename)
    
    # 如果文件不存在或是空文件，创建样本
    if not os.path.exists(filepath) or os.path.getsize(filepath) < 100:
        create_sample_game_image(filepath, sample_color)
        return f"创建了样本图片: {filename}"
    else:
        return f"图片已存在: {filename}"

# 处理所有汽车游戏图片
car_games = [
    ('turbo-race-3d.jpg', (255, 100, 100)),           # 红色
    ('race-clicker-drift-max.jpg', (100, 255, 100)),  # 绿色
    ('drift-king.jpg', (100, 100, 255)),              # 蓝色
    ('highway-traffic.jpg', (255, 255, 100)),         # 黄色
    ('traffic-jam-3d.jpg', (255, 100, 255)),          # 粉色
    ('gta-simulator.jpg', (100, 255, 255)),           # 青色
    ('drift-hunters-pro.jpg', (200, 100, 50)),        # 棕色
    ('stickman-gta-city-car.jpg', (150, 150, 150)),   # 灰色
    ('madalin-stunt-cars-pro.jpg', (200, 50, 200)),   # 紫色
    ('police-chase-drifter.jpg', (50, 200, 200))      # 青绿色
]

results = []
for game_file, color in car_games:
    result = ensure_game_image(game_file, color)
    results.append(result)

for result in results:
    print(result)

print("\n所有汽车游戏图片已处理完成！请刷新页面查看效果。") 