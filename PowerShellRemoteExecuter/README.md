# PSRemoteExecuter
## _Devoloped by Daniel Mandelblat_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This package will help you to execute remote PowerSell script on other Windows platforms in your domain. 

## Features

- Execute local PowerShell scripts
- Execute remote PowerShell scripts (Using invoke-command PS command)


## Using
r= Execute(hostname="hostname", username="username" , password='password', domain='myDomain', command="get-process", powershell=True)<br>
r.remote_execution()<br>
print(r.status)<br>
print(r.return_code)<br>
print(r.output)

