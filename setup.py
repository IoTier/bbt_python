from distutils.core import setup

setup(
    name='beebotte',
    version='0.1.1',
    description='Python library for interfacing with Beebotte',
    url='http://beebotte.com',
    author='Beebotte',
    author_email='contact@beebotte.com',
    maintainer="Bachar Wehbi",
    maintainer_email='bwehbi@beebotte.com',
    packages=['beebotte'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='beebotte, api, rest, pubsub, restful, iot, internet of things, device, realtime, connected, websockets',
    license='MIT',
)