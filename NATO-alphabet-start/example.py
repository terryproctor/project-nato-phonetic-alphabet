student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    #print(key, value)
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #print(index, row.student, row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
student_scores = {row.student : row.score for (index, row) in student_data_frame.iterrows()}
#print(student_scores)
