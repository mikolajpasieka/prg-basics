###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as file:
   content = file.read()
file.close
# write the content to the target file (copy)
with open(target_file, "w") as file1:
   file1.write(content)