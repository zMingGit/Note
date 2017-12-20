## Requirement


[docment](https://github.com/coolwanglu/pdf2htmlEX/wiki/Building)
* libspiro
* poppler >= 0.25.0
    * libpng
    * libjpeg
    * poppler-data
* fontforge



## Install


`First install all these prerequisites for compiling`:


```
```

```
sudo apt install g++ autoconf libfontconfig1-dev pkg-config libjpeg-dev libopenjpeg-dev gnome-common libglib2.0-dev gtk-doc-tools yelp-tools gobject-introspection libsecret-1-dev libyelp-dev libnautilus-extension-dev
```

### poppler-data
```
wget http://poppler.freedesktop.org/poppler-data-0.4.7.tar.gz
tar -xf poppler-data-0.4.7.tar.gz
cd poppler-data-0.4.7
sudo make install
cd ..
```


### libpng
```
git clone https://github.com/glennrp/libpng.git
cd libpng
./autogen.sh
./configure
make
sudo make install
```

### libjpeg
```
git clone https://github.com/LuaDist/libjpeg.git
cd libjpeg
./configure
make
sudo make install
```

### poppler

```
wget http://poppler.freedesktop.org/poppler-0.44.0.tar.xz
tar -xf poppler-0.44.0.tar.xz
cd poppler-0.44.0
./configure --enable-xpdf-headers
make
sudo make install
```

### fontforge

depend
```
sudo apt-get install libxml2-dev
```

```
git clone https://github.com/coolwanglu/fontforge.git
cd fontforge
git fetch origin pdf2htmlEX:pdf2htmlEX
git checkout pdf2htmlEX
./autogen.sh
./configure
make
sudo make install 
```

### pdf2htmlex

```
git clone https://github.com/coolwanglu/pdf2htmlEX.git
cd pdf2htmlEX
cmake .
make 
sudo make install
```