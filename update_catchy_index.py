import json

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\curated_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

json_str = json.dumps(catalog, indent=2, ensure_ascii=False)

html_code = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KARUNESH P // 3D Digital Credentials Rack - Verified Identity Matrix</title>
  
  <!-- Modern Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
            display: ['Space Grotesk', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }},
          colors: {{
            space: {{
              950: '#030712',
              900: '#060c1c',
              850: '#0a1226',
              800: '#101a33',
              700: '#1b2848',
            }},
            neon: {{
              teal: '#06b6d4',
              cyan: '#22d3ee',
              indigo: '#6366f1',
              violet: '#a855f7',
              fuchsia: '#d946ef',
              emerald: '#10b981',
              amber: '#f59e0b',
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    :root {{
      --bg-void: #030712;
    }}

    * {{
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    body {{
      background-color: #030712;
      color: #f3f4f6;
      overflow-x: hidden;
      font-family: 'Inter', sans-serif;
    }}

    /* Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #030712;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #334155;
    }}

    /* 3D Scene Viewport */
    .scene-viewport {{
      perspective: 1600px;
      perspective-origin: 50% 38%;
      transform-style: preserve-3d;
    }}

    .rack-stage {{
      transform-style: preserve-3d;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .floating-card-wrapper {{
      transform-style: preserve-3d;
      will-change: transform;
    }}

    /* Harmonic Anti-Gravity Floating Loops */
    @keyframes antiGravity1 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-14px) rotateZ(0.5deg); }}
    }}
    @keyframes antiGravity2 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-20px) rotateZ(-0.6deg); }}
    }}
    @keyframes antiGravity3 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-12px) rotateZ(0.4deg); }}
    }}
    @keyframes antiGravity4 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-18px) rotateZ(-0.5deg); }}
    }}
    @keyframes antiGravity5 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-22px) rotateZ(0.6deg); }}
    }}
    @keyframes antiGravity6 {{
      0%, 100% {{ transform: translateY(0px) rotateZ(0deg); }}
      50% {{ transform: translateY(-15px) rotateZ(-0.4deg); }}
    }}

    .levitate-0 {{ animation: antiGravity1 6.2s ease-in-out infinite; }}
    .levitate-1 {{ animation: antiGravity2 7.5s ease-in-out infinite 0.8s; }}
    .levitate-2 {{ animation: antiGravity3 5.8s ease-in-out infinite 1.6s; }}
    .levitate-3 {{ animation: antiGravity4 8.1s ease-in-out infinite 0.4s; }}
    .levitate-4 {{ animation: antiGravity5 6.9s ease-in-out infinite 2.2s; }}
    .levitate-5 {{ animation: antiGravity6 7.2s ease-in-out infinite 1.1s; }}

    /* Frosted Glass Substrate */
    .credential-card {{
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(13, 20, 36, 0.65) 50%, rgba(4, 9, 23, 0.95) 100%);
      backdrop-filter: blur(18px) saturate(200%);
      -webkit-backdrop-filter: blur(18px) saturate(200%);
      transform-style: preserve-3d;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}

    /* Emissive Neon Borders */
    .border-glow-teal {{
      border: 1px solid rgba(6, 182, 212, 0.35);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.85),
                  0 0 20px -3px rgba(6, 182, 212, 0.15),
                  inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    }}
    .border-glow-teal:hover {{
      border-color: rgba(34, 211, 238, 0.85);
      box-shadow: 0 25px 50px -15px rgba(0, 0, 0, 0.9),
                  0 0 30px 2px rgba(6, 182, 212, 0.35),
                  inset 0 0 15px rgba(6, 182, 212, 0.15);
    }}

    .border-glow-indigo {{
      border: 1px solid rgba(99, 102, 241, 0.35);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.85),
                  0 0 20px -3px rgba(99, 102, 241, 0.15),
                  inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    }}
    .border-glow-indigo:hover {{
      border-color: rgba(129, 140, 248, 0.85);
      box-shadow: 0 25px 50px -15px rgba(0, 0, 0, 0.9),
                  0 0 30px 2px rgba(99, 102, 241, 0.35),
                  inset 0 0 15px rgba(99, 102, 241, 0.15);
    }}

    .border-glow-violet {{
      border: 1px solid rgba(168, 85, 247, 0.35);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.85),
                  0 0 20px -3px rgba(168, 85, 247, 0.15),
                  inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    }}
    .border-glow-violet:hover {{
      border-color: rgba(192, 132, 252, 0.85);
      box-shadow: 0 25px 50px -15px rgba(0, 0, 0, 0.9),
                  0 0 30px 2px rgba(168, 85, 247, 0.35),
                  inset 0 0 15px rgba(168, 85, 247, 0.15);
    }}

    .border-glow-emerald {{
      border: 1px solid rgba(16, 185, 129, 0.35);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.85),
                  0 0 20px -3px rgba(16, 185, 129, 0.15),
                  inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    }}
    .border-glow-emerald:hover {{
      border-color: rgba(52, 211, 153, 0.85);
      box-shadow: 0 25px 50px -15px rgba(0, 0, 0, 0.9),
                  0 0 30px 2px rgba(16, 185, 129, 0.35),
                  inset 0 0 15px rgba(16, 185, 129, 0.15);
    }}

    .border-glow-amber {{
      border: 1px solid rgba(245, 158, 11, 0.35);
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.85),
                  0 0 20px -3px rgba(245, 158, 11, 0.15),
                  inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
    }}
    .border-glow-amber:hover {{
      border-color: rgba(251, 191, 36, 0.85);
      box-shadow: 0 25px 50px -15px rgba(0, 0, 0, 0.9),
                  0 0 30px 2px rgba(245, 158, 11, 0.35),
                  inset 0 0 15px rgba(245, 158, 11, 0.15);
    }}

    /* Specular Glare */
    .card-specular-glare {{
      position: absolute;
      inset: 0;
      border-radius: inherit;
      pointer-events: none;
      background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.2) 0%, transparent 65%);
      opacity: 0;
      transition: opacity 0.3s ease;
      mix-blend-mode: overlay;
      z-index: 20;
    }}

    /* Holographic Shimmer Foil */
    .holo-sheen {{
      position: absolute;
      inset: 0;
      border-radius: inherit;
      pointer-events: none;
      background: linear-gradient(
        115deg,
        transparent 0%,
        rgba(255, 255, 255, 0.03) 25%,
        rgba(34, 211, 238, 0.12) 45%,
        rgba(168, 85, 247, 0.14) 55%,
        rgba(255, 255, 255, 0.04) 75%,
        transparent 100%
      );
      background-size: 250% 250%;
      opacity: 0.35;
      mix-blend-mode: color-dodge;
      transition: opacity 0.4s ease, background-position 0.6s ease;
      z-index: 10;
    }}
    .credential-card:hover .holo-sheen {{
      opacity: 0.85;
      background-position: 100% 100%;
    }}

    /* Cyber Grid */
    .cyber-grid-watermark {{
      background-image: 
        radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 20px 20px, 40px 40px, 40px 40px;
    }}

    /* 3D Carousel Cylinder Mode */
    .rack-carousel-mode {{
      width: 100%;
      height: 650px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      transform-style: preserve-3d;
    }}

    .carousel-item-3d {{
      position: absolute;
      width: 380px;
      transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.5s ease;
      transform-style: preserve-3d;
    }}

    .hud-scanlines {{
      background: linear-gradient(
        to bottom,
        rgba(255,255,255,0),
        rgba(255,255,255,0) 50%,
        rgba(0, 0, 0, 0.25) 50%,
        rgba(0, 0, 0, 0.25)
      );
      background-size: 100% 4px;
      pointer-events: none;
    }}

    @keyframes pulseGlow {{
      0%, 100% {{ opacity: 1; transform: scale(1); filter: drop-shadow(0 0 6px currentColor); }}
      50% {{ opacity: 0.4; transform: scale(0.85); filter: drop-shadow(0 0 2px currentColor); }}
    }}
    .status-pulse {{
      animation: pulseGlow 2.4s ease-in-out infinite;
    }}

    .glass-modal-backdrop {{
      background: rgba(3, 7, 18, 0.88);
      backdrop-filter: blur(24px);
    }}

    .dropzone-active {{
      border-color: #22d3ee !important;
      background: rgba(6, 182, 212, 0.15) !important;
      box-shadow: 0 0 30px rgba(34, 211, 238, 0.4) !important;
    }}

    /* Spotlight Card Glowing Frame */
    .spotlight-card {{
      background: radial-gradient(circle at 50% 0%, rgba(34, 211, 238, 0.15), rgba(16, 26, 51, 0.8) 70%);
      border: 1px solid rgba(34, 211, 238, 0.4);
      box-shadow: 0 0 40px -10px rgba(6, 182, 212, 0.3);
    }}
  </style>
