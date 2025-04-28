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

