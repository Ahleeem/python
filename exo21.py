import statistics

def length(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return len(lst)



def mean(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("The list is empty, cannot calculate mean.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return sum(lst) / len(lst)



def range_of_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("The list is empty, cannot calculate range.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return max(lst) - min(lst)



def median(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("The list is empty, cannot calculate median.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return statistics.median(lst)




def standard_deviation(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("The list is empty, cannot calculate standard deviation.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements in the list must be numeric.")
    
    return statistics.stdev(lst)




def list_statistics(lst):
    stats = {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Standard Deviation": standard_deviation(lst)
    }
    return stats



numbers = [1, 2, 3, 4, 5]

print("Length:", length(numbers))  
print("Mean:", mean(numbers))  
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))  
print("Standard Deviation:", standard_deviation(numbers))  
print("List Statistics:", list_statistics(numbers))
