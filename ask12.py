from urllib.request import Request, urlopen
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=data.decode()
data=data.split(',')
last_round=""
a_string=''
max1=0
max0=0
last_round_string=data[0]
last_round_number=last_round_string[9:]
last_round_number_list=list(last_round_number)
for i in last_round_number_list:
    last_round=last_round+str(i)
last_round=int(last_round,10)
for i in reversed(range(last_round-100,last_round)):
    req2 = Request('https://drand.cloudflare.com/public/'+str(i), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data2 = urlopen(req2).read()
    data2=data2.decode()
    data2=data2.split(',')
    randomness=data2[1][15:-1]
    dec_randomness=int(randomness,16)
    bin_randomness=bin(dec_randomness)
    bin_randomness_final=bin_randomness[2:]
    a_string=a_string+str(bin_randomness_final)
string_of_ones=a_string.split('0')
string_of_zeros=a_string.split('1')
for i in string_of_ones:
    if len(i)>max1:
        max1=len(i)
        biggest_sequence_1=i
for i in string_of_zeros:
    if len(i)>max0:
        max0=len(i)
        biggest_sequence_0=i
print('The biggest sequence of ones is:'+str(biggest_sequence_1)+':'+str(max1))
print('The biggest sequence of zeros is:'+str(biggest_sequence_0)+':'+str(max0))



