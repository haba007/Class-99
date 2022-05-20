import os
import shutil

sources=input("enter your path")
destination=input("enter your destination path")
sources=sources+"/"
destination=destination+"/"
list=os.listdir(sources)
for file in list:
    shutil.copy((sources+file),destination)