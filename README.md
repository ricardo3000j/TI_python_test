# TI_python_test
Team International Python Test - Ricardo Jarquin

## Project Stack

- Python 3.11.4

## Project Structure
- `main.py` - Entrypoint for the execution of main app
- `data_capture.py` - Module where DataCapture and Statistics are defined
- `/tests` - test suite written with unittest
- `/tests/unit_test` - unit test of the project related to DataCapture and Statitics classes
- `/tests/integration_test`- Test to validate the full execution of the app


## Code Standards 
- This project uses Python `black` based code formatting, [read all about it](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)

### Running the project locally
- To run the application execute `python main.py`
- To run the test suite execute `python -m unittest discover tests`
## Testing
The test suite was designed using unittest test. 
This suite include unit testing for each method of the classes and integration testing to test the app execution. 
## Solving Explanation
# Assumptions
    - All the input integers are positive and have a value less than 1000. Negative interger and non interger values won't be stored in the collection
    - The collection of integers allows duplicated values, meaning the data collector can store the same values multiple times. The use of a set as a data structure is discarded.


Based on the assumption and the requirement to calculate the statistics, the data structure to store the collection of integers is a counter array. 
This allows storing numbers in a sorted collection where the index of the array is the integer itself, and the value of the array is the count of occurrences.


To calculate the statistics of the collection, an array will also be used as a data structure. 
where the index will be the interger itself but the value of element will be the cumulative sum of all the previuos elements 
and the count of ocurrence of the current interger. This allow to calculate the statitic Less, greater and between only providing
the interger(index) instead of interate over the array each time the any of the methods is requested. 

`DataCapture` class allows to create capture object
The capture object has these attributes
    Attributes:
    - `counter`: counter array for integer numbers. 
    - `cumulative_sum`: array for cumulative sum of counter array values
    Both attributes are initialized as an array of zeros with a length of 1000 since the assumption is to store integers with a value less than 1000.


`Statistics class` allows to create stats object
the stats object has these attributes
    attributes:
    - `cumulative_sum`: array for cumulative sum of counter array values

the calculation of the statistic through `less`, `greater` and `between` methods is done using the cumulative_sum attribute allowing an algorithm complexity of O(1)
 


