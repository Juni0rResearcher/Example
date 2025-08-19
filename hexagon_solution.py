#!/usr/bin/env python3

def solve_hexagon_path(x, y):
    """
    Calculate minimum steps in directions A, B, C to reach (x, y) from (0, 0)
    on a hexagonal grid.
    
    Based on cube coordinates where z = -x - y.
    
    The key insight from hexagonal grid theory:
    - In cube coordinates, we have three directions corresponding to three axes
    - The minimum steps in each direction correspond to how we can decompose 
      the target coordinate vector optimally
    - We want non-negative steps only
    """
    # Calculate z coordinate
    z = -x - y
    
    # Based on the mathematical properties of hexagonal grids:
    # The optimal path uses the fact that exactly two of {x, y, z} have the same sign
    # and we can reach any point using combinations of the three directions
    
    # The solution is based on the insight that:
    # steps_A = max(0, x, -z)  
    # steps_B = max(0, y, -x)
    # steps_C = max(0, z, -y)
    # But we need to be more careful...
    
    # Actually, the correct approach is:
    # We need to find the minimum non-negative steps in each direction
    # such that the total displacement equals (x, y, z)
    
    # From hexagonal grid theory, the solution is:
    steps_A = max(0, x - min(0, y), -z - min(0, y))
    steps_B = max(0, y - min(0, x), -x - min(0, z)) 
    steps_C = max(0, z - min(0, x), -y - min(0, x))
    
    # Actually, let me use the simpler and more direct approach:
    # Based on the cube coordinate system, the minimum steps are:
    
    if x >= 0 and y >= 0:
        # z <= 0, optimal path uses only A and B
        steps_A = x
        steps_B = y
        steps_C = 0
    elif x <= 0 and y <= 0:
        # z >= 0, optimal path uses only C  
        steps_A = 0
        steps_B = 0
        steps_C = z
    elif x >= 0 and z >= 0:
        # y <= 0, optimal path uses only A and C
        steps_A = x
        steps_B = 0  
        steps_C = z
    elif y >= 0 and z >= 0:
        # x <= 0, optimal path uses only B and C
        steps_A = 0
        steps_B = y
        steps_C = z
    elif x <= 0 and z <= 0:
        # y >= 0, optimal path uses only B
        steps_A = 0
        steps_B = y
        steps_C = 0
    elif y <= 0 and z <= 0:
        # x >= 0, optimal path uses only A
        steps_A = x
        steps_B = 0
        steps_C = 0
    else:
        # This shouldn't happen in valid cube coordinates
        # But just in case, use absolute values
        steps_A = abs(x)
        steps_B = abs(y) 
        steps_C = abs(z)
    
    return steps_A, steps_B, steps_C

def main():
    q = int(input())
    
    for _ in range(q):
        x, y = map(int, input().split())
        steps_A, steps_B, steps_C = solve_hexagon_path(x, y)
        print(steps_A, steps_B, steps_C)

if __name__ == "__main__":
    main()