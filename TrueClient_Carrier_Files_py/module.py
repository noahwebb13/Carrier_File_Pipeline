import os 
import re
import pandas as pd
import json

# Read file functions
# ---------------------------


def read_TrueClient_RealMedCarrier(f):

    # reading data frame
    df = pd.read_csv(f, 
            delimiter = ',',
            skiprows = 0, 
            header = 0, 
            dtype = str
            )
    return(df)

def read_TrueClient_RCRS(f):

    # reading data frame
    df = pd.read_fwf(f, 
            widths = [9,3,9,1,14,3,10,10,10,15,33,9,1,1,11,15,16,9,9,3,25,50,15,2,5,10,27],
            skiprows = 0, 
            header = None, 
            dtype = str
            )
    return(df)

def read_TrueClient_Dentlife(f):

    # reading data frame
    df = pd.read_csv(f, 
        delimiter = '|',
        skiprows = 1, 
        header = 0, 
        dtype = str,
        encoding= 'unicode_escape'
        )

    # removing the footer record
    df = df.drop(df.index[-1])

    return(df)

def read_TrueClient_VisionSavings(f):

    # reading data frame
    df = pd.read_csv(f, 
        delimiter = ',',
        skiprows = 0, 
        header = None, 
        dtype = str,
        # encoding= 'unicode_escape'
        )
    return(df)

# Map functions
# ---------------------------
def map_TrueClient_RealMedCarrier(batch, output_header, employer_code): 
    
    print('\n\nmapping file to standard format...')

    # creating a data frame with specified output_header
    output_df = pd.DataFrame(columns=output_header, dtype=str)
    

    # Filling in DataFrame columns from the batch dataframe 
    output_df['EMPLOYER_TAX_ID']            = ''
    output_df['PARTICIPANT_SSN']            = batch['ParticipantSSN']
    output_df['PARTICIPANT_LAST_NAME']      = batch['ParticipantLastName']
    output_df['PARTICIPANT_FIRST_NAME']     = batch['ParticipantFirstName']
    output_df['PARTICIPANT_MIDDLE_INITIAL'] = ''
    output_df['PARTICIPANT_DATE_OF_BIRTH']  = batch['ParticipantDOB']
    output_df['PATIENT_LAST_NAME']          = batch['PatientLastName']
    output_df['PATIENT_FIRST_NAME']         = batch['PatientFirstName']
    output_df['PATIENT_MIDDLE_INITIAL']     = ''
    output_df['CARRIER_SYSTEM']             = 'RealCarrierSystem'
    output_df['SERVICE_START_DATE']         = batch['ServiceStartDate']
    output_df['SERVICE_THRU_DATE']          = batch['ServiceEndDate']
    output_df['CLAIM_NUMBER']               = batch['ClaimID']

    output_df['CLAIM_AMOUNT']               = pd.to_numeric(batch['ClaimAmount'])
    
    output_df['PROVIDER_NAME']              = batch['MedicalProvider']
    output_df['PROVIDER_ADDRESS1']          = batch['ProviderAddress']
    output_df['PROVIDER_ADDRESS2']          = ''
    output_df['PROVIDER_CITY']              = batch['ProviderCity']
    output_df['PROVIDER_STATE']             = batch['ProviderState']
    output_df['PROVIDER_ZIP']               = batch['ProviderZipCode']
    output_df['PROVIDER_COUNTRY']           = batch['ProviderCountry']
    output_df['CLAIM_TYPE']                 = ""
    output_df['FILE_NAME']                  = batch['FILE_NAME']
    output_df['EXPENSE_CATEGORY']           = "Medical"
    output_df['EMPLOYER_CODE']              = employer_code

    return(output_df)

def map_TrueClient_RCRS(batch, output_header, employer_code): 
    
    print('\n\nmapping file to standard format...')

    # creating a data frame with specified output_header
    output_df = pd.DataFrame(columns=output_header, dtype=str)
    # output_df = output_df.astype(str)

    # Filling in DataFrame columns from the batch dataframe 
    output_df['EMPLOYER_TAX_ID']            = ""
    output_df['PARTICIPANT_SSN']            = batch[0].str.zfill(9)
    output_df['PARTICIPANT_LAST_NAME']      = batch[4]
    output_df['PARTICIPANT_FIRST_NAME']     = batch[2]
    output_df['PARTICIPANT_MIDDLE_INITIAL'] = batch[3]
    output_df['PARTICIPANT_DATE_OF_BIRTH']  = ""
    output_df['PATIENT_LAST_NAME']          = batch[15]
    output_df['PATIENT_FIRST_NAME']         = batch[14]
    output_df['PATIENT_MIDDLE_INITIAL']     = ""
    output_df['CARRIER_SYSTEM']             = ""
    output_df['SERVICE_START_DATE']         = batch[6]
    output_df['SERVICE_THRU_DATE']          = batch[7]
    output_df['CLAIM_NUMBER']               = batch[11]
    output_df['CLAIM_AMOUNT']               = pd.to_numeric(batch[9])
    output_df['PROVIDER_NAME']              = batch[20]
    output_df['PROVIDER_ADDRESS1']          = batch[21]
    output_df['PROVIDER_ADDRESS2']          = ""
    output_df['PROVIDER_CITY']              = batch[22]
    output_df['PROVIDER_STATE']             = batch[23]
    output_df['PROVIDER_ZIP']               = batch[24]
    output_df['PROVIDER_COUNTRY']           = ""
    output_df['CLAIM_TYPE']                 = ""
    output_df['FILE_NAME']                  = batch['FILE_NAME']
    output_df['EXPENSE_CATEGORY']           = "medical"
    output_df['EMPLOYER_CODE']              = employer_code

    return(output_df)

