# proz
Provisioning and Zero Touch Provisioning on MikroTik

## Requirement
<ul>
  <li>Python 3.x </li>
  <li>flask</li>
  <li>tqdm</li>
  <li>netmiko</li>
</ul>

## Install requirement library
```
pip3 install -r requirement
```

## To show help
```
python3 proz.py -h
```

## Example run script
```
python3 proz.py --module Mikrotik --action provision
```
### More info
 - the ztp by default is use pppoe
 - to change the pppoe script you can access the file on "./script/ztp/listen.txt"
 - to change the MikroTik name, ip, port, user, and password, chage from json files
 - to change the script to send on client or main router you can change from script files
