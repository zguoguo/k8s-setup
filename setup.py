import os

print("Installing Docker ... ")
os.system("apt-get update")
os.system("apt-get install docker docker.io")
print("Finished installing Docker ")
os.system("systemctl enable docker")
print("Installing K8s")
os.system("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add")
os.system('apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"')
os.system("apt install kubeadm")
os.system("swapoff -a")
