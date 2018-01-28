## prepare

### singal node cep intall 

```
echo deb http://download.ceph.com/debian-jewel/ trusty main | sudo tee /etc/apt/sources.list.d/ceph.list

sudo apt-get update && sudo apt-get install ceph-deploy

sudo useradd -m -s /bin/bash ceph-deploy
sudo passwd ceph-deploy

echo "ceph-deploy ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/ceph-deploy

sudo chmod 0440 /etc/sudoers.d/ceph-deploy

sudo su - ceph-deploy

ssh-keygen

ssh-copy-id ceph-deploy@ceph-single-node

cd ~
mkdir my-cluster
cd my-cluster

ceph-deploy new ceph-single-node

vim ceph.config

	#Add the following two lines:
	osd pool default size = 2
	osd crush chooseleaf type = 0

ceph-deploy install ceph-single-node

ceph-deploy mon create-initial

ceph-deploy osd prepare ceph-single-node:sdb
ceph-deploy osd prepare ceph-single-node:sdc
ceph-deploy osd prepare ceph-single-node:sdd

ceph-deploy osd activate ceph-single-node:/dev/sdb1
ceph-deploy osd activate ceph-single-node:/dev/sdc1
ceph-deploy osd activate ceph-single-node:/dev/sdd1

ceph-deploy admin ceph-single-node

sudo chmod +r /etc/ceph/ceph.client.admin.keyring

ceph -s
```

ref: http://palmerville.github.io/2016/04/30/single-node-ceph-install.html


### package 
pip install -r test-requirements.txt
sudo apt-get install python-ceph
pip install boto
sudo apt-get install python-rados


## Test

### Prepare

```
pip install -r test-requirements.txt
sudo apt-get install python-ceph python-rados
pip install boto
```

### Run

run command `python run_test.py --sotrage {{fs|ceph}}`

### note

`test/functional/crypto_test.py` will not be run. you can only run command `pytest -sv test/functional/crypto_test.py` to test.
	
	