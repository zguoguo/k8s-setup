# k8s-setup
k8s setup test

Hello Team, with this repository we will be able to build a 3 node kubernetes cluster
that incorporates the Kubernetes Networking Model using Flannel.

Assumptions are:

* 3 xl170 bare metal machines using the emulab-ops/UBUNTU18-64-OSCN-R image from CloudLab.

* The installation is being run as root.

* The master node can ssh into the worker nodes.

* The workers file has been modified with the IPv4 Addresses of your current worker nodes.

* Permissions on the install.sh file are modified to allow it to be executed.
    
Other than that, just running the install.sh file on your master node should get everything working

As note, the profile used to build this installation is called clusterTest6 and is available at CloudLab
