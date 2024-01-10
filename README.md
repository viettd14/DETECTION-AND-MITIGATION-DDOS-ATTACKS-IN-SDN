<div align="center">
  <h1><strong>A STUDY ON DETECTING AND MITIGATING DENIAL OF SERVICE ATTACKS IN SOFTWARE DEFINED NETWORKS</strong></h1>
</div>

# Table of Contents
1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Related Work](#related-work)
4. [Design SDN Network Infrastructure](#design-sdn-network-infrastructure)
5. [System Performance Evaluation](#system-performance-evaluation)
6. [Conclusion and Future Work](#conclusion-and-future-work)
7. [References](#references)

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

![Proposed system operating mode](https://i.imgur.com/iY8LWZU.png)
<div align="center"> *Figure 1: Proposed system operating mode* </div>

Within the system, the OpenFlow protocol is employed, where OpenFlow Switch devices analyze packet headers based on source IP, destination IP, port, switch, protocol, time, packet count, and send this information to the Controller for statistical analysis. Subsequently, the system is tested using machine learning models such as Decision Tree (DT), K-Nearest Neighbors (KNN), Random Forest (RF), and Support Vector Machine (SVM) to predict whether the incoming traffic to the system is normal or anomalous. The paper utilizes the CIC-DDOS2019 input dataset to evaluate machine learning algorithms in DDoS attack detection.  
After proposing an attack prevention solutions, I suggests an appropriate Software-Defined Networking architecture for detecting and mitigating Distributed Denial of Service attacks.


## Related Work
<a name="related-work"></a>

...

## Design SDN Network Infrastructure
<a name="design-sdn-network-infrastructure"></a>

...

## System Performance Evaluation
<a name="system-performance-evaluation"></a>

...

## Conclusion and Future Work
<a name="conclusion-and-future-work"></a>

...

## References
<a name="references"></a>

...
