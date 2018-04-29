from PIL import Image
from string import Template
import sys
import os
print("This is a single color bmp2c converter.")
print("Use it this way: bmp2c.exe [hex|bin] example.bmp")
if len(sys.argv) < 3:
    print('>>>failed!! check your params.')
    sys.exit(-1)

img = Image.open(os.path.join(os.path.abspath('.'), sys.argv[2]))
img_data = list(img.getdata())
# img_data = [i for i in range(0, 12)]
img_name = os.path.splitext(sys.argv[2])[0]
img_output_mode = sys.argv[1]
img_row = img.size[1]
img_col = img.size[0]
img_len = img_col * img_row
print("Image name: {0}, ".format(img_name),
      "Image size: {0}, ".format(img.size),
      "Image format: {0}".format(img.format))

# 加载模板
template_file = open(os.path.join(os.path.abspath('.'),
                                  "template.txt"), 'r')
template = Template(template_file.read())

# 填充模板参数
data = {'img_name': img_name,
        'img_row': img_row,
        'img_col': img_col,
        'img_len': img_len,
        'img_name_cap': img_name.upper(),
        'img_data': ''.join(['{' + ', '.join("0x{:02X}".format(x) for x in img_data[y: y + img_col]) + '},' + '\n\t' \
                             for y in range(0, img_len, img_col)]) if img_output_mode == 'hex' else \
                    ''.join(['{' + ', '.join(str(x % 254) for x in img_data[y: y + img_col]) + '},' + '\n\t' \
                             for y in range(0, img_len, img_col)])
        }

with open(img_name + '.h', 'w') as f:
    f.write(template.substitute(data))

# 防止窗口一闪而过
user_in = input("any key to exit")
