import pandas

#Creation of a  data frame

#starting dictionary


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

new_data_frame = pandas.DataFrame(data_dict)

#create a csv file from it 
new_data_frame.to_csv("new_data_csv")