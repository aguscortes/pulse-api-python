from distutils.core import setup

setup(
    name='tspapi',
    version='0.3.3',
    url="https://github.com/boundary/pulse-api-python",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tspapi', ],
#    entry_points={
#        'console_scripts': [
#            'actionhandler = boundary.webhook_handler:main',
#        ],
#    },
#    scripts=[
#        'tsp-cli-env.sh',
#   ],
#    package_data={'boundary': ['templates/*']},
    license='Apache 2',
    description='Python Bindings for the TrueSight Pulse REST APIs',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
	"six >= 1.10.0",
	"python-dateutil >= 2.5.2",
    ],
)
