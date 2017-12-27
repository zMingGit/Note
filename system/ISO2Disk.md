- change iso to dmg
```
hdiutil convert -format UDRW -o ~/linux.dmg /tmp/linux.iso
```
- umount disk

```
diskutil list #to find the device name
diskutil umountDisk /dev/disk1
```

- push dmg to disk
```
sudo dd if=linux.dmg of=/dev/rdisk1 bs=1m
```
- eject disk

```
diskutil eject /dev/disk1
```

