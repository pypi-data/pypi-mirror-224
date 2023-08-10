<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/EmadHelmi/herodotus">
    <img src="static/imgs/logo.png" alt="Logo">
  </a>

<h3 align="center">Herodotus</h3>

  <p align="center">
    An awesome enhanced python logger
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EmadHelmi/herodotus/tree/main/examples">Examples</a>
    ·
    <a href="https://github.com/EmadHelmi/herodotus/issues">Report Bug</a>
    ·
    <a href="https://github.com/EmadHelmi/herodotus/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-history-behind-the-project">The history behind the project</a></li>
        <li><a href="#the-naming-convention">The naming convention</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#basic-usage">Basic usage (no formatter)</a></li>
        <li><a href="#use-with-a-formatter">Use with a Formatter</a></li>
        <li><a href="#using-the-colorizer">Using the colorizer</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

### The history behind the project

Python [logging][python-logging-url] package is a powerful tool for logging your messages into any stream.
From a file to third party service, like [Elasticsearch][elastic-url].

But one day in a project I needed to log some messages through many streams with different severities.
For example I want a logger object in which three handlers one for a rotating file handler, one for stdout and one for
elasticsearch.
But I wanted to send each severity to a specific stream. And also I wanted to colorize the stdout log but not the one in
the file.

When I used something like this:

```python
import logging
import some_colorizer_function

my_logger = logging.getLogger("my_logger")
my_logger.debug(
    some_colorizer_function("some message with %s"),
    "args"
)
```

It sends a nice colorized output to the stdout. But an ugly text (with ansi color symbols) sent to the Elasticsearch or
written in the file. So I decided to make some enhancements on the logging package and also decided to publish it. So
please fill free to contribute.

### The naming convention

[Herodotus][Herodotus-wiki] was an ancient Greek historian known as the "Father of History."
He wrote the book "The Histories," one of the earliest historical works.
This book covers various subjects such as history, geography, cultures, civilizations, and wars.
He combined accurate descriptions of events with engaging storytelling.
His work is a blend of historical analysis and cultural narratives, making him a significant figure in the development
of historical writing.

<!-- GETTING STARTED -->

## Getting Started

I've also created a pypi package for this library. So you can easily use and install it with pip or clone the project.

### Installation

    pip install herodotus_logger --upgrade

<!-- USAGE EXAMPLES -->

## Usage

### Basic usage

1. First, you should define a logger object with a specific severity level.
   by this level setup, the logger will send all severities greater than or equal
   to.You can read more about severity numbers [here][severity-url].
   For example, if you define a logger object with `WARNING` level, it does not send any `INFO`, `DEBUG` or `NOTSET`
   levels to its handlers.

   ```python
   import logging
   from herodotus import logger
    
   lg = logger.Logger(
        name="test_logger",
        level=logging.WARNING
   )
   ```
2. You also should give it some handlers. You have two main options to do so:
    1. Use some basic provided handlers in the `herodotus.handlers` which are starting with `Enhanced*`
        - Note that all provided handlers' arguments are as the main one.
          They just accept some
          more arguments I'll explain.
    2. Use any custom or other handlers which are of type `Handler` in python.

    ```python
    import logging
    from sys import stdout
    
    from herodotus import logger
    from herodotus import handlers
    
    lg = logger.Logger(
        name="test_logger",
        level=logging.WARNING,
        handlers=[
            handlers.EnhancedStreamHandler(
                stream=stdout,
                level=logging.WARNING
            ),
            handlers.EnhancedFileHandler(
                filename="logs/test_logfile.log",
                mode="a",
                encoding="utf-8",
                level=logging.CRITICAL
            )
        ]
    )
    ```

3. It's finished!! Seat back and just tell your logger object to log!
    1. Create the `logs` directory:

       ```bash
       mkdir logs
       ```
    2. Call the `logger` logs functions (ex debug, info,...)
       ```python
       lg.logger.info("Hello")
       ```
   But at this point, nothing happened.
   Because the `lg` log level is
   `logging.WARNING` and we tell to log with `info` level.
   And we
   know that `log.INFO` < `log.WARNING`.

   Let's try another one:
   ```python
   lg.logger.warning("Hello")
   ```
   and the bash output is:
   ```bash
   2023-08-09T10:39:05|test_logger|WARNING|Hello
   ```
   But nothing logged in the log file. And the reason is clear.

   Let's run another example:
   ```python
   lg.logger.critical("Hello")
   ```
   and the bash output is:
   ```bash
   2023-08-09T10:45:45|test_logger|CRITICAL|Hello
   ```
   And finally in the log file located at `logs/test_logfile.log` we have the same output.

### Use with a Formatter

I define a default formatter for the logger as follow:

```python
self.formatter = formatter or logging.Formatter(
    datefmt="%Y-%m-%dT%H:%M:%S",
    fmt="%(asctime)s|%(name)s|%(levelname)s|%(message)s"
)
```

But you can change it when you create the logger:

```python
import logging
from sys import stdout

from herodotus import logger
from herodotus import handlers

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=stdout,
            level=logging.WARNING
        ),
        handlers.EnhancedFileHandler(
            filename="logs/test_logfile.log",
            mode="a",
            encoding="utf-8",
            level=logging.CRITICAL
        )
    ]
)
```

The most important note is that you can also set different formatter for each handler.
But if you don't set a formatter for your handler, the logger will use its formatter for.

