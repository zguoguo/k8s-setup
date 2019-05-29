#Script to install the kubernetes environment on a cloudlab cluster

#In this version, I'm using a 3 node cluster, with hardware being xl170, and the image
#is emulab-ops/UBUNTU18-64-OSCN-R

import os

#Installing Docker
print("Installing Docker ... ")
os.system("apt-get update")
os.system("apt-get install docker docker.io")
print("Finished installing Docker ")
os.system("systemctl enable docker")
os.system("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add")
os.system('apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"')
os.system("apt install kubeadm")
os.system("swapoff -a")