# Proxies
Free Proxy-List with Script to Update

## Figure 1-6 Parts of an IP Address

```
IP [1]
|
| Port [2]
|   |
|   | Country [3]
|   |   |
|   |   | Anonymity [4]
|   |   |  |
|   |   |  |  Type [5]
|   |   |  |   |_ _ _ _ _ _ 
|   |   |  |_ _ _ _ _ _ _  | Passed [6]
|   |   |_ _ _ _ _ _  | |  |
|   |_ _ _ _ _     |  | |  |
|             |    |  | |  |
129.144.50.56:8080 AR-N-S! +

1. IP address
2. Port number
3. Country code
4. Anonymity
   N = No anonymity
   A = Anonymity
   H = High anonymity
5. Type
     = HTTP
   S = HTTP/HTTPS
   ! = incoming IP different from outgoing IP
6. Passed
   + = Yes
   – = No
```

## How to use?
Open terminal and run following commands
```
>> sudo apt-get install git
```
```
>> git clone https://github.com/engineseller/proxies
```
```
>> cd proxies
```
```
>> chmod 755 ./proxies.py
```
```
>> pip3 install -r requirements.txt
```

## Run Proxies
```
>> python3 proxies.py
```

## Download Memcached Servers
```
>> curl -sSf "https://raw.githubusercontent.com/engineseller/data/main/memcached_servers.txt" > memcached_servers.txt
```

## Download NTP Servers
```
>> curl -sSf "https://raw.githubusercontent.com/engineseller/data/main/ntp_servers.txt" > ntp_servers.txt
```

## Download Referers
```
>> curl -sSf "https://raw.githubusercontent.com/engineseller/data/main/referers.txt" > referers.txt
```

## Download NTP Servers
```
>> curl -sSf "https://raw.githubusercontent.com/engineseller/data/main/useragent.txt" > useragent.txt
```
