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
*Figure 1: Proposed system operating mode*  

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
In this study, we propose a DDoS attack detection system in SDN network called uitSDNDDoSD. The uitSDNDDoSD system has a structure as shown in Figure 2. Our system comprises three main modules, as follows:
- Feature extraction from packets: When packets enter the system, we use the OpenFlow protocol to assist in extracting packet features such as IP, port, etc. Subsequently, these features are organized into flow tables and flow entries. Then, this information is sent to the detection module at the Controller after a specified time interval.
- Attack detection module: We utilize machine learning algorithms to compare statistical information with the input dataset.
• Mitigation module: After the comparison, if a dan gerous data network is identified, this module will implement mitigation policies to ensure system safety during an attack.
![Proposed system operating mode](https://i.imgur.com/z00gHc0.png)
*Figure 2: Proposed system architecture*  



## System Performance Evaluation
<a name="system-performance-evaluation"></a>

...

## Conclusion and Future Work
<a name="conclusion-and-future-work"></a>

...

## References
<a name="references"></a>

...
