def update_server_file(filepath,key,value):
    with open(filepath, 'r') as File:
        lines = File.readlines()

    with open(filepath, 'w') as File:
        for line in lines:
            if key in line:
                File.write(key + "=" + value)
            else:
                File.write(line)
                print(line)

filepath = r"C:\Users\acer\OneDrive\Desktop\projects\python-for-devops\server.conf"
key = "MAX_CONNECTIONS"
value = "1000"

update_server_file(filepath,key,value)