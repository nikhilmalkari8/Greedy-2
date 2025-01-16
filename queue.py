def reconstructQueue(people):
    # Sort by height in descending order, and by k in ascending order for ties
    people.sort(key=lambda x: (-x[0], x[1]))
    
    queue = []
    for person in people:
        queue.insert(person[1], person)  # Insert person at the k-th position
    return queue
