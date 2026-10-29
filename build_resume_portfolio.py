import json

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_formal_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

json_str = json.dumps(catalog, indent=2, ensure_ascii=False)

html_code = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Karunesh P — Systems & Embedded Intelligence Engineer | Official Dossier</title>
  
  <!-- Professional Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'system-ui', 'sans-serif'],
            display: ['Space Grotesk', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }},
          colors: {{
            corporate: {{
              950: '#070f26',
              900: '#0b1636',
              850: '#0f1f4a',
              800: '#152b66',
              700: '#1d3b8a',
            }},
            blue: {{
              500: '#3b82f6',
              600: '#2563eb',
              700: '#1d4ed8',
              800: '#1e40af',
              900: '#1e3a8a',
              950: '#172554',
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    * {{
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    body {{
      background-color: #070f26;
      color: #e2e8f0;
      font-family: 'Inter', sans-serif;
    }}

    /* Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #070f26;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e3a8a;
      border-radius: 9999px;
    }}

    /* Standard Blue Cards */
    .formal-card {{
      background: linear-gradient(180deg, rgba(15, 31, 74, 0.9) 0%, rgba(11, 22, 54, 0.95) 100%);
      border: 1px solid rgba(59, 130, 246, 0.2);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .formal-card:hover {{
      border-color: rgba(96, 165, 250, 0.6);
      transform: translateY(-3px);
      box-shadow: 0 14px 35px -10px rgba(0, 0, 0, 0.8), 0 0 20px -3px rgba(37, 99, 235, 0.25);
    }}

    .tier-badge-1 {{
      background: rgba(217, 119, 6, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }}
    .tier-badge-2 {{
      background: rgba(37, 99, 235, 0.2);
      border: 1px solid rgba(96, 165, 250, 0.4);
      color: #93c5fd;
    }}
    .tier-badge-3 {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: #6ee7b7;
    }}

    .modal-backdrop {{
      background: rgba(3, 7, 18, 0.88);
      backdrop-filter: blur(16px);
    }}

    .screen-fade {{
      animation: fadeIn 0.35s ease-in-out;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Print Styles */
    @media print {{
      body {{
        background: #ffffff !important;
        color: #000000 !important;
      }}
      header, .no-print {{
        display: none !important;
      }}
      #screenResume, #screenDossier {{
        display: block !important;
      }}
      table {{
        color: #000000 !important;
        border-collapse: collapse !important;
        width: 100% !important;
      }}
      th, td {{
        border: 1px solid #cccccc !important;
        padding: 6px !important;
        color: #000000 !important;
      }}
    }}
  </style>
</head>

<body class="min-h-screen flex flex-col antialiased selection:bg-blue-600/30 selection:text-white">

  <!-- TOP PERMANENT NAVIGATION BAR -->
  <header class="border-b border-blue-900/50 bg-corporate-950/90 backdrop-blur-md sticky top-0 z-40 px-4 sm:px-8 py-3.5 no-print">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Profile Branding -->
      <div class="flex items-center gap-3.5">
        <img src="./karunesh_avatar.jpg" alt="Karunesh P" class="w-11 h-11 rounded-xl object-cover border border-blue-400/40 shadow-md">
        <div>
          <div class="flex items-center gap-2">
            <h1 class="font-display font-extrabold text-lg text-white tracking-tight">KARUNESH P</h1>
            <span class="px-2 py-0.5 rounded-full bg-blue-950 border border-blue-500/40 text-blue-300 font-mono text-[10px] font-semibold tracking-wider">
              OFFICIAL ATTESTATION
            </span>
          </div>
          <p class="text-[11px] font-mono text-slate-400">Systems & Embedded Intelligence Engineer · KPRIET</p>
        </div>
      </div>

      <!-- Navigation Screen Tabs (Resume vs Credentials) -->
      <div class="flex items-center gap-3">
        <div class="flex items-center p-1 rounded-xl bg-corporate-900 border border-blue-900/60 shadow-inner">
          <button id="navBtnResume" onclick="showScreen('resume')" class="px-4 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all bg-blue-600 text-white shadow-sm flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Executive Resume</span>
          </button>
          
          <button id="navBtnDossier" onclick="showScreen('dossier')" class="px-4 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all text-slate-400 hover:text-white flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            <span>Credentials Dossier (70)</span>
          </button>
        </div>

        <!-- Direct LinkedIn Button -->
        <a href="https://www.linkedin.com/in/karunesh-p-4b4b1a381" target="_blank" class="px-3.5 py-1.5 rounded-xl bg-[#0a66c2] hover:bg-[#004182] text-white text-xs font-mono font-semibold transition-colors flex items-center gap-1.5 shadow-sm" title="View Official LinkedIn Profile">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          <span class="hidden sm:inline">LinkedIn</span>
        </a>

        <!-- Print -->
        <button onclick="window.print()" class="p-2 rounded-xl bg-corporate-900 hover:bg-corporate-850 border border-blue-900/60 text-slate-300 hover:text-white transition-colors" title="Print Formal Resume / Transcript">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        </button>
      </div>

    </div>
  </header>

  <!-- =========================================================================
       SCREEN 1 (FRONT PAGE): EXECUTIVE RESUME & TECHNICAL PROFILE
       ========================================================================= -->
  <section id="screenResume" class="screen-fade max-w-5xl mx-auto w-full px-4 sm:px-8 py-8 flex flex-col gap-8">

    <!-- RESUME HEADER CARD -->
    <div class="rounded-3xl p-6 sm:p-10 formal-card shadow-2xl relative overflow-hidden">
      <div class="absolute right-0 top-0 w-80 h-80 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>

      <div class="relative z-10 flex flex-col sm:flex-row items-start sm:items-center gap-6 pb-6 border-b border-blue-900/40">
        <!-- Photo -->
        <div class="relative shrink-0">
          <img src="./karunesh_photo.jpg" alt="Karunesh P" class="w-28 h-36 sm:w-32 sm:h-40 rounded-2xl object-cover border-2 border-blue-500/40 shadow-xl">
          <span class="absolute -bottom-2 -right-2 px-2 py-0.5 rounded-full bg-emerald-950 border border-emerald-500/40 text-emerald-300 text-[10px] font-mono font-bold">
            AVAILABLE
          </span>
        </div>

        <!-- Info -->
        <div class="flex-1 space-y-2">
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-xs font-mono uppercase tracking-wider text-blue-400 font-semibold">CANDIDATE CURRICULUM VITAE</span>
            <span class="text-slate-500">•</span>
            <span class="text-xs font-mono text-emerald-400 font-medium">B.E. ECE (2025–2029)</span>
          </div>

          <h2 class="text-3xl sm:text-4xl font-display font-extrabold text-white tracking-tight">
            KARUNESH P
          </h2>
          <p class="text-base text-blue-200 font-medium font-sans">
            Systems & Embedded Intelligence Engineer · KPR Institute of Engineering and Technology
          </p>

          <!-- Contact Coordinates -->
          <div class="pt-2 flex flex-wrap items-center gap-y-2 gap-x-5 text-xs font-mono text-slate-300">
            <span class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              karuneshp2007@gmail.com
            </span>
            <span class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              +91 8220480281
            </span>
            <span class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Coimbatore / Theni, Tamil Nadu
            </span>
            <a href="https://www.linkedin.com/in/karunesh-p-4b4b1a381" target="_blank" class="text-blue-400 hover:text-white flex items-center gap-1 underline">
              linkedin.com/in/karunesh-p-4b4b1a381
            </a>
          </div>
        </div>
      </div>

      <!-- Quick Metrics Counter -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-6 font-mono text-center">
        <div class="p-3 rounded-xl bg-corporate-950/80 border border-blue-900/40">
          <div class="text-2xl font-extrabold text-blue-400">70</div>
          <div class="text-[11px] text-slate-400 uppercase font-semibold mt-0.5">Verified Documents</div>
        </div>
        <div class="p-3 rounded-xl bg-corporate-950/80 border border-blue-900/40">
          <div class="text-2xl font-extrabold text-amber-400">28</div>
          <div class="text-[11px] text-slate-400 uppercase font-semibold mt-0.5">Tier 1 Flagship</div>
        </div>
        <div class="p-3 rounded-xl bg-corporate-950/80 border border-blue-900/40">
          <div class="text-2xl font-extrabold text-emerald-400">14</div>
          <div class="text-[11px] text-slate-400 uppercase font-semibold mt-0.5">Global Issuers</div>
        </div>
        <div class="p-3 rounded-xl bg-corporate-950/80 border border-blue-900/40">
          <div class="text-2xl font-extrabold text-white">100%</div>
          <div class="text-[11px] text-slate-400 uppercase font-semibold mt-0.5">Cryptographic Integrity</div>
        </div>
      </div>

    </div>

    <!-- EXECUTIVE INTRODUCTION / SUMMARY -->
    <div class="rounded-3xl p-6 sm:p-8 formal-card space-y-4">
      <div class="flex items-center gap-2 pb-2 border-b border-blue-900/40">
        <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
        <h3 class="font-display font-extrabold text-lg text-white uppercase tracking-wider">
          Executive Engineering Summary
        </h3>
      </div>
      
      <div class="text-sm text-slate-300 font-sans leading-relaxed space-y-3 font-light">
        <p>
          I am an engineering undergraduate specializing in <strong>Electronics and Communication Engineering</strong> at <strong>KPR Institute of Engineering and Technology (KPRIET)</strong>, Coimbatore. Driven by architectural precision and curiosity, my technical work bridges the physical and computational realms—spanning <strong>deep learning neural networks, multi-layer printed circuit board (PCB) design, dynamic system simulation in MATLAB & Simulink, secure cloud IoT infrastructure, and network cybersecurity</strong>.
        </p>
        <p>
          Holding <strong>70 cryptographically verified accreditations</strong> from industry-defining institutions—including <strong>Amazon Web Services (AWS), IBM SkillsBuild, MathWorks, Microsoft, Cisco Networking Academy, Fortinet, NIELIT (Govt of India), and NPTEL / IIT</strong>—I bring a disciplined engineering approach to solving mission-critical hardware-software integration challenges.
        </p>
        <p>
          My practical engineering track record includes authoring research at national symposiums, developing embedded firmware during industrial internships at <strong>Thiranex Technologies</strong>, winning prize honors at the <strong>CIT National Hackathon</strong>, and achieving an <strong>Elite Grade</strong> in IIT NPTEL’s examination on Electronic Systems for Biomedical Applications.
        </p>
      </div>
    </div>

    <!-- TWO-COLUMN EDUCATION & EXPERIENCE DECK -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- EDUCATION -->
      <div class="rounded-3xl p-6 formal-card space-y-5">
        <div class="flex items-center gap-2 pb-2 border-b border-blue-900/40">
          <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
          <h3 class="font-display font-extrabold text-base text-white uppercase tracking-wider font-mono">
            Education
          </h3>
        </div>

        <div class="space-y-4 font-sans">
          <div class="relative pl-4 border-l-2 border-blue-600">
            <span class="text-xs font-mono text-blue-400 font-semibold">2025 — 2029 (CURRENT)</span>
            <h4 class="font-bold text-white text-base mt-0.5">Bachelor of Engineering (B.E.)</h4>
            <div class="text-xs font-medium text-slate-300">Electronics and Communication Engineering</div>
            <div class="text-xs text-slate-400 mt-1">KPR Institute of Engineering and Technology (KPRIET), Coimbatore</div>
          </div>

          <div class="relative pl-4 border-l-2 border-slate-700">
            <span class="text-xs font-mono text-slate-400 font-semibold">2021 — 2025</span>
            <h4 class="font-bold text-white text-base mt-0.5">Higher Secondary & Secondary Education</h4>
            <div class="text-xs text-slate-300">Mary Matha CMI Public School</div>
            <div class="text-xs text-slate-400 mt-1">Distinction in Mathematics, Physics & Computer Science</div>
          </div>
        </div>
      </div>

      <!-- KEY PRACTICAL EXPERIENCE -->
      <div class="rounded-3xl p-6 formal-card space-y-5">
        <div class="flex items-center gap-2 pb-2 border-b border-blue-900/40">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
          <h3 class="font-display font-extrabold text-base text-white uppercase tracking-wider font-mono">
            Practical Engineering Experience
          </h3>
        </div>

        <div class="space-y-4 font-sans text-xs">
          <div class="relative pl-4 border-l-2 border-emerald-600">
            <span class="font-mono text-emerald-400 font-semibold">THIRANEX TECHNOLOGIES · JUL 2026</span>
            <h4 class="font-bold text-white text-sm mt-0.5">Industrial IoT & Embedded Engineering Intern</h4>
            <p class="text-slate-400 mt-0.5">Developed embedded sensor telemetry modules, configured hardware gateways, and validated industrial board firmware.</p>
          </div>

          <div class="relative pl-4 border-l-2 border-blue-600">
            <span class="font-mono text-blue-400 font-semibold">CODEALPHA SOFTWARE LAB · JUL 2026</span>
            <h4 class="font-bold text-white text-sm mt-0.5">Software Engineering Virtual Intern</h4>
            <p class="text-slate-400 mt-0.5">Implemented algorithmic Python modules, data structures, and object-oriented architectures.</p>
          </div>

          <div class="relative pl-4 border-l-2 border-amber-600">
            <span class="font-mono text-amber-400 font-semibold">CIT NATIONAL HACKATHON · FEB 2026</span>
            <h4 class="font-bold text-white text-sm mt-0.5">Innovation Prize Winner</h4>
            <p class="text-slate-400 mt-0.5">Awarded innovation honors at Coimbatore Institute of Technology for designing end-to-end intelligent physical prototypes.</p>
          </div>
        </div>
      </div>

    </div>

    <!-- CORE COMPETENCY & TECHNICAL SKILLS MATRIX -->
    <div class="rounded-3xl p-6 sm:p-8 formal-card space-y-5">
      <div class="flex items-center gap-2 pb-2 border-b border-blue-900/40">
        <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
        <h3 class="font-display font-extrabold text-lg text-white uppercase tracking-wider">
          Core Technical Skills & Tooling Architecture
        </h3>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 font-mono text-xs">
        
        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-blue-400 font-bold uppercase flex items-center gap-1.5">
            <span>🧠</span> AI & Deep Learning
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Neural Networks</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Signal Segmentation</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Prompt Engineering</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">IBM Watson</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Vertex AI Studio</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-amber-400 font-bold uppercase flex items-center gap-1.5">
            <span>⚡</span> Embedded & PCB Hardware
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Altium Designer</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Multi-Layer PCB</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Arduino TinyML</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">NIELIT MeitY Govt</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Microcontrollers</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-blue-400 font-bold uppercase flex items-center gap-1.5">
            <span>📊</span> MATLAB & Dynamic Simulation
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">MATLAB Coder C/C++</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Simulink Onramp</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Symbolic Math</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Linear Algebra</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Statistics Toolbox</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-cyan-400 font-bold uppercase flex items-center gap-1.5">
            <span>☁️</span> Cloud Architecture & IoT
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">AWS IoT Core</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Device Management</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">QuickSight Analytics</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">IBM Z Systems</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">MQTT Protocols</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-indigo-400 font-bold uppercase flex items-center gap-1.5">
            <span>🛡️</span> Cybersecurity & Network
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Fortinet NSE 1</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Fortinet NSE 2</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Next-Gen Firewalls</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Cloud Threat Hunting</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Zero-Trust Models</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-corporate-950/70 border border-blue-900/40 space-y-2">
          <div class="text-emerald-400 font-bold uppercase flex items-center gap-1.5">
            <span>🌐</span> Languages & Communication
          </div>
          <div class="flex flex-wrap gap-1 text-[11px]">
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Python 3 (PCAP)</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">C / Embedded C</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">English (Prof.)</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Tamil (Native)</span>
            <span class="px-2 py-0.5 rounded bg-blue-950 border border-blue-800 text-slate-300">Kannada (Native)</span>
          </div>
        </div>

      </div>
    </div>

    <!-- CATCHY CALL TO ACTION: PROCEED TO SCREEN 2 -->
    <div class="rounded-3xl p-6 sm:p-8 bg-gradient-to-r from-blue-900/80 via-blue-800/60 to-corporate-900/90 border border-blue-500/40 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-6">
      <div>
        <span class="px-2.5 py-0.5 rounded-full bg-blue-950 border border-blue-400/30 text-blue-300 text-[10px] font-mono font-bold tracking-wider">
          ATTESTED CREDENTIAL REPOSITORY
        </span>
        <h3 class="font-display font-extrabold text-2xl text-white mt-1">
          Explore All 70 Authenticated Documents
        </h3>
        <p class="text-xs text-blue-200 mt-1 max-w-xl">
          Review the complete catalog classified by importance tier, sorted by date, and backed by verifiable SHA-256 cryptographic hashes.
        </p>
      </div>

      <button onclick="showScreen('dossier')" class="px-6 py-3 rounded-2xl bg-blue-600 hover:bg-blue-500 text-white font-mono text-sm font-bold shadow-lg hover:shadow-blue-500/30 transition-all flex items-center gap-2 shrink-0">
        <span>VIEW CREDENTIALS (70)</span>
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
    </div>

  </section>

  <!-- =========================================================================
       SCREEN 2: VERIFIED CREDENTIALS DOSSIER (70 ATTESTATIONS)
       ========================================================================= -->
  <section id="screenDossier" class="screen-fade max-w-7xl mx-auto w-full px-4 sm:px-8 py-8 flex flex-col gap-6 hidden">

    <!-- SCREEN 2 HEADER & METRICS -->
    <div class="rounded-3xl p-6 sm:p-8 formal-card shadow-lg flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
      <div>
        <div class="flex items-center gap-2">
          <button onclick="showScreen('resume')" class="text-xs font-mono text-blue-400 hover:underline flex items-center gap-1">
            &larr; BACK TO RESUME
          </button>
          <span class="text-slate-600">|</span>
          <span class="text-xs font-mono text-slate-400">OFFICIAL DOSSIER</span>
        </div>
        
        <h2 class="text-2xl sm:text-3xl font-display font-black text-white mt-1 tracking-tight">
          70 Verified Documents & Specializations
        </h2>
        <p class="text-xs text-slate-400 font-sans mt-1">
          Classified by importance tier and chronological dates. Filter, sort, or open the formal transcript table.
        </p>
      </div>

      <!-- Action Toggles -->
      <div class="flex items-center gap-2.5 no-print">
        <div class="flex items-center p-1 rounded-xl bg-corporate-950 border border-blue-900/60">
          <button id="subBtnCards" onclick="setDossierSubView('cards')" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium bg-blue-600 text-white shadow-sm flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            <span>Cards Deck</span>
          </button>
          <button id="subBtnTable" onclick="setDossierSubView('table')" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium text-slate-400 hover:text-white flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line></svg>
            <span>Formal Table</span>
          </button>
        </div>
      </div>
    </div>

    <!-- FILTER & SORT BAR -->
    <div class="p-4 rounded-2xl bg-corporate-900 border border-blue-900/50 flex flex-col xl:flex-row items-stretch xl:items-center justify-between gap-4 font-mono text-xs no-print">
      
      <!-- Topic Filter Pills -->
      <div class="flex flex-wrap items-center gap-1.5" id="topicFilters">
        <button data-topic="all" class="topic-btn active px-3 py-1.5 rounded-lg bg-blue-600 text-white font-semibold">
          All (70)
        </button>
        <button data-topic="cloud" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          Cloud & AWS (9)
        </button>
        <button data-topic="ai" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          AI & LLMs (7)
        </button>
        <button data-topic="cyber" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          Cybersecurity (6)
        </button>
        <button data-topic="iot" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          IoT & Hardware (7)
        </button>
        <button data-topic="data" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          MATLAB & Simulation (13)
        </button>
        <button data-topic="programming" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          Python (3)
        </button>
        <button data-topic="honors" class="topic-btn px-3 py-1.5 rounded-lg bg-corporate-950 text-slate-400 hover:text-white border border-blue-900/40">
          Honors & CIT (25)
        </button>
      </div>

      <!-- Tier Filter, Sort & Search -->
      <div class="flex flex-wrap items-center gap-2.5">
        
        <select id="tierFilterSelect" class="bg-corporate-950 text-slate-200 border border-blue-900/60 rounded-lg px-3 py-1.5 focus:outline-none focus:border-blue-500">
          <option value="all">All Importance Tiers</option>
          <option value="1">Tier 1: High Importance (Govt / Industry Leaders)</option>
          <option value="2">Tier 2: Core Engineering Specializations</option>
          <option value="3">Tier 3: Honors, Awards & Experience</option>
        </select>

        <select id="sortSelect" class="bg-corporate-950 text-slate-200 border border-blue-900/60 rounded-lg px-3 py-1.5 focus:outline-none focus:border-blue-500">
          <option value="importance">Sort by Importance (Tier 1 &rarr; 3)</option>
          <option value="date-desc">Sort by Date (Newest First)</option>
          <option value="date-asc">Sort by Date (Oldest First)</option>
          <option value="title">Sort by Title (A &rarr; Z)</option>
          <option value="issuer">Sort by Issuer</option>
        </select>

        <div class="relative w-full sm:w-52">
          <input id="searchInput" type="text" placeholder="Search 70 certificates..." class="w-full bg-corporate-950 border border-blue-900/60 rounded-lg pl-8 pr-3 py-1.5 text-slate-200 placeholder-slate-500 focus:outline-none focus:border-blue-500">
          <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        </div>

      </div>

    </div>

    <!-- DOSSIER CARDS SUB-VIEW -->
    <div id="subViewCards" class="space-y-10">
      <div id="dossierContainer" class="space-y-10"></div>
    </div>

    <!-- FORMAL TRANSCRIPT TABLE SUB-VIEW -->
    <div id="subViewTable" class="rounded-3xl formal-card p-6 shadow-xl overflow-x-auto hidden">
      <div class="flex items-center justify-between pb-4 mb-4 border-b border-blue-900/40">
        <div>
          <h3 class="font-display font-extrabold text-xl text-white">Official Certificate Transcript & Verification Log</h3>
          <p class="text-xs text-slate-400 mt-1 font-mono">Verified record of 70 accreditations awarded to Karunesh P</p>
        </div>
        <span class="text-xs font-mono text-blue-300" id="transcriptCount">70 Records</span>
      </div>

      <table class="w-full text-left text-xs font-sans border-collapse">
        <thead>
          <tr class="border-b border-blue-900/60 font-mono text-[11px] text-slate-400 uppercase tracking-wider bg-corporate-950/70">
            <th class="py-3 px-3">#</th>
            <th class="py-3 px-3">Certificate Title</th>
            <th class="py-3 px-3">Issuing Organization</th>
            <th class="py-3 px-3">Topic Domain</th>
            <th class="py-3 px-3">Issue Date</th>
            <th class="py-3 px-3">Importance Tier</th>
            <th class="py-3 px-3">SHA-256 Hash</th>
            <th class="py-3 px-3 text-right no-print">Actions</th>
          </tr>
        </thead>
        <tbody id="transcriptTableBody" class="divide-y divide-blue-900/30"></tbody>
      </table>
    </div>

  </section>

  <!-- FORMAL INSPECTION MODAL (SPLIT-SCREEN) -->
  <div id="inspectorModal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 modal-backdrop opacity-0 pointer-events-none transition-opacity duration-200">
    <div id="inspectorContent" class="relative w-full max-w-5xl rounded-3xl bg-corporate-900 border border-blue-700/50 shadow-2xl transform scale-95 transition-transform duration-200 max-h-[92vh] flex flex-col overflow-hidden">
      
      <!-- Modal Header -->
      <div class="p-4 sm:px-6 border-b border-blue-900/60 flex items-center justify-between bg-corporate-950">
        <div class="flex items-center gap-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <span class="text-xs font-mono text-blue-300 font-semibold uppercase tracking-wider">OFFICIAL DOCUMENT VERIFICATION</span>
        </div>
        
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1 bg-corporate-900 border border-blue-900/60 rounded-lg p-0.5 text-xs font-mono">
            <button id="modalPrevBtn" class="px-2.5 py-1 text-slate-400 hover:text-white transition-colors">&larr; PREV</button>
            <span class="text-slate-600">|</span>
            <button id="modalNextBtn" class="px-2.5 py-1 text-slate-400 hover:text-white transition-colors">NEXT &rarr;</button>
          </div>
          <button onclick="closeInspector()" class="p-1.5 rounded-lg bg-corporate-850 hover:bg-corporate-800 text-slate-300 hover:text-white transition-colors">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
      </div>

      <!-- Modal Body -->
      <div id="modalBody" class="flex-1 overflow-y-auto"></div>

    </div>
  </div>

  <!-- Toast -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-300 pointer-events-none px-4 py-2.5 rounded-xl bg-corporate-900 border border-blue-500/40 text-blue-200 font-mono text-xs flex items-center gap-2 shadow-2xl">
    <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toastMsg">Action complete</span>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    const CATALOG = {json_str};
    let activeList = [...CATALOG];
    let currentCertIndex = 0;
    let selectedTopic = 'all';
    let selectedTier = 'all';
    let currentScreen = 'resume'; // 'resume' or 'dossier'

    const TOPIC_ORDER = [
      {{ id: 'cloud', name: 'Cloud Architecture & Infrastructure', badge: 'CLOUD & AWS' }},
      {{ id: 'ai', name: 'Artificial Intelligence & LLM Systems', badge: 'AI & NEURAL NETS' }},
      {{ id: 'cyber', name: 'Cybersecurity & Network Defense', badge: 'CYBERSECURITY' }},
      {{ id: 'iot', name: 'IoT & Embedded Hardware Systems', badge: 'IOT & EMBEDDED' }},
      {{ id: 'data', name: 'Data Science & Computational Simulation', badge: 'MATLAB & SIMULINK' }},
      {{ id: 'programming', name: 'Software Engineering & Python', badge: 'PYTHON & SOFTWARE' }},
      {{ id: 'honors', name: 'Professional Experience & Academic Honors', badge: 'HONORS & RESEARCH' }}
    ];

    function showScreen(screen) {{
      currentScreen = screen;
      const sResume = document.getElementById('screenResume');
      const sDossier = document.getElementById('screenDossier');
      const navResume = document.getElementById('navBtnResume');
      const navDossier = document.getElementById('navBtnDossier');

      if (screen === 'resume') {{
        sResume.classList.remove('hidden');
        sDossier.classList.add('hidden');
        navResume.classList.add('bg-blue-600', 'text-white');
        navResume.classList.remove('text-slate-400');
        navDossier.classList.remove('bg-blue-600', 'text-white');
        navDossier.classList.add('text-slate-400');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }} else {{
        sResume.classList.add('hidden');
        sDossier.classList.remove('hidden');
        navDossier.classList.add('bg-blue-600', 'text-white');
        navDossier.classList.remove('text-slate-400');
        navResume.classList.remove('bg-blue-600', 'text-white');
        navResume.classList.add('text-slate-400');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}

    function setDossierSubView(mode) {{
      const subCards = document.getElementById('subViewCards');
      const subTable = document.getElementById('subViewTable');
      const btnCards = document.getElementById('subBtnCards');
      const btnTable = document.getElementById('subBtnTable');

      if (mode === 'cards') {{
        subCards.classList.remove('hidden');
        subTable.classList.add('hidden');
        btnCards.classList.add('bg-blue-600', 'text-white');
        btnCards.classList.remove('text-slate-400');
        btnTable.classList.remove('bg-blue-600', 'text-white');
        btnTable.classList.add('text-slate-400');
      }} else {{
        subCards.classList.add('hidden');
        subTable.classList.remove('hidden');
        btnTable.classList.add('bg-blue-600', 'text-white');
        btnTable.classList.remove('text-slate-400');
        btnCards.classList.remove('bg-blue-600', 'text-white');
        btnCards.classList.add('text-slate-400');
      }}
    }}

    function getTierBadge(importance, label) {{
      if (importance === 1) {{
        return `<span class="tier-badge-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-semibold tracking-wider">${{label}}</span>`;
      }}
      if (importance === 2) {{
        return `<span class="tier-badge-2 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-semibold tracking-wider">${{label}}</span>`;
      }}
      return `<span class="tier-badge-3 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-semibold tracking-wider">${{label}}</span>`;
    }}

    function getIssuerLogo(issuer) {{
      const i = issuer.toLowerCase();
      if (i.includes('amazon') || i.includes('aws')) {{
        return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-cyan-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"></path></svg></div>`;
      }}
      if (i.includes('ibm')) {{
        return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-blue-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 12h8M12 8v8"></path></svg></div>`;
      }}
      if (i.includes('fortinet')) {{
        return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-indigo-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>`;
      }}
      if (i.includes('matlab') || i.includes('mathworks')) {{
        return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-amber-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>`;
      }}
      if (i.includes('altium') || i.includes('arduino')) {{
        return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-amber-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"></rect><circle cx="12" cy="12" r="3"></circle></svg></div>`;
      }}
      return `<div class="w-10 h-10 rounded-xl bg-corporate-950 border border-blue-900/60 flex items-center justify-center text-blue-300 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>`;
    }}

    // Render Cards in Dossier
    const dossierContainer = document.getElementById('dossierContainer');

    function renderDossier(list) {{
      dossierContainer.innerHTML = '';
      
      if (list.length === 0) {{
        dossierContainer.innerHTML = `
          <div class="text-center py-16 formal-card rounded-2xl">
            <p class="text-slate-400 text-sm font-mono">No certificates match the selected criteria.</p>
            <button onclick="resetFilters()" class="mt-3 px-4 py-1.5 rounded-lg bg-blue-600 text-white text-xs font-mono">Reset Filters</button>
          </div>
        `;
        return;
      }}

      TOPIC_ORDER.forEach(topic => {{
        const topicItems = list.filter(c => c.category === topic.id);
        if (topicItems.length === 0) return;

        const section = document.createElement('section');
        section.className = 'space-y-4';

        section.innerHTML = `
          <div class="flex items-center justify-between pb-3 border-b border-blue-900/40">
            <div>
              <span class="text-[11px] font-mono text-blue-400 uppercase tracking-wider font-semibold">${{topic.badge}}</span>
              <h3 class="font-display font-extrabold text-xl text-white tracking-tight">${{topic.name}}</h3>
            </div>
            <span class="px-2.5 py-0.5 rounded-full bg-corporate-950 border border-blue-800/60 text-blue-300 font-mono text-xs">
              ${{topicItems.length}} ${{topicItems.length === 1 ? 'Record' : 'Records'}}
            </span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            ${{topicItems.map(cert => `
              <div class="formal-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer" onclick="openInspector('${{cert.id}}')">
                <div>
                  <div class="flex items-start justify-between gap-3 mb-3">
                    <div class="flex items-center gap-3">
                      ${{getIssuerLogo(cert.issuer)}}
                      <div>
                        <div class="text-[11px] font-mono text-slate-400 font-medium truncate max-w-[150px]">${{cert.issuer}}</div>
                        <div class="text-[11px] font-mono text-blue-300">${{cert.date_display}}</div>
                      </div>
                    </div>
                    ${{getTierBadge(cert.importance, cert.tier_badge)}}
                  </div>

                  <h4 class="font-display font-bold text-base text-white tracking-tight leading-snug line-clamp-2 mb-2">
                    ${{cert.title}}
                  </h4>

                  <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed mb-3">
                    ${{cert.desc}}
                  </p>

                  <div class="flex flex-wrap gap-1 mb-4">
                    ${{cert.tags.slice(0, 3).map(t => `<span class="px-2 py-0.5 rounded bg-corporate-950 border border-blue-900/40 text-[10px] font-mono text-slate-300">${{t}}</span>`).join('')}}
                  </div>
                </div>

                <div class="pt-3 border-t border-blue-900/40 flex items-center justify-between text-xs font-mono">
                  <span class="text-[10px] text-slate-400 truncate max-w-[120px]" title="${{cert.sha256}}">
                    ${{cert.sha256.slice(0, 8)}}...${{cert.sha256.slice(-6)}}
                  </span>

                  <div class="flex items-center gap-2">
                    <button onclick="event.stopPropagation(); openInspector('${{cert.id}}')" class="px-2.5 py-1 rounded-lg bg-blue-900/60 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-semibold transition-colors flex items-center gap-1">
                      VIEW
                    </button>
                    <a href="${{cert.filepath}}" download="${{cert.filename}}" onclick="event.stopPropagation();" class="p-1 rounded-lg bg-corporate-850 hover:bg-corporate-800 text-slate-300 border border-blue-900/50 transition-colors" title="Download Document">
                      <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    </a>
                  </div>
                </div>
              </div>
            `).join('')}}
          </div>
        `;

        dossierContainer.appendChild(section);
      }});
    }}

    // Render Transcript Table
    const transcriptTableBody = document.getElementById('transcriptTableBody');
    const transcriptCount = document.getElementById('transcriptCount');

    function renderTranscript(list) {{
      transcriptTableBody.innerHTML = '';
      transcriptCount.innerText = `${{list.length}} Records`;

      list.forEach((cert, idx) => {{
        const row = document.createElement('tr');
        row.className = 'hover:bg-blue-900/20 transition-colors cursor-pointer';
        row.onclick = () => openInspector(cert.id);

        row.innerHTML = `
          <td class="py-3 px-3 font-mono text-slate-400">${{idx + 1}}</td>
          <td class="py-3 px-3 font-semibold text-white max-w-[280px]">
            <div class="truncate" title="${{cert.title}}">${{cert.title}}</div>
          </td>
          <td class="py-3 px-3 text-slate-300 max-w-[200px]">
            <div class="truncate">${{cert.issuer}}</div>
          </td>
          <td class="py-3 px-3 font-mono text-[11px] text-blue-300">
            ${{cert.topic_label}}
          </td>
          <td class="py-3 px-3 font-mono text-slate-300 whitespace-nowrap">
            ${{cert.date_display}}
          </td>
          <td class="py-3 px-3">
            ${{getTierBadge(cert.importance, cert.tier_badge)}}
          </td>
          <td class="py-3 px-3 font-mono text-[10px] text-slate-400">
            ${{cert.sha256.slice(0, 10)}}...
          </td>
          <td class="py-3 px-3 text-right no-print">
            <div class="inline-flex items-center gap-1.5" onclick="event.stopPropagation()">
              <button onclick="openInspector('${{cert.id}}')" class="px-2 py-0.5 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-mono">
                View
              </button>
              <a href="${{cert.filepath}}" download="${{cert.filename}}" class="p-1 rounded bg-corporate-850 hover:bg-corporate-800 text-slate-300 border border-blue-900/50">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              </a>
            </div>
          </td>
        `;

        transcriptTableBody.appendChild(row);
      }});
    }}

    // Filter & Sort Logic
    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const sortVal = document.getElementById('sortSelect').value;

      activeList = CATALOG.filter(c => {{
        const matchesTopic = (selectedTopic === 'all' || c.category === selectedTopic);
        const matchesTier = (selectedTier === 'all' || c.importance.toString() === selectedTier);
        const matchesQuery = !query || 
          c.title.toLowerCase().includes(query) ||
          c.issuer.toLowerCase().includes(query) ||
          c.filename.toLowerCase().includes(query) ||
          c.sha256.toLowerCase().includes(query) ||
          c.tags.some(t => t.toLowerCase().includes(query));

        return matchesTopic && matchesTier && matchesQuery;
      }});

      if (sortVal === 'importance') {{
        activeList.sort((a, b) => a.importance - b.importance || b.date.localeCompare(a.date));
      }} else if (sortVal === 'date-desc') {{
        activeList.sort((a, b) => b.date.localeCompare(a.date));
      }} else if (sortVal === 'date-asc') {{
        activeList.sort((a, b) => a.date.localeCompare(b.date));
      }} else if (sortVal === 'title') {{
        activeList.sort((a, b) => a.title.localeCompare(b.title));
      }} else if (sortVal === 'issuer') {{
        activeList.sort((a, b) => a.issuer.localeCompare(b.issuer));
      }}

      renderDossier(activeList);
      renderTranscript(activeList);
    }}

    document.querySelectorAll('.topic-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.topic-btn').forEach(b => {{
          b.classList.remove('active', 'bg-blue-600', 'text-white');
          b.classList.add('bg-corporate-950', 'text-slate-400');
        }});
        btn.classList.add('active', 'bg-blue-600', 'text-white');
        btn.classList.remove('bg-corporate-950', 'text-slate-400');
        selectedTopic = btn.getAttribute('data-topic');
        applyFilters();
      }});
    }});

    document.getElementById('tierFilterSelect').addEventListener('change', (e) => {{
      selectedTier = e.target.value;
      applyFilters();
    }});

    document.getElementById('sortSelect').addEventListener('change', applyFilters);
    document.getElementById('searchInput').addEventListener('input', applyFilters);

    function resetFilters() {{
      document.querySelector('[data-topic="all"]').click();
      document.getElementById('tierFilterSelect').value = 'all';
      document.getElementById('searchInput').value = '';
      selectedTier = 'all';
      applyFilters();
    }}

    // Split-Screen Inspector
    function openInspector(certId) {{
      const idx = activeList.findIndex(c => c.id === certId);
      if (idx !== -1) currentCertIndex = idx;
      const cert = activeList[currentCertIndex] || CATALOG[0];

      const modal = document.getElementById('inspectorModal');
      const content = document.getElementById('inspectorContent');
      const body = document.getElementById('modalBody');

      const isPdf = cert.filename.toLowerCase().endsWith('.pdf');
      const isImg = cert.filename.toLowerCase().endsWith('.png') || cert.filename.toLowerCase().endsWith('.jpg') || cert.filename.toLowerCase().endsWith('.jpeg');

      body.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-12 min-h-[580px]">
          
          <!-- LEFT: DOCUMENT VIEWER -->
          <div class="lg:col-span-7 bg-black/60 border-b lg:border-b-0 lg:border-r border-blue-900/60 flex flex-col">
            <div class="p-3 bg-corporate-950 border-b border-blue-900/60 flex items-center justify-between text-xs font-mono">
              <span class="text-slate-300 truncate max-w-[240px]">${{cert.filename}}</span>
              <div class="flex items-center gap-2">
                <a href="${{cert.filepath}}" target="_blank" class="px-2.5 py-1 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-semibold">
                  FULLSCREEN &nearr;
                </a>
                <a href="${{cert.filepath}}" download="${{cert.filename}}" class="px-2.5 py-1 rounded bg-corporate-850 hover:bg-corporate-800 text-slate-200 border border-blue-900/50 text-[11px]">
                  DOWNLOAD
                </a>
              </div>
            </div>

            <div class="flex-1 w-full flex items-center justify-center p-2 min-h-[380px] sm:min-h-[480px]">
              ${{isPdf ? `
                <iframe src="${{cert.filepath}}#toolbar=0" class="w-full h-full min-h-[460px] border-none rounded-2xl"></iframe>
              ` : (isImg ? `
                <img src="${{cert.filepath}}" alt="${{cert.title}}" class="max-h-[500px] max-w-full object-contain rounded-2xl p-2">
              ` : `
                <div class="text-center p-8 text-slate-400">
                  <p class="text-sm">Preview not supported inline for this format.</p>
                  <a href="${{cert.filepath}}" target="_blank" class="mt-3 inline-block px-4 py-2 bg-blue-600 text-white rounded-lg">Open File Directly</a>
                </div>
              `)}}
            </div>
          </div>

          <!-- RIGHT: METADATA -->
          <div class="lg:col-span-5 p-6 flex flex-col justify-between font-mono space-y-4 bg-corporate-900/80">
            <div class="space-y-4">
              
              <div class="flex items-center justify-between gap-2">
                ${{getTierBadge(cert.importance, cert.tier_badge)}}
                <span class="text-xs text-blue-300">${{cert.date_display}}</span>
              </div>

              <div>
                <h3 class="font-display font-extrabold text-2xl text-white leading-tight">
                  ${{cert.title}}
                </h3>
                <div class="text-blue-400 text-sm mt-1 font-semibold">${{cert.issuer}}</div>
              </div>

              <div class="p-3.5 rounded-2xl bg-corporate-950 border border-blue-900/60 space-y-2 text-xs">
                <div class="flex justify-between">
                  <span class="text-slate-400">CANDIDATE:</span>
                  <span class="text-white font-bold">KARUNESH P</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-slate-400">TOPIC DOMAIN:</span>
                  <span class="text-slate-200">${{cert.topic_label}}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-slate-400">IMPORTANCE:</span>
                  <span class="text-slate-200">${{cert.importance_label}}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-slate-400">FILE SIZE:</span>
                  <span class="text-slate-200">${{cert.size_kb}} KB</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-slate-400">LEDGER STATUS:</span>
                  <span class="text-emerald-400 font-semibold">VERIFIED & INTEGRITY-CHECKED</span>
                </div>
              </div>

              <p class="text-xs text-slate-300 font-sans leading-relaxed">
                ${{cert.desc}}
              </p>

              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-400 mb-1">
                  <span>SHA-256 HASH</span>
                  <button onclick="copyHash('${{cert.sha256}}')" class="text-blue-400 hover:text-white underline text-[10px]">COPY HASH</button>
                </div>
                <div class="p-2 rounded-lg bg-corporate-950 border border-blue-900/60 text-blue-300 font-mono text-[11px] break-all select-all">
                  ${{cert.sha256}}
                </div>
              </div>

              <div>
                <div class="text-[10px] text-slate-400 uppercase tracking-wider mb-1.5 font-semibold">VERIFIED COMPETENCIES</div>
                <div class="flex flex-wrap gap-1.5">
                  ${{cert.tags.map(t => `<span class="px-2.5 py-0.5 rounded-md bg-corporate-950 border border-blue-900/60 text-slate-300 text-xs">${{t}}</span>`).join('')}}
                </div>
              </div>

            </div>

            <div class="pt-3 border-t border-blue-900/60 flex items-center justify-between gap-3">
              <a href="${{cert.filepath}}" download="${{cert.filename}}" class="flex-1 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-mono text-xs font-semibold text-center transition-colors">
                DOWNLOAD ORIGINAL DOCUMENT
              </a>
              <button onclick="closeInspector()" class="px-4 py-2 rounded-xl bg-corporate-850 hover:bg-corporate-800 text-slate-300 font-mono text-xs transition-colors">
                CLOSE
              </button>
            </div>

          </div>

        </div>
      `;

      modal.classList.remove('opacity-0', 'pointer-events-none');
      content.classList.remove('scale-95');
      content.classList.add('scale-100');
    }}

    function closeInspector() {{
      const modal = document.getElementById('inspectorModal');
      const content = document.getElementById('inspectorContent');
      modal.classList.add('opacity-0', 'pointer-events-none');
      content.classList.remove('scale-100');
      content.classList.add('scale-95');
    }}

    document.getElementById('modalPrevBtn').addEventListener('click', () => {{
      if (activeList.length === 0) return;
      currentCertIndex = (currentCertIndex - 1 + activeList.length) % activeList.length;
      openInspector(activeList[currentCertIndex].id);
    }});

    document.getElementById('modalNextBtn').addEventListener('click', () => {{
      if (activeList.length === 0) return;
      currentCertIndex = (currentCertIndex + 1) % activeList.length;
      openInspector(activeList[currentCertIndex].id);
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeInspector();
      if (!document.getElementById('inspectorModal').classList.contains('pointer-events-none')) {{
        if (e.key === 'ArrowLeft') document.getElementById('modalPrevBtn').click();
        if (e.key === 'ArrowRight') document.getElementById('modalNextBtn').click();
      }}
    }});

    document.getElementById('inspectorModal').addEventListener('click', (e) => {{
      if (e.target === document.getElementById('inspectorModal')) closeInspector();
    }});

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').innerText = msg;
      toast.classList.remove('translate-y-16', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-16', 'opacity-0');
      }}, 2600);
    }}

    function copyHash(text) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast("SHA-256 Hash copied to clipboard");
      }}).catch(() => {{
        showToast("Copied: " + text.slice(0, 16) + "...");
      }});
    }}

    // Initial render
    applyFilters();
  </script>

</body>
</html>
'''

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated complete two-screen executive resume and credentials dossier in index.html!")
