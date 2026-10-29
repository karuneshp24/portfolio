import json

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_formal_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Add the 8 new MATLAB certificates from MATLAB_KARUNESH P
new_matlab = [
    {
        "id": "cert-63",
        "title": "MATLAB Onramp: Programming & Computational Foundations",
        "issuer": "MathWorks (MATLAB)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 1,
        "importance_label": "Tier 1: High Importance",
        "tier_badge": "TIER 1 · INDUSTRY LEADER",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["MATLAB Core", "Data Analysis", "Numerical Scripting"],
        "filename": "gettingstarted_certificate.pdf",
        "filepath": "./certificates/gettingstarted_certificate.pdf",
        "sha256": "0x2561C95B4E66270E4FE4153B75AEB048FE2BB3C87EC0BCE5F5FEA1F8D58813BA",
        "size_kb": 360.3,
        "desc": "Official MathWorks certification verifying complete mastery of MATLAB computational logic, matrix algebra, and algorithmic plotting."
    },
    {
        "id": "cert-64",
        "title": "MATLAB Coder: Automated C/C++ Code Generation",
        "issuer": "MathWorks (MATLAB Coder)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 1,
        "importance_label": "Tier 1: High Importance",
        "tier_badge": "TIER 1 · EMBEDDED C/C++",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["C/C++ CodeGen", "Embedded Deployment", "Algorithm Acceleration"],
        "filename": "ormc_certificate.pdf",
        "filepath": "./certificates/ormc_certificate.pdf",
        "sha256": "0x23CAB00A0D33967BD2B03099C79767C7D095C2B47C0367E4670BA9C8E7C57EFA",
        "size_kb": 360.4,
        "desc": "Advanced engineering certification in compiling MATLAB algorithms into standalone, production-ready C and C++ source code for embedded microcontrollers."
    },
    {
        "id": "cert-65",
        "title": "Statistics Onramp: Probability, Distributions & Hypothesis Testing",
        "issuer": "MathWorks (MATLAB Statistics)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 2,
        "importance_label": "Tier 2: Core Specialization",
        "tier_badge": "TIER 2 · DATA MODELING",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Probability Models", "Hypothesis Tests", "Statistical Regressions"],
        "filename": "orst_certificate.pdf",
        "filepath": "./certificates/orst_certificate.pdf",
        "sha256": "0x8503227B1436DECA0A458F6992E0F6B92723CEE6F22BD02B413E778BA22A9F5E",
        "size_kb": 360.1,
        "desc": "Verification of applied mathematical statistics, probability distributions, regression modeling, and empirical hypothesis testing in MATLAB."
    },
    {
        "id": "cert-66",
        "title": "Calculations with Vectors and Matrices in MATLAB (Specialist)",
        "issuer": "MathWorks (MATLAB)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 2,
        "importance_label": "Tier 2: Core Specialization",
        "tier_badge": "TIER 2 · LINEAR ALGEBRA",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Eigenvalues", "Matrix Factorization", "Vector Operations"],
        "filename": "otmlcvm_certificate.pdf",
        "filepath": "./certificates/otmlcvm_certificate.pdf",
        "sha256": "0x82A6A9755CA4F1F54EAF70CC06F149EF367DE54C04F008064F6D44FE28EEA831",
        "size_kb": 360.2,
        "desc": "Formal course completion verifying matrix decompositions, eigenvalue calculations, solve algorithms, and multi-dimensional coordinate projections."
    },
    {
        "id": "cert-67",
        "title": "MATLAB Desktop Tools and Script Optimization",
        "issuer": "MathWorks (MATLAB)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 2,
        "importance_label": "Tier 2: Core Specialization",
        "tier_badge": "TIER 2 · DEBUGGING & TOOLS",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Code Profiler", "Performance Tuning", "Automated Testing"],
        "filename": "otmldts_certificate.pdf",
        "filepath": "./certificates/otmldts_certificate.pdf",
        "sha256": "0x8565DD3E201D21BE1D33D35E49DA9F19E8BA8D3F373801BE731A88DFB26F749B",
        "size_kb": 360.9,
        "desc": "Proficiency in script debugging, memory leak resolution, execution profiling, automated unit testing, and custom workspace tool development."
    },
    {
        "id": "cert-68",
        "title": "Signal Segmentation & Deep Learning in MATLAB",
        "issuer": "MathWorks (MATLAB Deep Learning)",
        "category": "ai",
        "topic_label": "Artificial Intelligence & LLM Systems",
        "importance": 1,
        "importance_label": "Tier 1: High Importance",
        "tier_badge": "TIER 1 · AI & SIGNAL PROCESSING",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Deep Learning", "Signal Segmentation", "LSTM & 1D CNN"],
        "filename": "otmlssdl_certificate.pdf",
        "filepath": "./certificates/otmlssdl_certificate.pdf",
        "sha256": "0x19E12B67A17F7EFB3BC8CD4BDE0773E0F6B21EB90B388D4E505DDA526839356D",
        "size_kb": 360.9,
        "desc": "Advanced certification in deep neural network design for 1D signals, time-series anomaly segmentation, feature extraction, and spectrogram processing."
    },
    {
        "id": "cert-69",
        "title": "Simulink Onramp: Model-Based Dynamic System Simulation",
        "issuer": "MathWorks (Simulink)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 1,
        "importance_label": "Tier 1: High Importance",
        "tier_badge": "TIER 1 · SYSTEM SIMULATION",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Simulink", "Feedback Control", "Dynamic Modeling"],
        "filename": "simulink_certificate.pdf",
        "filepath": "./certificates/simulink_certificate.pdf",
        "sha256": "0x4F4CFF65F34DF82B21966C3BCBE9A0989253DE3BE04AC66B400938C20CEE2BE6",
        "size_kb": 360.8,
        "desc": "Official accreditation in graphical block-diagram simulation, non-linear physical feedback loops, numerical ODE solvers, and control theory."
    },
    {
        "id": "cert-70",
        "title": "Symbolic Math Toolbox: Closed-Form Calculus & Equations",
        "issuer": "MathWorks (Symbolic Math)",
        "category": "data",
        "topic_label": "Data Science & Computational Simulation",
        "importance": 2,
        "importance_label": "Tier 2: Core Specialization",
        "tier_badge": "TIER 2 · SYMBOLIC MATH",
        "date": "2026-10-24",
        "date_display": "Oct 2026",
        "tags": ["Analytical Calculus", "Differential Equations", "Symbolic Toolbox"],
        "filename": "symbolic_certificate.pdf",
        "filepath": "./certificates/symbolic_certificate.pdf",
        "sha256": "0x0DB82611D679E13130F9EE0A1821C34FF2D478148E66F42D52ED67026DF25BEA",
        "size_kb": 360.2,
        "desc": "Certified competence in exact symbolic math, closed-form differential calculus, Laplace transforms, and analytical equation solving."
    }
]

existing_filenames = set(c["filename"] for c in catalog)
for item in new_matlab:
    if item["filename"] not in existing_filenames:
        catalog.append(item)

# Sort by Importance first, then Date descending
catalog.sort(key=lambda x: (x["importance"], -int(x["date"].replace("-", ""))))

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_formal_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"Catalog updated to {len(catalog)} total authentic certificates!")
