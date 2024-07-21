# library: opencv-python
import cv2

# Compression func
def compress_image(input_path, output_path, quality):

    image = cv2.imread(input_path)
    
    if image is None:
        print(f"Error: Could not open or find the image at {input_path}")
        return

    # Compress the image
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    print(f"Image saved at {output_path} with quality {quality}")

# Take the inputs of these from user
input_image_path = r'D:\IMG_3133.jpg'
output_image_path = r'D:\image.jpg'
compression_quality = 10  # Quality: 0 to 100(best)
# mention the condition to user, anything above 100 should be taken as 100 and below 0 as 0, to be mentioned in the output

# %%
compress_image(input_image_path, output_image_path, compression_quality)

# %%



