def draw_christmas_tree(height):
    if height < 3:
        print("La hauteur doit être au moins 3 pour un sapin valide.")
        return
    
    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
    
    trunk_width = 3 if height > 5 else 1  
    trunk_height = max(2, height // 4)
    trunk_space = (2 * height - 1 - trunk_width) // 2 
    
    for _ in range(trunk_height):
        print(" " * trunk_space + "|" * trunk_width)

try:
    height = int(input("Quelle est la hauteur du sapin ? (entier >= 3) : "))
    draw_christmas_tree(height)
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
