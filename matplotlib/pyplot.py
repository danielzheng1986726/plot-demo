import struct
import zlib

_x = []
_y = []


def figure():
    pass


def plot(x, y):
    global _x, _y
    _x = list(x)
    _y = list(y)


def xlabel(label):
    pass


def ylabel(label):
    pass


def title(label):
    pass


def grid(flag=True):
    pass


def _write_png(data, width, height, filename):
    def png_pack(tag, data):
        return struct.pack('!I', len(data)) + tag + data + struct.pack('!I', zlib.crc32(tag + data) & 0xffffffff)

    raw_data = b''.join(b'\x00' + bytes(data[i:i + width * 3]) for i in range(0, len(data), width * 3))
    with open(filename, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        f.write(png_pack(b'IHDR', struct.pack('!2I5B', width, height, 8, 2, 0, 0, 0)))
        f.write(png_pack(b'IDAT', zlib.compress(raw_data)))
        f.write(png_pack(b'IEND', b''))


def savefig(filename):
    width, height = 200, 200
    data = [255] * width * height * 3
    if _x and _y:
        xmin, xmax = min(_x), max(_x)
        ymin, ymax = min(_y), max(_y)
        dx = xmax - xmin or 1
        dy = ymax - ymin or 1
        for xv, yv in zip(_x, _y):
            x_idx = int((xv - xmin) / dx * (width - 1))
            y_idx = int((ymax - yv) / dy * (height - 1))
            idx = (y_idx * width + x_idx) * 3
            data[idx:idx + 3] = [0, 0, 0]
    _write_png(data, width, height, filename)
