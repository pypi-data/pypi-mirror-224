# FancyLogger
![Downloads](https://pepy.tech/badge/pyfancylogger)
![Downloads](https://pepy.tech/badge/pyfancylogger/week)
![Downloads](https://pepy.tech/badge/pyfancylogger/month)  
With this library, Log in style!

### This library is still under development, so we appreciate if you help us improve it on the GitHub!

### Having an issue?
You can always find someone on our discord server here:
> https://discord.agmstudio.xyz/

### Wiki
The official wiki of this library is now available at GitHub
> https://git.agmstudio.xyz/FancyLogger/wiki

## How to install
To install just use following command
```shell
pip install PyFancyLogger
```
This library will have dev/beta builds on the GitHub, to install them you can use

```shell
pip install --upgrade git+https://github.com/AGM-Studio/FancyLogger.git
```

# Example

```python
from FancyLogger import FancyLogger, FancyFormatter, Formats

logger = FancyLogger('Test', FancyFormatter(Formats.detailed))

logger.setLevel(0)

logger.debug('This is a debug')
logger.info('This is an info')
logger.warning('This is a warning')

try:
    int('Not an int')
except Exception as e:
    logger.error(f'This is an error for {e}')
    
try:
    int('Not an int either')
except Exception as e:
    logger.exception(f'This is an error for {e}')

logger.critical('IMPORTANT: THIS IS A CRITICAL MESSAGE')
```
![Result](https://raw.githubusercontent.com/AGM-Studio/FancyLogger/master/Example.jpg)

[![Advertisement Banner](https://2captcha.com/referral-banners/2captcha/08.gif)](https://2captcha.com/?from=19092307)

## Extras & Features
...