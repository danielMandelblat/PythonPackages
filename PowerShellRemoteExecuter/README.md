# PSRemoteExecuter
## _Devoloped by Daniel Mandelblat_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This package will help you to execute remote PowerSell script on other Windows platforms in your domain. 

## Features

- Execute local PowerShell scripts
- Execute remote PowerShell scripts (Using invoke-command PS command)


## Using
###install PSRemoter using pip
pip install PSRemoter

```
from psremoter.connector import Execute
exec= Execute(hostname="hostname", username="username" , password='password', domain='myDomain', command="hostame", powershell=True)

#Execute command on remote host
exec.remote_execution()

#Read execution status
print(r.status)

#Read return code
print(r.return_code)

#Read console output
print(r.output)
````

###Output:<br>
True<br>
0<br>
dnsserver
