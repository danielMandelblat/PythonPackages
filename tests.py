from psremoter import connector

exec= connector.Execute(hostname="danielm", username="danielm" , password='054842Dd', domain='inr', command="hostame", powershell=True)

#Execute command on remote host
exec.remote_execution()

#Read execution status
print(r.status) #True

#Read return code
print(r.return_code) #0

#Read console output
print(r.output) #DnsServer01