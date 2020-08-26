import ast
import pandas as pd
import yaml as ym

def organize_data(file_loc):

    json_file  = file_loc
    data_list = []

    # open the file and read lines
    with open(json_file) as f: 
        data_list.append(f.readlines()) 


    url_data= []
    content_data = []
    auth_datetime = []

    # this for loop is over is the list of data points 
    for row in data_list[0]: 
        
        if len(row) > 2: 

            # ast.literal_eval converts a string to a
            # python object, in this case a list 
            obj= ast.literal_eval(row)
        

            # try statement since the last article entry 
            # does not seem to work with obj[0]. Its just 
            # a work around
            try: 
                auth_datetime.append(obj[0]["auth_datetime"])
                url_data.append(obj[0]["url"])
                content_data.append(obj[0]["content"])
            except: 
                auth_datetime.append(obj["auth_datetime"])
                url_data.append(obj["url"])
                content_data.append(obj["content"]) 
        
    
    return auth_datetime, url_data, content_data


if __name__ == "__main__":
    with open("config.yaml", 'r') as yaml_file:
        config_file = ym.safe_load(yaml_file)
    
    auth_datetime, url_data, content_data =organize_data(config_file["file_loc"])
    print("auth_datetime_length {}" .format( len(auth_datetime)))
