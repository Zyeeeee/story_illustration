from PIL import Image,ImageFilter
import os
import io

def blur_image(img):

    # print(img.size)
    # 获取原图的宽高
    width, height = img.size

    # 创建4:3的目标背景大小
    target_width = width
    target_height = int(width * 3 / 4)

    if target_height > height:
        target_height = height
        target_width = int(height * 4 / 3)

    # 将图片调整为4:3的背景图
    background = img.resize((target_width, target_height))

    # 对背景应用高斯模糊
    background_blurred = background.filter(ImageFilter.GaussianBlur(25))  # 模糊半径可调整

    # 计算原图的等比例缩放后的尺寸
    scale_factor = min(target_width / width, target_height / height)
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # 将原图等比例缩放到新尺寸
    img_resized = img.resize((new_width, new_height))

    # 将缩放后的原图粘贴到模糊背景的中央
    paste_x = (target_width - new_width) // 2
    paste_y = (target_height - new_height) // 2

    # 将原图粘贴到背景上
    background_blurred.paste(img_resized, (paste_x, paste_y))
    # ---------------------------------------------------------------------------
    # 高斯模糊转化为4:3完成 可以直接返回图像 return background_blurred
    # print(background_blurred.size)
    image = resize_image(background_blurred)
    return image

def resize_image(image):
    max_size = 1500
    min_size = 200
    width, height = image.size

    # 计算缩放比例
    if max(width, height) > max_size:
        scale = max_size / max(width, height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # 确保最小尺寸不小于 200
    if min(image.size) < min_size:
        scale = min_size / min(image.size)
        new_width = max(int(image.size[0] * scale), min_size)
        new_height = max(int(image.size[1] * scale), min_size)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return image


if __name__ == '__main__':
    image_path = '/Users/xiaoxiongmao/pycharm/2025.2.28/测试/cat (16).jpg'
    # 转化图片尺寸并高斯模糊背景
    img_blue = blur_image(image_path)
    # 将处理后的图像保存到内存中
    img_byte = io.BytesIO()
    img_blue.save(img_byte, format='PNG')
    img_byte.seek(0)


