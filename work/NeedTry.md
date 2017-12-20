```
Hardware Notes - J-Link
The following tables list the platform Java compiler and runtime requirements for J-Link. J-Link is available on the standard Pro/ENGINEER CD and is installed automatically with Pro/ENGINEER. J-Link is supported on certain minimum versions of Java 1.1 for each platform, plus Java 1.2.
Using Java 1.2 with synchronous J-Link:
The default Pro/ENGINEER configuration attempts to use the Java Runtime Enviroment command "jre" to run J-Link applications. This command is not included in Java 1.2 installations. Users should set the system environment variable PRO_JAVA_COMMAND to use the "java" command, plus the J-Link starter class, instead. For example:
setenv PRO_JAVA_COMMAND "java com.ptc.pfc.Implementation.Starter"
on UNIX systems, or
set PRO_JAVA_COMMAND=java com.ptc.pfc.Implementation.Starter
on Windows systems (this variable can also be set through the Settings dialog on the Windows Control Panel).
Optionally, the environment variable setting may include the full path to the java executable.
```