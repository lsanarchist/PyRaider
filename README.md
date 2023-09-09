# PyRaider

This program collects system information and file paths from the specified directories and sends them as a document to a specified chat using the Telegram bot API. Here's an overview of how the program works:

 1) It imports necessary modules: telebot for interacting with the Telegram bot API, platform for retrieving system information, os for interacting with the operating system, time for timing the execution, psutil for retrieving system resource information, and zipfile for creating a compressed archive.

 2) The write_file_paths function is defined to write the file paths of a specified directory to an output file. It traverses the directory recursively and writes each file path to the output file.

 3) The program sets up the Telegram bot using the provided TOKEN and CHAT_ID.

 4) System information is collected using the platform and psutil modules. Information such as the operating system, processor, Python version, memory usage, CPU usage, and disk space is collected and stored in the info variable.

 5) The program initializes variables for storing CPU usage, memory information, and disk usage.

 6) The write_file_paths function is called for each drive letter from 'A' to 'Z'. The file paths for each drive are written to the output_file_path file, along with the system information stored in the info variable.

 7) The file paths are then compressed into a ZIP archive using the zipfile module and saved as archive_file_path.

 8) The output_file_path file is deleted as it is no longer needed.

 9) The program sends the compressed archive file as a document to the specified chat using the Telegram bot.

 10) The compressed archive file is deleted from the local system.

 11) The program exits.

Overall, this program collects system information, retrieves file paths from specified directories, and sends the collected data as a compressed archive file to a Telegram chat using a bot.


![image](https://github.com/lsanarchist/PyRaider/assets/59514149/d45a74bd-bbb6-4fe9-a8b0-dd263ea52d5a)
Do we got wallet.dat?
Better, we got path to wallet.dat




