def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    # TC: O(nlogn) due to sorting
    # SC: O(n)
    # Create a 2d array, sort it by position of the cars(in descending order)
    # Sorting ensures we process the cars from the closest to the target to the farthest.

    pairs = [[p, s] for p, s in zip(position, speed)] # [[10, 2], [8, 4], ...]
    stack = []

    for p, s in sorted(pairs)[::-1]: # in descending order
        stack.append((target - p) / s) # at what time(t) will this current car reach the destination?
        if len(stack) >= 2 and stack[-1] <= stack[-2]: # need at least two cars to compare
        # If the latest car (stack's top) takes less time or the same time as the car before it,
        # that means the two cars merge into one fleet.
            stack.pop() # We pop the faster car because it becomes part of the fleet.
    
    return len(stack) # represents the number of separate fleets that will reach the destination.