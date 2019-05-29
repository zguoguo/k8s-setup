#!/bin/sh

apt-get update
apt-get -y install docker docker.io
systemctl enable docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
apt-get -y install kubeadm
swapoff -a
kubeadm init --ignore-preflight-errors='all' --pod-network-cidr=10.244.0.0/16
kubeadm token create --print-join-command > joincommand.sh
chmod 755 joincommand.sh
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        scp joincommand.sh root@$line:/root
        scp setup.py root@$line:/root
        ssh -o StrictHostKeyChecking=no root@$line -n "cd /root && python3 setup.py && ./joincommand.sh"
        echo "Finished config node $line"
        echo "########################################################"
    fi
done

echo "Finished Installation"
kubectl get nodes
