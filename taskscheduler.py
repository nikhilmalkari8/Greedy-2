from collections import Counter

def leastInterval(tasks, n):
    # Count the frequency of tasks
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_count = sum(1 for task, freq in task_counts.items() if freq == max_freq)

    # Calculate the least time
    part_count = max_freq - 1
    part_length = n + 1
    empty_slots = part_count * part_length
    available_tasks = len(tasks) - max_freq * max_count
    idles = max(0, empty_slots - available_tasks)

    return len(tasks) + idles
