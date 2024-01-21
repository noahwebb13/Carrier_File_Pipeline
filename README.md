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



## Carrier files
Let's say carriers send their files into this directory: 

![alt text](images/carrier_files.png)

Notice that each file has it's own naming convention. Although each file name contains a date, the dates are in different formats. 

---


Lets open the RCRS file (Real Carrier Real Service - aka fake carrier): 

![alt text](images/RCRS.png)

The file is in a fixed width format and does not contain columne names. 
![alt text](images/Vision_Savings.png)
![alt text](images/Dentlife.png)

![alt text](images/RCRS_mapped.png)
![alt text](images/Vision_Savings_mapped.png)
![alt text](images/Dentlife_mapped.png)



## Python project directory
![alt text](images/py_folder.png)

## module.py file

![alt text](images/module_1.png)
![alt text](images/module_2.png)

![alt text](images/module_read.png)
![alt text](images/module_map.png)
![alt text](images/module_dict.png)

## config.json file

![alt text](images/config_1.png)
![alt text](images/config_RCRS.png)

