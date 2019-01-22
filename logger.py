import re
import glob, os

# # Specifies directory path, if blank glob looks in current directory
# # os.chdir('')

# Looks for .txt files starting with lo 
log_files = glob.glob('lo*.txt')

# # for prd
# dir = os.listdir()
# log_files = list(filter(lambda s: not s.endswith('z') and s.startswith('c'), dir))

# Accepts user input and enters user input into regex objext
search = input('Enter search string >  ')
regex = re.compile(search, re.IGNORECASE)

# Instantiates list to append log data in to  
results = []

# Loops through log_files variable, opens and splits each file into a list, 
# applies regex search, and appends output to results
for file in log_files:
    log_file = open(file, 'r')
    logs = log_file.read().split('\n')
    output = list(filter(regex.search, logs))
    results = results + output
    for item in results:
        print(item)

# Allows to search deeper into returned results, will continue deeper until n or no is specified.
cont_search = input('Search output? y/n > ')

while cont_search != 'n' and cont_search != 'no':
    search = input('Enter search string >  ')
    cont_regex = re.compile(search, re.IGNORECASE)
    cont_output = list(filter(cont_regex.search, results))
    
    for item in cont_output:
        print(item)

    cont_search = input('Search output? y/n > ')






    