import os 
import shutil
sources="C:/Users/medar/OneDrive/Desktop/Python/Class-99/copy1.txt"
destination="C:/Users/medar/OneDrive/Desktop/Python/Class-99/copy2.txt"
sou=shutil.copy(sources,destination)
dest=shutil.move(sources,destination)