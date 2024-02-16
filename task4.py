def read_input_files(filenames):
    sequences = []
    for filename in filenames:
        with open(filename, 'r') as file:
            sequence = file.read()
            sequences.append(sequence)
    if sequences == []:
        print("Error: No files provided. Please provide at least one filename.")
    else:
        file = open('output.txt', 'w')
        file.write(sequence)
        file.close()
        return sequences
A = 0
C = 0
T = 0
G = 0
for i in sequence:
    if i == 'a':
        A += 1
    elif i == 'c':
        C += 1
    elif i == 't':
        T += 1
    elif i == 'g':
        G += 1
base_counts = {'A': A, 'C': C, 'T': T, 'G': G}
print(base_counts)

def complement(seq, reverse=False):
    for s in seq:
        s = s[:50]
        complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
        complement_sequence = ''
        for base in s:
            complement_sequence += complement_dict[base]
        if reverse:
            complement_sequence = complement_sequence[::-1]
        return complement_sequence

def calculate_gc_content(seq, window_size):
    total_sum = 0
    for s in seq:
        for i in range(len(s) - window_size + 1):
            window = seq[i:i + window_size]
            sum_g = window.count('G')
            sum_c = window.count('C')
            total_sum += (sum_g + sum_c) / len(window)
    return total_sum

def detect_gc_islands(seq, window_size, gc_threshold):
    gc_islands = []
    for s in seq:
        for i in range(len(s) - window_size + 1):
            window = seq[i:i + window_size]
            sum_g = window.count('G')
            sum_c = window.count('C')
            total_sum = len(window)
            gc_content = calculate_gc_content()
            if gc_content >= gc_threshold:
                gc_islands.append((i, i + window_size - 1, gc_content))
        numbers_islands = len(gc_islands)
        return numbers_islands