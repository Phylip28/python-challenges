blocks = int(input("Enter the number of blocks: "))
block_count = 0
used_blocks = 0
height = 0

while used_blocks + (block_count + 1) <= blocks:
    block_count += 1
    used_blocks += block_count
    height += 1

print("The height of the pyramid is:", height)
