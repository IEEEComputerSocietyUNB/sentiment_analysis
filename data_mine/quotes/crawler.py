import os
import re
import requests
import time

url = 'https://sumitgohil-random-quotes-v1.p.mashape.com/fetch/randomQuote'
myfile = open("a.txt", "a")
for i in range(0,1000):
    start_time = time.time()
    r = requests.get(url, headers={
        "X-Mashape-Key": "4XDW7nDRXdmshu2otYmxX0Qsufuwp1eUiA7jsn9m6AplF3EkLR",
        "Accept": "application/json"
    })
    json_data = r.json()
    quote = json_data[0]['quote']
    quote = re.sub('[^a-zA-Z]+', ' ', quote)    
    myfile.write(quote + '\n')
    myfile.flush()
    print(str(i) + ' ',end="", flush=True)
    elapsed_time = time.time() - start_time
    if(elapsed_time > 15.0):
        print('took too long ' + str(elapsed_time))
        exit(0)

duration = 1  # second
freq = 440  # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))