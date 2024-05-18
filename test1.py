from PIL import Image
import os

# 定义源文件夹和目标文件夹
source_folder = '/Users/lushenhuan/Library/Mobile Documents/com~apple~CloudDocs/User Documents/本科Work doing/Zou Lab/data-plant-pic-relation-0516/pics'  # 您的原始图片文件夹路径
target_folder = '/Users/lushenhuan/Library/Mobile Documents/com~apple~CloudDocs/User Documents/本科Work doing/Zou Lab/data-plant-pic-relation-0516/pics1'  # 保存处理后图片的文件夹路径

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 定义目标尺寸
target_size = (800, 800)  # 替换为所需的尺寸

def process_image(image_path, output_path, size):
    # 打开图片
    with Image.open(image_path) as img:
        # 创建一个新的黑色背景图片
        new_img = Image.new("RGB", size, (0, 0, 0))
        
        # 获取原始图片的尺寸
        original_size = img.size
        
        # 计算缩放比例并缩放图片
        ratio = min(size[0] / original_size[0], size[1] / original_size[1])
        new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
        img = img.resize(new_size, Image.LANCZOS)
        
        # 计算图片放置的位置，使其居中
        position = ((size[0] - new_size[0]) // 2, (size[1] - new_size[1]) // 2)
        
        # 将缩放后的图片粘贴到黑色背景图片上
        new_img.paste(img, position)
        
        # 保存图片为jpg格式
        new_img.save(output_path, 'JPEG')

# 遍历源文件夹中的所有图片文件
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'webp')):
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, os.path.splitext(filename)[0] + '.jpg')
        
        process_image(source_path, target_path, target_size)

print(f"All images have been processed and saved to {target_folder}")
