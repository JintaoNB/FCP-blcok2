def read_input_output_files(filenames):
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

def base_count(filenames):
    A = 0
    C = 0
    T = 0
    G = 0
    for filename in filenames:
        with open(filename, 'r') as file:
            sequence = file.read()
    for i in sequence:
        if i == 'A':
            A += 1
        elif i == 'C':
            C += 1
        elif i == 'T':
            T += 1
        elif i == 'G':
            G += 1
        base_counts = {'A': A, 'C': C, 'T': T, 'G': G}
        return base_counts


def complement(filenames, reverse=False):
    for filename in filenames:
        with open(filename, 'r') as file:
            sequence = file.read()
    for s in sequence:
        s = s[:50]
        complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
        complement_sequence = ''
        for base in s:
            complement_sequence += complement_dict[base]
        if reverse:
            complement_sequence = complement_sequence[::-1]
        return complement_sequence


def calculate_gc_content(filenames, window_size):
    for filename in filenames:
        with open(filename, 'r') as file:
            sequence = file.read()
    total_sum = 0
    for s in sequence:
        for i in range(len(s) - window_size + 1):
            window = sequence[i:i + window_size]
            sum_g = window.count('G')
            sum_c = window.count('C')
            total_sum += (sum_g + sum_c) / len(window)
        return total_sum






def detect_gc_islands(filenames, window_size, gc_threshold):
    for filename in filenames:
        with open(filename, 'r') as file:
            sequence = file.read()
    gc_islands = []
    for s in sequence:
        for i in range(len(s) - window_size + 1):
            window = sequence[i:i + window_size]
            sum_g = window.count('G')
            sum_c = window.count('C')
            total_sum = len(window)
            gc_content = calculate_gc_content()
            if gc_content >= gc_threshold:
                gc_islands.append((i, i + window_size - 1, gc_content))
        numbers_islands = len(gc_islands)
        return numbers_islands