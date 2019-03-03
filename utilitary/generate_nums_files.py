from os import path

dirname = path.dirname(__file__)


def write(in_file, out_file):
    bytes_to_write = []

    with open(in_file) as r:
        while True:
            a = r.read(2)
            if not a:
                break

            first, second = divmod(int(a), 10)

            byte = first << 4 | second

            bytes_to_write.append(byte)

    with open(out_file, 'wb') as w:
        w.write(bytes(bytes_to_write))


write(path.join(dirname, '../nums_data/pi_src'), path.join(dirname, '../nums_data/pi'))
write(path.join(dirname, '../nums_data/euler_src'), path.join(dirname, '../nums_data/euler'))
