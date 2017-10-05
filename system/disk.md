## 使用fdisk 将硬盘挂载到一个挂载点

```
sudo fdisk /dev/sda
```

1. make sure have free space

input `F` commond check free space

2. create new primary partition

input `n` to create partition

input `p` to choose primary partition

input `Enter` to choose default number (case for 3)

input the sector start point for the free space.

input `Enter` to use all free space.

3. trans `Linux` file system to `Linux LVM`

input `t` to change file system type

choose the number of the partition.

input `8e` trans to `Linux LVM`

4. create pv

```
sudo pvcreate  /dev/sda3
```

5. create vg

`ubuntu-vg-extra-zm` is the vg name
```
sudo vgcreate  ubuntu-vg-extra-zm /dev/sda3
```

6. create lv

`data` is lv name
`ubuntu-vg-extra-zm` is the vg name

```
sudo lvcreate -l 20 -n data ubuntu-vg-extra-zm
```

7. create file system
```
sudo /sbin/mkfs.ext3 /dev/ubuntu-vg-extra-zm/data
```

8. extra size to 20G

`20480` is the size you want to changed
```
sudo lvextend -L20480 /dev/ubuntu-vg-extra-zm/data
```

9. mount 

`/dev/ubuntu-vg-extra-zm/data` is lv path
`/data` is mount point

```
sudo mount /dev/ubuntu-vg-extra-zm/data /data
```

## 扩展LVM容量

LVM的设计本身就是可扩展的
步骤:
1. 创建主分区并改为`Linux LVM`格式  
    步骤与上面一样
2. 创建pv  
    步骤与上面一样
3. 扩展VG  
    `/dev/sdd1` 为上面创建的pv  
    `lvmdisk` 为vg名称
    ```
    vgextend lvmdisk /dev/sdd1 
    ```
4. 扩展LV
    `-L+20G` 为逻辑卷添加20G的空间
    `/dev/ubuntu-vg/root` lv path
    ```
    sudo lvextend -L+20G /dev/ubuntu-vg/root
    ```


文本设计的概念有:  
物理分区(physical Partions)  
物理卷(physical volume)  
卷组(volume group)  
逻辑卷(logic volume)  
逻辑卷上创建ext3文件系统  
扩展卷组、逻辑卷和挂载  



