from fileinput import filename

file = '/shome/ubuntu/alert_hub/README.md'

try:
    with open(file, 'r') as r:
        print(r.read())

except FileNotFoundError as error :
    print(error)
except:
    print("deuruim")

print("OK")