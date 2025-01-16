def partitionLabels(s):
    # Step 1: Record the last occurrence of each character
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    
    partitions = []
    start, end = 0, 0

    # Step 2: Traverse the string to determine partitions
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])  # Update the end of the current partition
        if i == end:  # If we reach the end of the partition
            partitions.append(end - start + 1)  # Add partition size
            start = i + 1  # Move start to the next character

    return partitions

