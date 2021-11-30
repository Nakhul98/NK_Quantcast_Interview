echo -e "Let's run some tests!!\n"


echo  "Test Case 1: Here's a regular CSV file, like the given test cases: "

time python cookieCounter.py "test1.csv"  "2018-12-09"


echo -e "\nTest Case 2: Here's an empty CSV file: "

time python cookieCounter.py "test2.csv"  "2018-12-09"


echo -e "\nTest Case 3: Here's a CSV file with just the header: "

time python cookieCounter.py "test5.csv" "2018-11-09"


echo -e "\nTest Case 4: Here's a missing argument on command line (file name)"

time python cookieCounter.py  "2018-12-09"


echo -e "\nTest Case 5: Here's a missing argument on command line (date)"

time python cookieCounter.py  "test2.csv"


echo -e "\nTest Case 6: Here's a CSV file with  missing lines: "

time python cookieCounter.py "test3.csv" "2018-12-09"


echo -e "\nTest Case 7: Here's passing in a date out of range: "

time python cookieCounter.py "test4.csv" "2018-11-09"




