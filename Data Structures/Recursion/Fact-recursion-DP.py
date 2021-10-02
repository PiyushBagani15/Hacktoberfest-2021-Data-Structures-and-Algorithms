New_memory = {} #creating speacial extra space where we store the output of once calculatd sub operations

def f(n, memo):   # O(n): linear 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif  n < 0:
        return "not supported"
    if not n in memo:
        memo[n] = f(n-1 , memo) + f(n-2, memo)
    return memo[n]
