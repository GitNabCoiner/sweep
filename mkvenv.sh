#!/bin/bash
echo $SHELL
echo $BASH_VERSION
venvname="pyinterpret"
pipd="./$venvname/bin"
progs=(urllib3 qrcode Pillow)

#create venv
python3 -m venv --without-pip $venvname

#get pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$pipd/python3 get-pip.py

#install modules
for p in "${progs[@]}"
do
	echo "$p"
	$pipd/pip install $p
done

#source pyinterpret/bin/activate

#create output dir
mkdir -p out/bch
mkdir out/sv

#clean
rm get-pip.py
