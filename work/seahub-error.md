locale.getdefaultlocale() raise ValueError, unknown locale: UTF-8


解决办法:
```
export LANG=en_US.UTF-8
unset LC_CTYPE
```