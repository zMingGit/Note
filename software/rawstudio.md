install rawstudio from source.


download: git clone https://github.com/rawstudio/rawstudio.git 



this way will need lot of packpage.



This can solve most of the dependencies

```
yum install libxml2-devel libcurl-devel lcms-devel libxml-devel dbus-devel flickcurl-devel lensfun-devel sqlite-devel GConf2-devel openssl-devel libgphoto2-devel exiv2-devel
yum install gtk3-devel
yum install fftw-devel fftw-doc
```

and then you can use `sudo ./autogen.sh` command. It will tell you what to install.

ps: may u will get error like sqlite db clock. u can delete all yum process, it work.
