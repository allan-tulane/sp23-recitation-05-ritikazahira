import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a)<= 1:
      return a
    else:
      pivot_index = pivot_fn(a)
      pivot = a[pivot_index]
      left = []
      right = []
      pivots = []
      for i, x in enumerate(a):
        if i!= pivot_index:
          if x < pivot:
            left.append(x)
          else:
            right.append(x)
        else:
          pivots.append(x)
      return qsort(left, pivot_fn) + [pivot] + qsort(right, pivot_fn)
    pass
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.
    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.
    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 
    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.
    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    def qsort_fixed_pivot(lst):
      if not lst:
        return []
      else:
        pivot = lst[0]
        left = [x for x in lst[1:] if x < pivot]
        right = [x for x in lst[1:] if x >= pivot]
        return qsort_fixed_pivot(left) + [pivot] + qsort_fixed_pivot(right)

    def qsort_random_pivot(lst):
      if not lst:
        return []
      else:
        pivot_index = random.randint(0, len(lst)-1)
        pivot = lst[pivot_index]
        left = [x for i, x in enumerate(lst) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(lst) if x > pivot and i != pivot_index]
        return qsort_random_pivot(left) + [pivot] + qsort_random_pivot(right)

    def tim_sort(lst):
      return sorted(lst)

    def time_sort(algorithm, lst):
      start_time = time.time()
      algorithm(lst)
      end_time = time.time()
      return (end_time - start_time) * 1000

  
    result = []
    for size in sizes:
        
        mylist = list(range(size))
        
        random.shuffle(mylist)
        qsort_fixed_pivot_time = time_sort(qsort_fixed_pivot, mylist)
        qsort_random_pivot_time = time_sort(qsort_random_pivot, mylist)
        time_sort_time = time_sort(tim_sort, mylist)
        result.append([len(mylist), qsort_fixed_pivot_time, qsort_random_pivot_time, time_sort_time])
        
    print_results(result)
    ###

def print_results(result):
    """ change as needed for comparisons """
    print(tabulate.tabulate(result,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort([100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]))

random.seed()
test_print()
