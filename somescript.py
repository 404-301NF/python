def process(string):
    print('Processing:',string)
with open(r'g:\dbm\somefilt.txt','r+') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)