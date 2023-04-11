# CMPS 2200 Reciation 5
## Answers

**Name:** Ritika Mishra and Izzy Chow (I think she submitted the lab but Im adding these just incase). 


Place all written answers from `recitation-06.md` here for easier grading.





- **1b.**
If n is small, qsort-random-pivot is significantly faster than qsort-fixed-pivot which is evident when you graph the results with Matplot.lib. When n gets larger the turns change as qsort-fixed-pivot becomes faster than qsort-random-pivot, which can be seen through the graph and the table which comes up when you run the code, with very large values of n, the runing times of qsort-random-pivot are much larger compared to qsort-fixed-pivot. The running times make sense compared to the asympotic bounds. The bounds we know for quicsort is the worst case is O(n^2) and the average case is O(n lg n). As seen through the graph, when n is small, both running times stay within the average case bounds of O(n lg n). When n gets large, qsort-random-pivot stays within the bounds of the worse case bound of O(n^2) and qsort-fixed-pivot stays within the average case boungs of O(n lg n). There are many different scenarios where changing the type of input list matters. Depending on the type of the list there will be different runtimes. For example, using a randomly sorted input list vs. an already sorted input list. For an already sorted list, qsort-random-pivot would be better where as for a random list, both runtimes will be similar. 



- **1c.**
For all values of n, Timesort was much much faster than my sorting implementations. The worst-case running time of Timesort is O(n lg n) which is the same as the average-case running time of my algorithm. 
