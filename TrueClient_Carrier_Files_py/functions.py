import os 
import re
import pandas as pd
import json

# List files function
# ---------------------------
def list_files_date_regx(file_input_path, file_name_pattern, date_start_regx, date_length):
    print(f"\n\nListing files from directory [{file_input_path}] ...")

    # setting the working directory to file_input_path 
    # os.chdir(file_input_path)

    # listing files from the directory that match file_name_pattern 
    file_list = []
    for f in os.listdir(file_input_path):
        if re.search(file_name_pattern, f):
            
            # getting absolute path and converting to raw string
            fpath = file_input_path + '/' + f

            # attaching path to file_list
            file_list.append(fpath)

    # finding the index of the date in the file name
    index_list = []
    for f in file_list:
        m = re.search(date_start_regx, f)
        if m: 
            index_list.append(m.end())

    # saving dates in a list
    file_dates = []
    for f, i, in zip(file_list, index_list):
        file_dates.append(f[i:i+date_length])

    # creating a data frame with the file_list and file_dates
    file_list_df = pd.DataFrame({"file_list": file_list, "file_dates": file_dates})

    # returning file_list_df
    return(file_list_df)


# concat function
# ---------------------------
def concat_carrier(carrier, file_input_path, file_name_pattern, date_start_regx, date_length, date_format):

    # listing files
    file_list_df = list_files_date_regx(file_input_path, file_name_pattern, date_start_regx, date_length)
    file_list_df['file_dates'] = pd.to_datetime(file_list_df['file_dates'], format = date_format)     # converting dates 
    file_list_df = file_list_df.sort_values(by='file_dates', ascending=True)                      # sorting 

    # creating empty dataframe 
    batch = pd.DataFrame()

    # iterating through list of files
    for f in file_list_df['file_list']:

        # retrieving the base file name for logging
        fName = os.path.basename(f)

        print(f"reading file [{fName}]...")

        # read file by referencing the read_file dictionary
        df = read[carrier](f)

        # removing NAs
        df.fillna('', inplace=True)

        # adding file_name column
        df['FILE_NAME'] = fName

        # concating rows to the batch dataframe
        batch = pd.concat([batch, df])

    print(f"\nfiles batched!")

    # getting date range from the list of files within the folder (selecting the first 10 characters only)
    files_end_dt = str(file_list_df.iloc[0,1])[:10]
    files_start_dt = str(file_list_df.iloc[-1,1])[:10]

    # returning variables 
    return(batch, file_name_pattern, files_start_dt, files_end_dt)


# concat and map function
# ---------------------------
def concat_and_map(carrier):
    
    # open and read config.json file
    with open('config.json', 'r') as config_file: 
        config = json.load(config_file)

    # storing variables from config.json file 
    file_input_path   = config[carrier]['file_input_path']
    file_name_pattern = config[carrier]['file_name_pattern']
    date_start_regx   = config[carrier]['date_start_regx']
    date_length       = config[carrier]['date_length']
    date_format       = config[carrier]['date_format']
    output_header     = config['output']['output_header']
    output_path       = config['output']['mapped_output_path']
    employer_code     = config['output']['employer_code']

    # calling function from the concat dictionary and saving variables
    batch, file_name_pattern, files_start_dt, files_end_dt = concat_carrier(carrier, file_input_path, file_name_pattern, date_start_regx, date_length, date_format)

    # calling function from the map dictionary and saving the output dataframe
    output_df = map[carrier](batch, output_header, employer_code)

    # writing a csv file to output path
    file_name = employer_code + '_' + carrier + '_mapped_' + files_start_dt + '_to_' + files_end_dt + '.csv'
    file_output_path = output_path + '/' + file_name

    print(f'\n\nwriting file [{file_name}] to directory: ')
    print(f'[{output_path}]...')

    output_df.to_csv(file_output_path, index = False)
    print('\n\nDone!')

    return output_df, file_name


# batching all carrier files
# ---------------------------
def batch_carrier_files(): 
    
    # reading config.json file
    with open('config.json', 'r') as config_file: 
        config = json.load(config_file)

    # saving variables from the json file
    input_path = config['output']['mapped_output_path'] 
    file_name_pattern = '(.*)(_mapped_)(.*)(_to_)'
    date_start_regx = '(.*)(_mapped_)(.*)(_to_)'
    date_length = 10

    # listing files from the directory
    file_list_df = list_files_date_regx(input_path, file_name_pattern, date_start_regx, date_length)

    # creating empty dataframe 
    batch = pd.DataFrame()

    # iterating through list of files
    for f in file_list_df['file_list']:

        # retrieving the base file name for logging
        fName = os.path.basename(f)
        print(f"reading file [{fName}]...")

        # reading data frame
        df = pd.read_csv(f, 
                delimiter = ',',
                skiprows = 0, 
                header = 0, 
                dtype = str,
                # encoding= 'unicode_escape'
                )

        # removing NAs
        df.fillna('', inplace=True)

        # concating rows to the batch dataframe
        batch = pd.concat([batch, df])
    

    print(f"\nfiles batched!")
    return(batch)

