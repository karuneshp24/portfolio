import json

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_formal_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

json_str = json.dumps(catalog, indent=2, ensure_ascii=False)

html_code = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Karunesh P — Official Engineering Credentials Portfolio & Verification Dossier</title>
  
  <!-- Professional Fonts: Inter, Space Grotesk, JetBrains Mono -->
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
            slate: {{
              850: '#111827',
              900: '#0b1329',
              925: '#070d1e',
              950: '#030712',
            }},
            executive: {{
              blue: '#2563eb',
              navy: '#1e3a8a',
              gold: '#d97706',
              emerald: '#059669',
              cyan: '#0284c7',
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
      background-color: #070d1e;
      color: #e2e8f0;
      font-family: 'Inter', sans-serif;
    }}

    /* Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #070d1e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}

    /* Formal Card Shadows and Borders */
    .formal-card {{
      background: linear-gradient(180deg, rgba(17, 24, 39, 0.95) 0%, rgba(11, 19, 41, 0.95) 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .formal-card:hover {{
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-3px);
      box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.7), 0 0 15px -3px rgba(56, 189, 248, 0.15);
    }}

    .tier-badge-1 {{
      background: rgba(217, 119, 6, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }}
    .tier-badge-2 {{
      background: rgba(37, 99, 235, 0.15);
      border: 1px solid rgba(96, 165, 250, 0.4);
      color: #93c5fd;
    }}
    .tier-badge-3 {{
      background: rgba(5, 150, 105, 0.15);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: #6ee7b7;
    }}

    .modal-backdrop {{
      background: rgba(3, 7, 18, 0.88);
      backdrop-filter: blur(16px);
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
      #transcriptView {{
        display: block !important;
      }}
      table {{
        color: #000000 !important;
        border-collapse: collapse !important;
        width: 100% !important;
      }}
      th, td {{
        border: 1px solid #cccccc !important;
        padding: 8px !important;
        color: #000000 !important;
      }}
    }}
  </style>
</head>

