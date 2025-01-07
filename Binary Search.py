sequence = [1, 2, 3, 4, 5, 6, 7]

find = 7

start_index = 0

end_index = len(sequence) - 1

while start_index <= end_index:

        midpoint = end_index + start_index // 2
        if sequence[midpoint] == find:
             print("Found at index: ",midpoint)
        break
        if sequence[midpoint] > find:
            end_index = midpoint - 1

        else:
            end_index = midpoint +1