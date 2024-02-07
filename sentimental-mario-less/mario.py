from cs50 import get_int

height = 0
blocks = 1
spaces = 0

# Get input between 1 and 8, else repeat prompt
while height < 1 or height > 8:
    height = get_int('Height: ')

# Set spaces required for alignment
spaces = height - 1

# Print right-aligned pyramid
for n in range(int(height)):
    print(' ' * spaces + '#' * blocks)
    blocks += 1
    spaces -= 1
