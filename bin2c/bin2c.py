import os
if __name__ == '__main__':
    data = []
    size = 0
    with open(os.path.join(os.path.abspath('.'), 'data.dat'), 'rb') as f:
        while True:
            a_byte = f.read(1)
            if len(a_byte) == 0:
                break
            else:
                data.append("0x%.2X" % ord(a_byte))

    with open(os.path.join(os.path.abspath('.'), './template.txt'), 'r') as f1:
        f1_content = f1.read()
    with open(os.path.join(os.path.abspath('.'), './template.h'), 'w') as f2:
        f1_content = f1_content.replace("data_transformed", data[0] + ",\n\t" + ",\n\t".join(data[1:])).replace('len_of_data', str(len(data)))\
            .replace('spilt_size', '1')
        f2.write(f1_content)
    pass
