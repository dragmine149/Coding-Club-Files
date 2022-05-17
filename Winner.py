import random
import Run

# Generate List
numbers = []
for i in range(49):
    numbers.append(i)

def generate_List():
    # print(numbers)
    # Swap numbers around
    for i in range(len(numbers)):
        position = random.randint(0, len(numbers) - 1) # get pos of item
        temp = numbers[i] # temp

        # replace
        numbers[i] = numbers[position]
        numbers[position] = temp

    return numbers

def Select():
    return generate_List()[0:6]

if __name__ == '__main__':
    print(numbers)

    generate_List()

    # Print out first 6 digit
    selection = numbers[0:6]
    print(selection)

    # Time counter
    print(Run.end(True, False))
