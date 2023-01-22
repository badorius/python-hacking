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

 
