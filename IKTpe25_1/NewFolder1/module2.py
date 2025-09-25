import math

# Küsi kasutajalt puu ümbermõõtu
ümbermõõt = float(input("Sisesta puu ümbermõõt (cm): "))

# Arvute puu läbimõõdu
läbimõõt = ümbermõõt / math.pi

# printi tulemus
print(f"Puu läbimõõt on {läbimõõt:.2f} cm")
