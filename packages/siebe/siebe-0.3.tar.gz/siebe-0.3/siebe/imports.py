# datastructing means manipulating the actual structure 'around the data' for enhanced convenience but does not affect the data itself 

def keys_to_dataframe_by1stLetter(keys):
    """
    input: list of keys

    This function takes a LIST of keys and returns a DF with the first letter of each key under COLUMN[A-Z] to which the first letter of the key corresponds

    returns a dataframe
    """
    import pandas as pd
    
    letter_dict = {chr(i): [] for i in range(97, 123)} # create a dictionary with the letters a to z as keys
    
    # add every letter to the dictionary as a VALUE to the KEY that corresponds to the first letter of the company name
    for key in keys:
        try:
         letter_dict[key[0]].append(key)
        except KeyError:
            pass
        
    # convert the dictionary to a dataframe with nan for empty values
    df = pd.DataFrame.from_dict(letter_dict, orient='index').T
    
    return df

def read_excel_file(file_path, sheet_name):
    import pandas as pd
    """
    This function will read an excel file and return a dataframe.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
        exit()
    except KeyError:
        print("The specified sheet was not found in the file. Please check the sheet name and try again.")
        exit()
