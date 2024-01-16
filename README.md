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
8. [Testing the Proposed System Against Attacks](#testing-the-proposed-system-against-attacks)
9. [References](#references)
10. [Acknowledgement](#acknowledgement)


# Abstract
<a name="abstract"></a>

The escalating risks to network security, stemming from the continual evolution of network infrastructure and application systems, have significantly impacted system availability, with Denial of Service (DDoS) attacks standing out as a particularly disruptive threat capable of overwhelming and even incapacitating systems. In response, this study introduces a comprehensive system designed to detect and mitigate DDoS attacks within Software-Defined Networks (SDNs). Our proposed solution involves a multi-modules architecture operating as an Intrusion Prevent System (IPS), strategically engineered for seamless integration into the Controller device. The system's functionality includes the periodic extraction of multiple parameters from flow entries on the OpenFlow switch, complemented by machine learning (ML) models, enabling the identification of abnormal packets infiltrating the system. Upon detecting an attack, the controller promptly dispatches policies to the OpenFlow switch, initiating the removal of malicious packets. This autonomous system employs common machine learning algorithms and real-time processes to detect and counteract attacks on OpenFlow Switches. The study evaluates the system’s performance using four distinct algorithms such as Decision Tree(DT), Random Forest (RF), K-Nearest Neighbors (KNN), and Support Vector Machine (SVM). The CIC-DDOS2019 input dataset [1] is used to evaluate machine learning algorithms in detecting DDoS attacks, experimental results show that the Decision Tree (DT) algorithm exhibits high F1 scores. highest with 99.87%.  



# Introduction
<a name="introduction"></a>

Software-Defined Networking (SDN) is a networking technology that improves performance and optimizes network management compared to traditional networks due to its highly flexible nature and rapid deployment capabilities. SDN allows centralized network management, empowering administrators to program network devices within the system. However, SDN has many potential information security risks, such as:
- Man-in-the-Middle Attacks: Attackers position themselves between the Controller and the Switch, aiming to sniffer and steal information.
- Software System Vulnerabilities: Various risks associated with the system's software, such as software vulnerabilities and the exposure of administrative credentials.
- Controller Device Security: Ensuring the security of the Controller device is crucial, as any compromise could severely impact the entire system, leading to service disruptions.
- Particularly, Distributed Denial of Service (DDoS) attacks that aim to overload the entire system. In addition to targeting a specific network service or server, attackers may focus on the Controller device or directly launch DDoS attacks against the system management software to cause a system-wide overload.

DDoS is a highly dangerous type of attack on the Internet, as it causes system overload, resulting in slow or unresponsive system operations. In some cases, it can even block access to servers, denying legitimate users the ability to use system services. With the diversity of devices and the rapid development of network attack models over the past decades, the complexity of attacks has increased. Attackers continuously change their attack patterns to avoid detection, introducing anomalies in network traffic, or employing Low-Rate DDoS attacks (LR-DDOS). This complexity makes it challenging to detect and block each attack source. However, effective defense against these attacks requires quick detection and prevention to avoid system resources being overwhelmed.  
Despite numerous research efforts and implemented measures to prevent these attacks. However, DDoS attacks are becoming increasingly diverse, posing significant difficulties and challenges. The complexity of algorithms has introduced certain delays in DDoS attack detection methods. Therefore, monitoring changes in access traffic patterns and timely, accurate identification of DDoS attacks are essential and urgent.  
One optimized solution is the utilization of SDN network for the current network infrastructure. While SDN architecture has the potential to enhance security by centrally monitoring and controlling the network through the Controller device, facilitating easy configuration of network devices, it also presents a significant challenge. The very nature of SDN architecture makes it susceptible to becoming a target for DDoS attacks.  
In my study, I propose an automated solution for detect and mitigation DDoS attacks in SDN network. This solution introduces a new, compact module that integrates directly into the SDN network's Controller device. This module operates as an Intrusion Detection System (IDS), monitoring all inbound and outbound traffic to the system to observe and predict potential attack risks.  
Within the system, the OpenFlow protocol is employed, where OpenFlow Switch devices analyze packet headers based on source IP, destination IP, port, switch, protocol, time, packet count, and send this information to the Controller for statistical analysis. Subsequently, the system is tested using machine learning models such as Decision Tree (DT), K-Nearest Neighbors (KNN), Random Forest (RF), and Support Vector Machine (SVM) to predict whether the incoming traffic to the system is normal or anomalous. The paper utilizes the CIC-DDOS2019 input dataset to evaluate machine learning algorithms in DDoS attack detection.  
After proposing an attack prevention solutions, I suggests an appropriate Software-Defined Networking architecture for detecting and mitigating Distributed Denial of Service attacks.


# Related Work
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
A proposed system model for detecting intrusions by monitoring incoming packets into the system, with Input-Output details illustrated in Figure 1.  
Input: Packets arriving at the system.  
Output: If the packet is normal, it will be allowed to enter the system and proceed with processing. If the packet poses
a DDoS attack risk, the system will implement mitigation measures and send alerts to users.  
<p align="center">
  <img width="700" src="https://i.imgur.com/36uOr4V.jpg" alt="Proposed system operating mode">
</p>
<p align="center">
  <em>Figure 1: Proposed system operating mode</em>
</p>

# Design SDN Network Infrastructure
<a name="design-sdn-network-infrastructure"></a>

### Proposed Solution for DDoS Attack Prevention
In this study, we propose a DDoS attack detection system in SDN network called uitSDNDDoSD. Our system comprises three main modules, as follows:
- Feature extraction from packets: When packets enter the system, we use the OpenFlow protocol to assist in extracting packet features such as IP, port, etc. Subsequently, these features are organized into flow tables and flow entries. Then, this information is sent to the detection module at the Controller after a specified time interval.
- Attack detection module: We utilize machine learning algorithms to compare statistical information with the input dataset.
- Mitigation module: After the comparison, if a dan gerous data network is identified, this module will implement mitigation policies to ensure system safety during an attack.

## Packet Processing In the OpenFlow Protocol
With the characteristics of an SDN based on the separation of the control plane from the data plane. In the control plane, with the Controller as the brain of the entire system, can monitor, provide, and enforce policies to OF switches through the OpenFlow protocol [7] in a flexible manner. Packets are processed by the system on a per-flow basis and controlled in flow tables within OF switch through flow entries.  
<p align="center">
  <img width="500" src="https://i.imgur.com/fhldzcv.png" alt="Extracting packet features to matching flow tables">
</p>
<p align="center">
  <em>Figure 2: Extracting packet features to matching flow tables</em>
</p>

An OpenFlow protocol consists of three main components:
- Flow: The OpenFlow protocol automatically groups new packets with the same attributes into a flow. These attributes are typically defined by the administrator, often based on layers in the OSI model such as Layer 4 (datagram), Layer 3 (packet), or Layer 2 (dataframe).
- Flow Entry: Located at the switching devices, it performs matching based on information within a flow (Figure 2).
- Flow Table: OpenFlow manages flows and organizes them in a flow table to optimize the flow of traffic within the system.

Thus, the process of collecting flow traffic, detecting, and mitigating forms a closed loop from the Controller device to the switch devices and vice versa. These devices work continuously and synchronize data with each other seamlessly.

## Extracting Packet Features
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
  <img width="500" src="https://i.imgur.com/Fi5BMLK.png" alt="Processing each flow table in the system">
</p>
<p align="center">
  <em>Figure 3: Processing each flow table in the system</em>
</p>
In Figure 3, OpenFlow will continue to divide the extracted IP information into multiple flow tables, with each flow table corresponding to a destination IP, and source IPs will be placed into individual flow entries. If the number of destination IPs increases, the number of flow tables will also increase.  
After being extracted packet and processed, for each periodic statistical interval (in our case, every 20 seconds), the OpenFlow Switch will send the information from these flow tables to the Controller device.

As shown in the example in Table 1, when a packet arrives in the system, the OF Switch will extract the packet based on each destination IP to create a flow table. In this case, we extract packets with the destination IP: 10.0.0.1 into one flow table. The source IPs become flow entries within that flow table, and for each packet that needs to go through, a new flow entry is created, and the counters continue to increment.  
| IN PORT | SWITCH ID | IP SRC | IP DST | PROTOCOL | SRC PORT | DST PORT | COUNTER PACKET |
|:-------:|:---------:|:------:|:------:|:--------:|:--------:|:--------:|:--------------:|
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
  <img width="600" src="https://i.imgur.com/uTaFdFb.jpg" alt="The packet processing workflow of the system">
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


# A Proposed Design for SDN Infrastructure
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


# System Performance Evaluation
<a name="system-performance-evaluation"></a>

## Metrics
The performance of our detection DDoS algorithm, we use metrics including Precision, Recall, and F1-Score with the following detailed parameters:
- Precision: Precision measures the ratio of true positive predictions to the total predicted positives.
$$Precision = {TP \over TP + FP}$$
- Recall Rate: Recall measures the ratio of true positive predictions to the total actual positives.
$$Recall = {TP \over 𝑇𝑃 + 𝐹𝑁}$$
- F1-Score: which is the harmonic mean of Precision and Recall, providing a balanced measure.
$$F1 = {2 * 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ∗ 𝑅𝑒𝑐𝑎𝑙𝑙 \over 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 + 𝑅𝑒𝑐𝑎𝑙𝑙}$$

|           | True | False |
|-----------|:----:|:-----:|
| Positives | TP | FP |
| Negative | TN | FP |

*Table 2: Algorithm metrics*

## Dataset details
We utilize the CICDDOS2019 dataset as the input for the learning system to recognize patterns in potentially dangerous traffic flows. Machine learning algorithms leverage the statistically derived outcomes to compare against the dataset, enabling the prediction of attack traffic.  
"Dataset Information (Figure 6):
- Attributes: 22 columns and approximately 5 billion rows.
- Number of rows labeled ’1’ (DDOS): 49.01.
- Number of rows labeled ’0’ (normal): 50.99.

The features used in the CICDDOS2019 dataset for comparison with statistical methods are as follows:
- Switch-id: Information about the switch from which the packet originates, including the associated port.
- Ip source: Source IP address.
- Ip destination: Destination IP address.
- Port source.
- Port destination.
- Protocol (packet protocol): TCP, UDP, ICMP.
- Flow duration: Duration of a flow, with a maximum of 20 seconds.
- Idle time: Waiting time for a flow, also known as idle time, with a maximum of 100 seconds.
- Packet count: Count of the number of packets.
- Byte count: Count of the packet size in bytes.
- Label: Indicates whether the packet is DDoS marked as ’1’ or normal marked as ’0’.
<p align="center">
  <img width="700" src="https://i.imgur.com/cq0etXH.png" alt="Dataset details">
</p>
<p align="center">
  <em>Figure 6: Dataset details</em>
</p>

## Algorithm Evaluation
To evaluate accuracy, training time, and system resource consumption for each algorithm, aiming to identify the optimal algorithm for the system. We employed physical server hardware with the Windows Server 2019 operating system. Virtualization was achieved using VMWARE Workstation software to emulate Controller devices through RYU and Mininet software, with the goal of simulating a SDN Network infrastructure for system experimentation. Detailed system configuration information is provided in Table 2.

| Hardware | Physical Server | Ryu Controller | Mininet |
|:--------:|:----:|:-----:|:-----:|
| OS | Windown Server 2019 | Ubuntu 18.04 LTS |Ubuntu 18.04 Desktop|
| RAM | 10GB | 4GB | 4GB |
| CPU | Xeon(R) Gold 6240 @ 2.60GHz | 4vCPU | 4vCPU |

*Table 3: The detailed system configuration*

As evident from the experimental results in Table 4, the decision tree algorithm the highest accuracy among the algorithms we employed. In addition to its high accuracy, the decision tree exhibited the lowest model training time, processing speed, and resource consumption compared to other algorithms.  
For the requirements of a network system, which demand quick processing and low computational resource consumption, the decision tree proves to be well-suited for DDoS attack detection.

| Algorithm | Precision (%) | Recall (%) | F1-Score (%) | Model Training Time (s) | CPU Usage (%) | RAM Usage (%)  |
|:---------:|:-------------:|:----------:|:------------:|:-----------------------:|:-------------:|:--------------:|
| KNN | 97.65 | 98.04 | 97.84  | 78 | 51 | 80 
| **DT** | **99.82** | **99.89** | **99.87** | **19** | **50** | **70** |
| RF | 99.92 | 99.64 | 99.78 | 40 | 50 | 70 |
| SVM | 87.30 | 88.23 | 87.77 | 3600 | 70 | 90 |

*Table 4: The detailed system configuration*

<p align="center">
  <img width="800" src="https://i.imgur.com/BRH9u2V.png" alt="Confusion matrix of the algorithm">
</p>
<p align="center">
  <em>Figure 7: Confusion matrix of the algorithm</em>
</p>


# Testing the Proposed System Against Attacks
<a name="testing-the-proposed-system-against-attacks"></a>

To conduct the experiment, we will randomly select both an attacking server and a target server. For the attacking server, we will use the flood attack technique to generate random source IPs. The execution process is divided into stages as outlined below:
- Scenario 1: The system operates normally, without any attacks.
- Scenario 2: The system experiences a denial-of-service attack, but the system only incorporates attack detection module.
- Scenario 3: The system is under a denial-of-service attack, and the system is equipped with both detection module and mitigation module to minimize the impact of the attack.
- Scenario 4: The Controller is subjected to a DDoS attack.

`Scenario 1:` Our system is operating normally, and we conducted a ping test between hosts to check the stability of the system.  
`Scenario 1 Result:` At this stage, the system is functioning normally, and connections are stable.  
The system continually monitors the incoming and outgoing packets, and after 20 seconds, it updates the status as either normal (Traffic is legitimate) or anomalous."

<p align="center">
  <img width="700" src="https://i.imgur.com/mypnU6b.png" alt="Scenario 1 Result">
</p>
<p align="center">
  <em>Figure 8: Scenario 1 Result</em>
</p>

`Scenario 2:` We conducted an attack from server h1 to server h6 (Figure 10) using tools such as hping3, HOIC, LOIC, and slowloris.

<p align="center">
  <img width="400" src="https://i.imgur.com/CU7B6IC.png" alt="Scenario 2">
</p>
<p align="center">
  <em>Figure 9: Scenario 2</em>
</p>

`Scenario 2 Result:` At this stage, the system is only integrated at the attack detection module, so when an attack occurs, the system is still affected as the Controller is overloaded during the attack. In Figure 11, the Controller has to handle over 900 packets per second, and the CPU usage peaks at nearly 90% to process the information.  
When traffic flows into the system, the OpenFlow protocol assists by collecting data flows from the switches and pushing the information to the detection module. Here, the module conducts statistical analysis based on the data provided by the switching devices. After conducting statistics for approximately 20s to 30s, the machine learning model predicts whether an attack is occurring. If yes, continuous alerts are sent to the administrator.

<p align="center">
  <img width="500" src="https://i.imgur.com/vFsnafg.png" alt="Scenario 2 Result">
</p>
<p align="center">
  <em>Figure 10: Scenario 2 Result</em>
</p>

`Scenario 3:` We integrate the attack mitigation module into the system.  
Similar to scenario 2, when an attack occurs, the system can identify that it is under attack after approximately 20s to 30s. Subsequently, the system automatically initiates mitigation by identifying which devices in the system are under attack.  
`Scenario 3 Result:` The system detected that the source of the attack originated from the device directly connected to port 2 of switch-id 3. Therefore, the Controller issued a command to this switch-id 3 device to close port number 2, thereby blocking all traffic from the attacking device.
After the mitigation, the entire system’s traffic returned to normal, and the system resources stabilized. Following the conclusion of the attack, the system automatically reopened the connection after approximately 60s.

<p align="center">
  <img width="500" src="https://i.imgur.com/8WAcm1w.png" alt="Scenario 3 Result">
</p>
<p align="center">
  <em>Figure 11: Scenario 3 Result</em>
</p>

`Scenario 4:` In this scenario, we carried out an attack on the Controller from server h6.

<p align="center">
  <img width="400" src="https://i.imgur.com/n8W11Ki.png" alt="Scenario 4">
</p>
<p align="center">
  <em>Figure 12: Scenario 4</em>
</p>

`Scenario 4 Result:` The system autonomously detected and mitigated the attack. Throughout the attack, the Controller remained operational in a normal and stable.

<p align="center">
  <img width="500" src="https://i.imgur.com/emh5I23.png" alt="Scenario 4 Result">
</p>
<p align="center">
  <em>Figure 13: Scenario 4 Result</em>
</p>




# Conclusion and Future Work
<a name="conclusion-and-future-work"></a>

## Conclusion
Leveraging the fundamental principles of Software Defined Networking (SDN), we have put forward a solution to detect and mitigate DDoS attacks. This solution is implemented through a compact module designed for integration into existing systems, operating effectively as an Intrusion Detection System (IDS). Once the module is incorporated into the system, the Controller is capable of performing:
- Detecting and mitigating DDoS attacks automatically.
- If an attacker conducts port scanning with a high volume of traffic, the proposed system is designed to detect and prevent port scanning.
- Based on the policy of Flow, the task of prevention and drop of attack packets will be carried out by the OF Switch devices.
- Use packet features extractor from the OF Switch serves as statistical parameters for the DDoS attack detection solution.

Because of directly utilizing statistical parameters from the OF Switch and, upon detecting an attack, the Controller will instruct the OF Switch to perform attack mitigation as well. Therefore, the system operates with low computational resources, enabling real-time monitoring and defense against attacks.  
With both detection and mitigation centered on the OF Switch devices, this approach minimizes deployment costs as well as operational expenses. The entire solution is encapsulated within a compact module, seamlessly integrated directly into the Controller, without the need for additional devices for solution deployment.  
During the system experimentation, the paper identified the Decision Tree machine learning algorithm as the most effective and optimal for the system. Throughout the training of the model and the detection process, the algorithm demonstrated the lowest system resource usage while achieving rapid detection of attacks.

## Future Work
To enhance and optimize the attack detection and mitigation model for improved and more accurate predictions:
1. Train Additional Deep Learning Models:
- Train and evaluate additional deep learning models to explore their potential effectiveness in enhancing the system’s capabilities.
2. Cross-Validate Across Multiple Datasets:
- Perform cross-validation on diverse datasets to ensure the robustness and generalization of the model across different scenarios.
3. Integration with Other Tools:
- Integrate the IDS-DDoS solution with other complementary tools to enhance overall reliability and effectiveness in handling a variety of cyber threats.
4. Explore Superior Models:
- Investigate and explore more advanced models that have the capability to identify tools and patterns beyond those present in the current dataset.




# References
<a name="references"></a>
[1] Sharafaldin, I., Lashkari, A.H., Hakaka, S., Ghorbani, A.A., 2019. Developing realistic distributed denial of service (ddos) attack dataset and taxonomy. Digital Investigation.  
[2] Doriguzzi-Corin, R., Millar, S., Scott-Hayward, S., del Rincón, J.M., Siracusa, D., 2020. Lucid: A practical, lightweight deep learning solution for ddos attack detection. IEEE Transactions on Network and Service Management 17, S876–S88.  
[3] Xiao, P., Qu, W., Qi, H., Li, Z., 2015. Detecting ddos attacks against data centers with correlation analysis. Computer Communications 67, 66–74. doi:https://doi.org/10.1016/j.comcom.2015.06.012.  
[4] Singh, S., Jayakumar, S.K.V., 2022. Ddos attack detection in sdn: Optimized deep convolutional neural network with optimal feature set. Wireless Personal Communications: An International Journal 125, 2781–2797. doi:https://doi.org/10.1007/s11277-022-09685-z.  
[5] Feinstein, Schnackenberg, 2003. Statistical approaches to ddos attack detection and response. DARPA Information Survivability Conference and Exposition 2, 303–314. doi:10.1109/DISCEX.2003.1194894.  
[6] Gebremeskel, T.G., Gemeda, K.A., Krishna, T.G., Ramulu, P.J., 2023. Ddos attack detection and classification using hybrid model for multicontroller sdn. Wireless Communications and Mobile Computing 2023, 1–18. doi:https://doi.org/10.1155/2023/9965945.  
[7] Wang, J., Wang, L., Wang, R., 2023. A method of ddos attack detection and mitigation for the comprehensive coordinated protection of sdn controllers. https://www.mdpi.com/1099-4300/25/8/1210 25. doi:https://doi.org/10.3390/e25081210.  
[8] Noe, M.Y.N., Vargas-Rosales, C., Pérez-Díaz, J.A., Carrera, D.F., 2022. A flexible sdn-based framework for slow-rate ddos attack mitigation by using deep reinforcement learning. Journal of Network and Computer Applications 205, 103444.
 doi:https://doi.org/10.1016/j.jnca.2022. 103444.  
[9] PÉREZ-DÍAZ1, J.A., VALDOVINOS, I.A., KIM-KWANG RAYMOND CHOO 3, D.Z., 2020. Flexible sdn-based architecture for identifying and mitigating low-rate ddos attacks using machine learning. IEEE Access 8, 99. doi:10.1109/ACCESS.2020.3019330.  


# Acknowledgement
<a name="acknowledgement"></a>
This research was supported by The VNUHCM-University of Information Technology’s Scientific Research Support Fund.
