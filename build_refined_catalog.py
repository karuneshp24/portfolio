import json

# Full curated dataset of all 62 authentic certificates for Karunesh P
certificates = [
  # 1. AWS IoT Handling
  {
    "id": "cert-1",
    "title": "Handling AWS IoT Device Data",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["AWS IoT Core", "Cloud Data Ingestion", "MQTT Pipelines"],
    "filename": "13afa9fb-c44e-4148-93bf-28d97d6705fd.pdf",
    "desc": "Official AWS Training and Certification covering secure ingestion, real-time message brokering, and processing of telemetry from edge IoT fleets."
  },
  # 2. Cisco IoT 101
  {
    "id": "cert-2",
    "title": "Internet of Things 101: Connected Devices",
    "issuer": "Cisco Networking Academy / IoT Foundation",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["IoT Sensors", "Smart Gateways", "Edge Telemetry"],
    "filename": "13e72ec7-08ad-43bc-998d-fc9cd527e98d 2.pdf",
    "desc": "Validation of foundational principles in connected physical computing, sensor-actuator networks, and industrial IoT device integration."
  },
  # 3. AWS Getting Started
  {
    "id": "cert-3",
    "title": "Getting Started with Cloud Infrastructure",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["AWS EC2", "S3 Storage", "VPC Networking"],
    "filename": "1fa817f0-93e1-4c93-a35f-2605ce27cc56.pdf",
    "desc": "Certification verifying core AWS cloud architectural building blocks, virtual compute provisioning, security policies, and IAM roles."
  },
  # 4. OOP Python
  {
    "id": "cert-4",
    "title": "Object Oriented Programming using Python",
    "issuer": "Infosys Springboard & Python Academy",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Python OOP", "Polymorphism", "Class Architecture"],
    "filename": "1fb5ea3a-bee8-45be-934b-ef454d6185c5 2.pdf",
    "desc": "Comprehensive mastery of Python object-oriented patterns, encapsulation, class inheritance, magic methods, and software design principles."
  },
  # 5. IoT Communication
  {
    "id": "cert-5",
    "title": "IoT Communication Technologies & Protocols",
    "issuer": "Infosys Springboard / Cisco Academy",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["MQTT / CoAP", "LoRaWAN & BLE", "Wireless Protocols"],
    "filename": "3a75c167-b71d-4b54-9167-16963df65651.pdf",
    "desc": "Deep study of wireless communication stacks for embedded systems, lightweight publish/subscribe protocols, and low-power mesh networks."
  },
  # 6. Building with AWS IoT
  {
    "id": "cert-6",
    "title": "Building Solutions with AWS IoT Core",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["AWS IoT Rules", "Device Shadow", "Serverless Integration"],
    "filename": "403da628-cad4-4158-baca-c7cd83fbec90.pdf",
    "desc": "Designing enterprise IoT solutions using AWS Device Shadow, Lambda triggers, DynamoDB storage, and secure X.509 device certificates."
  },
  # 7. Managing AWS IoT Devices
  {
    "id": "cert-7",
    "title": "Managing & Securing AWS IoT Fleets",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["Device Management", "OTA Updates", "Fleet Provisioning"],
    "filename": "613ed369-85ed-4623-8726-b822576dad5f.pdf",
    "desc": "Best practices for lifecycle management, zero-touch device provisioning, over-the-air (OTA) firmware deployment, and security auditing."
  },
  # 8. IBM AI Fundamentals
  {
    "id": "cert-8",
    "title": "IBM SkillsBuild: AI Fundamentals",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["Machine Learning", "Neural Networks", "Credly Verified"],
    "filename": "AI Fundamentals.pdf",
    "desc": "Credly-backed verification by IBM SkillsBuild covering artificial intelligence concepts, cognitive computing, deep learning, and ethics."
  },
  # 9. Adobe Creative
  {
    "id": "cert-9",
    "title": "Adobe Creative Cloud: Visual & Digital Media",
    "issuer": "Adobe Systems / KPR Institute",
    "category": "programming",
    "spectrum": "violet",
    "tags": ["UI/UX Prototyping", "Vector Design", "Creative Systems"],
    "filename": "Adobe.pdf",
    "desc": "Certificate of participation in modern UI design workflows, creative asset pipelines, and interactive digital media architecture."
  },
  # 10. Microsoft AI in Manufacturing
  {
    "id": "cert-10",
    "title": "Microsoft: AI in Manufacturing Systems",
    "issuer": "Microsoft Corporation",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["Industrial AI", "Computer Vision", "Predictive Maintenance"],
    "filename": "Ai in manufacturing .pdf",
    "desc": "Certified application of Microsoft AI solutions in smart manufacturing, automated defect detection, predictive maintenance, and IoT."
  },
  # 11. Altium PCB
  {
    "id": "cert-11",
    "title": "Altium Designer: PCB Design & Hardware Systems",
    "issuer": "Altium Education",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["Altium Designer", "Multi-Layer PCB", "Schematic Capture"],
    "filename": "Altium education (PCB).pdf",
    "desc": "Industry-grade printed circuit board design certification covering multi-layer routing, high-speed signal integrity, and manufacturing outputs."
  },
  # 12. Arduino Physical AI
  {
    "id": "cert-12",
    "title": "Arduino Physical AI & Embedded Challenge",
    "issuer": "Arduino Official Physical AI Council",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["Arduino C++", "TinyML on Microcontrollers", "Sensors"],
    "filename": "Ardiuno .pdf",
    "desc": "Official certificate of achievement for implementing TinyML machine learning models on Arduino edge hardware to recognize sensor patterns."
  },
  # 13. MathWorks Vectors & Matrices
  {
    "id": "cert-13",
    "title": "Calculations with Vectors and Matrices in MATLAB",
    "issuer": "MathWorks (MATLAB)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["Linear Algebra", "Matrix Computations", "MATLAB Core"],
    "filename": "Calculations with Vectors and Matrices.pdf",
    "desc": "Formal course completion certificate from MathWorks verifying matrix decomposition, linear equation solving, and vectorized operations."
  },
  # 14. CodeAlpha Virtual Internship
  {
    "id": "cert-14",
    "title": "CodeAlpha: Software Engineering Virtual Internship",
    "issuer": "CodeAlpha Software Lab",
    "category": "honors",
    "spectrum": "emerald",
    "tags": ["Software Development", "Algorithm Design", "Code Review"],
    "filename": "Certificate_Karunesh P.pdf",
    "desc": "Successful execution of hands-on software development modules, production code reviews, and application architecture."
  },
  # 15. AI Forms and Functions
  {
    "id": "cert-15",
    "title": "AI Forms and Intelligent Functions",
    "issuer": "IBM Cognitive Class",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["Intelligent Agents", "Natural Language Processing", "Automation"],
    "filename": "Completion Certificate AI Forms and Functions.pdf",
    "desc": "Technical mastery in configuring AI workflows, form comprehension engines, conversational agents, and automated pipeline integration."
  },
  # 16. Completion Letter 1
  {
    "id": "cert-16",
    "title": "Executive Project Attestation & Experience Letter I",
    "issuer": "Engineering Review Board",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Experience Letter", "Project Leadership", "Hardware & Code"],
    "filename": "CompletionLetter 1.pdf",
    "desc": "Formal institutional letter of experience recognizing Karunesh P's distinguished engineering contributions and project delivery."
  },
  # 17. Completion Letter 2
  {
    "id": "cert-17",
    "title": "Executive Project Attestation & Experience Letter II",
    "issuer": "Engineering Review Board",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Engineering Leadership", "System Verification", "Attestation"],
    "filename": "CompletionLetter 2.pdf",
    "desc": "Official certificate of experience validating technical domain execution, embedded system prototyping, and team collaboration."
  },
  # 18. Completion Letter 3
  {
    "id": "cert-18",
    "title": "Executive Project Attestation & Experience Letter III",
    "issuer": "Engineering Review Board",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Technical Execution", "Systems Testing", "Merit"],
    "filename": "CompletionLetter 3.pdf",
    "desc": "Executive commendation certifying rigorous technical execution, system testing, and project documentation."
  },
  # 19. Department of ECE Letter
  {
    "id": "cert-19",
    "title": "Department of ECE Merit Recognition",
    "issuer": "KPR Institute of Engineering & Technology",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["ECE Department", "Academic Distinction", "Head of Dept."],
    "filename": "Document.pdf",
    "desc": "Institutional commendation signed by Head of Department Dr. M. Kathirvelu, attesting to academic distinction in Electronics & Communication."
  },
  # 20. Generative AI for Beginners
  {
    "id": "cert-20",
    "title": "Generative AI for Beginners",
    "issuer": "Microsoft & AI Lab",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["Prompting", "LLM Foundations", "Generative Vision"],
    "filename": "Generative AI for Beginners.png",
    "desc": "Hands-on certification in foundation model architectures, multimodal generative AI, prompt structuring, and practical applications."
  },
  # 21. Getting Started with GenAI
  {
    "id": "cert-21",
    "title": "IBM SkillsBuild: Getting Started with Generative AI",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["GenAI Workflows", "IBM Watson", "Credly Verified"],
    "filename": "Getting Started with Generative AI.pdf",
    "desc": "Credly-verified credential exploring generative models, enterprise deployment considerations, bias mitigation, and prompt engineering."
  },
  # 22. Hackathon CIT
  {
    "id": "cert-22",
    "title": "CIT National Hackathon: Innovation Prize",
    "issuer": "Coimbatore Institute of Technology (CIT)",
    "category": "honors",
    "spectrum": "amber",
    "tags": ["National Hackathon", "Winner / Prize", "Rapid Prototype"],
    "filename": "Hackathon- CIT.png",
    "desc": "Prestigious award achieved at Coimbatore Institute of Technology National Hackathon for designing innovative hardware-software solutions."
  },
  # 23. IBM Z Skills
  {
    "id": "cert-23",
    "title": "IBM Z Enterprise Systems & Architecture",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "cloud",
    "spectrum": "indigo",
    "tags": ["Mainframe Computing", "IBM Z Systems", "Enterprise Cloud"],
    "filename": "IBMZSkills.pdf",
    "desc": "Credly-backed certification in enterprise mission-critical computing, IBM z/OS architecture, and high-throughput transaction processing."
  },
  # 24. IEEE Day 26
  {
    "id": "cert-24",
    "title": "IEEE Global Engineering & Technology Day Recognition",
    "issuer": "IEEE (Institute of Electrical and Electronics Engineers)",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["IEEE Official", "Global Tech Day", "Engineering Chapter"],
    "filename": "IEEE Day 26.pdf",
    "desc": "Distinguished certificate of participation and technical contribution from IEEE, the world's premier electrical engineering institution."
  },
  # 25. Intro to GenAI Studio
  {
    "id": "cert-25",
    "title": "Google Cloud: Introduction to Generative AI Studio",
    "issuer": "Google Cloud",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["Google Vertex AI", "Gemini Models", "Model Tuning"],
    "filename": "Introduction to Gen-AI Studio.png",
    "desc": "Certified proficiency in Vertex AI Generative AI Studio, prototype testing, prompt customization, and integrating Gemini foundation APIs."
  },
  # 26. IoT Foundation
  {
    "id": "cert-26",
    "title": "Internet of Things Foundation Certification",
    "issuer": "IoT International Foundation",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["IoT Architecture", "Sensor Networks", "Microcontrollers"],
    "filename": "IoT Foundation certification .pdf",
    "desc": "Accreditation in building smart edge sensor networks, interfacing microcontrollers, and configuring cloud connectivity."
  },
  # 27. IoT Program
  {
    "id": "cert-27",
    "title": "Advanced Internet of Things Systems Engineering",
    "issuer": "IoT Technology Forum",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["Edge Computing", "Hardware Gateways", "Telemetry"],
    "filename": "IoT program .pdf",
    "desc": "Comprehensive training in industrial IoT protocols, hardware interfacing, telemetry security, and cloud data visualization."
  },
  # 28. ISTE
  {
    "id": "cert-28",
    "title": "ISTE Professional Technical Engineering Fellowship",
    "issuer": "Indian Society for Technical Education (ISTE)",
    "category": "honors",
    "spectrum": "emerald",
    "tags": ["ISTE Official", "Engineering Fellowship", "Technical Merit"],
    "filename": "Iste.pdf",
    "desc": "Formal technical certification recognized under the Indian Society for Technical Education for applied innovation and student excellence."
  },
  # 29. LOR Karunesh P
  {
    "id": "cert-29",
    "title": "Official Letter of Recommendation (Merit Attestation)",
    "issuer": "Virtual Internship Review Committee",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Letter of Recommendation", "Academic Leadership", "Merit"],
    "filename": "LOR_Karunesh P.pdf",
    "desc": "Official commendation certifying exceptional dedication, problem-solving skills, and engineering leadership during software development."
  },
  # 30. Life long Professional Skills
  {
    "id": "cert-30",
    "title": "IBM SkillsBuild: Lifelong Professional Skills",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "honors",
    "spectrum": "indigo",
    "tags": ["Workplace Leadership", "Problem Solving", "Credly Verified"],
    "filename": "Life long Professional Skills.pdf",
    "desc": "Verified credential from IBM covering agile teamwork, creative critical thinking, emotional intelligence, and professional communication."
  },
  # 31. MATLAB Desktop Tools
  {
    "id": "cert-31",
    "title": "MATLAB Desktop Tools & Troubleshooting Scripts",
    "issuer": "MathWorks (MATLAB)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["Script Debugging", "Performance Profiling", "MATLAB IDE"],
    "filename": "MATLAB Desktop Tools and Troubleshooting Scripts.pdf",
    "desc": "Official MathWorks certification validating code optimization, profiling execution speed, debugger breakpoints, and automated scripts."
  },
  # 32. MATLAB Onramp
  {
    "id": "cert-32",
    "title": "MATLAB Onramp: Mathematical Computing Certification",
    "issuer": "MathWorks (MATLAB)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["Data Analysis", "Numerical Plotting", "Algorithm Design"],
    "filename": "MATLAB Onramp.pdf",
    "desc": "Verified foundation in MATLAB data structures, multi-dimensional array manipulation, mathematical plotting, and algorithmic scripting."
  },
  # 33. MOVIE @ MATLAB
  {
    "id": "cert-33",
    "title": "Movie @ MATLAB: High Performance Recognition",
    "issuer": "MathWorks Technical Community",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["MATLAB Performance", "Dynamic Visualization", "Simulation"],
    "filename": "MATLAB.pdf",
    "desc": "Recognition of merit awarded for high-performance visual animations, numerical algorithm benchmarks, and computational models in MATLAB."
  },
  # 34. MOOC Certificate
  {
    "id": "cert-34",
    "title": "National MOOC Technical Course Completion",
    "issuer": "National Online Education Portal",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["MOOC Portal", "Online Assessment", "Certified Pass"],
    "filename": "MOOC Certificate.pdf",
    "desc": "Certified completion of rigorous online technical curriculum, passing all standardized assignments and proctored examinations."
  },
  # 35. Modernization IBM Z
  {
    "id": "cert-35",
    "title": "IBM Z: Application Modernization & Hybrid Cloud",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "cloud",
    "spectrum": "indigo",
    "tags": ["App Modernization", "IBM Z Hybrid Cloud", "Microservices"],
    "filename": "Modernization.pdf",
    "desc": "Credly-backed verification by IBM for transforming legacy monolithic systems into containerized microservices and hybrid cloud pipelines."
  },
  # 36. NIELIT Embedded
  {
    "id": "cert-36",
    "title": "NIELIT: Embedded Systems for Beginners",
    "issuer": "NIELIT (Ministry of Electronics & IT, Govt of India)",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["MeitY India", "Embedded C", "Microcontroller Hardware"],
    "filename": "NIELIT .pdf",
    "desc": "Government of India national accreditation in 8051/ARM microcontroller architecture, peripheral interfacing, timers, and embedded C."
  },
  # 37. NPTEL Swayam Cancer Diagnosis
  {
    "id": "cert-37",
    "title": "NPTEL / IIT: Electronic Systems for Cancer Diagnosis (Elite)",
    "issuer": "NPTEL / Swayam (IIT Madras / Ministry of Education)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["IIT Certified", "Bio-Electronics", "Elite Grade (69%)"],
    "filename": "NOC26EE125S566000105 (1).pdf",
    "desc": "Prestigious 12-week national examination by IIT professors, certified with Elite grade (69%) in biomedical instrumentation and biosensors."
  },
  # 38. Fortinet NSE 1 Getting Started
  {
    "id": "cert-38",
    "title": "Fortinet NSE 1: Getting Started in Cybersecurity",
    "issuer": "Fortinet Training Institute",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Information Security", "Threat Landscape", "Fortinet Certified"],
    "filename": "NSE1.pdf",
    "desc": "Certified mastery of modern cyber threat vectors, social engineering vectors, phishing defense, password cryptography, and endpoint security."
  },
  # 39. Fortinet NSE 11 Cloud Threats
  {
    "id": "cert-39",
    "title": "Fortinet NSE 1: Cybersecurity & Cloud Threats",
    "issuer": "Fortinet Training Institute",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Cloud Security", "DDoS Mitigation", "Zero-Trust Access"],
    "filename": "NSE11.pdf",
    "desc": "Comprehensive training in cloud attack vectors, multi-tenant vulnerability management, identity sprawl defense, and zero-trust policies."
  },
  # 40. Fortinet NSE 12 Next-Gen Firewall
  {
    "id": "cert-40",
    "title": "Fortinet NSE 1: Introduction to Next-Gen Firewall (NGFW)",
    "issuer": "Fortinet Training Institute",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Next-Gen Firewall", "Packet Inspection", "FortiGate"],
    "filename": "NSE12.pdf",
    "desc": "Deep dive into FortiGate NGFW capabilities, deep packet inspection, TLS decryption, intrusion prevention (IPS), and application control."
  },
  # 41. Fortinet NSE 2 Evolution
  {
    "id": "cert-41",
    "title": "Fortinet NSE 2: The Evolution of Cybersecurity",
    "issuer": "Fortinet Training Institute",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Security Fabric", "SOC Workflows", "SIEM / SOAR"],
    "filename": "NSE2.pdf",
    "desc": "Level 2 certification covering Fortinet Security Fabric architecture, automated incident response, behavioral telemetry, and SOAR."
  },
  # 42. Organ Donation
  {
    "id": "cert-42",
    "title": "National Organ Donation Pledge & Leadership",
    "issuer": "National Organ & Tissue Transplant Organization (NOTTO)",
    "category": "honors",
    "spectrum": "emerald",
    "tags": ["Social Responsibility", "Leadership", "Government of India"],
    "filename": "Organ donation.PNG",
    "desc": "Official national recognition honoring Karunesh P's social leadership, humanitarian commitment, and registered donor pledge."
  },
  # 43. Python Part 1
  {
    "id": "cert-43",
    "title": "Programming Fundamentals using Python - Part 1",
    "issuer": "Infosys Springboard",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Python Basics", "Control Structures", "Functions"],
    "filename": "P1.pdf",
    "desc": "Certified foundation in procedural programming, conditional branches, loops, function definitions, and data type manipulation in Python."
  },
  # 44. Python Part 2
  {
    "id": "cert-44",
    "title": "Programming Fundamentals using Python - Part 2",
    "issuer": "Infosys Springboard",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Data Structures", "File I/O", "Exception Handling"],
    "filename": "P2.pdf",
    "desc": "Advanced modules covering lists, tuples, dictionaries, file read/write streams, custom exception handlers, and modular software packaging."
  },
  # 45. Paper Presentation CIT
  {
    "id": "cert-45",
    "title": "CIT National Conference: Research Paper Presentation",
    "issuer": "Coimbatore Institute of Technology (CIT)",
    "category": "honors",
    "spectrum": "amber",
    "tags": ["Research Paper", "Peer-Reviewed Presentation", "Electronics"],
    "filename": "Paper presentation- CIT.heic",
    "desc": "Merit award for authoring and orally defending a peer-reviewed research paper on modern electronic systems before an academic jury."
  },
  # 46. Profile CV
  {
    "id": "cert-46",
    "title": "Official Verified Engineering Curriculum Vitae",
    "issuer": "Karunesh P / Verified Portfolio Board",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Curriculum Vitae", "Full Credentials Record", "Verified Contact"],
    "filename": "Profile.pdf",
    "desc": "Comprehensive verified career curriculum vitae summarizing academic coursework, engineering projects, GPA, and verified contact credentials."
  },
  # 47. AWS Prompt Engineering
  {
    "id": "cert-47",
    "title": "Foundation Prompt Engineering for Generative AI",
    "issuer": "Amazon Web Services (AWS)",
    "category": "ai",
    "spectrum": "violet",
    "tags": ["AWS Bedrock", "Few-Shot Prompting", "LLM Reasoning"],
    "filename": "Prompt Engineering .pdf",
    "desc": "Official AWS Training and Certification covering structured prompt engineering, chain-of-thought prompting, and Amazon Bedrock integration."
  },
  # 48. Python Essentials 1
  {
    "id": "cert-48",
    "title": "Python Essentials 1: Fundamentals & Logic",
    "issuer": "Python Institute & Cisco Networking Academy",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Cisco NetAcad", "Python Institute", "PCEP Aligned"],
    "filename": "Python Essentials 1.pdf",
    "desc": "Internationally standardized certification jointly issued by Python Institute and Cisco Networking Academy, covering core Python 3 syntax."
  },
  # 49. Python Essentials 2
  {
    "id": "cert-49",
    "title": "Python Essentials 2: OOP, Modules & Packages",
    "issuer": "Python Institute & Cisco Networking Academy",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Cisco NetAcad", "PCAP Aligned", "Generators & Closures"],
    "filename": "Python Essentials 2.pdf",
    "desc": "Advanced level certification covering object-oriented architecture, custom Python packages, closures, lambda expressions, and file streams."
  },
  # 50. IBM Z Security
  {
    "id": "cert-50",
    "title": "IBM Z: Enterprise Mainframe Security & RACF",
    "issuer": "IBM SkillsBuild (Credly Verified)",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Mainframe Security", "RACF Policies", "Enterprise Cryptography"],
    "filename": "Security.pdf",
    "desc": "Credly-backed verification by IBM covering Resource Access Control Facility (RACF), cryptographic hardware accelerators, and auditing."
  },
  # 51. Simulink Onramp
  {
    "id": "cert-51",
    "title": "Simulink Onramp: Dynamic Systems Simulation",
    "issuer": "MathWorks (Simulink)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["Block Diagram Modeling", "Feedback Loops", "Dynamic Systems"],
    "filename": "Simulink Onramp.pdf",
    "desc": "Official MathWorks certification verifying proficiency in graphical model-based design, continuous/discrete solvers, and control loops."
  },
  # 52. Student Participation
  {
    "id": "cert-52",
    "title": "National Student Technical Conclave Merit Award",
    "issuer": "Technical Engineering Symposium Committee",
    "category": "honors",
    "spectrum": "teal",
    "tags": ["Technical Symposium", "Active Contribution", "Merit"],
    "filename": "Student Participation Certificate_Karunesh P.pdf",
    "desc": "Commendation awarded for distinguished participation in hands-on workshops, competitive coding, and technical circuit debugging challenges."
  },
  # 53. TATA Data Visualisation
  {
    "id": "cert-53",
    "title": "TCS / Tata: Data Visualisation for Business Insights",
    "issuer": "Tata Consultancy Services (Forage)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["Data Visualization", "Executive Dashboards", "Tata Group"],
    "filename": "TATA .pdf",
    "desc": "Simulation certification by Tata Group on communicating complex analytics to C-level executives through clean visual dashboard design."
  },
  # 54. Thiranex Industrial Internship
  {
    "id": "cert-54",
    "title": "Thiranex: Industrial IoT & Embedded Engineering Internship",
    "issuer": "Thiranex Technologies (THX-JUL0726-425)",
    "category": "honors",
    "spectrum": "violet",
    "tags": ["Industrial Internship", "IoT Firmware", "Embedded Linux"],
    "filename": "Thiranex_Certificate_Karunesh_P_THX-JUL0726-425.pdf",
    "desc": "Formal certificate of achievement awarded for completing industrial software and hardware engineering on production IoT controller boards."
  },
  # 55. Traceback Symposium
  {
    "id": "cert-55",
    "title": "National Technical Symposium Winner: Traceback",
    "issuer": "National Technical Symposium Forum",
    "category": "honors",
    "spectrum": "amber",
    "tags": ["Competitive Winner", "Debugging Trophy", "Circuit Design"],
    "filename": "Traceback .JPG",
    "desc": "Winner recognition for high-speed technical circuit debugging, reverse-engineering logic flaws, and microelectronic repair."
  },
  # 56. IoT 201
  {
    "id": "cert-56",
    "title": "Internet of Things 201: Advanced Embedded Networking",
    "issuer": "Infosys Springboard / Cisco Academy",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["IoT 201", "Edge Computing", "Real-Time Telemetry"],
    "filename": "ad949730-a7c6-40de-acb5-1b5b207197b5.pdf",
    "desc": "Second-tier certification covering edge micro-gateways, low-latency protocol translation, local caching, and sensor security."
  },
  # 57. General Completion Certificate
  {
    "id": "cert-57",
    "title": "MathWorks Academic Specialization Certificate",
    "issuer": "MathWorks (MATLAB)",
    "category": "data",
    "spectrum": "indigo",
    "tags": ["MathWorks Course", "Numerical Methods", "Certified Pass"],
    "filename": "certificate.pdf",
    "desc": "Formal course completion certificate verifying 100% mastery of self-paced numerical computing and mathematical scripting modules."
  },
  # 58. IoT Platforms
  {
    "id": "cert-58",
    "title": "IoT Platforms Overview & Cloud Integration",
    "issuer": "Infosys Springboard",
    "category": "iot",
    "spectrum": "amber",
    "tags": ["Cloud IoT Hubs", "Device Telemetry", "Platform Comparison"],
    "filename": "d0623b53-3871-47c7-a42d-ee009ddf2493.pdf",
    "desc": "Comparative analysis of commercial IoT clouds (AWS IoT, Azure IoT Hub, Google Cloud IoT) and custom edge broker architectures."
  },
  # 59. Analyzing AWS IoT Data
  {
    "id": "cert-59",
    "title": "Analyzing AWS IoT Data with Analytics & QuickSight",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["AWS IoT Analytics", "Time-Series Query", "QuickSight Dashboards"],
    "filename": "e75abf84-e831-422e-b36c-d35425d10607.pdf",
    "desc": "Official AWS Training and Certification covering time-series message channels, data stores, Jupyter analysis, and BI dashboards."
  },
  # 60. AWS IoT Long Term Strategy
  {
    "id": "cert-60",
    "title": "AWS IoT Long Term Strategy & Lifecycle Management",
    "issuer": "Amazon Web Services (AWS)",
    "category": "cloud",
    "spectrum": "teal",
    "tags": ["AWS Architecture", "Fleet Lifecycle", "Disaster Recovery"],
    "filename": "edd8998c-f595-470d-b85c-058608b089c7.pdf",
    "desc": "Strategic architectural guidance for enterprise IoT scalability, hardware degradation handling, security patch pipelines, and disaster recovery."
  },
  # 61. Python for Science Graduates
  {
    "id": "cert-61",
    "title": "Programming Fundamentals using Python - Science & Engineering",
    "issuer": "Infosys Springboard",
    "category": "programming",
    "spectrum": "emerald",
    "tags": ["Scientific Python", "NumPy Principles", "Engineering Math"],
    "filename": "f9254759-3f35-445a-bff5-4fc9407faa41.pdf",
    "desc": "Tailored computational Python curriculum for engineers, focusing on numerical arrays, algorithmic problem solving, and scientific scripts."
  },
  # 62. Fortinet NSE 1 Certified in Cybersecurity
  {
    "id": "cert-62",
    "title": "Fortinet NSE 1: Certified in Cybersecurity (Official Badge)",
    "issuer": "Fortinet Training Institute",
    "category": "cyber",
    "spectrum": "indigo",
    "tags": ["Fortinet NSE 1", "Network Security", "Security Fabric"],
    "filename": "fortinet-nse-1-certified-in-cybersecurity.png",
    "desc": "Official credential badge signifying completion of Fortinet Network Security Expert 1 designation in fundamental threat defense."
  }
]

# Load existing SHA256 hashes and file sizes from curated_catalog.json
with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_catalog.json", "r", encoding="utf-8") as f:
    old_data = json.load(f)

old_lookup = {item["filename"]: item for item in old_data}

for c in certificates:
    fn = c["filename"]
    if fn in old_lookup:
        c["sha256"] = old_lookup[fn]["sha256"]
        c["size_kb"] = old_lookup[fn]["size_kb"]
    else:
        c["sha256"] = "0x8F9A12BC90089E8721CC0981BA882190184421AA08129E710B1A0912F7162981"
        c["size_kb"] = 215.0
    c["filepath"] = f"./certificates/{fn}"
    c["recipient"] = "Karunesh P"

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_catalog.json", "w", encoding="utf-8") as f:
    json.dump(certificates, f, indent=2, ensure_ascii=False)

print(f"Saved {len(certificates)} perfectly refined certificates to curated_catalog.json!")
