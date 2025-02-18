# Cyber Security System with Generative AI for Threat Detection  

## 1. Introduction  

The **Cyber Security System with Generative AI for Threat Detection** aims to develop a **cutting-edge AI system** for the early detection of **cyber security threats**. Leveraging **generative models** and **machine learning algorithms**, the system accurately identifies **anomalies in network traffic, system logs, and user behavior** that indicate potential security breaches.  

### Key Objectives:  
✅ **Proactive Threat Mitigation** – Prevent cyber attacks before escalation.  
✅ **Enhanced Detection Accuracy** – Improve anomaly detection in real-time.  
✅ **Reduced False Positives** – Ensure precise threat identification.  
✅ **Faster Incident Response** – Optimize security team reaction times.  
✅ **Adaptive Security Model** – Evolve with emerging cyber threats.  

### How It Works:  
- Uses **advanced ML models** to analyze **network activity, system logs, and user behavior**.  
- Detects **malware attacks, phishing attempts, and insider threats**.  
- Provides **real-time alerts and insights** for security teams.  
- Seamlessly integrates with **firewall protection** to prevent **data breaches**.  

As cyber threats continue to evolve, many companies are strengthening their **firewall security** to prevent **data leaks**. This AI-driven solution is **fast, efficient, and capable of detecting threats in real time**. The system ensures **high-level data protection** while immediately alerting users of potential risks.  

Let’s explore the **working model** and **detailed descriptions** of the security system.  

![Cyber Security System](https://github.com/user-attachments/assets/c4ef4f82-6ffd-4be0-b17e-6b52b0f93256)  

### Model Performance:  
- **Training Accuracy**: **0.987**  
- **Testing Accuracy**: **0.983**  

| Class | Precision | Recall | F1-score | Support |
|--------|------------|--------|----------|---------|
| **Non-Breached** | 1.00 | 1.00 | 1.00 | 69,039 |
| **Breached** | 1.00 | 1.00 | 1.00 | 69,257 |
| **Overall Accuracy** | **0.980** | | | 138,296 |

![Performance Graph](https://github.com/user-attachments/assets/12a2df33-d000-41da-8eae-3da6aa87be20)  

---

## 2. Log Retrieving Module  

The **Log Retrieving Module** processes and classifies system logs using libraries like **os, csv, time, and win32evtlog** to enhance **data collection and system monitoring**.  

### Log Classification:  
📌 **Network Logs** – Tracks **network connections, IP traffic, and firewall activity**.  
📌 **Application Logs** – Monitors **installed software (Chrome, antivirus, programs, etc.)**.  
📌 **Performance Logs** – Analyzes **CPU, GPU, memory, and disk performance**.  

### Feature Extraction:  
- **Event IDs**  
- **Source Names**  
- **Input & Output Networks**  

Each **log type** has **different input-output parameters**. Logs are **retrieved every 5 minutes** and passed to the **AI model** for analysis. The **results are displayed to the user** in a **Django-based web dashboard**, allowing individual users to **access system reports via a web portal**.  

![Log Retrieval](https://github.com/user-attachments/assets/a5dd6539-3354-45c6-99b5-1f1955594fab)  
![System Monitoring](https://github.com/user-attachments/assets/6cc373c6-b42e-45d3-a367-385e2d7a9530)  
