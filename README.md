1.Introduction 


The cyber security system with generative AI for threat detection, the aim of the project is to develop a cutting-edge AI system for early detection of cyber security threats. Leveraging generative models and machine learning algorithms, the system aims to accurately identify anomalies in network traffic, system logs, and user behavior indicative of potential security breaches. The system enables organizations to proactively mitigate risks and prevent cyber Attacks before they escalate. The goal is to enhance threat detection accuracy, reduce false positives, improve incident response times, and adapt to evolving threats. Ultimately, the project aims to empower organizations with actionable intelligence to strengthen their cyber security defense and protect critical assets. In recent digital landscape, cyber threats are becoming increasingly complex. To combat this, our project aims to create an advanced AI system that can detect cyber security threats early on. 
In response to the escalating complexity of cyber threats, this project endeavors to develop a sophisticated generative AI-based system for the early detection of cyber security threats. Using cutting-edge machine learning techniques, our system analyses different types of data like network activity, system events, and user behavior. It looks for any unusual patterns that could signal a security breach, such as malware attacks, phishing attempts, or insider threats. By providing real-time insights and alerts, our system helps organizations take proactive steps to protect themselves, keeping their valuable data and assets safe from modern cyber threats. Even threats are increasing, recent times most of the product companies are increasing their firewall as they are facing data leakage and the threads. The motive towards the project is that, it is much convenient in time duration as they do not take much time in the detection of the threats. Securing the reputed data’s from the company are mandatory in every field to take over these data’s the firewall protection should be much efficient and powerful. It should be highly active and valuable to secure the data and alert the users if any type of threats is detected. Let us further move on in detail about the working model of the security system and descriptions of the project. 


<img width="263" alt="image" src="https://github.com/user-attachments/assets/c4ef4f82-6ffd-4be0-b17e-6b52b0f93256" />



Accuracy on Training dataset :  0.987
Accuracy on Testing dataset :  0.983
precision         recall  f1-score   support

non-breached       1.00      1.00      1.00     69039
breached           1.00      1.00      1.00     69257
accuracy                               0.980    138296
macro avg          1.00      1.00      1.00    138296
weighted avg       1.00      1.00      1.00    138296



<img width="223" alt="image" src="https://github.com/user-attachments/assets/12a2df33-d000-41da-8eae-3da6aa87be20" />




2.Log retrieving module


The module uses libraries like os, csv, time, and win32evtlog to handle file operations, CSV files, time-related functions and Windows event logs, streamlining data collection and analysis, and enhancing system monitoring.
After retrieving the logs we classify into 3 types, the log manages networking wil be classified network logs, the log manage installed applications such as chrome, anti-virus software, programs etc ., will be classified as application logs, the log manages the performance of cpu, gpu, memory and disk will be classified as performance logs. The feature extracted from the logs are event ids, source  name of the event, input and output networks. It varies for every logs based on the log type input and output range will differ. These 3 logs are retrieved for every 5 minutes and will be passed to the model one by one and the results will be displayed to the user.  The report is integrated with Django frame work so that every user can have separate access to software and user can view their system report in their web portal.  <img width="177" alt="image" src="https://github.com/user-attachments/assets/a5dd6539-3354-45c6-99b5-1f1955594fab" />
<img width="183" alt="image" src="https://github.com/user-attachments/assets/6cc373c6-b42e-45d3-a367-385e2d7a9530" />
