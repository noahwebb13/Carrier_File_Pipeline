# Carrier_File_Pipeline
I created this project to map files sent from health insurance carriers into a standard format. Because health insurance companies use proprietary file formats and naming conventions, it was important to create the code simple and scalable. 

Here is the process: 
1) files are dropped into a directory
2) The files are filtered by filename pattern
3) The files are sorted by the date in the file name
4) The files are batched
5) The files are mapped to the standard format
6) Finally, a file is created and dropped to the output directory


In practice, cleints send files through an SFTP and a scheduled job will run this code. Then, the output file is appended to a database table. Futhermore, there are separate jobs that focus on moving files to their correct location - such as a processing folder or archive folder. 

