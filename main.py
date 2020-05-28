import os
import time

start = time.time()
path = r"your path"
tot_count = 0

# define your rules
def rule(file_path):
    return file_path.endswith('.go')


for path, dir_list, file_list in os.walk(path):
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        if rule(file_path):
            with open(file_path, 'rb') as f:
                count = 0
                last_data = '\n'
                while True:
                    data = f.read(0x400000)
                    if not data:
                        break
                    count += data.count(b'\n')
                    last_data = data
                if last_data[-1:] != b'\n':
                    count += 1  # Remove this if a wc-like count is needed
            tot_count += count

end = time.time()
print(f"Total_lines:{tot_count}. Time elapsed:{(end - start) * 1000:.3f}")
