环境变量:

`CLASSPATH`: jdk-path;project-path;pfc-path;%CLASSPATH%

```
e.g. C:\j2sdk1.4.1;C:\Users\Hu\workspace\ProE\src；C:\Program Files\PTC\Creo Elements\Pro5.0\jlink\jlink_appls\install_test;C:\Program Files\PTC\Creo Elements\Pro5.0\text\java\pfc.jar;%CLASSPATH%;
```

`PATH`:  %PATH%;pfc-pah;project-jre-path;jdk-path;

```
%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;%USERPROFILE%\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\Program Files\PTC\Creo Elements\Pro5.0\bin;C:\Program Files\PTC\Creo Elements\Pro5.0\mech\bin;C:\Program Files\PTC\Creo Elements\Pro5.0\text\java\pfc.jar;C:\Program Files\PTC\Creo Elements\Pro5.0\x86e_win64\obj\JRE\bin;C:\j2sdk1.4.1\bin;
```

`JAVA_HTOME`: jdk-path;

```
C:\j2sdk1.4.1
```

`PRO_COMM_MSG_EXE`
```
xxxxx/win64/obj/pro_comm_msg.exe
```


config.pro下添加java.exe的路径[运行时环境]


`开启远程debug，让eclipse可以进行调试`

```
jlink_java_command C:\Program Files\PTC\Creo Elements\Pro5.0\x86e_win64\obj\JRE\bin\java.exe -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=8000,server=y,suspend=y
```


!!!! almost cost two day!!!!!
carefuly creo default directory, XToolKitgeneratorerror almost is can't find file!!!!

solution



```
search_path C:\Users\Hu\Desktop
```
