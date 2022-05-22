from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION= "Execute PowerShell script on remote host"
LONG_DESCRIPTION = "Execute Powershell script on your local machine and on remote domain hosts.\n" \
                   "from psremoter.connector import Execute\n" \
                   "exec = Execute(hostname='hostname', username='username' , password='password', domain='myDomain', command='get-process', powershell=True)\n" \
                   "r.remote_execution()\n" \
                   "print(r.status)\n" \
                   "print(r.return_code)\n" \
                   "print(r.output)\n"

#Setting up
setup(
    name='PSRemoter',
    version= VERSION,
    author= 'Daniel Mandelblat',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_dirs=[],
    keywords=['powershell', 'remote powershell', 'execute powershell', 'powershell domain', 'domain', 'windows remote', 'windows server'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
