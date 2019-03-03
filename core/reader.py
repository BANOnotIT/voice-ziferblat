def read(in_file):
    with open(in_file, 'rb') as r:
        while True:
            byte = r.read(1)
            if not len(byte):
                break

            byte = int.from_bytes(byte, byteorder='big')
            second = byte & 0b1111
            first = byte >> 4 & 0b1111

            yield first
            yield second
