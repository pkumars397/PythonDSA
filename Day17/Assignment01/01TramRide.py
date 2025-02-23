def solve (N, start, finish, ticket_cost):
    start -= 1
    finish -= 1
    
    # If the start and finish are the same, cost is zero
    if start == finish:
        return 0
 
    # Compute clockwise cost
    if start < finish:
        clockwise_cost = sum(ticket_cost[start:finish])
    else:
        clockwise_cost = sum(ticket_cost[start:]) + sum(ticket_cost[:finish])
 
    # Compute total cost of all tickets
    total_cost = sum(ticket_cost)
 
    # Compute anti-clockwise cost
    anti_clockwise_cost = total_cost - clockwise_cost
 
    # Return the minimum of the two costs
    return min(clockwise_cost, anti_clockwise_cost)

N=4
start=1
end=4
tList=[1,2,2,4]
print(solve(N,start,end,tList))