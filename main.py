import heapq

def min_cost_of_connection(cables):

    heapq.heapify(cables)
    
    total_cost = 0

    while len(cables) > 1:

        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost


if __name__ == "__main__":
    
    # Тестування
    cables = [10, 74, 5, 40, 35, 21, 60, 67, 12]
    print("Мінімальні загальні витрати:", min_cost_of_connection(cables))