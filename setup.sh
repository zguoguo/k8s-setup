#!/bin/sh

apt-get update
apt-get install docker docker.io
systemctl enable docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
apt install kubeadm
swapoff -a
kubeadm init --ignore-preflight-errors='all' --pod-network-cidr=10.244.0.0/16
kubeadm token create --print-join-command > joincommand.sh
chmod 755 joincommand.sh
cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        scp joincommand.sh root@$line:/root
        ssh root@$line
        cd
        apt-get update
        apt-get install docker docker.io
        systemctl enable docker
        curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
        apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
        apt install kubeadm
        ./joincommand.sh
        echo "Finished config node $line"
        echo "########################################################"
    fi
done
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
kubectl get nodes