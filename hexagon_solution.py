#!/usr/bin/env python3

def solve_hexagon_path(x, y):
    """
    Calculate minimum steps in directions A, B, C to reach (x, y) from (0, 0)
    on a hexagonal grid where axes x and y are at 60° angle.
    Movement vectors A, B, C are at 120° angles to each other.
    
    Using cube coordinates: z = -x - y
    Three directions A, B, C correspond to movements that change cube coordinates.
    
    The key insight: we need to find non-negative steps a, b, c such that:
    - Total displacement equals (x, y, z) 
    - Total steps = a + b + c is minimized
    - This equals max(|x|, |y|, |z|)
    """
    # Calculate z coordinate  
    z = -x - y
    
    # The mathematical solution for hexagonal grids:
    # We want to find non-negative a, b, c such that the net effect
    # of a steps in direction A, b steps in direction B, c steps in direction C
    # results in displacement (x, y, z)
    
    # Key insight: exactly two of {x, y, z} will have the same sign
    # (or be zero), and we can use this to find optimal decomposition
    
    # The optimal solution uses the property that we can reach any point
    # using at most two of the three directions
    
    # Case analysis based on which coordinates are non-negative:
    if x >= 0 and y >= 0:
        # z = -(x+y) <= 0
        # Use directions A and B only
        steps_A = x
        steps_B = y  
        steps_C = 0
    elif x >= 0 and z >= 0:
        # y = -(x+z) <= 0  
        # Use directions A and C only
        steps_A = x
        steps_B = 0
        steps_C = z
    elif y >= 0 and z >= 0:
        # x = -(y+z) <= 0
        # Use directions B and C only  
        steps_A = 0
        steps_B = y
        steps_C = z
    elif x <= 0 and y <= 0:
        # z = -(x+y) >= 0
        # Use direction C only
        steps_A = 0
        steps_B = 0
        steps_C = z
    elif x <= 0 and z <= 0:
        # y = -(x+z) >= 0
        # Use direction B only
        steps_A = 0  
        steps_B = y
        steps_C = 0
    elif y <= 0 and z <= 0:
        # x = -(y+z) >= 0
        # Use direction A only
        steps_A = x
        steps_B = 0
        steps_C = 0
    else:
        # This case should never occur due to constraint x + y + z = 0
        # But handle it defensively
        steps_A = max(0, x)
        steps_B = max(0, y)
        steps_C = max(0, z)
    
    return steps_A, steps_B, steps_C

def main():
    # Read number of queries
    q = int(input())
    
    # Process each coordinate pair
    for _ in range(q):
        x, y = map(int, input().split())
        steps_A, steps_B, steps_C = solve_hexagon_path(x, y)
        print(steps_A, steps_B, steps_C)

if __name__ == "__main__":
    main()