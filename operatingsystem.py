import os
import shutil

res=os.access(r'D:\Desktop\Python_assignments\ret.txt',os.F_OK)#tells whether the file is present(available) or not
res1=os.access(r'D:\Desktop\Python_assignments\ret.txt',os.R_OK)#tells whether the file is readable or not
res2=os.access(r'D:\Desktop\Python_assignments\ret.txt',os.W_OK)#tells whether the file is writable or not
res3=os.access(r'D:\Desktop\Python_assignments\ret.txt',os.X_OK)#tells whether the file is executable or not
print(res)
print(res1)
print(res2)
print(res3)

res4=os.getcwd()#shows the current working directory
print(res4)

os.chdir(r'D:\Desktop\Python_assignments')#to change directory
res5=os.getcwd()
print(res5)
os.chdir(r'C:\Users\Karthik\AppData\Local\Programs\Python\Python37-32')
res6=os.getcwd()
print(res6)

res=os.environ#to get environment variable
res=os.getenv('AppData')
print(res)

res=os.listdir(r'D:/Desktop')#to list directories
print(res)

#os.mkdir(r'D:/Desktop/PYTHON')#to create folder
#os.makedirs(r'D:/Desktop/PYT/A/B/C')# to create multiple folders recursively

#os.rmdir(r'D:/Desktop/PYT/A/B/C')#delete the last folder

#os.remove(r'D:/Desktop/sumne.txt')#remove text file created

#os.rename(r'D:/Desktop/sumne.txt',r'D:/Desktop/sumne2.txt')#rename file

print(dir(shutil))

#shutil.copy(r'D:/Desktop/sumne.txt',r'C:\Users\Karthik\AppData\Local\Programs\Python\Python37-32\sumne.txt')#copy and paste file n to different directory
#shutil.copy(r'D:/Desktop/sumne.txt',r'C:\Users\Karthik\AppData\Local\Programs\Python\Python37-32\sumne.txt')#cut and paste

res=os.stat(r'D:/Desktop/sumne.txt')#to know complete statistical data about file
print(res)

os.link(r'D:/Desktop/sumne.txt',r'D:/Desktop/Python_assignments/sumne.txt')#it will create shortcut of the file and changes made will reflect in both files
os.system('calc')#it will open calculator#it uses system functions which bridges between command prompt and os

#os.chown(file,oldid, newid)- to change the owner of the file
#os.chmod(file, mode)- to change mode of the file