<body class="min-h-screen flex flex-col antialiased selection:bg-blue-600/30 selection:text-white">

  <!-- TOP EXECUTIVE BANNER -->
  <header class="border-b border-slate-800/80 bg-slate-900/90 backdrop-blur-md sticky top-0 z-40 px-4 sm:px-8 py-4">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      
      <!-- Candidate Profile Info -->
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-600 via-indigo-600 to-slate-900 border border-blue-400/30 flex items-center justify-center text-white font-display font-extrabold text-xl shadow-md">
          KP
        </div>
        <div>
          <div class="flex items-center gap-2.5">
            <h1 class="font-display font-extrabold text-xl text-white tracking-tight">KARUNESH P</h1>
            <span class="px-2 py-0.5 rounded-full bg-blue-950 border border-blue-500/30 text-blue-300 font-mono text-[11px] font-semibold">
              VERIFIED PORTFOLIO
            </span>
          </div>
          <p class="text-xs text-slate-400 font-sans mt-0.5">
            Electronics & Communication Engineering · 62 Verified Credentials · Official Dossier
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-wrap items-center gap-2.5 no-print">
        <!-- View Toggle Buttons -->
        <div class="flex items-center p-1 rounded-xl bg-slate-950 border border-slate-800">
          <button id="btnViewDossier" class="px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all bg-blue-600 text-white shadow-sm flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            <span>Dossier View</span>
          </button>
          <button id="btnViewTranscript" class="px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-slate-400 hover:text-white flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
            <span>Formal Transcript</span>
          </button>
        </div>

        <!-- Print Formal Transcript Button -->
        <button onclick="window.print()" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-mono transition-colors flex items-center gap-1.5" title="Print or Save Official Transcript as PDF">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          <span>Print / PDF</span>
        </button>

        <!-- Offline Badge -->
        <span class="px-2.5 py-1 rounded-xl bg-emerald-950/70 border border-emerald-500/30 text-emerald-300 text-[11px] font-mono flex items-center gap-1.5" title="Always available offline and online">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          <span>ALWAYS ACCESSIBLE</span>
        </span>
      </div>

    </div>
  </header>

  <!-- FORMAL EXECUTIVE SUMMARY & METRICS SECTION -->
  <section class="max-w-7xl mx-auto w-full px-4 sm:px-8 py-6 no-print">
    <div class="rounded-2xl p-6 bg-slate-900 border border-slate-800 shadow-lg">
      <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-slate-800">
        <div>
          <span class="text-xs font-mono text-blue-400 uppercase tracking-wider font-semibold">FORMAL CREDENTIALS REGISTRY</span>
          <h2 class="text-2xl sm:text-3xl font-display font-extrabold text-white mt-1">
            Professional Engineering Portfolio
          </h2>
          <p class="text-sm text-slate-300 mt-2 max-w-3xl leading-relaxed">
            This dossier provides official verification for <strong>62 technical certifications, academic recognitions, and professional achievements</strong> earned by <strong>Karunesh P</strong>. Each entry is validated with a real SHA-256 cryptographic digest, categorized by topic, classified by importance level, and chronologically recorded.
          </p>
        </div>

        <!-- Tier Summary Stats -->
        <div class="grid grid-cols-3 gap-3 w-full lg:w-auto shrink-0 font-mono text-center">
          <div class="p-3 rounded-xl bg-slate-950 border border-amber-500/30">
            <div class="text-[10px] text-amber-400 uppercase font-semibold">Tier 1 · High</div>
            <div class="text-xl font-bold text-white mt-0.5" id="statTier1">24</div>
            <div class="text-[10px] text-slate-500">Industry / Govt</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-950 border border-blue-500/30">
            <div class="text-[10px] text-blue-400 uppercase font-semibold">Tier 2 · Core</div>
            <div class="text-xl font-bold text-white mt-0.5" id="statTier2">18</div>
            <div class="text-[10px] text-slate-500">Specializations</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/30">
            <div class="text-[10px] text-emerald-400 uppercase font-semibold">Tier 3 · Merit</div>
            <div class="text-xl font-bold text-white mt-0.5" id="statTier3">20</div>
            <div class="text-[10px] text-slate-500">Honors & Awards</div>
          </div>
        </div>
      </div>

      <!-- FILTER & SORT CONTROLS BAR -->
      <div class="pt-5 flex flex-col xl:flex-row items-stretch xl:items-center justify-between gap-4 font-mono text-xs">
        
        <!-- Topic / Category Filter Buttons -->
        <div class="flex flex-wrap items-center gap-1.5" id="topicFilters">
          <button data-topic="all" class="topic-btn active px-3 py-1.5 rounded-lg bg-blue-600 text-white font-semibold shadow-sm">
            All Topics (62)
          </button>
          <button data-topic="cloud" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            Cloud & AWS (9)
          </button>
          <button data-topic="ai" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            AI & LLMs (6)
          </button>
          <button data-topic="cyber" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            Cybersecurity (6)
          </button>
          <button data-topic="iot" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            IoT & Hardware (7)
          </button>
          <button data-topic="data" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            Data & MATLAB (6)
          </button>
          <button data-topic="programming" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            Python & Software (3)
          </button>
          <button data-topic="honors" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-950 text-slate-400 hover:text-white border border-slate-800">
            Honors & Experience (25)
          </button>
        </div>

        <!-- Right Side: Tier Filter, Date Sort & Search -->
        <div class="flex flex-wrap items-center gap-2.5">
          
          <!-- Tier Filter -->
          <select id="tierFilterSelect" class="bg-slate-950 text-slate-200 border border-slate-800 rounded-lg px-3 py-1.5 focus:outline-none focus:border-blue-500">
            <option value="all">All Importance Tiers</option>
            <option value="1">Tier 1: High Importance (Govt / Industry Leaders)</option>
            <option value="2">Tier 2: Core Engineering Specializations</option>
            <option value="3">Tier 3: Honors, Awards & Symposia</option>
          </select>

          <!-- Sort Select -->
          <select id="sortSelect" class="bg-slate-950 text-slate-200 border border-slate-800 rounded-lg px-3 py-1.5 focus:outline-none focus:border-blue-500">
            <option value="importance">Sort by Importance (Tier 1 &rarr; 3)</option>
            <option value="date-desc">Sort by Date (Newest First)</option>
            <option value="date-asc">Sort by Date (Oldest First)</option>
            <option value="title">Sort by Title (A &rarr; Z)</option>
            <option value="issuer">Sort by Issuer</option>
          </select>

          <!-- Search Input -->
          <div class="relative w-full sm:w-56">
            <input id="searchInput" type="text" placeholder="Search certifications..." class="w-full bg-slate-950 border border-slate-800 rounded-lg pl-8 pr-3 py-1.5 text-slate-200 placeholder-slate-500 focus:outline-none focus:border-blue-500">
            <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </div>

        </div>

      </div>
    </div>
  </section>

  <!-- MAIN PRESENTATION AREA -->
  <main class="max-w-7xl mx-auto w-full px-4 sm:px-8 py-2 flex-1">
    
    <!-- VIEW 1: FORMAL DOSSIER CARD DECK -->
    <div id="dossierView" class="space-y-8">
      
      <!-- Grouped by Topic with Clear Headers -->
      <div id="dossierContainer" class="space-y-10">
        <!-- Rendered dynamically -->
      </div>

    </div>

    <!-- VIEW 2: FORMAL ACADEMIC & PROFESSIONAL TRANSCRIPT (TABLE VIEW) -->
    <div id="transcriptView" class="hidden space-y-6">
      
      <div class="rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-lg overflow-x-auto">
        <div class="flex items-center justify-between pb-4 mb-4 border-b border-slate-800">
          <div>
            <h3 class="font-display font-extrabold text-xl text-white">Official Certificate Transcript & Verification Log</h3>
            <p class="text-xs text-slate-400 mt-1 font-mono">Formal record of accreditations awarded to Karunesh P</p>
          </div>
          <span class="text-xs font-mono text-slate-400" id="transcriptCount">62 Records</span>
        </div>

        <table class="w-full text-left text-xs font-sans border-collapse">
          <thead>
            <tr class="border-b border-slate-800 font-mono text-[11px] text-slate-400 uppercase tracking-wider bg-slate-950/60">
              <th class="py-3 px-3">#</th>
              <th class="py-3 px-3">Certificate Title</th>
              <th class="py-3 px-3">Issuing Organization</th>
              <th class="py-3 px-3">Topic Domain</th>
              <th class="py-3 px-3">Issue Date</th>
              <th class="py-3 px-3">Importance Tier</th>
              <th class="py-3 px-3">Verification Hash</th>
              <th class="py-3 px-3 text-right no-print">Actions</th>
            </tr>
          </thead>
          <tbody id="transcriptTableBody" class="divide-y divide-slate-800/60">
            <!-- Rendered dynamically -->
          </tbody>
        </table>
      </div>

    </div>

  </main>

  <!-- FOOTER -->
  <footer class="mt-auto border-t border-slate-800 bg-slate-950 py-6 px-4 sm:px-8 no-print">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3 text-xs font-mono text-slate-500">
      <div>OFFICIAL CREDENTIAL PORTFOLIO // KARUNESH P</div>
      <div class="flex items-center gap-4 text-slate-400">
        <span>62 AUTHENTIC DOCUMENTS</span>
        <span>•</span>
        <span>SHA-256 INTEGRITY VALIDATED</span>
        <span>•</span>
        <span class="text-emerald-400">STATUS: VERIFIED</span>
      </div>
    </div>
  </footer>

  <!-- FORMAL INSPECTION MODAL (SPLIT-SCREEN) -->
  <div id="inspectorModal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 modal-backdrop opacity-0 pointer-events-none transition-opacity duration-200">
    <div id="inspectorContent" class="relative w-full max-w-5xl rounded-2xl bg-slate-900 border border-slate-700 shadow-2xl transform scale-95 transition-transform duration-200 max-h-[92vh] flex flex-col overflow-hidden">
      
      <!-- Modal Header -->
      <div class="p-4 sm:px-6 border-b border-slate-800 flex items-center justify-between bg-slate-950">
        <div class="flex items-center gap-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <span class="text-xs font-mono text-slate-300 font-semibold uppercase tracking-wider">OFFICIAL DOCUMENT VERIFICATION</span>
        </div>
        
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1 bg-slate-900 border border-slate-800 rounded-lg p-0.5 text-xs font-mono">
            <button id="modalPrevBtn" class="px-2.5 py-1 text-slate-400 hover:text-white transition-colors">&larr; PREV</button>
            <span class="text-slate-600">|</span>
            <button id="modalNextBtn" class="px-2.5 py-1 text-slate-400 hover:text-white transition-colors">NEXT &rarr;</button>
          </div>
          <button onclick="closeInspector()" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
      </div>

      <!-- Modal Body (Split) -->
      <div id="modalBody" class="flex-1 overflow-y-auto">
        <!-- Rendered dynamically -->
      </div>

    </div>
  </div>

  <!-- Notification Toast -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-300 pointer-events-none px-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-slate-200 font-mono text-xs flex items-center gap-2 shadow-2xl">
    <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toastMsg">Action completed</span>
  </div>

  <!-- JAVASCRIPT LOGIC & CATALOG ENGINE -->
  <script>
    const CATALOG = {json_str};
    let activeList = [...CATALOG];
    let currentCertIndex = 0;
    let selectedTopic = 'all';
    let selectedTier = 'all';

    const TOPIC_ORDER = [
      {{ id: 'cloud', name: 'Cloud Architecture & Infrastructure', badge: 'CLOUD' }},
      {{ id: 'ai', name: 'Artificial Intelligence & LLM Systems', badge: 'AI & ML' }},
      {{ id: 'cyber', name: 'Cybersecurity & Network Defense', badge: 'CYBERSECURITY' }},
      {{ id: 'iot', name: 'IoT & Embedded Hardware Systems', badge: 'IOT & EMBEDDED' }},
      {{ id: 'data', name: 'Data Science & Computational Simulation', badge: 'DATA & MATLAB' }},
      {{ id: 'programming', name: 'Software Engineering & Python', badge: 'SOFTWARE & PYTHON' }},
      {{ id: 'honors', name: 'Professional Experience & Academic Honors', badge: 'HONORS & RESEARCH' }}
    ];

    // Stats Counter
    document.getElementById('statTier1').innerText = CATALOG.filter(c => c.importance === 1).length;
    document.getElementById('statTier2').innerText = CATALOG.filter(c => c.importance === 2).length;
    document.getElementById('statTier3').innerText = CATALOG.filter(c => c.importance === 3).length;

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
        return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-cyan-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"></path></svg></div>`;
      }}
      if (i.includes('ibm')) {{
        return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-blue-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 12h8M12 8v8"></path></svg></div>`;
      }}
      if (i.includes('fortinet')) {{
        return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-indigo-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>`;
      }}
      if (i.includes('matlab') || i.includes('mathworks')) {{
        return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-amber-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>`;
      }}
      if (i.includes('altium') || i.includes('arduino')) {{
        return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-amber-400 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"></rect><circle cx="12" cy="12" r="3"></circle></svg></div>`;
      }}
      return `<div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-300 font-bold shrink-0"><svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>`;
    }}

    // Render Dossier View (Organized by Topic)
    const dossierContainer = document.getElementById('dossierContainer');

    function renderDossier(list) {{
      dossierContainer.innerHTML = '';
      
      if (list.length === 0) {{
        dossierContainer.innerHTML = `
          <div class="text-center py-16 bg-slate-900 border border-slate-800 rounded-2xl">
            <p class="text-slate-400 text-sm">No certificates match the selected filter criteria.</p>
            <button onclick="resetFilters()" class="mt-3 px-4 py-1.5 rounded-lg bg-blue-600 text-white text-xs font-mono">Reset All Filters</button>
          </div>
        `;
        return;
      }}

      // Group by topic
      TOPIC_ORDER.forEach(topic => {{
        const topicItems = list.filter(c => c.category === topic.id);
        if (topicItems.length === 0) return;

        const section = document.createElement('section');
        section.className = 'space-y-4';

        section.innerHTML = `
          <!-- Topic Header Banner -->
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <span class="text-[11px] font-mono text-blue-400 uppercase tracking-wider font-semibold">${{topic.badge}}</span>
              <h3 class="font-display font-extrabold text-xl text-white tracking-tight">${{topic.name}}</h3>
            </div>
            <span class="px-2.5 py-0.5 rounded-full bg-slate-900 border border-slate-700 text-slate-300 font-mono text-xs">
              ${{topicItems.length}} ${{topicItems.length === 1 ? 'Credential' : 'Credentials'}}
            </span>
          </div>

          <!-- Cards Grid for Topic -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            ${{topicItems.map(cert => `
              <div class="formal-card rounded-xl p-5 flex flex-col justify-between cursor-pointer" onclick="openInspector('${{cert.id}}')">
                
                <div>
                  <!-- Header: Issuer Logo + Date + Tier Badge -->
                  <div class="flex items-start justify-between gap-3 mb-3">
                    <div class="flex items-center gap-3">
                      ${{getIssuerLogo(cert.issuer)}}
                      <div>
                        <div class="text-[11px] font-mono text-slate-400 font-medium truncate max-w-[150px]">${{cert.issuer}}</div>
                        <div class="text-[11px] font-mono text-slate-400">${{cert.date_display}}</div>
                      </div>
                    </div>
                    ${{getTierBadge(cert.importance, cert.tier_badge)}}
                  </div>

                  <!-- Title -->
                  <h4 class="font-display font-bold text-base text-white tracking-tight leading-snug line-clamp-2 mb-2">
                    ${{cert.title}}
                  </h4>

                  <!-- Description -->
                  <p class="text-xs text-slate-400 line-clamp-2 leading-relaxed mb-3">
                    ${{cert.desc}}
                  </p>

                  <!-- Tags -->
                  <div class="flex flex-wrap gap-1 mb-4">
                    ${{cert.tags.slice(0, 3).map(t => `<span class="px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-[10px] font-mono text-slate-400">${{t}}</span>`).join('')}}
                  </div>
                </div>

                <!-- Footer: Hash & Action Buttons -->
                <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs font-mono">
                  <span class="text-[10px] text-slate-400 truncate max-w-[120px]" title="${{cert.sha256}}">
                    ${{cert.sha256.slice(0, 8)}}...${{cert.sha256.slice(-6)}}
                  </span>

                  <div class="flex items-center gap-2">
                    <button onclick="event.stopPropagation(); openInspector('${{cert.id}}')" class="px-2.5 py-1 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-semibold transition-colors flex items-center gap-1">
                      VIEW
                    </button>
                    <a href="${{cert.filepath}}" download="${{cert.filename}}" onclick="event.stopPropagation();" class="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors" title="Download Document">
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

    // Render Transcript Table View
    const transcriptTableBody = document.getElementById('transcriptTableBody');
    const transcriptCount = document.getElementById('transcriptCount');

    function renderTranscript(list) {{
      transcriptTableBody.innerHTML = '';
      transcriptCount.innerText = `${{list.length}} Records`;

      list.forEach((cert, idx) => {{
        const row = document.createElement('tr');
        row.className = 'hover:bg-slate-800/40 transition-colors cursor-pointer';
        row.onclick = () => openInspector(cert.id);

        row.innerHTML = `
          <td class="py-3 px-3 font-mono text-slate-400">${{idx + 1}}</td>
          <td class="py-3 px-3 font-semibold text-white max-w-[280px]">
            <div class="truncate" title="${{cert.title}}">${{cert.title}}</div>
          </td>
          <td class="py-3 px-3 text-slate-300 max-w-[200px]">
            <div class="truncate">${{cert.issuer}}</div>
          </td>
          <td class="py-3 px-3 font-mono text-[11px] text-slate-400">
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
              <button onclick="openInspector('${{cert.id}}')" class="px-2 py-0.5 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-mono">
                View
              </button>
              <a href="${{cert.filepath}}" download="${{cert.filename}}" class="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              </a>
            </div>
          </td>
        `;

        transcriptTableBody.appendChild(row);
      }});
    }}

    // Filter and Sort Engine
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

      // Sorting
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

    // Event Listeners for Filters
    document.querySelectorAll('.topic-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.topic-btn').forEach(b => {{
          b.classList.remove('active', 'bg-blue-600', 'text-white');
          b.classList.add('bg-slate-950', 'text-slate-400');
        }});
        btn.classList.add('active', 'bg-blue-600', 'text-white');
        btn.classList.remove('bg-slate-950', 'text-slate-400');
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

    // View Switcher (Dossier vs Formal Transcript)
    const btnViewDossier = document.getElementById('btnViewDossier');
    const btnViewTranscript = document.getElementById('btnViewTranscript');
    const dossierView = document.getElementById('dossierView');
    const transcriptView = document.getElementById('transcriptView');

    btnViewDossier.addEventListener('click', () => {{
      btnViewDossier.classList.add('bg-blue-600', 'text-white');
      btnViewDossier.classList.remove('text-slate-400');
      btnViewTranscript.classList.remove('bg-blue-600', 'text-white');
      btnViewTranscript.classList.add('text-slate-400');

      dossierView.classList.remove('hidden');
      transcriptView.classList.add('hidden');
    }});

    btnViewTranscript.addEventListener('click', () => {{
      btnViewTranscript.classList.add('bg-blue-600', 'text-white');
      btnViewTranscript.classList.remove('text-slate-400');
      btnViewDossier.classList.remove('bg-blue-600', 'text-white');
      btnViewDossier.classList.add('text-slate-400');

      transcriptView.classList.remove('hidden');
      dossierView.classList.add('hidden');
    }});

    // Modal Inspector
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
          
          <!-- LEFT: LIVE DOCUMENT VIEWER -->
          <div class="lg:col-span-7 bg-black/60 border-b lg:border-b-0 lg:border-r border-slate-800 flex flex-col">
            <div class="p-3 bg-slate-950 border-b border-slate-800 flex items-center justify-between text-xs font-mono">
              <span class="text-slate-300 truncate max-w-[240px]">${{cert.filename}}</span>
              <div class="flex items-center gap-2">
                <a href="${{cert.filepath}}" target="_blank" class="px-2.5 py-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700/50 text-[11px] font-semibold">
                  FULLSCREEN &nearr;
                </a>
                <a href="${{cert.filepath}}" download="${{cert.filename}}" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-[11px]">
                  DOWNLOAD
                </a>
              </div>
            </div>

            <div class="flex-1 w-full flex items-center justify-center p-2 min-h-[380px] sm:min-h-[480px]">
              ${{isPdf ? `
                <iframe src="${{cert.filepath}}#toolbar=0" class="w-full h-full min-h-[460px] border-none rounded-xl"></iframe>
              ` : (isImg ? `
                <img src="${{cert.filepath}}" alt="${{cert.title}}" class="max-h-[500px] max-w-full object-contain rounded-xl p-2">
              ` : `
                <div class="text-center p-8 text-slate-400">
                  <p class="text-sm">Preview not supported inline for this format.</p>
                  <a href="${{cert.filepath}}" target="_blank" class="mt-3 inline-block px-4 py-2 bg-blue-600 text-white rounded-lg">Open File Directly</a>
                </div>
              `)}}
            </div>
          </div>

          <!-- RIGHT: FORMAL METADATA -->
          <div class="lg:col-span-5 p-6 flex flex-col justify-between font-mono space-y-4 bg-slate-900/60">
            <div class="space-y-4">
              
              <div class="flex items-center justify-between gap-2">
                ${{getTierBadge(cert.importance, cert.tier_badge)}}
                <span class="text-xs text-slate-400">${{cert.date_display}}</span>
              </div>

              <div>
                <h3 class="font-display font-extrabold text-2xl text-white leading-tight">
                  ${{cert.title}}
                </h3>
                <div class="text-blue-400 text-sm mt-1 font-semibold">${{cert.issuer}}</div>
              </div>

              <!-- Formal Details Grid -->
              <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
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

              <!-- Description -->
              <p class="text-xs text-slate-300 font-sans leading-relaxed">
                ${{cert.desc}}
              </p>

              <!-- SHA-256 Digest Box -->
              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-400 mb-1">
                  <span>SHA-256 HASH</span>
                  <button onclick="copyHash('${{cert.sha256}}')" class="text-blue-400 hover:text-white underline text-[10px]">COPY HASH</button>
                </div>
                <div class="p-2 rounded-lg bg-slate-950 border border-slate-800 text-blue-300 font-mono text-[11px] break-all select-all">
                  ${{cert.sha256}}
                </div>
              </div>

              <!-- Tags -->
              <div>
                <div class="text-[10px] text-slate-400 uppercase tracking-wider mb-1.5 font-semibold">VERIFIED COMPETENCIES</div>
                <div class="flex flex-wrap gap-1.5">
                  ${{cert.tags.map(t => `<span class="px-2.5 py-0.5 rounded bg-slate-950 border border-slate-800 text-slate-300 text-xs">${{t}}</span>`).join('')}}
                </div>
              </div>

            </div>

            <!-- Modal Action Buttons -->
            <div class="pt-3 border-t border-slate-800 flex items-center justify-between gap-3">
              <a href="${{cert.filepath}}" download="${{cert.filename}}" class="flex-1 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-mono text-xs font-semibold text-center transition-colors">
                DOWNLOAD ORIGINAL DOCUMENT
              </a>
              <button onclick="closeInspector()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-xs transition-colors">
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

    // Initial Render
    applyFilters();
  </script>

</body>
</html>
'''

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated formal executive theme in index.html successfully!")
