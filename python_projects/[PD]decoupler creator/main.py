import pandas as pd

result = []

duplicates = pd.read_csv('query_input.csv')  # output of SQL query
people = pd.read_csv('CRM_PEOPLE.csv')  # CRM itself

result_df = pd.merge(people, duplicates, how='left', left_on=['firstname', 'lastname'],  # merging both dataframes
                     right_on=['firstname_cor', 'lastname_cor'])

to_delete = result_df[~result_df['firstname_cor'].isnull()]  # selecting only rows where we have duplicates with people from CRM
#to_delete.to_excel('to_delete.xlsx')  # outputs excel of duplicates (just for visual check)

decoup = list(zip(to_delete['firstname_cor'].tolist(), to_delete['lastname_cor'].tolist()))  # list of duplicated names/surnames

for elem in decoup:  # adding firstname, lastname to our template, repeating for each duplicate
    (fn, ln) = elem
    result.append("""  {{
  "firstname": "{}",
  "lastname": "{}",
  "corrected_firstname": "{}",
  "corrected_lastname": "{}"
  }}""".format(ln, fn, fn, ln))

with open('result.txt', 'w') as file:  # saving previous result to .txt file
    for line in result:
        file.write(str(line))
        file.write(',')
        file.write('\n')
