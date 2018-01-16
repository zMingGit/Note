1. 下载好iso文件
2. 转换iso为dmg文件
```
hdiutil convert -format UDRW -o ~/fedora.dmg ./Fedora-Workstation-Live-x86_64-27-1.6.iso
```
3. 插入u盘
4. 取消u盘的挂载
```
diskutil umountDisk /dev/disk1
```
5. 利用dd命令将文件写入u盘
```
sudo dd if=fedora.dmg of=/dev/rdisk1 bs=1m
```
6. 弹出u盘，然后就可以开始引导安装了.
```
diskutil eject /dev/disk1
```