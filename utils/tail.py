

def tail(filename, num_lines):
    line_buf = []
    chunk_size = 200
    append_first = 0
    iter_count = 1
    with open(filename) as f:
        f.seek(0,2)
        file_size = f.tell()

        while len(line_buf) <= num_lines+1 or seek_step == file_size:
            seek_step = iter_count * chunk_size
            if seek_step > file_size:
                seek_step = file_size
            f.seek(-seek_step, 2)
            data = f.read(chunk_size)
            if data:
                temp = data.split('\n')
                if temp[-1] == '':
                    temp.pop(-1)
                if append_first and line_buf:
                    line_buf[0] = temp[-1] + line_buf[0]
                    temp.pop(-1)
                    append_first = 0
                temp.extend(line_buf)
                line_buf = temp
                if data[0] != '\n':
                    append_first = 1
            iter_count += 1
        return line_buf[1:]

print tail('test.txt', 50)
