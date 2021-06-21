# PMP

PMP is a simple calculator for pool operators. It prompts the user for the results of their daily test results, then caculates the amount and type of chemicals to add to effect the desired change in chemistry. While there are some bugs listed below, it is functional at this point. 

## To Run
This is a small CLI program, and no installation is necessary. Simply navigate to the directory containing PMP in your chosen terminal and type:

```
$ python PMP.py
```
You will be prompted for the results of your daily chemical tests, and from there you can select from the menu options.


## *Updates*
10/13/20

Added the export_test_results function which exports the daily tests to a csv file. Currently, I'm looking at implementing an SQlite database that would store the test results and that you could query to pull specific results from. 

The print_table function is still not displaying properly. I have no idea why. I'm seriously considering scrapping this function, putting the information into a Pandas dataframe and pretty printing it. 


5/25/20

The print_table function is not displaying the table properly


