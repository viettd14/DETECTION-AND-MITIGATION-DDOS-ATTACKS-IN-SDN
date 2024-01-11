<div align="center">
  <h1><strong>A STUDY ON DETECTING AND MITIGATING DENIAL OF SERVICE ATTACKS IN SOFTWARE DEFINED NETWORKS</strong></h1>
</div>

# Table of Contents
1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Related Work](#related-work)
4. [Design SDN Network Infrastructure](#design-sdn-network-infrastructure)
5. [A Proposed Design for SDN Infrastructure](#a-proposed-design-for-sdn-infrastructure)
6. [System Performance Evaluation](#system-performance-evaluation)
7. [Conclusion and Future Work](#conclusion-and-future-work)
8. [References](#references)

## Abstract
<a name="abstract"></a>

The escalating risks to network security, stemming from the continual evolution of network infrastructure and application systems, have significantly impacted system availability, with Denial of Service (DDoS) attacks standing out as a particularly disruptive threat capable of overwhelming and even incapacitating systems. In response, this study introduces a comprehensive system designed to detect and mitigate DDoS attacks within Software-Defined Networks (SDNs). Our proposed solution involves a multi-modules architecture operating as an Intrusion Prevent System (IPS), strategically engineered for seamless integration into the Controller device. The system's functionality includes the periodic extraction of multiple parameters from flow entries on the OpenFlow switch, complemented by machine learning (ML) models, enabling the identification of abnormal packets infiltrating the system. Upon detecting an attack, the controller promptly dispatches policies to the OpenFlow switch, initiating the removal of malicious packets. This autonomous system employs common machine learning algorithms and real-time processes to detect and counteract attacks on OpenFlow Switches. The study evaluates the system’s performance using four distinct algorithms such as Decision Tree(DT), Random Forest (RF), K-Nearest Neighbors (KNN), and Support Vector Machine (SVM). The CIC-DDOS2019 input dataset [1] is used to evaluate machine learning algorithms in detecting DDoS attacks, experimental results show that the Decision Tree (DT) algorithm exhibits high F1 scores. highest with 99.87%

## Introduction
<a name="introduction"></a>

Software-Defined Networking (SDN) is a networking technology that improves performance and optimizes network management compared to traditional networks due to its highly flexible nature and rapid deployment capabilities. SDN allows centralized network management, empowering administrators to program network devices within the system. However, SDN has many potential information security risks, such as:
- Man-in-the-Middle Attacks: Attackers position themselves between the Controller and the Switch, aiming to sniffer and steal information.
- Software System Vulnerabilities: Various risks associated with the system's software, such as software vulnerabilities and the exposure of administrative credentials.
- Controller Device Security: Ensuring the security of the Controller device is crucial, as any compromise could severely impact the entire system, leading to service disruptions.
- Particularly, Distributed Denial of Service (DDoS) attacks that aim to overload the entire system. In addition to targeting a specific network service or server, attackers may focus on the Controller device or directly launch DDoS attacks against the system management software to cause a system-wide overload.

DDoS is a highly dangerous type of attack on the Internet, as it causes system overload, resulting in slow or unresponsive system operations. In some cases, it can even block access to servers, denying legitimate users the ability to use system services. With the diversity of devices and the rapid development of network attack models over the past decades, the complexity of attacks has increased. Attackers continuously change their attack patterns to avoid detection, introducing anomalies in network traffic, or employing Low-Rate DDoS attacks (LR-DDOS). This complexity makes it challenging to detect and block each attack source. However, effective defense against these attacks requires quick detection and prevention to avoid system resources being overwhelmed.  
Despite numerous research efforts and implemented measures to prevent these attacks. However, DDoS attacks are becoming increasingly diverse, posing significant difficulties and challenges. The complexity of algorithms has introduced certain delays in DDoS attack detection methods. Therefore, monitoring changes in access traffic patterns and timely, accurate identification of DDoS attacks are essential and urgent.  
One optimized solution is the utilization of SDN network for the current network infrastructure. While SDN architecture has the potential to enhance security by centrally monitoring and controlling the network through the Controller device, facilitating easy configuration of network devices, it also presents a significant challenge. The very nature of SDN architecture makes it susceptible to becoming a target for DDoS attacks.  
In my study, I propose an automated solution for detect and mitigation DDoS attacks in SDN network (Figure 1). This solution introduces a new, compact module that integrates directly into the SDN network's Controller device. This module operates as an Intrusion Detection System (IDS), monitoring all inbound and outbound traffic to the system to observe and predict potential attack risks.

<p align="center">
  <img width="800" src="https://i.imgur.com/iY8LWZU.png" alt="Proposed system operating mode">
</p>
<p align="center">
  <em>Figure 1: Proposed system operating mode</em>
</p>

Within the system, the OpenFlow protocol is employed, where OpenFlow Switch devices analyze packet headers based on source IP, destination IP, port, switch, protocol, time, packet count, and send this information to the Controller for statistical analysis. Subsequently, the system is tested using machine learning models such as Decision Tree (DT), K-Nearest Neighbors (KNN), Random Forest (RF), and Support Vector Machine (SVM) to predict whether the incoming traffic to the system is normal or anomalous. The paper utilizes the CIC-DDOS2019 input dataset to evaluate machine learning algorithms in DDoS attack detection.  
After proposing an attack prevention solutions, I suggests an appropriate Software-Defined Networking architecture for detecting and mitigating Distributed Denial of Service attacks.


## Related Work
<a name="related-work"></a>

Currently, there have been numerous studies on detecting and mitigation DDoS attacks. Detection methods are commonly divided into four main categories: machine learning methods, methods that function as an Intrusion Detection System (IDS)/Intrusion Prevention System (IPS), methods using Entropy thresholds, and statistical methods:
- Machine Learning Methods: Typically, employ algorithms such as SVM, Decision Tree, Random Forest, KNN, etc., to identify anomalous network traffic. This type of model is simple and effective, with numerous studies and widespread application across various network infrastructures. These studies propose lightweight framework models that are easy to integrate into systems. Doriguzzi-Corin et al. (2020) [2] The approach is used in resource-constrained environments like IoT networks or small-scale network systems. Xiao et al. (2015) [3] the model is directly integrated into the Controller. Experimental results showed a 96% accuracy.
- Operating as an IDS/IPS: These studies may represent one of the future trends in the field of network security. JESÚS ARTURO PÉREZ-DÍAZ1 (2020) [4] and Noe et al. (2022) [5], a flexible architecture in the form of modules operating as both IDS and IPS based on deep learning. However, these studies are still in the experimental phase within research environments using virtualized models like Onos, Ryu and Mininet. Experimental results showed a 98% accuracy.
- Entropy Threshold Method: Feinstein and Schnackenberg (2003) [6] The algorithm utilizes an appropriate entropy threshold to measure network traffic. => Administrators are required to determine the suitable entropy randomness calculation parameters for their systems: Results showed a 99% accuracy.
- Statistical Method: Tuyen et al. (2019) [7] Utilizes the OpenFlow protocol to support statistical methods. This solution leverages the existing resources of the SDN network without the need to install additional devices for network traffic information collection. Experimental results showed a 96% accuracy.

The studies [2,3,4,5] have proposed methods to prevention DDoS attacks. Although the authors have introduced flexible and easily integrable models compatible with diverse infrastructures, [2] is specifically applied to IoT systems, and [3] is suitable for LR-DDoS prevention. In the research [4,5], the authors presented a system operating as an IDS/IPS to detect attacks promptly. In [6], the authors extracted packet header fields such as IP, port, switch, etc.. to traffic statistics and attack detection. In [7], the OpenFlow protocol was employed to support statistical methods and communication between network components.  
With the contributions from the related works, we propose a solution for detecting and mitigating attacks based on module components, following:
- Build a module integrated directly into the Controller.
- Function as an IDS system to monitor the entire system’s traffic.
- Use the OpenFlow protocol to assist in extracting packet header for statistical methods.
- Combine statistical methods with machine learning to predict attack traffic.


## Design SDN Network Infrastructure
<a name="design-sdn-network-infrastructure"></a>

### Proposed Solution for DDoS Attack Prevention
In this study, we propose a DDoS attack detection system in SDN network called uitSDNDDoSD. Our system comprises three main modules, as follows:
- Feature extraction from packets: When packets enter the system, we use the OpenFlow protocol to assist in extracting packet features such as IP, port, etc. Subsequently, these features are organized into flow tables and flow entries. Then, this information is sent to the detection module at the Controller after a specified time interval.
- Attack detection module: We utilize machine learning algorithms to compare statistical information with the input dataset.
- Mitigation module: After the comparison, if a dan gerous data network is identified, this module will implement mitigation policies to ensure system safety during an attack.

### Packet Processing In the OpenFlow Protocol
With the characteristics of an SDN based on the separation of the control plane from the data plane. In the control plane, with the Controller as the brain of the entire system, can monitor, provide, and enforce policies to OF switches through the OpenFlow protocol [7] in a flexible manner. Packets are processed by the system on a per-flow basis and controlled in flow tables within OF switch through flow entries.  
<p align="center">
  <img width="600" src="https://i.imgur.com/fhldzcv.png" alt="Extracting packet features to matching flow tables">
</p>
<p align="center">
  <em>Figure 2: Extracting packet features to matching flow tables</em>
</p>

An OpenFlow protocol consists of three main components:
- Flow: The OpenFlow protocol automatically groups new packets with the same attributes into a flow. These attributes are typically defined by the administrator, often based on layers in the OSI model such as Layer 4 (datagram), Layer 3 (packet), or Layer 2 (dataframe).
- Flow Entry: Located at the switching devices, it performs matching based on information within a flow
(Figure 2).
- Flow Table: OpenFlow manages flows and organizes them in a flow table to optimize the flow of traffic within the system.

Thus, the process of collecting flow traffic, detecting, and mitigating forms a closed loop from the Controller device to the switch devices and vice versa. These devices work continuously and synchronize data with each other seamlessly.

### Extracting Packet Features
When a packet enters the system, the system will extract the packet features, specifically as follows (Figure 2):
- Switch-id: information about which switch the packet originates from and which port.
- IP source.
- IP destination.
- Port source.
- Port destination.
- Protocol (packet protocol): TCP, UDP, ICMP.
- Byte: packet size.

Based on the characteristics of DDoS attacks, attackers target a specific server or service, meaning the destination IP is clear, and the source of the attack is obscured by generating random source IPs. Thus, based on this attack DDoS characteristic, when a packet enters the system, the OF Switch devices will perform checks and extract distinctive features of the packet, such as source IP and destination IP.  
For each flow, there will be additional counters:
- Flow duration: the time a flow lasts, up to a maximum of 20 seconds.
- Idle time: the waiting time of a flow, also known as
idle time, up to a maximum of 100 seconds.
- Packet count: a counter for the number of packets.
- Byte count: a counter for the packet size.

<p align="center">
  <img width="600" src="https://i.imgur.com/Fi5BMLK.png" alt="Processing each flow table in the system">
</p>
<p align="center">
  <em>Figure 3: Processing each flow table in the system</em>
</p>
In Figure 3, OpenFlow will continue to divide the extracted IP information into multiple flow tables, with each flow table corresponding to a destination IP, and source IPs will be placed into individual flow entries. If the number of destination IPs increases, the number of flow tables will also increase.  
After being extracted packet and processed, for each periodic statistical interval (in our case, every 20 seconds), the OpenFlow Switch will send the information from these flow tables to the Controller device.

As shown in the example in Table 1, when a packet arrives in the system, the OF Switch will extract the packet based on each destination IP to create a flow table. In this case, we extract packets with the destination IP: 10.0.0.1 into one flow table. The source IPs become flow entries within that flow table, and for each packet that needs to go through, a new flow entry is created, and the counters continue to increment.  
| IN PORT | SWITCH ID | IP SRC | IP DST | PROTOCOL | SRC PORT | DST PORT | COUNTER PACKET |
|---------|-----------|--------|--------|----------|----------|----------|----------------|
| 1 | 1 | 192.168.0.5 | 10.0.0.1 | TCP (6) | * | 80 | 1 |
| 2 | 3 | 172.16.0.5 | 10.0.0.4 | UDP (17) | * | 22 | 2 |
| 2 | 3 | 192.168.10.10 | 10.0.0.4 | UDP (17) | 30 | 665 | 3 |
| 3 | 2 | 192.168.0.1 | 10.0.0.4 | IDCMP (1) | 55 | 3389 | 4 |

*Table 1: An example of packet extraction and matching packet into flow entries within the flow table*

### Attack Detection Module and Mitigation Module
After receiving statistical information from the flow tables, the Attack Detection Module use the formulas outlined in section `Statistical Method`. Subsequently, it utilizes machine learning algorithms such as DT, KNN, RF, or SVM to compare the statistical results with the input dataset, predicting whether the traffic flow network is dangerous.  
If the traffic flow is deemed normal, the packets continue to enter the system. However, if the traffic flow is predicted as dangerous, the information about that flow is forwarded to the Mitigation Module.  
When a hazardous traffic flow is identified by the detection module, suppose the switch with switch-id-1 and port 1 is currently receiving this hazardous traffic flow. The Mitigation Module will send a request to the Controller to instruct switch-id-1 to remove the traffic flows coming from port 1. Simultaneously, the Mitigation Module sends continuous alerts to the administrator for system monitoring. After the attack flow concludes, approximately after 60s, the system will automatically re-establish the connection to port 1 to
maintain system operation.
The packet processing workflow of the system is detailed in Figure 4.  
<p align="center">
  <img width="600" src="https://i.imgur.com/EtBCyZt.png" alt="The packet processing workflow of the system">
</p>
<p align="center">
  <em>Figure 4: The packet processing workflow of the system</em>
</p>

### Statistical Method
The parameters used for statistical calculations are the values within the counters of the flow entries in the OF switch. For each time cycle T, the OF Switch devices will send flow entry information to the module on the Controller. The specific statistical information includes:
- SIPS (Speed of IP Sources): Number of source IP addresses accessing the server.
$$SIPS = {Sumary(IP) \over T}$$
- SPN (Source Port Number): The total number of source ports accessing the server.
$$SPN = {Sumary(PORT) \over T}$$
- PN (Packet Number): The number of packets in each flow table.
$$SPN = {Sumary(PACKET) \over T}$$
- SFE (Speed of Flow Entries): The total number of flow entries in each flow table.
$$SFE = {Sumary(Flow Entry) \over T}$$


## A Proposed Design for SDN Infrastructure
<a name="a-proposed-design-for-sdn-infrastructure"></a>

To ensure the system’s effectiveness in detection and mitigation DDOS attacks, we propose a suitable design of an SDN Network system as depicted in Figure 5.  
<p align="center">
  <img width="600" src="https://i.imgur.com/Bar64di.png" alt="The proposed SDN network design">
</p>
<p align="center">
  <em>Figure 5: The proposed SDN network design</em>
</p>

The network infrastructure is divided into three layers, following the standards of a SDN network infrastructure.
- Control Layer: This layer is considered the brain of the entire system and contains the Controller device. The proposed attack prevention modules named uitSDNDDoSD, as outlined in section 3.4, will be directly integrated into the Controller. This module functions as a proxy to collect all network traffic flows from the OpenFlow protocol to serve statistical computation. Upon detecting an attack on the system, the module will notify the Controller, which, in turn, will instruct the OF Switch to discard malicious packets. For the purposes of this research, we utilize the RYU software to simulate a Controller device within the system.
- Data Plane Layer: This layer houses network infrastructure devices such as servers and switches. The OpenFlow protocol is used to interconnect these devices. All activities related to traffic, packet forwarding, and control are managed by the Control Layer. In this study, the Mininet software is employed to simulate this network infrastructure layer.
- Application Layer: This layer includes applications managing the network infrastructure, traffic processing policies, system security policies, and all these applications are installed, stored, and operated independently on one or more servers within the system. They are connected and controlled by the Controller through a Rest API. In this research, we only implement applications related to monitoring network infrastructure, such as monitoring the Controller’s resources and monitoring the system bandwidth for throughout the experimentation process, we will monitor and observe how the system is affected in terms of resource utilization. This approach allows us to conduct a comprehensive assessment of the system’s performance under various conditions.




## System Performance Evaluation
<a name="system-performance-evaluation"></a>

...

## Conclusion and Future Work
<a name="conclusion-and-future-work"></a>

...

## References
<a name="references"></a>

...
