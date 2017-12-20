

下载后的文件为 Creo.Elements.Pro.5.0.M180.Win32.DVD.iso，可以用 winrar 解压 ISO 文件或者使用虚拟光驱软件载入 ISO 然后安装，步骤如下：
1) 运行 Creo Elements/Pro 5.0 安装程序 setup.exe；
2) 用记事本或写字板打开 WF5_Win32_crk 下 license.dat，用你自己的主机 id （运行setup.exe时左下角提示的主机ID）全部替换文件中的 00-00-00-00-00-00，保存文件；
3) 安装 Creo Elements/Pro & Creo Elements/Pro Mechanic，在指定许可证服务器时选择“锁定的许可证文件”并添加前面保存的 license.dat，继续完成安装。
安装完后不要运行 Creo 首先打补丁：

对 Creo Elements/Pro:
复制 "proe_WF5_Win64_crk.exe" 到 Creo Elements/Pro5.0/x86e_win64/obj 下运行，然后点击 "Next > OK > Next > OK > Next > OK > Next > OK > Finish > OK"; ［切记用admin运行，如果还是找不到，就复制到../x86e_win64/obj32下同样步骤执行一遍］

复制 "proe_mech_WF5_Win64_#1_crk.exe" 到 Creo Elements/Pro5.0/mech/x86e_win64/bin 下运行，然后点击 "Next > OK > Next > OK > Next > OK > Next > OK > Finish > OK"； [这里同样会错误，也复制到bin64下执行一遍]
复制 "proe_mech_WF5_Win32_#2_crk.exe" 到 Creo Elements/Pro5.0/mech/x86e_win64/ptc 下运行，然后点击 "Start > OK"。[这里不会出错]


然后就可以开始二次开发的道路了。