```python
import logging
from sys import stdout

from herodotus import logger
from herodotus import handlers

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=stdout,
            level=logging.WARNING
        ),
        handlers.EnhancedFileHandler(
            filename="logs/test_logfile.log",
            mode="a",
            encoding="utf-8",
            level=logging.CRITICAL,
            formatter=logging.Formatter(
                datefmt="%H:%M:%S",
                fmt="%(asctime)s: %(message)s"
            )
        )
    ]
)
```

### Using the colorizer

Using colors everywhere undoubtedly gives another view, in the logging so.
You can use `colored` [package][colored-pip-url].
But I also put some easy to use functions to add colors to your logs.
Let's see some examples:

```python
import logging
from sys import stdout

from herodotus import logger
from herodotus import handlers
from herodotus.utils import colorizer

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=stdout,
            level=logging.WARNING
        )
    ]
)

lg.logger.critical(colorizer.colorize("Hello", foreground="green"))
```

and the output will be something like this:

![colorizer ex1](static/imgs/colorizer-ex1.png)

You can also add styles (as noted in the `colored` [package][colored-style-documentation]).
To do so, just pass your desired styles as a list to the `colorize` function:

```python
lg.logger.critical(colorizer.colorize("Hello", foreground="green", styles=['bold', 'underline']))
```

And the output will be something like this:

![colorizer ex2](static/imgs/colorizer-ex2.png)

But what happens if we add a file handler to a logger which uses the `colorize` function? Let's see:

```python
import logging
from sys import stdout

from herodotus import logger
from herodotus import handlers
from herodotus.utils import colorizer

lg = logger.Logger(
    name="test_logger",
    level=logging.WARNING,
    formatter=logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
        fmt="%(asctime)s %(levelname)s: %(message)s"
    ),
    handlers=[
        handlers.EnhancedStreamHandler(
            stream=stdout,
            level=logging.WARNING
        ),
        handlers.EnhancedFileHandler(
            filename="logs/test_logfile.log",
            mode="a",
            encoding="utf-8",
            level=logging.CRITICAL,
            formatter=logging.Formatter(
                datefmt="%H:%M:%S",
                fmt="%(asctime)s: %(message)s"
            )
        )
    ]
)

lg.logger.critical(colorizer.colorize("Hello", foreground="green"))
```

In the log file, you will probably see something like this (If you don't have any plugin or extention to convert ansii
chars to the colors):

![colorize ex3](static/imgs/colorizer-ex3.png)

So ugly! So what to do? Don't be worry. I also have a soloution for this.

You can use the `msg_func` argument for each of `Enhanced*` handlers.
It has the type of `function` So, you should pass it a function.
I, for example, have written a `decolorize` function in the `herodotus.utils.colorize` package which get a `str`
with ansii color chars and remove them:

```python
handlers.EnhancedFileHandler(
    filename="logs/test_logfile.log",
    mode="a",
    encoding="utf-8",
    level=logging.CRITICAL,
    msg_func=colorizer.decolorize,
    formatter=logging.Formatter(
        datefmt="%H:%M:%S",
        fmt="%(asctime)s: %(message)s"
    )

lg.logger.critical(colorizer.colorize("Hello", foreground="green"))
```

Finally, in the log file you will see something like this:

![colorize ex4](static/imgs/colorizer-ex4.png)

<!-- ROADMAP -->


See the [open issues](https://github.com/EmadHelmi/herodotus/issues) for a full list of proposed features(
and known issues).



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement."
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->

## Contact

Emad Helmi | Find me on Twitter [@EmadHelmi](https://twitter.com/emadhelmi)

Or send me Email [s.emad.helmi@gmail.com](mailto://s.emad.helmi@gmail.com)

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/EmadHelmi/herodotus?style=for-the-badge

[contributors-url]: https://github.com/EmadHelmi/herodotus/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/EmadHelmi/herodotus?style=for-the-badge

[forks-url]: https://github.com/EmadHelmi/herodotus/network/members

[stars-shield]: https://img.shields.io/github/stars/EmadHelmi/herodotus?style=for-the-badge

[stars-url]: https://github.com/EmadHelmi/herodotus/stargazers

[issues-shield]: https://img.shields.io/github/issues/EmadHelmi/herodotus?style=for-the-badge

[issues-url]: https://github.com/EmadHelmi/herodotus/issues

[license-shield]: https://img.shields.io/github/license/EmadHelmi/herodotus?style=for-the-badge

[license-url]: https://github.com/EmadHelmi/herodotus/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/emad-helmi-1aa321135/

[twitter-shield]: https://img.shields.io/twitter/follow/EmadHelmi?style=for-the-badge

[twitter-url]: https://twitter.com/EmadHelmi

[python-logging-url]: https://docs.python.org/3/library/logging.html

[elastic-url]: https://www.elastic.co/

[Herodotus-wiki]: https://en.wikipedia.org/wiki/Herodotus

[Python.badge]: https://img.shields.io/badge/Python-20233A?style=for-the-badge&logo=python&logoColor=61DAFB

[Python-url]: https://python.org

[severity-url]: https://docs.python.org/3/library/logging.html#logging-levels

[colored-pip-url]: https://pypi.org/project/colored/

[colored-style-documentation]: https://dslackw.gitlab.io/colored/api/functions/#formatting
