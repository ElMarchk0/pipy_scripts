# Write 'temp' to the file called "file_name"
def write_temp(temp, file_name):
    f = open(file_name, "w")
    f.write(str(temp))
    f.close()
# Return the value contained in the file called "file_name"
def read_temp(file_name):
    f = open(file_name, "r")
    temp = f.read()
    f.close()
    return float(temp)
