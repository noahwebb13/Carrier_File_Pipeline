# Overview of the code: 
Insurance carriers send participant claims on behalf of a client through a file, usually on a scheduled basis such as daily, weekly, or monthly. However, each insurance carrier uses a proprietary file format. And to import the data into a database, these files need to be standardized. 

Here are the high-level steps in this code: 
1) files are dropped into a directory
2) The files are filtered by filename pattern
3) The files are batched
4) The files are mapped to the standard format
5) Finally, an output file is created and dropped to a directory



*Additional Info:*

*In practice, carriers send files through an SFTP and a scheduled job will run this code. Then, the output file is appended to a database table. Futhermore, there are separate jobs that focus on moving files to their correct location - such as a processing folder or archive folder.* 



### Carrier files
Let's say carriers send their files into this directory: 

![alt text](images/carrier_files.png)

Notice that each file has it's own naming convention. Although each file name contains a date, the dates are in different formats. 

---


Lets open the **RCRS** file `medclms.TrueClient_RCRS.01062023.txt`: 


![alt text](images/RCRS.png)

This is a fixed-width file and does not contain column names. In this example, we'll assume the client has already defined the data for us. We know the participant SSN, name, service dates, and claim amount are shown in this screenshot. 

In Summary: 
 - fixed-width
 - no column names


---
Here is the file for **Vision Savings** `VisionSavings_FSA_TrueClient_20230127.txt`: 

![alt text](images/Vision_Savings.png)

- comma-delimited
- no column names
- saved in quotations

---
And here is the file for **Dentlife** `TrueClient_dentlife_01182023.txt`: 

![alt text](images/Dentlife.png)
- pipe-delimited
- has column names
- header and footer data



---

After the process runs, the files are batched together standardized. This makes the data much easier to compare.

**RCRS**: 
![alt text](images/RCRS_mapped.png)

**Vision Savings**:
![alt text](images/Vision_Savings_mapped.png)

**Dentlife**:
![alt text](images/Dentlife_mapped.png)

---

## So how did we get here? 
### Python project directory
Let's open the python project directory. `config.json` and `module.py` are the important files to note. 

![alt text](images/py_folder.png)

---
### config.json file

Important details of the files are stored here such as the file input path, file name pattern, file name date start location, file name date length, and file name date format. 

*Additional Info:*

*Often, clients will include optional text within the file name. Some files received will include this info and some will not. Because of this, the code uses regular expression to get the index position of the file date.*

![alt text](images/config_1.png)

Here's a closer look at the **RCRS** file: 

![alt text](images/config_RCRS.png)


### module.py file

![alt text](images/module_1.png)
![alt text](images/module_2.png)

![alt text](images/module_read.png)
![alt text](images/module_map.png)
![alt text](images/module_dict.png)