def map_TrueClient_Dentlife(batch, output_header, employer_code): 
    
    print('\n\nmapping file to standard format...')

    # creating a data frame with specified output_header
    output_df = pd.DataFrame(columns=output_header, dtype=str)
    # output_df = output_df.astype(str)

    # Filling in DataFrame columns from the batch dataframe 
    output_df['EMPLOYER_TAX_ID']            = batch['EMPLOYER_TAX_ID']
    output_df['PARTICIPANT_SSN']            = batch['PARTICIPANT_SSN']
    output_df['PARTICIPANT_LAST_NAME']      = batch['PARTICIPANT_LAST_NAME']
    output_df['PARTICIPANT_FIRST_NAME']     = batch['PARTICIPANT_FIRST_NAME']
    output_df['PARTICIPANT_MIDDLE_INITIAL'] = batch['PARTICIPANT_MIDDLE_INITIAL']
    output_df['PARTICIPANT_DATE_OF_BIRTH']  = batch['PARTICIPANT_DATE_OF_BIRTH']
    output_df['PATIENT_LAST_NAME']          = batch['PATIENT_LAST_NAME']
    output_df['PATIENT_FIRST_NAME']         = batch['PATIENT_FIRST_NAME']
    output_df['PATIENT_MIDDLE_INITIAL']     = batch['PATIENT_MIDDLE_INITIAL']
    output_df['CARRIER_SYSTEM']             = batch['CARRIER_SYSTEM']
    output_df['SERVICE_START_DATE']         = batch['SERVICE_START_DATE']
    output_df['SERVICE_THRU_DATE']          = batch['SERVICE_THRU_DATE']
    output_df['CLAIM_NUMBER']               = batch['CLAIM_NUMBER']

    output_df['CLAIM_AMOUNT']               = pd.to_numeric(batch['CLAIM_AMOUNT'].str[:-1])  # removing the last character ('{' or 'B')
    output_df['CLAIM_AMOUNT']               = output_df['CLAIM_AMOUNT'] / 100                    # dividing by 100 

    output_df['PROVIDER_NAME']              = batch['PROVIDER_NAME']
    output_df['PROVIDER_ADDRESS1']          = batch['PROVIDER_ADDRESS1']
    output_df['PROVIDER_ADDRESS2']          = batch['PROVIDER_ADDRESS2']
    output_df['PROVIDER_CITY']              = batch['PROVIDER_CITY']
    output_df['PROVIDER_STATE']             = batch['PROVIDER_STATE']
    output_df['PROVIDER_ZIP']               = batch['PROVIDER_ZIP']
    output_df['PROVIDER_COUNTRY']           = batch['PROVIDER_COUNTRY']
    output_df['CLAIM_TYPE']                 = ""  
    output_df['FILE_NAME']                  = batch['FILE_NAME']
    output_df['EXPENSE_CATEGORY']           = "dental"
    output_df['EMPLOYER_CODE']              = employer_code

    return(output_df)

def map_TrueClient_VisionSavings(batch, output_header, employer_code): 
    
    print('\n\nmapping file to standard format...')
    
    # creating a data frame with specified output_header
    output_df = pd.DataFrame(columns=output_header, dtype=str)

    # Filling in DataFrame columns from the batch dataframe
    output_df['EMPLOYER_TAX_ID']            = batch[0]
    output_df['PARTICIPANT_SSN']            = batch[1]
    output_df['PARTICIPANT_LAST_NAME']      = batch[2]
    output_df['PARTICIPANT_FIRST_NAME']     = batch[3]
    output_df['PARTICIPANT_MIDDLE_INITIAL'] = batch[4]
    output_df['PARTICIPANT_DATE_OF_BIRTH']  = batch[5]
    output_df['PATIENT_LAST_NAME']          = batch[6]
    output_df['PATIENT_FIRST_NAME']         = batch[7]
    output_df['PATIENT_MIDDLE_INITIAL']     = batch[8]
    output_df['CARRIER_SYSTEM']             = batch[9]
    output_df['SERVICE_START_DATE']         = batch[10]
    output_df['SERVICE_THRU_DATE']          = batch[11]
    output_df['CLAIM_NUMBER']               = batch[12]
    output_df['CLAIM_AMOUNT']               = pd.to_numeric(batch[13])
    output_df['PROVIDER_NAME']              = batch[14]
    output_df['PROVIDER_ADDRESS1']          = batch[15]
    output_df['PROVIDER_ADDRESS2']          = batch[16]
    output_df['PROVIDER_CITY']              = batch[17]
    output_df['PROVIDER_STATE']             = batch[18]
    output_df['PROVIDER_ZIP']               = batch[19]
    output_df['PROVIDER_COUNTRY']           = batch[20]
    output_df['CLAIM_TYPE']                 = batch[21]
    output_df['FILE_NAME']                  = batch['FILE_NAME']
    output_df['EXPENSE_CATEGORY']           = "vision"
    output_df['EMPLOYER_CODE']              = employer_code

    

    return(output_df)


# Creating dictionaries
# The carrier names must be the same as the config.json file
# ---------------------------
read = {
    'RealMedCarrier': read_TrueClient_RealMedCarrier,
    'RCRS': read_TrueClient_RCRS,
    'Dentlife': read_TrueClient_Dentlife, 
    'VisionSavings': read_TrueClient_VisionSavings, 
}

map = {
    'RealMedCarrier': map_TrueClient_RealMedCarrier,
    'RCRS': map_TrueClient_RCRS,
    'Dentlife': map_TrueClient_Dentlife, 
    'VisionSavings': map_TrueClient_VisionSavings, 
}






# --- EDIT ABOVE ONLY --- 







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