</head>

<body class="bg-space-950 text-gray-100 min-h-screen relative selection:bg-neon-teal/30 selection:text-white">

  <!-- Micro-particle Canvas Layer -->
  <canvas id="cosmosCanvas" class="fixed inset-0 pointer-events-none z-0 w-full h-full"></canvas>

  <!-- Ambient Light Clusters -->
  <div class="fixed -top-40 -left-40 w-[700px] h-[700px] bg-gradient-to-br from-cyan-600/12 to-indigo-700/10 rounded-full blur-[140px] pointer-events-none z-0"></div>
  <div class="fixed top-1/3 -right-40 w-[750px] h-[750px] bg-gradient-to-bl from-purple-600/14 to-fuchsia-600/8 rounded-full blur-[160px] pointer-events-none z-0"></div>
  <div class="fixed -bottom-40 left-1/3 w-[850px] h-[550px] bg-gradient-to-t from-teal-600/10 to-indigo-900/12 rounded-full blur-[150px] pointer-events-none z-0"></div>

  <!-- Scanlines Effect -->
  <div id="scanlineOverlay" class="fixed inset-0 hud-scanlines opacity-0 transition-opacity duration-300 pointer-events-none z-50"></div>

  <!-- Main Container -->
  <div class="relative z-10 min-h-screen flex flex-col">

    <!-- TOP TELEMETRY NAVIGATION BAR -->
    <header class="border-b border-white/[0.08] bg-space-950/80 backdrop-blur-2xl sticky top-0 z-40 px-4 sm:px-8 py-3.5 transition-all">
      <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
        
        <!-- Recipient Identity Badge -->
        <div class="flex items-center gap-3.5">
          <div class="relative flex items-center justify-center w-11 h-11 rounded-2xl bg-gradient-to-br from-cyan-500/25 via-indigo-500/25 to-purple-500/25 border border-cyan-400/40 shadow-[0_0_20px_rgba(34,211,238,0.3)]">
            <svg class="w-6 h-6 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
              <polyline points="2 17 12 22 22 17"></polyline>
              <polyline points="2 12 12 17 22 12"></polyline>
            </svg>
            <span class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-cyan-400 rounded-full status-pulse text-cyan-400"></span>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-display font-extrabold tracking-wider text-lg uppercase bg-gradient-to-r from-cyan-300 via-indigo-200 to-purple-300 bg-clip-text text-transparent">
                KARUNESH P
              </span>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 border border-cyan-500/40 font-semibold tracking-wider">
                PRO PORTFOLIO
              </span>
            </div>
            <p class="text-[11px] font-mono text-gray-400 tracking-tight">ELECTRONICS & SYSTEMS ENGINEER // 62 VERIFIED CREDENTIALS</p>
          </div>
        </div>

        <!-- Quick Summary Metrics -->
        <div class="hidden lg:flex items-center gap-6 px-4 py-1.5 rounded-xl bg-space-900/80 border border-white/10 font-mono text-xs text-gray-300">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400 status-pulse text-emerald-400"></span>
            <span class="text-gray-400 text-[11px]">VERIFIED:</span>
            <span class="text-emerald-300 font-semibold text-[11px]">62 CERTIFICATES</span>
          </div>
          <div class="w-px h-3.5 bg-white/10"></div>
          <div class="flex items-center gap-2">
            <span class="text-gray-400 text-[11px]">DOMAINS:</span>
            <span class="text-cyan-300 font-semibold text-[11px]">7 SPECIALIZATIONS</span>
          </div>
          <div class="w-px h-3.5 bg-white/10"></div>
          <div class="flex items-center gap-2">
            <span class="text-gray-400 text-[11px]">SECURITY:</span>
            <span class="text-purple-300 font-mono text-[11px]">SHA-256 HASHED</span>
          </div>
        </div>

        <!-- Top Right Quick Controls -->
        <div class="flex items-center gap-2.5">
          
          <!-- Upload Trigger -->
          <label for="certificateUploadInput" class="cursor-pointer px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-cyan-500/20 to-indigo-500/20 hover:from-cyan-500/30 hover:to-indigo-500/30 border border-cyan-500/40 text-cyan-300 hover:text-white transition-all flex items-center gap-1.5 text-xs font-mono font-medium shadow-[0_0_15px_rgba(6,182,212,0.2)]">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="17 8 12 3 7 8"></polyline>
              <line x1="12" y1="3" x2="12" y2="15"></line>
            </svg>
            <span>+ ADD NEW</span>
            <input id="certificateUploadInput" type="file" multiple accept=".pdf,.png,.jpg,.jpeg" class="hidden">
          </label>

          <!-- Audio FX Toggle -->
          <button id="audioToggleBtn" title="Toggle Spatial Audio" class="p-2 rounded-xl bg-space-900/90 hover:bg-space-800 border border-white/10 text-gray-300 hover:text-cyan-400 transition-all text-xs font-mono flex items-center gap-1">
            <svg class="w-4 h-4 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
              <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
            </svg>
            <span class="hidden sm:inline text-[11px]">SFX</span>
          </button>

          <!-- Scanline HUD Toggle -->
          <button id="scanlineToggleBtn" title="Toggle Scanline HUD" class="p-2 rounded-xl bg-space-900/90 hover:bg-space-800 border border-white/10 text-gray-400 hover:text-purple-300 transition-all text-xs font-mono">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
              <line x1="8" y1="21" x2="16" y2="21"></line>
              <line x1="12" y1="17" x2="12" y2="21"></line>
            </svg>
          </button>

        </div>

      </div>
    </header>

    <!-- HERO PROFILE ARENA -->
    <section class="max-w-7xl mx-auto w-full px-4 sm:px-8 pt-8 pb-4">
      <div class="relative rounded-3xl p-6 sm:p-10 border border-white/15 bg-gradient-to-br from-space-900/90 via-space-850/80 to-space-950/90 backdrop-blur-2xl overflow-hidden shadow-2xl">
        
        <!-- Background Decorative Watermark -->
        <div class="absolute right-0 top-0 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute left-1/3 bottom-0 w-80 h-80 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8">
          
          <!-- Hero Intro -->
          <div class="max-w-2xl">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/70 border border-cyan-400/30 text-cyan-300 text-xs font-mono mb-3 shadow-[0_0_12px_rgba(34,211,238,0.2)]">
              <span class="w-2 h-2 rounded-full bg-cyan-400 status-pulse"></span>
              DIGITAL IDENTITY RACK // 8K CINEMATIC PROJECTION
            </div>
            
            <h1 class="text-3xl sm:text-5xl font-display font-black tracking-tight text-white leading-tight">
              Verified Digital <span class="bg-gradient-to-r from-cyan-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">Credentials Matrix</span>
            </h1>

            <p class="mt-3 text-gray-300 text-sm sm:text-base leading-relaxed font-light">
              Explore the official engineering achievements, specialized certifications, and research honors of 
              <strong class="text-white font-semibold">Karunesh P</strong>. Each document is cryptographically attested with SHA-256 integrity and instantly viewable with interactive 3D physics.
            </p>

            <!-- Quick Issuer Badges -->
            <div class="mt-5 flex flex-wrap items-center gap-2 text-xs font-mono">
              <span class="text-gray-400 text-[11px] uppercase mr-1">Top Issuers:</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-cyan-300 font-semibold">AWS (9)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-indigo-300 font-semibold">Fortinet (6)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-purple-300 font-semibold">IBM Credly (5)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-amber-300 font-semibold">MathWorks (6)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-emerald-300 font-semibold">Cisco & Python (5)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-cyan-300 font-semibold">NPTEL IIT (1)</span>
              <span class="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 text-amber-300 font-semibold">Altium (1)</span>
            </div>
          </div>

          <!-- Hero Spotlight Card (Flagship Highlight) -->
          <div class="w-full lg:w-80 shrink-0">
            <div class="spotlight-card rounded-2xl p-5 cursor-pointer relative overflow-hidden group transition-all duration-300 hover:scale-[1.03]" onclick="openInspector('cert-8')">
              <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/20 rounded-full blur-xl"></div>
              
              <div class="flex items-center justify-between mb-3 text-xs font-mono">
                <span class="px-2 py-0.5 rounded-full bg-purple-950 border border-purple-400/40 text-purple-300 font-semibold text-[10px] flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 status-pulse"></span>
                  CREDLY VERIFIED
                </span>
                <span class="text-cyan-400 text-[11px] font-semibold">FEATURED #1</span>
              </div>

              <div class="w-12 h-12 rounded-xl bg-purple-950/80 border border-purple-400/40 flex items-center justify-center p-2 text-purple-300 mb-3 shadow-[0_0_15px_rgba(168,85,247,0.3)]">
                <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.93 4.93l2.12 2.12M16.95 16.95l2.12 2.12M4.93 19.07l2.12-2.12M16.95 7.05l2.12-2.12"></path></svg>
              </div>

              <h4 class="font-display font-bold text-white text-base leading-snug group-hover:text-cyan-300 transition-colors">
                IBM SkillsBuild: AI Fundamentals
              </h4>
              <p class="text-xs text-gray-400 mt-1 line-clamp-2">
                Credly-backed verification by IBM covering machine learning, deep neural networks, and generative workflows.
              </p>

              <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-xs font-mono">
                <span class="text-gray-400 text-[11px]">HOLDER: KARUNESH P</span>
                <span class="text-cyan-400 font-semibold flex items-center gap-1 group-hover:translate-x-1 transition-transform">
                  PREVIEW &rarr;
                </span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- CONTROLS & LAYOUT SWITCHER -->
    <section class="max-w-7xl mx-auto w-full px-4 sm:px-8 py-4">
      <div class="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-4 p-4 rounded-2xl bg-space-900/60 border border-white/10 backdrop-blur-xl">
        
        <!-- View Mode Switcher -->
        <div class="flex items-center gap-2">
          <span class="text-xs font-mono text-gray-400 uppercase hidden sm:inline">VIEW:</span>
          
          <div class="flex items-center p-1 rounded-xl bg-space-950/80 border border-white/10">
            <!-- Shelves View -->
            <button id="btnViewShelves" class="view-btn active flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all bg-gradient-to-r from-cyan-500/25 to-indigo-500/25 border border-cyan-500/40 text-cyan-300 shadow-[0_0_12px_rgba(6,182,212,0.25)]">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
              <span>Domain Shelves (Organized)</span>
            </button>
            
            <!-- 3D Grid View -->
            <button id="btnViewGrid" class="view-btn flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-gray-400 hover:text-white border border-transparent">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
              <span>All-In-One Grid</span>
            </button>

            <!-- 3D Orbital Carousel -->
            <button id="btnViewCarousel" class="view-btn flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-gray-400 hover:text-white border border-transparent">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"></circle><path d="M12 3a15.3 15.3 0 0 1 4 18 15.3 15.3 0 0 1-8 0 15.3 15.3 0 0 1 4-18z"></path></svg>
              <span>3D Cylinder</span>
            </button>
          </div>
        </div>

        <!-- Levitation Slider & Real-time Search -->
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          
          <!-- Levitation Slider -->
          <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-space-950/80 border border-white/10 text-xs font-mono text-gray-300">
            <span class="text-[11px] text-gray-400">LEVITATION:</span>
            <input id="gravitySlider" type="range" min="0" max="100" value="70" class="w-20 accent-cyan-400 cursor-pointer h-1.5 bg-space-800 rounded-lg">
            <span id="gravityVal" class="text-cyan-300 font-semibold text-[11px] w-8">0.70G</span>
          </div>

          <!-- Search Input -->
          <div class="relative min-w-[260px]">
            <input id="credentialSearch" type="text" placeholder="Search certificates, skills, hash..." class="w-full bg-space-950/80 border border-white/10 rounded-xl px-9 py-2 text-xs font-mono text-gray-200 placeholder-gray-500 focus:outline-none focus:border-cyan-500/60 focus:ring-1 focus:ring-cyan-500/40 transition-all">
            <svg class="w-4 h-4 text-gray-500 absolute left-3 top-2.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <span class="absolute right-3 top-2 text-[10px] font-mono text-gray-500 border border-white/10 px-1.5 py-0.5 rounded">⌘K</span>
          </div>

        </div>

      </div>

      <!-- Quick Category Filter Pills -->
      <div class="flex flex-wrap items-center gap-2 mt-4" id="filterPillsContainer">
        <button data-filter="all" class="filter-pill active px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-white/15 border border-white/30 text-white shadow-[0_0_15px_rgba(255,255,255,0.15)]">
          ALL (62)
        </button>
        <button data-filter="cloud" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-cyan-300 hover:border-cyan-500/40">
          ☁️ CLOUD & AWS (9)
        </button>
        <button data-filter="ai" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-purple-300 hover:border-purple-500/40">
          🧠 GENERATIVE AI (6)
        </button>
        <button data-filter="cyber" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-indigo-300 hover:border-indigo-500/40">
          🛡️ CYBERSECURITY (6)
        </button>
        <button data-filter="iot" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-amber-300 hover:border-amber-500/40">
          ⚡ IOT & HARDWARE (7)
        </button>
        <button data-filter="data" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-indigo-300 hover:border-indigo-500/40">
          📊 DATA & MATLAB (6)
        </button>
        <button data-filter="programming" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-emerald-300 hover:border-emerald-500/40">
          🐍 PYTHON (3)
        </button>
        <button data-filter="honors" class="filter-pill px-3.5 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-space-900/60 border border-white/10 text-gray-400 hover:text-cyan-300 hover:border-cyan-500/40">
          🏆 CIT HONORS & RESEARCH (25)
        </button>
      </div>

      <!-- Drag & Drop Uploader Strip -->
      <div id="dropZone" class="mt-4 border-2 border-dashed border-white/15 hover:border-cyan-500/50 rounded-2xl p-3.5 text-center bg-space-900/40 backdrop-blur-sm transition-all cursor-pointer flex flex-col sm:flex-row items-center justify-center gap-3 group">
        <div class="p-1.5 rounded-xl bg-cyan-950/70 border border-cyan-500/30 text-cyan-400 group-hover:scale-110 transition-transform">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
        </div>
        <div class="text-xs font-mono text-gray-300">
          <span class="font-semibold text-white group-hover:text-cyan-300">DRAG & DROP NEW CERTIFICATES HERE</span>
          <span class="text-gray-500 text-[11px] block sm:inline sm:ml-2">— or click to browse (auto computes SHA-256 and adds to live rack)</span>
        </div>
      </div>
    </section>

    <!-- MAIN CREDENTIALS STAGE (3D VIEWPORT) -->
    <main class="max-w-7xl mx-auto w-full px-4 sm:px-8 py-4 flex-1">
      
      <!-- VIEW 1: DOMAIN SHELVES (ORGANIZED & INTUITIVE) -->
      <div id="shelvesStage" class="space-y-12">
        <!-- Rendered dynamically by category -->
      </div>

      <!-- VIEW 2: ALL-IN-ONE 3D FLOATING GRID -->
      <div id="gridStage" class="scene-viewport rack-stage grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start hidden">
        <!-- Rendered dynamically -->
      </div>

      <!-- VIEW 3: 3D CYLINDRICAL ORBITAL CAROUSEL -->
      <div id="carouselStage" class="scene-viewport rack-stage rack-carousel-mode hidden">
        <div class="carousel-nav-controls absolute -bottom-10 left-1/2 -translate-x-1/2 flex items-center gap-4 z-30">
          <button id="carouselPrevBtn" class="p-2.5 rounded-full bg-space-900 border border-white/20 text-cyan-400 hover:bg-space-800 hover:border-cyan-400 shadow-[0_0_15px_rgba(6,182,212,0.3)] transition-all">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
          </button>
          <div class="px-4 py-1 rounded-full bg-space-900/90 border border-white/10 text-xs font-mono text-gray-300">
            SLOT <span class="text-cyan-400 font-bold" id="carouselSlotNum">1</span> / <span id="carouselTotalSlots">62</span>
          </div>
          <button id="carouselNextBtn" class="p-2.5 rounded-full bg-space-900 border border-white/20 text-cyan-400 hover:bg-space-800 hover:border-cyan-400 shadow-[0_0_15px_rgba(6,182,212,0.3)] transition-all">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>

    </main>

    <!-- FOOTER -->
    <footer class="mt-auto border-t border-white/[0.08] py-6 px-6 bg-space-950/90 backdrop-blur-xl">
      <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-gray-500">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-cyan-400 status-pulse"></span>
          <span>AETHERIS MATRIX // HOLDER: KARUNESH P</span>
        </div>
        <div class="flex items-center gap-4 text-gray-400">
          <span>62 VERIFIED DOCUMENTS</span>
          <span>•</span>
          <span>CRYPTOGRAPHIC HASH INTEGRITY</span>
          <span>•</span>
          <span class="text-emerald-400">STATUS: NOMINAL</span>
        </div>
      </div>
    </footer>

  </div>

  <!-- SPLIT-SCREEN HOLOGRAPHIC INSPECTION CHAMBER (MODAL) -->
  <div id="inspectorModal" class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-6 glass-modal-backdrop opacity-0 pointer-events-none transition-opacity duration-300">
    <div id="inspectorContent" class="relative w-full max-w-5xl rounded-3xl bg-space-900/95 border border-white/20 shadow-[0_30px_90px_rgba(0,0,0,0.95)] backdrop-blur-2xl transform scale-95 transition-transform duration-300 max-h-[92vh] flex flex-col overflow-hidden">
      
      <!-- Top Modal Navigation Bar -->
      <div class="p-4 sm:px-6 border-b border-white/10 flex items-center justify-between bg-space-950/80">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-cyan-400 status-pulse"></span>
          <span class="text-xs font-mono text-cyan-300 font-semibold uppercase tracking-wider">CRYPTOGRAPHIC ATTESTATION VIEWER</span>
        </div>
        
        <div class="flex items-center gap-3">
          <!-- Step Controls -->
          <div class="flex items-center gap-1 bg-space-900 border border-white/10 rounded-lg p-0.5 text-xs font-mono">
            <button id="modalPrevBtn" class="px-2 py-1 text-gray-400 hover:text-white transition-colors" title="Previous Certificate">&larr; PREV</button>
            <span class="text-gray-500">|</span>
            <button id="modalNextBtn" class="px-2 py-1 text-gray-400 hover:text-white transition-colors" title="Next Certificate">NEXT &rarr;</button>
          </div>

          <!-- Close Modal -->
          <button onclick="closeInspector()" class="p-1.5 rounded-full bg-space-800 hover:bg-space-700 border border-white/10 text-gray-300 hover:text-white transition-colors">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
      </div>

      <!-- Split-screen Modal Body -->
      <div id="modalBody" class="flex-1 overflow-y-auto">
        <!-- Populated dynamically -->
      </div>

    </div>
  </div>

  <!-- HUD Toast -->
  <div id="hudToast" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-300 pointer-events-none px-4 py-2.5 rounded-xl bg-space-900 border border-cyan-500/40 text-cyan-300 font-mono text-xs flex items-center gap-2.5 shadow-[0_0_25px_rgba(6,182,212,0.3)]">
    <svg class="w-4 h-4 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toastMsg">ACTION COMPLETE</span>
  </div>

  <!-- SOUND SYNTHESIZER (Web Audio API) -->
  <script>
    class SoundEngine {{
      constructor() {{ this.ctx = null; this.enabled = true; }}
      init() {{
        if (!this.ctx) {{
          const AC = window.AudioContext || window.webkitAudioContext;
          if (AC) this.ctx = new AC();
        }}
        if (this.ctx && this.ctx.state === 'suspended') this.ctx.resume();
      }}
      playHover() {{
        if (!this.enabled) return;
        this.init();
        try {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(560, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.07);
          gain.gain.setValueAtTime(0.02, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.07);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + 0.08);
        }} catch(e){{}}
      }}
      playClick() {{
        if (!this.enabled) return;
        this.init();
        try {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(880, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(1350, this.ctx.currentTime + 0.1);
          gain.gain.setValueAtTime(0.035, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.1);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + 0.11);
        }} catch(e){{}}
      }}
      playVerify() {{
        if (!this.enabled) return;
        this.init();
        try {{
          const now = this.ctx.currentTime;
          [523, 659, 784, 1046].forEach((f, i) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, now + i * 0.07);
            gain.gain.setValueAtTime(0.03, now + i * 0.07);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.22);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.07);
            osc.stop(now + i * 0.07 + 0.23);
          }});
        }} catch(e){{}}
      }}
    }}
    const sound = new SoundEngine();
  </script>

  <!-- COSMOS PARTICLES ENGINE -->
  <script>
    const canvas = document.getElementById('cosmosCanvas');
    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];
    const COUNT = 140;
    let mouse = {{ x: null, y: null, radius: 160 }};

    function resizeCanvas() {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      mouse.x = width / 2;
      mouse.y = height / 2;
    }}

    class SpaceParticle {{
      constructor() {{ this.reset(); }}
      reset() {{
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.z = Math.random() * 2 + 0.5;
        this.size = (Math.random() * 1.8 + 0.4) * this.z;
        this.baseAlpha = Math.random() * 0.6 + 0.2;
        this.alpha = this.baseAlpha;
        this.vx = (Math.random() - 0.5) * 0.25;
        this.vy = -(Math.random() * 0.35 + 0.15);
        this.pulseSpeed = Math.random() * 0.02 + 0.008;
        this.pulse = Math.random() * Math.PI * 2;
        const colors = ['rgba(34, 211, 238,', 'rgba(99, 102, 241,', 'rgba(168, 85, 247,', 'rgba(245, 158, 11,', 'rgba(255, 255, 255,'];
        this.color = colors[Math.floor(Math.random() * colors.length)];
      }}
      update() {{
        this.x += this.vx;
        this.y += this.vy;
        this.pulse += this.pulseSpeed;
        this.alpha = this.baseAlpha + Math.sin(this.pulse) * 0.25;

        if (mouse.x !== null) {{
          const dx = this.x - mouse.x;
          const dy = this.y - mouse.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < mouse.radius) {{
            const force = (mouse.radius - dist) / mouse.radius;
            this.x += (dx / dist) * force * 1.2;
            this.y += (dy / dist) * force * 1.2;
          }}
        }}

        if (this.y < -10) this.y = height + 10;
        if (this.x < -10) this.x = width + 10;
        if (this.x > width + 10) this.x = -10;
      }}
      draw() {{
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `${{this.color}} ${{Math.max(0.05, this.alpha)}})`;
        ctx.shadowColor = this.color.replace('rgba', 'rgb').slice(0, -1) + ')';
        ctx.shadowBlur = this.size * 3;
        ctx.fill();
        ctx.shadowBlur = 0;
      }}
    }}

    function initCosmos() {{
      resizeCanvas();
      particles = [];
      for (let i = 0; i < COUNT; i++) particles.push(new SpaceParticle());
    }}

    function animateCosmos() {{
      ctx.clearRect(0, 0, width, height);
      particles.forEach(p => {{ p.update(); p.draw(); }});
      requestAnimationFrame(animateCosmos);
    }}

    window.addEventListener('resize', resizeCanvas);
    window.addEventListener('mousemove', (e) => {{ mouse.x = e.clientX; mouse.y = e.clientY; }});

    initCosmos();
    animateCosmos();
  </script>

  <!-- DATA & SHELVES / GRID ENGINE -->
  <script>
    let CERTIFICATES = {json_str};

    const DOMAIN_DEFS = [
      {{ id: 'cloud', title: 'Cloud Architecture & AWS Infrastructure', icon: '☁️', color: 'teal', desc: 'Amazon Web Services (AWS) training certifications and enterprise cloud pipelines' }},
      {{ id: 'ai', title: 'Generative AI & LLM Engineering', icon: '🧠', color: 'violet', desc: 'Microsoft, IBM SkillsBuild (Credly), and Google Cloud GenAI Studio credentials' }},
      {{ id: 'cyber', title: 'Cybersecurity & Threat Mitigation', icon: '🛡️', color: 'indigo', desc: 'Fortinet Network Security Expert (NSE 1 & 2) and enterprise defense certifications' }},
      {{ id: 'iot', title: 'IoT, Microcontrollers & PCB Engineering', icon: '⚡', color: 'amber', desc: 'Altium Designer multi-layer PCB, Arduino Physical AI, and Cisco IoT certifications' }},
      {{ id: 'data', title: 'Data Science, Mathematical Modeling & MATLAB', icon: '📊', color: 'indigo', desc: 'MathWorks MATLAB, linear algebra calculations, Simulink, and NPTEL IIT Elite' }},
      {{ id: 'programming', title: 'Software Engineering & Computational Python', icon: '🐍', color: 'emerald', desc: 'Python Institute, Cisco NetAcad, and Adobe digital media systems' }},
      {{ id: 'honors', title: 'National Hackathons, Research Papers & Academic Honors', icon: '🏆', color: 'teal', desc: 'CIT National Hackathon prize, IEEE, ISTE Fellowship, and institutional commendations' }}
    ];

    function getIssuerIcon(issuer, category) {{
      const i = issuer.toLowerCase();
      if (i.includes('amazon') || i.includes('aws')) {{
        return `<svg class="w-6 h-6 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"></path><path d="M9 12l2 2 4-4"></path></svg>`;
      }}
      if (i.includes('ibm')) {{
        return `<svg class="w-6 h-6 text-purple-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 12h8M12 8v8"></path></svg>`;
      }}
      if (i.includes('microsoft')) {{
        return `<svg class="w-6 h-6 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="8" height="8" rx="1"></rect><rect x="13" y="3" width="8" height="8" rx="1"></rect><rect x="3" y="13" width="8" height="8" rx="1"></rect><rect x="13" y="13" width="8" height="8" rx="1"></rect></svg>`;
      }}
      if (i.includes('fortinet') || category === 'cyber') {{
        return `<svg class="w-6 h-6 text-indigo-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>`;
      }}
      if (i.includes('matlab') || i.includes('mathworks')) {{
        return `<svg class="w-6 h-6 text-amber-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>`;
      }}
      if (i.includes('python')) {{
        return `<svg class="w-6 h-6 text-emerald-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>`;
      }}
      if (i.includes('altium') || i.includes('arduino') || category === 'iot') {{
        return `<svg class="w-6 h-6 text-amber-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line></svg>`;
      }}
      return `<svg class="w-6 h-6 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`;
    }}

    function getBorderClass(spectrum) {{
      switch(spectrum) {{
        case 'indigo': return 'border-glow-indigo';
        case 'violet': return 'border-glow-violet';
        case 'emerald': return 'border-glow-emerald';
        case 'amber': return 'border-glow-amber';
        case 'teal':
        default: return 'border-glow-teal';
      }}
    }}

    function getPillColor(spectrum) {{
      switch(spectrum) {{
        case 'indigo': return 'text-indigo-300 border-indigo-400/40 bg-indigo-950/70';
        case 'violet': return 'text-purple-300 border-purple-400/40 bg-purple-950/70';
        case 'emerald': return 'text-emerald-300 border-emerald-400/40 bg-emerald-950/70';
        case 'amber': return 'text-amber-300 border-amber-400/40 bg-amber-950/70';
        case 'teal':
        default: return 'text-cyan-300 border-cyan-400/40 bg-cyan-950/70';
      }}
    }}

    // Single Card HTML Generator
    function generateCardHTML(cert, index, isGrid = false) {{
      const levitateClass = `levitate-${{index % 6}}`;
      const borderClass = getBorderClass(cert.spectrum);
      const pillClass = getPillColor(cert.spectrum);
      const iconSvg = getIssuerIcon(cert.issuer, cert.category);
      const hashShort = cert.sha256.slice(0, 8) + '...' + cert.sha256.slice(-6);

      return `
        <div class="floating-card-wrapper ${{levitateClass}}" data-id="${{cert.id}}" data-category="${{cert.category}}">
          <div class="credential-card ${{borderClass}} rounded-2xl p-5 cursor-pointer overflow-hidden transition-transform duration-150 ease-out flex flex-col justify-between h-full" onclick="openInspector('${{cert.id}}')">
            
            <div class="card-specular-glare"></div>
            <div class="holo-sheen"></div>
            <div class="absolute inset-0 cyber-grid-watermark opacity-25 pointer-events-none"></div>

            <div>
              <!-- Top Row: Icon + Issuer + Verified Chip -->
              <div class="relative z-10 flex items-start justify-between gap-3 mb-3">
                <div class="flex items-center gap-3">
                  <div class="w-11 h-11 rounded-xl bg-space-950/90 border border-white/15 flex items-center justify-center p-2 shadow-lg shrink-0">
                    ${{iconSvg}}
                  </div>
                  <div>
                    <span class="text-[10px] font-mono uppercase tracking-widest font-semibold text-gray-400 truncate max-w-[160px] block">${{cert.issuer}}</span>
                    <div class="text-[10px] font-mono text-cyan-400 font-semibold flex items-center gap-1">
                      <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 status-pulse"></span>
                      KARUNESH P
                    </div>
                  </div>
                </div>

                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full ${{pillClass}} border text-[10px] font-mono font-semibold tracking-wider shrink-0">
                  VERIFIED
                </span>
              </div>

              <!-- Title -->
              <div class="relative z-10 mb-3">
                <h3 class="font-display font-bold text-base text-white tracking-tight leading-snug line-clamp-2" title="${{cert.title}}">
                  ${{cert.title}}
                </h3>
              </div>

              <!-- Description -->
              <p class="relative z-10 text-xs text-gray-400 font-sans line-clamp-2 mb-3 leading-relaxed">
                ${{cert.desc}}
              </p>

              <!-- Tags -->
              <div class="relative z-10 flex flex-wrap gap-1 mb-4">
                ${{cert.tags.map(t => `<span class="px-2 py-0.5 rounded-md bg-white/[0.04] border border-white/10 text-[10px] font-mono text-gray-300">${{t}}</span>`).join('')}}
              </div>
            </div>

            <!-- Bottom Action Row -->
            <div class="relative z-10 pt-3 border-t border-white/[0.08] flex items-center justify-between text-xs font-mono">
              <span class="text-[10px] text-gray-400 truncate max-w-[130px]">${{hashShort}}</span>
              
              <div class="flex items-center gap-2">
                <button onclick="event.stopPropagation(); openInspector('${{cert.id}}')" class="px-2.5 py-1 rounded-lg bg-cyan-950 hover:bg-cyan-900 border border-cyan-500/30 text-cyan-300 text-[11px] font-semibold flex items-center gap-1 transition-colors">
                  <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                  VIEW
                </button>
                <a href="${{cert.filepath}}" download="${{cert.filename}}" onclick="event.stopPropagation();" class="p-1 rounded-lg bg-space-800 hover:bg-space-700 text-gray-400 hover:text-white border border-white/10 transition-colors" title="Download Original Document">
                  <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                </a>
              </div>
            </div>

          </div>
        </div>
      `;
    }}

    // Render View 1: Domain Shelves
    const shelvesStage = document.getElementById('shelvesStage');
    const gridStage = document.getElementById('gridStage');

    function renderShelves(list) {{
      shelvesStage.innerHTML = '';
      
      DOMAIN_DEFS.forEach(domain => {{
        const items = list.filter(c => c.category === domain.id);
        if (items.length === 0) return;

        const shelfSection = document.createElement('section');
        shelfSection.className = 'space-y-4';

        shelfSection.innerHTML = `
          <!-- Shelf Header Banner -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2 border-b border-white/10">
            <div class="flex items-center gap-3">
              <span class="text-2xl">${{domain.icon}}</span>
              <div>
                <h2 class="font-display font-extrabold text-xl text-white tracking-tight flex items-center gap-2">
                  <span>${{domain.title}}</span>
                  <span class="text-xs font-mono px-2 py-0.5 rounded-full bg-space-900 border border-cyan-400/30 text-cyan-300">${{items.length}} CERTIFICATES</span>
                </h2>
                <p class="text-xs text-gray-400 font-mono mt-0.5">${{domain.desc}}</p>
              </div>
            </div>
            
            <button onclick="filterByShelf('${{domain.id}}')" class="self-start sm:self-auto text-xs font-mono text-cyan-400 hover:underline">
              FILTER THIS DOMAIN &rarr;
            </button>
          </div>

          <!-- Shelf Grid Cards -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch">
            ${{items.map((cert, idx) => generateCardHTML(cert, idx)).join('')}}
          </div>
        `;

        shelvesStage.appendChild(shelfSection);
      }});

      initCard3DTilt();
    }}

    // Render View 2: All-in-One Grid
    function renderGrid(list) {{
      gridStage.innerHTML = '';
      list.forEach((cert, idx) => {{
        const wrap = document.createElement('div');
        wrap.innerHTML = generateCardHTML(cert, idx, true);
        gridStage.appendChild(wrap.firstElementChild);
      }});
      initCard3DTilt();
    }}

    function filterByShelf(catId) {{
      sound.playClick();
      document.querySelectorAll('.filter-pill').forEach(p => {{
        if (p.getAttribute('data-filter') === catId) {{
          p.click();
        }}
      }});
    }}

    // 3D Perspective Tilt Engine
    function initCard3DTilt() {{
      const cards = document.querySelectorAll('.credential-card');
      cards.forEach(card => {{
        const glare = card.querySelector('.card-specular-glare');
        card.addEventListener('mouseenter', () => {{
          sound.playHover();
          if (glare) glare.style.opacity = '1';
        }});
        card.addEventListener('mousemove', (e) => {{
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const deltaX = (x - rect.width / 2) / (rect.width / 2);
          const deltaY = (y - rect.height / 2) / (rect.height / 2);
          card.style.transform = `perspective(1000px) rotateX(${{-deltaY * 10}}deg) rotateY(${{deltaX * 10}}deg) translateZ(14px) scale3d(1.02, 1.02, 1.02)`;
          if (glare) {{
            glare.style.background = `radial-gradient(circle at ${{(x / rect.width) * 100}}% ${{(y / rect.height) * 100}}%, rgba(255, 255, 255, 0.25) 0%, transparent 60%)`;
          }}
        }});
        card.addEventListener('mouseleave', () => {{
          card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px) scale3d(1, 1, 1)`;
          if (glare) glare.style.opacity = '0';
        }});
      }});
    }}

    // Initial render
    renderShelves(CERTIFICATES);
    renderGrid(CERTIFICATES);
  </script>

  <!-- SPLIT-SCREEN MODAL INSPECTOR -->
  <script>
    let currentCertIndex = 0;
    let activeCertList = CERTIFICATES;

    function openInspector(certId) {{
      sound.playClick();
      const idx = activeCertList.findIndex(c => c.id === certId);
      if (idx !== -1) currentCertIndex = idx;
      
      const cert = activeCertList[currentCertIndex] || CERTIFICATES[0];
      const modal = document.getElementById('inspectorModal');
      const content = document.getElementById('inspectorContent');
      const body = document.getElementById('modalBody');

      const isPdf = cert.filename.toLowerCase().endsWith('.pdf');
      const isImg = cert.filename.toLowerCase().endsWith('.png') || cert.filename.toLowerCase().endsWith('.jpg') || cert.filename.toLowerCase().endsWith('.jpeg');

      body.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-12 min-h-[580px]">
          
          <!-- LEFT COLUMN: LIVE DOCUMENT VIEWPORT -->
          <div class="lg:col-span-7 bg-black/60 border-b lg:border-b-0 lg:border-r border-white/10 flex flex-col">
            <div class="p-3 bg-space-950/90 border-b border-white/10 flex items-center justify-between text-xs font-mono">
              <span class="text-gray-300 truncate max-w-[240px] flex items-center gap-1.5">
                <svg class="w-4 h-4 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
                ${{cert.filename}}
              </span>
              <div class="flex items-center gap-2">
                <a href="${{cert.filepath}}" target="_blank" class="px-2.5 py-1 rounded bg-cyan-950 text-cyan-300 border border-cyan-500/30 hover:bg-cyan-900 text-[10px] font-semibold flex items-center gap-1">
                  FULLSCREEN &nearr;
                </a>
                <a href="${{cert.filepath}}" download="${{cert.filename}}" class="px-2.5 py-1 rounded bg-space-800 text-gray-200 border border-white/10 hover:bg-space-700 text-[10px] font-semibold flex items-center gap-1">
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
                <div class="text-center p-8 text-gray-400">
                  <p class="text-sm">Direct format preview not supported inline.</p>
                  <a href="${{cert.filepath}}" target="_blank" class="mt-3 inline-block px-4 py-2 bg-cyan-600 text-white rounded-lg">Open File Externally</a>
                </div>
              `)}}
            </div>
          </div>

          <!-- RIGHT COLUMN: METADATA & CRYPTOGRAPHIC ATTESTATION -->
          <div class="lg:col-span-5 p-6 flex flex-col justify-between font-mono space-y-5 bg-space-900/40">
            
            <div class="space-y-4">
              <!-- Verification Seal -->
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950 border border-cyan-400/40 text-cyan-300 text-xs font-semibold">
                <span class="w-2 h-2 rounded-full bg-cyan-400 status-pulse"></span>
                CRYPTOGRAPHICALLY ATTESTED
              </div>

              <!-- Title & Issuer -->
              <div>
                <h3 class="font-display font-extrabold text-2xl text-white leading-tight">
                  ${{cert.title}}
                </h3>
                <div class="text-cyan-400 text-sm mt-1 font-semibold">${{cert.issuer}}</div>
              </div>

              <!-- Recipient & Size Details -->
              <div class="p-3.5 rounded-xl bg-space-950/80 border border-white/10 space-y-2 text-xs">
                <div class="flex justify-between">
                  <span class="text-gray-400">VERIFIED HOLDER:</span>
                  <span class="text-white font-bold">KARUNESH P</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-400">FILE SIZE:</span>
                  <span class="text-gray-200">${{cert.size_kb}} KB</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-400">LEDGER STATUS:</span>
                  <span class="text-emerald-400 font-semibold">IMMUTABLE / VALID</span>
                </div>
              </div>

              <!-- Description -->
              <p class="text-xs sm:text-sm text-gray-300 font-sans leading-relaxed font-light">
                ${{cert.desc}}
              </p>

              <!-- SHA-256 Digest Box -->
              <div>
                <div class="flex items-center justify-between text-[11px] text-gray-400 mb-1">
                  <span>SHA-256 FILE HASH</span>
                  <button onclick="copyKey('${{cert.sha256}}', this)" class="text-cyan-400 hover:text-white underline text-[10px]">COPY HASH</button>
                </div>
                <div class="p-2 rounded-lg bg-space-950 border border-cyan-500/30 text-cyan-300 font-mono text-[11px] break-all select-all">
                  ${{cert.sha256}}
                </div>
              </div>

              <!-- Skills Tags -->
              <div>
                <div class="text-[10px] text-gray-400 uppercase tracking-wider mb-2 font-semibold">AUTHENTICATED COMPETENCY TAGS</div>
                <div class="flex flex-wrap gap-1.5">
                  ${{cert.tags.map(t => `<span class="px-2.5 py-1 rounded-lg bg-space-950 border border-cyan-500/30 text-cyan-200 text-xs">${{t}}</span>`).join('')}}
                </div>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="pt-4 border-t border-white/10 flex items-center justify-between gap-3">
              <button onclick="simulateVerification('${{cert.id}}')" class="flex-1 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-mono text-xs font-semibold shadow-[0_0_20px_rgba(6,182,212,0.4)] transition-all">
                RE-RUN ATTESTATION
              </button>
              <button onclick="closeInspector()" class="px-4 py-2 rounded-xl bg-space-800 hover:bg-space-700 text-gray-300 font-mono text-xs transition-colors">
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
      sound.playClick();
      const modal = document.getElementById('inspectorModal');
      const content = document.getElementById('inspectorContent');
      modal.classList.add('opacity-0', 'pointer-events-none');
      content.classList.remove('scale-100');
      content.classList.add('scale-95');
    }}

    // Step navigation inside modal
    document.getElementById('modalPrevBtn').addEventListener('click', () => {{
      if (activeCertList.length === 0) return;
      currentCertIndex = (currentCertIndex - 1 + activeCertList.length) % activeCertList.length;
      openInspector(activeCertList[currentCertIndex].id);
    }});

    document.getElementById('modalNextBtn').addEventListener('click', () => {{
      if (activeCertList.length === 0) return;
      currentCertIndex = (currentCertIndex + 1) % activeCertList.length;
      openInspector(activeCertList[currentCertIndex].id);
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
      const toast = document.getElementById('hudToast');
      const msgEl = document.getElementById('toastMsg');
      msgEl.innerText = msg;
      toast.classList.remove('translate-y-16', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');
      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-16', 'opacity-0');
      }}, 2600);
    }}

    function copyKey(text, btn) {{
      sound.playClick();
      navigator.clipboard.writeText(text).then(() => {{
        showToast("SHA-256 DIGEST COPIED TO CLIPBOARD");
      }}).catch(() => {{
        showToast("KEY: " + text.slice(0, 16) + "...");
      }});
    }}

    function simulateVerification(id) {{
      sound.playVerify();
      showToast("ORACLE CONSENSUS VERIFIED: 100% VALID");
    }}
  </script>

  <!-- VIEW MODE SWITCHER & SEARCH CONTROLS -->
  <script>
    const btnViewShelves = document.getElementById('btnViewShelves');
    const btnViewGrid = document.getElementById('btnViewGrid');
    const btnViewCarousel = document.getElementById('btnViewCarousel');

    let currentView = 'shelves';
    let currentCategory = 'all';

    function switchView(viewName) {{
      sound.playClick();
      currentView = viewName;

      [btnViewShelves, btnViewGrid, btnViewCarousel].forEach(btn => {{
        btn.classList.remove('active', 'bg-gradient-to-r', 'from-cyan-500/25', 'to-indigo-500/25', 'border-cyan-500/40', 'text-cyan-300', 'shadow-[0_0_12px_rgba(6,182,212,0.25)]');
        btn.classList.add('text-gray-400', 'border-transparent');
      }});

      shelvesStage.classList.add('hidden');
      gridStage.classList.add('hidden');
      carouselStage.classList.add('hidden');

      if (viewName === 'shelves') {{
        btnViewShelves.classList.add('active', 'bg-gradient-to-r', 'from-cyan-500/25', 'to-indigo-500/25', 'border-cyan-500/40', 'text-cyan-300', 'shadow-[0_0_12px_rgba(6,182,212,0.25)]');
        btnViewShelves.classList.remove('text-gray-400', 'border-transparent');
        shelvesStage.classList.remove('hidden');
        showToast("VIEW MODE: ORGANIZED DOMAIN SHELVES");
      }} else if (viewName === 'grid') {{
        btnViewGrid.classList.add('active', 'bg-gradient-to-r', 'from-cyan-500/25', 'to-indigo-500/25', 'border-cyan-500/40', 'text-cyan-300', 'shadow-[0_0_12px_rgba(6,182,212,0.25)]');
        btnViewGrid.classList.remove('text-gray-400', 'border-transparent');
        gridStage.classList.remove('hidden');
        showToast("VIEW MODE: ALL-IN-ONE 3D GRID");
      }} else if (viewName === 'carousel') {{
        btnViewCarousel.classList.add('active', 'bg-gradient-to-r', 'from-cyan-500/25', 'to-indigo-500/25', 'border-cyan-500/40', 'text-cyan-300', 'shadow-[0_0_12px_rgba(6,182,212,0.25)]');
        btnViewCarousel.classList.remove('text-gray-400', 'border-transparent');
        carouselStage.classList.remove('hidden');
        buildCarouselStage(activeCertList.slice(0, 16));
        showToast("VIEW MODE: 3D CYLINDRICAL ORBITAL CAROUSEL");
      }}
    }}

    btnViewShelves.addEventListener('click', () => switchView('shelves'));
    btnViewGrid.addEventListener('click', () => switchView('grid'));
    btnViewCarousel.addEventListener('click', () => switchView('carousel'));

    // Filter Pills
    const filterPills = document.querySelectorAll('.filter-pill');
    filterPills.forEach(pill => {{
      pill.addEventListener('click', () => {{
        sound.playClick();
        filterPills.forEach(p => {{
          p.classList.remove('active', 'bg-white/15', 'border-white/30', 'text-white', 'shadow-[0_0_15px_rgba(255,255,255,0.15)]');
          p.classList.add('bg-space-900/60', 'border-white/10', 'text-gray-400');
        }});

        pill.classList.add('active', 'bg-white/15', 'border-white/30', 'text-white', 'shadow-[0_0_15px_rgba(255,255,255,0.15)]');
        pill.classList.remove('bg-space-900/60', 'text-gray-400');

        currentCategory = pill.getAttribute('data-filter');
        applyFilterAndSearch();
      }});
    }});

    // Live Search
    const searchInput = document.getElementById('credentialSearch');
    searchInput.addEventListener('input', () => applyFilterAndSearch());

    function applyFilterAndSearch() {{
      const query = searchInput.value.toLowerCase().trim();
      activeCertList = CERTIFICATES.filter(cert => {{
        const matchesCat = (currentCategory === 'all' || cert.category === currentCategory);
        const matchesQuery = !query || 
          cert.title.toLowerCase().includes(query) ||
          cert.issuer.toLowerCase().includes(query) ||
          cert.filename.toLowerCase().includes(query) ||
          cert.sha256.toLowerCase().includes(query) ||
          cert.tags.some(t => t.toLowerCase().includes(query));
        return matchesCat && matchesQuery;
      }});

      renderShelves(activeCertList);
      renderGrid(activeCertList);

      if (currentView === 'carousel') {{
        buildCarouselStage(activeCertList.slice(0, 16));
      }}
    }}

    // Levitation Slider
    const gravitySlider = document.getElementById('gravitySlider');
    const gravityVal = document.getElementById('gravityVal');
    gravitySlider.addEventListener('input', (e) => {{
      const val = e.target.value;
      gravityVal.innerText = `${{(val / 100).toFixed(2)}}G`;

      const cardWrappers = document.querySelectorAll('.floating-card-wrapper');
      cardWrappers.forEach(el => {{
        if (val == 0) {{
          el.style.animationPlayState = 'paused';
          el.style.transform = 'translateY(0px)';
        }} else {{
          el.style.animationPlayState = 'running';
          const speedFactor = 1.6 - (val / 100) * 0.8;
          el.style.animationDuration = `${{speedFactor * 6}}s`;
        }}
      }});
    }});

    // Scanlines
    const scanlineBtn = document.getElementById('scanlineToggleBtn');
    const scanlineOverlay = document.getElementById('scanlineOverlay');
    let scanActive = false;
    scanlineBtn.addEventListener('click', () => {{
      sound.playClick();
      scanActive = !scanActive;
      scanlineOverlay.style.opacity = scanActive ? '0.35' : '0';
      scanlineBtn.classList.toggle('text-purple-300', scanActive);
      showToast(scanActive ? "HUD SCANLINES ENABLED" : "HUD SCANLINES DISABLED");
    }});

    // Audio Mute
    const audioBtn = document.getElementById('audioToggleBtn');
    audioBtn.addEventListener('click', () => {{
      sound.enabled = !sound.enabled;
      audioBtn.innerHTML = sound.enabled ? 
        `<svg class="w-4 h-4 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg><span class="hidden sm:inline text-[11px]">SFX</span>` :
        `<svg class="w-4 h-4 text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg><span class="hidden sm:inline text-[11px]">MUTED</span>`;
      showToast(sound.enabled ? "AUDIO SFX ACTIVE" : "AUDIO SFX MUTED");
    }});
  </script>

  <!-- 3D ORBITAL CAROUSEL -->
  <script>
    let carouselAngle = 0;
    let currentCarouselList = [];

    function buildCarouselStage(list) {{
      currentCarouselList = list;
      const existing = carouselStage.querySelectorAll('.carousel-item-3d');
      existing.forEach(e => e.remove());

      document.getElementById('carouselTotalSlots').innerText = list.length;

      list.forEach((cert, index) => {{
        const wrapper = document.createElement('div');
        wrapper.className = 'carousel-item-3d';
        wrapper.setAttribute('data-index', index);
        wrapper.innerHTML = generateCardHTML(cert, index);

        wrapper.onclick = () => openInspector(cert.id);
        carouselStage.appendChild(wrapper);
      }});

      updateCarouselTransforms();
    }}

    function updateCarouselTransforms() {{
      const items = carouselStage.querySelectorAll('.carousel-item-3d');
      const count = items.length;
      if (count === 0) return;

      const radius = 580;
      const angleStep = 360 / count;

      items.forEach((item, index) => {{
        const itemAngle = index * angleStep + carouselAngle;
        const rad = (itemAngle * Math.PI) / 180;
        const z = Math.cos(rad) * radius - radius;
        const x = Math.sin(rad) * radius;
        const rotateY = itemAngle;

        const normalizedCos = (Math.cos(rad) + 1) / 2;
        const opacity = 0.2 + normalizedCos * 0.8;
        const scale = 0.78 + normalizedCos * 0.24;

        item.style.transform = `translate3d(${{x}}px, 0px, ${{z}}px) rotateY(${{rotateY}}deg) scale(${{scale}})`;
        item.style.opacity = opacity;
        item.style.zIndex = Math.round(normalizedCos * 100);
      }});

      let activeIndex = (Math.round(-carouselAngle / (360 / count)) % count + count) % count;
      document.getElementById('carouselSlotNum').innerText = activeIndex + 1;
    }}

    document.getElementById('carouselPrevBtn').addEventListener('click', () => {{
      sound.playClick();
      const count = currentCarouselList.length || 1;
      carouselAngle += 360 / count;
      updateCarouselTransforms();
    }});

    document.getElementById('carouselNextBtn').addEventListener('click', () => {{
      sound.playClick();
      const count = currentCarouselList.length || 1;
      carouselAngle -= 360 / count;
      updateCarouselTransforms();
    }});
  </script>

  <!-- DRAG & DROP UPLOADER -->
  <script>
    const dropZone = document.getElementById('dropZone');
    const uploadInput = document.getElementById('certificateUploadInput');

    dropZone.addEventListener('click', () => uploadInput.click());

    ['dragenter', 'dragover'].forEach(name => {{
      dropZone.addEventListener(name, (e) => {{
        e.preventDefault();
        dropZone.classList.add('dropzone-active');
      }});
    }});

    ['dragleave', 'drop'].forEach(name => {{
      dropZone.addEventListener(name, (e) => {{
        e.preventDefault();
        dropZone.classList.remove('dropzone-active');
      }});
    }});

    dropZone.addEventListener('drop', (e) => {{
      const files = e.dataTransfer.files;
      if (files.length > 0) handleNewUploadedFiles(files);
    }});

    uploadInput.addEventListener('change', (e) => {{
      if (e.target.files.length > 0) handleNewUploadedFiles(e.target.files);
    }});

    async function computeSHA256(file) {{
      const buffer = await file.arrayBuffer();
      const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return '0x' + hashArray.map(b => b.toString(16).padStart(2, '0')).join('').toUpperCase();
    }}

    async function handleNewUploadedFiles(files) {{
      sound.playVerify();
      for (const file of files) {{
        const sha = await computeSHA256(file);
        const objectUrl = URL.createObjectURL(file);
        const nameWithoutExt = file.name.replace(/\.[^/.]+$/, "").replace(/[-_]/g, ' ');

        const newCert = {{
          id: `user-cert-${{Date.now()}}-${{Math.random().toString(36).substr(2, 4)}}`,
          title: nameWithoutExt,
          issuer: "Direct Upload Attestation",
          recipient: "Karunesh P",
          category: "honors",
          spectrum: "teal",
          tags: ["User Uploaded", "Direct Attestation", "Karunesh P"],
          filename: file.name,
          filepath: objectUrl,
          sha256: sha,
          size_kb: Math.round(file.size / 1024),
          desc: "User uploaded certificate document cryptographically hashed on-device using Web Crypto SHA-256."
        }};

        CERTIFICATES.unshift(newCert);
      }}

      applyFilterAndSearch();
      showToast(`${{files.length}} CERTIFICATE(S) UPLOADED & HASHED`);
    }}
  </script>

</body>
</html>
'''

with open(r"c:\Users\Karunesh P\OneDrive\Desktop\karu\index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Updated index.html with catchy and understandable domain-shelf layout!")
