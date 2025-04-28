import matplotlib.pyplot as plt

# 1. Läser DNA-filen och returnerar en dictionary med namn och sekvenser
def read_dna_file(filename):
    sequences = {}
    current_name = ""
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Tar bort radbrytningar och mellanslag
            
            if line.startswith('>'):  # Om raden börjar med '>' är det ett nytt namn
                current_name = line[1:]  # Sparar namnet (utan '>')
                sequences[current_name] = ""  # Skapar en tom sekvens
            else:
                sequences[current_name] += line.upper()  # Lägger till sekvensen
    
    return sequences

# 2. Räknar hur många A, T, C, G det finns i en sekvens
def count_bases(sequence):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    for base in sequence:
        if base in counts:  # Kontrollerar att det är en giltig bokstav.
            counts[base] += 1
    
    return counts

# 3. Ritar en stapeldiagrammet.
def plot_bases(counts, sequence_name):
    plt.bar(counts.keys(), counts.values(), color=['blue', 'red', 'green', 'yellow'])
    plt.xlabel("DNA-bas")
    plt.ylabel("Antal")
    plt.title(f"DNA-sekvens: {sequence_name}")
    plt.show()
