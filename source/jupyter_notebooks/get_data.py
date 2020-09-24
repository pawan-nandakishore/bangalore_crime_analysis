import ast
import pandas as pd
import yaml as ym
import json
def organize_data(file_loc):

    json_file  = file_loc
    data_list = []

    # open the file and read lines
    with open(json_file) as f: 
        data_list = json.load(f) 

   
    url_data= []
    content_data = []
    auth_datetime = []

    # this for loop is over is the list of data points 
    for indx, row in enumerate(data_list): 

        if len(row) > 2: 

            try: 

                auth_datetime.append(row["auth_datetime"])
                url_data.append(row["url"])
                content_data.append(row["content"])

            except: 
                auth_datetime.append(row["auth_datetime"])
                url_data.append(row["url"])
                content_data.append(row["content"]) 

    
    
    return auth_datetime, url_data, content_data


if __name__ == "__main__":
    with open("config.yaml", 'r') as yaml_file:
        config_file = ym.safe_load(yaml_file)
    
    auth_datetime, url_data, content_data =organize_data(config_file["file_loc"])
    print("auth_datetime_length {}" .format( len(auth_datetime)))
