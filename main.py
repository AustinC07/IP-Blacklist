import requests, csv, subprocess

#source=Abuse CH
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv%22).text

rule="netsh advfirewall firewall delete rule name='MaliciousIPs'"
subprocess.run(["Powershell", "-Command", rule])

mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
for row in myscv:
         ip = row[1]
         if(ip)!=("dst_ip"):
         print("Added Rule to block:",ip)
         rule="netsh advfirewall firewall add rule name='MaliciousIps' Dir=Out Action=Block RemoteIP="+ip
         subprocess.run(["Powershell", "-Command", rule])
       
