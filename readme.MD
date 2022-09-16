# Software Design with Python
## Assignment 1 Repository

>Run _main.py_ to see how tasks are completed. 

All source (*.py) files are stored in '_src/_' directory
1. **_main.py_**
   * file to run.
   * contains test function
   * apply implemented in tasks 1-4 decorators on test functions
   * shows test results
2. **_task1.py_** 
   * contains function decorator that print information about decorated function:
     * function name
     * number of this function calls
     * function execution time
3. **_task2.py_**
    * contains function decorator that print information about decorated function:
   1. information row from task 1
   2. function name
   3. type of object
   4. object signature
   5. arguments
      1. positional
      2. key-worded
   6. docstring
   7. source
   8. output
4. **_task3.py_**
    * contains class decorators with the same behaviour as ones from tasks 1 and 2
    * also implemented class decorator that rank decorated functions by the execution time 
5. **_task4.py_**
   * extend **decorator1** behaviour protecting functions from errors using '_Try and Except_' statement
   * in case of error redirects stderr to log file with timestamp of error.