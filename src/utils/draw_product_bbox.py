import os

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def draw_bbox_results(image, results, input_path, font_path="./utils/simfang.ttf", save_dir=None):
    """
    Using Pillow to draw a bounding box for product image.
    Args:
        image:
        results:
        input_path:
        font_path:
        save_dir:

    Returns:

    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    font_size = 18
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")

    color = (0, 102, 255)

    for result in results:
        # empty results
        if result["product_names"] is None:
            continue

        xmin, ymin, xmax, ymax = result["bbox"]
        text = "{}, {:.2f}".format(result["product_names"], result["scores"])
        th = font_size
        tw = font.getsize(text)[0]
        start_y = max(0, ymin - th)

        draw.rectangle([(xmin + 1, start_y), (xmin + tw + 1, start_y + th)], fill=color)

        draw.text((xmin + 1, start_y), text, fill=(255, 255, 255), font=font)

        draw.rectangle([(xmin, ymin), (xmax, ymax)], outline=(255, 0, 0), width=2)

    image_name = os.path.basename(input_path)
    if save_dir is None:
        save_dir = "output"
    os.makedirs(save_dir, exist_ok=True)
    output_path = os.path.join(save_dir, image_name)

    image.save(output_path, quality=95)
    return np.array(image)
