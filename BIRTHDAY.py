<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AREESHA</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Bodoni+Moda:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
 
  :root {
    --theme-h: 330;
    --theme-s: 40%;
    --theme-l: 14%;
    --accent-h: 330;
    --accent-s: 60%;
    --accent-l: 68%;
    --bg: hsl(var(--theme-h), var(--theme-s), var(--theme-l));
    --accent: hsl(var(--accent-h), var(--accent-s), var(--accent-l));
    --glow: rgba(255,180,200,0.32);
  }
 
  html { scroll-behavior: smooth; }
 
  body {
    font-family: 'Cormorant Garamond', serif;
    background: var(--bg);
    color: var(--accent);
    overflow-x: hidden;
    transition: background 1.1s ease, color 1.1s ease;
  }
 
  /* ── CURSOR ── */
  .cursor {
    position: fixed; width: 10px; height: 10px;
    background: var(--accent); border-radius: 50%;
    pointer-events: none; z-index: 9999;
    transform: translate(-50%,-50%);
    transition: background 0.8s, width .18s, height .18s;
    mix-blend-mode: screen;
  }
  .cursor-ring {
    position: fixed; width: 34px; height: 34px;
    border: 1px solid var(--accent); border-radius: 50%;
    pointer-events: none; z-index: 9998;
    transform: translate(-50%,-50%);
    transition: left .11s ease, top .11s ease, border-color .8s, width .2s, height .2s;
    opacity: 0.55;
  }
 
  /* ══════════ HOME PAGE ══════════ */
  #home {
    position: relative;
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    overflow: hidden;
  }
 
  /* Particle */
  .particle {
    position: absolute; border-radius: 50%;
    background: var(--accent);
    pointer-events: none; opacity: 0;
    animation: floatUp linear infinite;
  }
  @keyframes floatUp {
    0%   { opacity: 0; transform: translateY(0) scale(0.3); }
    8%   { opacity: 0.45; }
    90%  { opacity: 0.2; }
    100% { opacity: 0; transform: translateY(-110vh) scale(1.1); }
  }
 
  /* Home background aurora */
  .aurora {
    position: absolute; inset: 0;
    pointer-events: none; z-index: 0;
    background: radial-gradient(ellipse 80% 55% at 50% 110%,
      hsl(var(--accent-h), var(--accent-s), 28%) 0%,
      transparent 70%);
    opacity: 0.5;
    animation: auroraPulse 8s ease-in-out infinite;
    transition: background 1.1s ease;
  }
  @keyframes auroraPulse {
    0%,100% { transform: scaleY(1); opacity: 0.4; }
    50%      { transform: scaleY(1.15); opacity: 0.65; }
  }
 
  .home-title {
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(3.2rem, 10vw, 8.5rem);
    font-weight: 900; letter-spacing: .2em;
    color: var(--accent); text-align: center;
    position: relative; z-index: 2;
    animation: titleGlow 5s ease-in-out infinite;
    transition: color 1.1s ease;
  }
  @keyframes titleGlow {
    0%,100% { text-shadow: 0 0 50px var(--glow), 0 0 100px var(--glow); }
    50%      { text-shadow: 0 0 90px var(--glow), 0 0 180px var(--glow); }
  }
 
  .home-sub {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic; font-size: clamp(.9rem,2vw,1.4rem);
    letter-spacing: .45em; opacity: .55;
    margin: .8rem 0 3.5rem; z-index: 2; position: relative;
    transition: color 1.1s ease;
  }
 
  /* ── DRUM SELECTOR ── */
  .selector-wrap { position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: .5rem; }
  .sel-label { font-size: .72rem; letter-spacing: .5em; text-transform: uppercase; opacity: .45; margin-bottom: .4rem; transition: color 1.1s ease; }
 
  .drum-outer {
    position: relative;
    width: min(430px, 88vw); height: 240px;
    overflow: hidden;
    border: 1px solid transparent;
    border-image: linear-gradient(to bottom, transparent, hsl(var(--accent-h),var(--accent-s),var(--accent-l)), transparent) 1;
    transition: border-image-source 1.1s ease;
  }
 
  /* fade masks */
  .drum-outer::before,.drum-outer::after {
    content:''; position:absolute; left:0; right:0; height:82px; z-index:3; pointer-events:none;
  }
  .drum-outer::before { top:0; background: linear-gradient(to bottom, var(--bg) 30%, transparent); }
  .drum-outer::after  { bottom:0; background: linear-gradient(to top,   var(--bg) 30%, transparent); }
 
  /* active highlight */
  .drum-hl {
    position: absolute; top:50%; left:10px; right:10px;
    height: 52px; transform: translateY(-50%);
    border: 1px solid var(--accent);
    border-radius: 3px; pointer-events: none; z-index: 4;
    opacity: .35; transition: border-color 1.1s;
  }
  .drum-hl::before,.drum-hl::after {
    content:''; position:absolute; left:-6px; right:-6px; height:1px; background:var(--accent); opacity:.35; transition: background 1.1s;
  }
  .drum-hl::before { top:-1px; } .drum-hl::after { bottom:-1px; }
 
  .drum-track {
    display:flex; flex-direction:column; align-items:center;
    cursor:grab; user-select:none; will-change:transform;
  }
  .drum-track.snap { transition: transform .42s cubic-bezier(.34,1.56,.64,1); }
  .drum-track:active { cursor:grabbing; }
 
  .drum-item {
    width:100%; height:52px; flex-shrink:0;
    display:flex; align-items:center; justify-content:center; gap:14px;
    padding: 0 18px;
    font-family:'Bodoni Moda',serif;
    font-size: clamp(.85rem,2.2vw,1.05rem);
    letter-spacing:.28em; text-transform:uppercase;
    color:var(--accent); opacity:.28;
    transform: scale(.85) perspective(300px) rotateX(25deg);
    transition: opacity .25s, transform .25s, color 1.1s;
    pointer-events:none;
  }
  .drum-item.near { opacity:.6; transform: scale(.92) perspective(300px) rotateX(10deg); }
  .drum-item.active { opacity:1; transform: scale(1) perspective(300px) rotateX(0deg); }
  .drum-item.ghost { opacity:0; pointer-events:none; }
 
  .dot { width:12px; height:12px; border-radius:50%; flex-shrink:0; box-shadow:0 0 7px currentColor; }
 
  .enter-btn {
    margin-top:1.6rem; padding:13px 50px;
    background:transparent; border:1px solid var(--accent);
    color:var(--accent); font-family:'Cinzel Decorative',serif;
    font-size:.72rem; letter-spacing:.42em; text-transform:uppercase;
    cursor:pointer; position:relative; overflow:hidden;
    transition: color .35s, border-color 1.1s;
    z-index:2;
  }
  .enter-btn span { position:relative; z-index:1; }
  .enter-btn::before {
    content:''; position:absolute; inset:0;
    background:var(--accent); transform:scaleX(0);
    transform-origin:left; transition:transform .38s cubic-bezier(.4,0,.2,1);
  }
  .enter-btn:hover::before { transform:scaleX(1); }
  .enter-btn:hover { color:var(--bg); }
 
  .scroll-hint {
    position:absolute; bottom:2.2rem; left:50%; transform:translateX(-50%);
    display:flex; flex-direction:column; align-items:center; gap:7px;
    opacity:.38; font-size:.68rem; letter-spacing:.45em; z-index:2;
    animation: hintFloat 2.6s ease-in-out infinite;
  }
  .hint-line { width:1px; height:38px; background:linear-gradient(to bottom, transparent, var(--accent)); }
  @keyframes hintFloat {
    0%,100%{ transform:translateX(-50%) translateY(0); opacity:.32; }
    50%    { transform:translateX(-50%) translateY(7px); opacity:.6; }
  }
 
  /* ══════════ MAIN PAGE ══════════ */
  #main {
    position: relative;
    min-height: 220vh;
    overflow: hidden;
    transition: background 1.1s ease;
  }
  #main::before {
    content:''; position:absolute;
    top:0; left:0; right:0; height:35vh;
    background: linear-gradient(to bottom, var(--bg) 0%, transparent 100%);
    z-index:4; pointer-events:none; transition: background 1.1s ease;
  }
 
  /* Stars */
  .stars { position:absolute; inset:0; pointer-events:none; z-index:0; }
  .star {
    position:absolute; border-radius:50%;
    background: rgba(255,255,230,.85);
    animation: twinkle linear infinite;
  }
  @keyframes twinkle {
    0%,100%{ opacity:.15; transform:scale(.7); }
    50%    { opacity:1;   transform:scale(1.3); }
  }
 
  /* Shooting stars */
  .shoot {
    position:absolute; width:90px; height:1px;
    background: linear-gradient(to right, rgba(255,255,220,.9), transparent);
    animation: shoot linear infinite;
    pointer-events:none; border-radius:4px;
  }
  @keyframes shoot {
    0%  { opacity:0; transform:translateX(0) translateY(0) rotate(-25deg); }
    5%  { opacity:1; }
    30% { opacity:0; transform:translateX(200px) translateY(80px) rotate(-25deg); }
    100%{ opacity:0; transform:translateX(200px) translateY(80px) rotate(-25deg); }
  }
 
  /* Moon — fixed to viewport, always visible while on main page */
  #moonCanvas {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 20;
    opacity: 0;
    transition: opacity .7s ease;
  }
  #moonCanvas.visible { opacity: 1; }
 
  /* Main content */
  .main-body {
    position:relative; z-index:5;
    display:flex; flex-direction:column;
    align-items:center; justify-content:flex-start;
    padding-top: 100vh; padding-bottom:22vh;
  }
 
  .main-card {
    max-width:720px; width:88%;
    text-align:center; padding:5rem 2rem;
  }
 
  .m-title {
    font-family:'Cinzel Decorative',serif;
    font-size:clamp(2.2rem,7vw,5.8rem);
    font-weight:900; letter-spacing:.22em;
    color:var(--accent);
    position:relative; display:inline-block;
    animation:mGlow 6s ease-in-out infinite;
    transition: color 1.1s ease;
  }
  .m-title::after {
    content:attr(data-t); position:absolute; inset:0;
    color:transparent; -webkit-text-stroke:1px var(--accent);
    opacity:.25; transform:translate(3px,3px);
    pointer-events:none; transition:-webkit-text-stroke-color 1.1s;
  }
  @keyframes mGlow {
    0%,100%{ text-shadow:0 0 55px var(--glow),0 0 110px var(--glow); }
    50%    { text-shadow:0 0 95px var(--glow),0 0 200px var(--glow); }
  }
 
  .divider {
    width:1px; height:75px;
    background:linear-gradient(to bottom, transparent, var(--accent), transparent);
    margin:1.8rem auto; opacity:.4; transition: background 1.1s;
  }
  .ornament { font-size:1.3rem; letter-spacing:.7em; opacity:.3; transition:color 1.1s; }
  .m-quote {
    font-style:italic; font-size:clamp(1rem,2.2vw,1.4rem);
    line-height:2; letter-spacing:.04em; opacity:.68;
    transition: color 1.1s;
  }
 
  /* Progress bar */
  .prog { position:fixed; top:0; left:0; height:2px; background:var(--accent); z-index:9997; width:0; transition:background 1.1s; }
 
  /* Flash overlay */
  .flash { position:fixed; inset:0; background:var(--accent); opacity:0; pointer-events:none; z-index:9990; transition:opacity .15s; }
  .flash.on { opacity:.1; }
 
  /* ── SPLASH SCREEN ── */
  #splash {
    position: fixed; inset: 0; z-index: 99999;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    background: #08060f;
    cursor: pointer;
    transition: opacity .9s ease, visibility .9s ease;
  }
  #splash.gone { opacity: 0; visibility: hidden; pointer-events: none; }
 
  .splash-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.06);
    animation: splashRingPulse 4s ease-in-out infinite;
  }
  .splash-ring:nth-child(1){ width:200px;height:200px;animation-delay:0s; }
  .splash-ring:nth-child(2){ width:320px;height:320px;animation-delay:.6s; }
  .splash-ring:nth-child(3){ width:460px;height:460px;animation-delay:1.2s; }
  .splash-ring:nth-child(4){ width:620px;height:620px;animation-delay:1.8s; }
  @keyframes splashRingPulse {
    0%,100%{ transform:scale(1); opacity:.4; }
    50%    { transform:scale(1.06); opacity:.12; }
  }
 
  .splash-note {
    font-size: 3.5rem; margin-bottom: 1.5rem;
    animation: splashNoteFloat 2.5s ease-in-out infinite;
  }
  @keyframes splashNoteFloat {
    0%,100%{ transform:translateY(0) rotate(-8deg); }
    50%    { transform:translateY(-14px) rotate(8deg); }
  }
 
  .splash-title {
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(1.4rem, 4vw, 2.4rem);
    letter-spacing: .22em; color: #fff;
    margin-bottom: .6rem; text-align: center;
    opacity: .9;
  }
  .splash-sub {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic; font-size: clamp(.9rem,2vw,1.1rem);
    letter-spacing: .32em; color: rgba(255,255,255,.45);
    margin-bottom: 3rem; text-align: center;
  }
 
  .splash-btn {
    position: relative; overflow: hidden;
    padding: 16px 52px;
    border: 1px solid rgba(255,255,255,.5);
    background: transparent; color: #fff;
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(.8rem,1.8vw,.95rem);
    letter-spacing: .38em; cursor: pointer;
    animation: splashBtnGlow 2s ease-in-out infinite;
    transition: background .3s;
  }
  .splash-btn:hover { background: rgba(255,255,255,.08); }
  @keyframes splashBtnGlow {
    0%,100%{ box-shadow:0 0 14px rgba(255,255,255,.15),0 0 30px rgba(255,255,255,.08); }
    50%    { box-shadow:0 0 28px rgba(255,255,255,.35),0 0 60px rgba(255,255,255,.15); }
  }
 
  .splash-hint {
    position: absolute; bottom: 2rem;
    font-size: .65rem; letter-spacing: .45em;
    color: rgba(255,255,255,.22); font-style: italic;
  }
 
  /* ── Floating Music Player ── */
  #musicPlayer {
    position: fixed;
    bottom: 2rem; right: 2rem;
    z-index: 9500;
    display: flex; align-items: center; gap: .75rem;
    background: rgba(10,8,18,.72);
    border: 1px solid var(--accent);
    padding: .7rem 1.1rem .7rem .85rem;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 0 28px var(--glow), 0 8px 32px rgba(0,0,0,.5);
    transition: border-color 1.1s, box-shadow 1.1s, opacity .4s, transform .4s;
    animation: playerPulse 3s ease-in-out infinite;
    cursor: default;
  }
  @keyframes playerPulse {
    0%,100% { box-shadow: 0 0 18px var(--glow), 0 8px 28px rgba(0,0,0,.5); }
    50%      { box-shadow: 0 0 38px var(--glow), 0 8px 40px rgba(0,0,0,.5); }
  }
  #musicPlayer.hidden { opacity: 0; transform: translateY(10px); pointer-events:none; }
 
  /* Vinyl disc */
  .vinyl {
    width: 38px; height: 38px; border-radius: 50%; flex-shrink: 0;
    background: conic-gradient(
      #111 0deg, var(--accent) 4deg, #111 8deg, #1a1a1a 30deg,
      var(--accent) 34deg, #111 38deg, #1a1a1a 70deg,
      var(--accent) 74deg, #111 78deg, #1a1a1a 120deg,
      var(--accent) 124deg, #111 128deg, #1a1a1a 180deg,
      var(--accent) 184deg, #111 188deg, #1a1a1a 240deg,
      var(--accent) 244deg, #111 248deg, #1a1a1a 300deg,
      var(--accent) 304deg, #111 308deg, #1a1a1a 360deg
    );
    position: relative;
    animation: vinylSpin 3s linear infinite;
    transition: animation-play-state .3s;
  }
  .vinyl.paused { animation-play-state: paused; }
  @keyframes vinylSpin { to { transform: rotate(360deg); } }
  .vinyl::after {
    content:''; position:absolute; top:50%; left:50%;
    transform:translate(-50%,-50%);
    width:11px; height:11px; border-radius:50%;
    background: var(--bg); border: 2px solid var(--accent);
    transition: background 1.1s, border-color 1.1s;
  }
 
  /* Bars (equalizer) */
  .eq-bars {
    display: flex; align-items: flex-end; gap: 2px; height: 20px;
  }
  .eq-bar {
    width: 3px; background: var(--accent); border-radius: 2px;
    transition: background 1.1s;
    animation: eqAnim ease-in-out infinite alternate;
  }
  .eq-bar:nth-child(1){ height:30%; animation-duration:.5s; animation-delay:0s; }
  .eq-bar:nth-child(2){ height:80%; animation-duration:.7s; animation-delay:.1s; }
  .eq-bar:nth-child(3){ height:55%; animation-duration:.4s; animation-delay:.2s; }
  .eq-bar:nth-child(4){ height:90%; animation-duration:.6s; animation-delay:.05s; }
  .eq-bar:nth-child(5){ height:40%; animation-duration:.8s; animation-delay:.15s; }
  .eq-bars.paused .eq-bar { animation: none; height: 20%; }
  @keyframes eqAnim { from{transform:scaleY(1)} to{transform:scaleY(.2)} }
 
  /* Song info */
  .music-info { display:flex; flex-direction:column; justify-content:center; min-width:0; }
  .music-title {
    font-family: 'Bodoni Moda', serif;
    font-size: .72rem; letter-spacing: .18em;
    color: var(--accent); white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis;
    max-width: 140px; transition: color 1.1s;
  }
  .music-sub {
    font-style:italic; font-size:.6rem;
    letter-spacing:.12em; opacity:.45; margin-top:.15rem;
    transition: color 1.1s;
  }
 
  /* Play/pause toggle */
  .music-toggle {
    background: transparent; border: 1px solid var(--accent);
    color: var(--accent); width: 28px; height: 28px;
    border-radius: 50%; cursor: pointer; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    font-size: .7rem; transition: background .25s, border-color 1.1s, color 1.1s;
    padding:0;
  }
  .music-toggle:hover { background: var(--accent); color: var(--bg); }
 
  /* hidden YouTube iframe */
  #ytFrame { position:fixed; top:-9999px; left:-9999px; width:1px; height:1px; pointer-events:none; }
 
  /* ══════════ K-DRAMA SECTION ══════════ */
  #kdrama {
    position: relative;
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    overflow: hidden;
    padding: 6rem 2rem;
    z-index: 1;
  }
 
  /* Floating background quotes */
  .float-quote {
    position: absolute;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    color: var(--accent);
    opacity: 0;
    pointer-events: none;
    white-space: nowrap;
    font-size: clamp(.65rem, 1.4vw, .95rem);
    letter-spacing: .08em;
    animation: floatQuote linear infinite;
    will-change: transform, opacity;
    transition: color 1.1s ease;
    text-shadow: 0 0 18px var(--glow);
    z-index: 0;
  }
  @keyframes floatQuote {
    0%   { opacity: 0;    transform: translateY(0)   translateX(0); }
    8%   { opacity: 0.18; }
    50%  { opacity: 0.13; }
    92%  { opacity: 0.18; }
    100% { opacity: 0;    transform: translateY(-80px) translateX(var(--drift)); }
  }
 
  /* Section header */
  .kd-header {
    position: relative; z-index: 5;
    text-align: center; margin-bottom: 3.5rem;
  }
  .kd-header h2 {
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(1rem, 3vw, 1.8rem);
    letter-spacing: .35em; font-weight: 400;
    color: var(--accent); opacity: .7;
    transition: color 1.1s;
  }
  .kd-header p {
    font-style: italic; font-size: clamp(.8rem, 1.6vw, 1rem);
    letter-spacing: .28em; opacity: .4; margin-top: .6rem;
    transition: color 1.1s;
  }
 
  /* Drama cards row */
  .drama-row {
    position: relative; z-index: 5;
    display: flex; flex-wrap: wrap;
    gap: 1.8rem; justify-content: center;
    max-width: 1000px; width: 100%;
  }
 
  .drama-card {
    position: relative;
    flex: 1 1 260px; max-width: 300px;
    border: 1px solid var(--accent);
    padding: 2.2rem 1.8rem 2rem;
    cursor: pointer;
    overflow: hidden;
    transition: transform .35s cubic-bezier(.34,1.56,.64,1), border-color 1.1s, box-shadow .35s;
    opacity: 0;
    transform: translateY(40px);
    animation: cardReveal .7s ease forwards;
  }
  .drama-card:nth-child(1) { animation-delay: .1s; }
  .drama-card:nth-child(2) { animation-delay: .25s; }
  .drama-card:nth-child(3) { animation-delay: .4s; }
  @keyframes cardReveal {
    to { opacity: 1; transform: translateY(0); }
  }
 
  .drama-card::before {
    content: '';
    position: absolute; inset: 0;
    background: var(--accent);
    opacity: 0;
    transition: opacity .35s;
    z-index: 0;
  }
  .drama-card:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 20px 60px rgba(0,0,0,.4); }
  .drama-card:hover::before { opacity: .07; }
  .drama-card.active { box-shadow: 0 0 0 1px var(--accent), 0 0 40px var(--glow); }
 
  .drama-card > * { position: relative; z-index: 1; }
 
  .drama-num {
    font-family: 'Bodoni Moda', serif;
    font-size: .72rem; letter-spacing: .5em;
    opacity: .4; margin-bottom: .8rem;
    display: block; transition: color 1.1s;
  }
  .drama-title {
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(.85rem, 2vw, 1.1rem);
    font-weight: 700; letter-spacing: .12em;
    line-height: 1.4; color: var(--accent);
    margin-bottom: .8rem; transition: color 1.1s;
  }
  .drama-sub {
    font-style: italic; font-size: .82rem;
    letter-spacing: .1em; opacity: .5;
    line-height: 1.5; transition: color 1.1s;
  }
  .drama-icon {
    font-size: 1.6rem; display: block;
    margin-bottom: .9rem; filter: saturate(1.4);
  }
  .drama-select-hint {
    display: inline-block; margin-top: 1.2rem;
    font-size: .65rem; letter-spacing: .45em;
    text-transform: uppercase; opacity: .35;
    border-top: 1px solid var(--accent); padding-top: .6rem;
    width: 100%; transition: opacity .3s, color 1.1s;
  }
  .drama-card:hover .drama-select-hint { opacity: .75; }
  .drama-card.active .drama-select-hint { opacity: 1; letter-spacing: .5em; }
 
  /* ── Drama content panel ── */
  #dramaPanel {
    position: relative; z-index: 5;
    width: 100%; max-width: 860px;
    margin-top: 4rem;
    opacity: 0; transform: translateY(30px);
    transition: opacity .6s ease, transform .6s ease;
    pointer-events: none;
  }
  #dramaPanel.show { opacity: 1; transform: translateY(0); pointer-events: auto; }
 
  .panel-inner {
    border: 1px solid var(--accent);
    padding: 3rem 2.5rem;
    position: relative;
    overflow: hidden;
  }
  .panel-inner::before {
    content: attr(data-symbol);
    position: absolute; right: -1rem; top: -2rem;
    font-size: clamp(6rem, 18vw, 12rem);
    color: var(--accent); opacity: .04;
    font-family: 'Cinzel Decorative', serif;
    pointer-events: none;
    line-height: 1;
  }
 
  .panel-show-title {
    font-family: 'Cinzel Decorative', serif;
    font-size: clamp(1.1rem, 3.5vw, 2rem);
    letter-spacing: .2em; color: var(--accent);
    margin-bottom: .5rem; transition: color 1.1s;
  }
  .panel-tagline {
    font-style: italic; font-size: clamp(.85rem, 1.8vw, 1.05rem);
    letter-spacing: .15em; opacity: .5; margin-bottom: 2.2rem;
    transition: color 1.1s;
  }
 
  .panel-divider { width: 60px; height: 1px; background: var(--accent); opacity: .3; margin: 0 0 2.2rem; transition: background 1.1s; }
 
  /* Facts grid */
  .facts-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap: 1.2rem; margin-bottom: 2.5rem;
  }
  .fact-chip {
    border: 1px solid var(--accent); padding: .85rem 1rem;
    font-size: .78rem; letter-spacing: .12em;
    opacity: .7; line-height: 1.5;
    transition: opacity .3s, color 1.1s, border-color 1.1s;
  }
  .fact-chip:hover { opacity: 1; }
  .fact-chip strong {
    display: block; font-family: 'Bodoni Moda', serif;
    letter-spacing: .25em; font-size: .68rem;
    opacity: .55; margin-bottom: .3rem; text-transform: uppercase;
  }
 
  /* Dialogue carousel */
  .dialogue-section { margin-top: .5rem; }
  .dialogue-label {
    font-size: .68rem; letter-spacing: .5em; text-transform: uppercase;
    opacity: .4; margin-bottom: 1.4rem;
  }
  .dialogue-card {
    border-left: 2px solid var(--accent);
    padding: 1rem 1.5rem;
    margin-bottom: 1rem;
    opacity: 0;
    transform: translateX(-15px);
    transition: opacity .5s ease, transform .5s ease, border-color 1.1s;
  }
  .dialogue-card.visible { opacity: 1; transform: translateX(0); }
  .dialogue-text {
    font-style: italic;
    font-size: clamp(.95rem, 2vw, 1.2rem);
    line-height: 1.8; letter-spacing: .04em; opacity: .85;
    transition: color 1.1s;
  }
  .dialogue-speaker {
    font-size: .68rem; letter-spacing: .4em; text-transform: uppercase;
    opacity: .45; margin-top: .6rem; transition: color 1.1s;
  }
</style>
</head>
<body>
 
<!-- ══ SPLASH (required click for audio autoplay) ══ -->
<div id="splash">
  <div class="splash-ring"></div>
  <div class="splash-ring"></div>
  <div class="splash-ring"></div>
  <div class="splash-ring"></div>
  <div class="splash-note">🎵</div>
  <h1 class="splash-title">AREESHA</h1>
  <p class="splash-sub">tap enter · your song will play 🎵</p>
  <button class="splash-btn" id="splashBtn">✦ &nbsp; Enter &nbsp; ✦</button>
  <span class="splash-hint">opens Jhumritalaiyya in a new tab</span>
</div>
 
<div class="cursor"      id="cur"></div>
<div class="cursor-ring" id="curRing"></div>
<div class="prog"  id="prog"></div>
<div class="flash" id="flash"></div>
 
<!-- ── Music Player ── -->
<div id="musicPlayer" class="hidden">
  <div class="vinyl" id="vinyl"></div>
  <div class="music-info">
    <div class="music-title">Jhumritalaiyya</div>
    <div class="music-sub">♪ &nbsp; now playing</div>
  </div>
  <div class="eq-bars" id="eqBars">
    <div class="eq-bar"></div>
    <div class="eq-bar"></div>
    <div class="eq-bar"></div>
    <div class="eq-bar"></div>
    <div class="eq-bar"></div>
  </div>
  <button class="music-toggle" id="musicToggle" title="Play / Pause">▐▐</button>
</div>
 
<!-- YouTube Mini Player — visible so browser allows audio -->
<div id="ytPlayerWrap" style="
  position: fixed; bottom: 2rem; left: 2rem;
  z-index: 9500;
  display: none;
  flex-direction: column;
  align-items: flex-start;
  gap: 0;
">
  <div style="
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: .7rem;
    letter-spacing: .28em;
    color: var(--accent);
    opacity: .6;
    margin-bottom: .35rem;
    padding-left: 2px;
    transition: color 1.1s;
  ">♪ &nbsp; Jhumritalaiyya</div>
  <iframe id="ytFrame"
    width="200" height="113"
    src="https://www.youtube.com/embed/exUQkIkyBBI?autoplay=1&loop=1&playlist=exUQkIkyBBI&rel=0&playsinline=1"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen
    style="border: 1px solid var(--accent); opacity: .85; display: block;"
  ></iframe>
</div>
 
<!-- ══ HOME ══ -->
<section id="home">
  <div class="aurora"></div>
 
  <h1 class="home-title">AREESHA</h1>
  <p class="home-sub">choose your world</p>
 
  <div class="selector-wrap">
    <div class="sel-label">Select a theme</div>
    <div class="drum-outer" id="drumOuter">
      <div class="drum-hl"></div>
      <div class="drum-track" id="drumTrack"></div>
    </div>
    <button class="enter-btn" id="enterBtn"><span>Enter</span></button>
  </div>
 
  <div class="scroll-hint">
    <span>scroll</span>
    <div class="hint-line"></div>
  </div>
</section>
 
<!-- ══ MAIN ══ -->
<section id="main">
  <div class="stars" id="stars"></div>
 
  <!-- Moon: fixed canvas, drawn with JS, always on screen while scrolling main -->
  <canvas id="moonCanvas"></canvas>
 
  <div class="main-body">
    <div class="main-card">
      <div class="ornament">✦ ✦ ✦</div>
      <div class="divider"></div>
      <h2 class="m-title" data-t="AREESHA">AREESHA</h2>
      <div class="divider"></div>
      <p class="m-quote">
        She is the quiet glow<br>
        before the stars forget to shine —<br>
        a name the moon whispers<br>
        on its long journey across the sky.
      </p>
      <div class="divider"></div>
      <div class="ornament">✦ ✦ ✦</div>
    </div>
  </div>
</section>
 
<!-- ══ K-DRAMA ══ -->
<section id="kdrama">
  <!-- Floating background quotes injected by JS -->
 
  <div class="kd-header">
    <h2>Her Favourite Worlds</h2>
    <p>choose a drama · enter its universe</p>
  </div>
 
  <div class="drama-row" id="dramaRow">
    <div class="drama-card" data-drama="dots" tabindex="0">
      <span class="drama-icon">☀️</span>
      <span class="drama-num">01</span>
      <div class="drama-title">Descendants<br>of the Sun</div>
      <div class="drama-sub">Love forged in war, duty, and sacrifice</div>
      <span class="drama-select-hint">click to enter</span>
    </div>
    <div class="drama-card" data-drama="dearest" tabindex="0">
      <span class="drama-icon">🌸</span>
      <span class="drama-num">02</span>
      <div class="drama-title">My Dearest</div>
      <div class="drama-sub">A love that outlasts kingdoms and time</div>
      <span class="drama-select-hint">click to enter</span>
    </div>
    <div class="drama-card" data-drama="translate" tabindex="0">
      <span class="drama-icon">💬</span>
      <span class="drama-num">03</span>
      <div class="drama-title">Can This Be<br>Translated</div>
      <div class="drama-sub">Where language becomes the bridge to love</div>
      <span class="drama-select-hint">click to enter</span>
    </div>
  </div>
 
  <div id="dramaPanel">
    <div class="panel-inner" id="panelInner" data-symbol="★">
      <h3 class="panel-show-title" id="panelTitle">—</h3>
      <p class="panel-tagline" id="panelTagline">—</p>
      <div class="panel-divider"></div>
      <div class="facts-grid" id="factsGrid"></div>
      <div class="dialogue-section">
        <div class="dialogue-label">✦ &nbsp; Memorable Dialogues &nbsp; ✦</div>
        <div id="dialogueList"></div>
      </div>
    </div>
  </div>
</section>
 
<script>
// ─── THEMES ───────────────────────────────────────────────
const THEMES = [
  { name:'BAROQUE ROSE',    dot:'#c0607a',
    v:{'--theme-h':'338','--theme-s':'38%','--theme-l':'13%','--accent-h':'338','--accent-s':'58%','--accent-l':'68%','--glow':'rgba(255,170,195,0.32)'} },
  { name:'CHERRY CAKE',     dot:'#cc4455',
    v:{'--theme-h':'354','--theme-s':'40%','--theme-l':'12%','--accent-h':'354','--accent-s':'65%','--accent-l':'70%','--glow':'rgba(255,155,165,0.32)'} },
  { name:'BLUEBERRY BLUE',  dot:'#5566cc',
    v:{'--theme-h':'232','--theme-s':'42%','--theme-l':'13%','--accent-h':'232','--accent-s':'65%','--accent-l':'72%','--glow':'rgba(155,175,255,0.32)'} },
  { name:'LAVENDER LILY',   dot:'#9966cc',
    v:{'--theme-h':'272','--theme-s':'36%','--theme-l':'13%','--accent-h':'272','--accent-s':'58%','--accent-l':'74%','--glow':'rgba(190,155,255,0.32)'} },
  { name:'PISTACHIO',       dot:'#7aaa66',
    v:{'--theme-h':'112','--theme-s':'28%','--theme-l':'13%','--accent-h':'112','--accent-s':'48%','--accent-l':'68%','--glow':'rgba(165,220,145,0.32)'} },
];
 
let selIdx = 0;
function applyTheme(idx, withFlash=false) {
  selIdx = idx;
  const t = THEMES[idx], r = document.documentElement;
  Object.entries(t.v).forEach(([k,v]) => r.style.setProperty(k,v));
  r.style.setProperty('--bg',  `hsl(${t.v['--theme-h']},${t.v['--theme-s']},${t.v['--theme-l']})`);
  r.style.setProperty('--accent',`hsl(${t.v['--accent-h']},${t.v['--accent-s']},${t.v['--accent-l']})`);
  if(withFlash){ const f=document.getElementById('flash'); f.classList.add('on'); setTimeout(()=>f.classList.remove('on'),200); }
}
 
// ─── CURSOR ───────────────────────────────────────────────
const cur=document.getElementById('cur'), ring=document.getElementById('curRing');
document.addEventListener('mousemove',e=>{
  cur.style.left=e.clientX+'px'; cur.style.top=e.clientY+'px';
  ring.style.left=e.clientX+'px'; ring.style.top=e.clientY+'px';
});
document.addEventListener('mousedown',()=>{cur.style.width='5px';cur.style.height='5px';ring.style.width='46px';ring.style.height='46px';});
document.addEventListener('mouseup',()=>{cur.style.width='10px';cur.style.height='10px';ring.style.width='34px';ring.style.height='34px';});
 
// ─── PARTICLES ────────────────────────────────────────────
const homeEl = document.getElementById('home');
for(let i=0;i<30;i++){
  const p=document.createElement('div'); p.className='particle';
  const s=Math.random()*4+1;
  p.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}%;top:${100+Math.random()*20}%;animation-duration:${Math.random()*20+12}s;animation-delay:${-Math.random()*20}s`;
  homeEl.appendChild(p);
}
 
// ─── DRUM ─────────────────────────────────────────────────
const track = document.getElementById('drumTrack');
const IH = 52; // item height px
 
function buildDrum(){
  track.innerHTML='';
  // 2 ghost spacers top
  for(let g=0;g<2;g++){ const d=document.createElement('div'); d.className='drum-item ghost'; d.style.height=IH+'px'; track.appendChild(d); }
  THEMES.forEach((t,i)=>{
    const d=document.createElement('div'); d.className='drum-item'; d.dataset.i=i;
    d.innerHTML=`<span class="dot" style="background:${t.dot}"></span><span>${t.name}</span>`;
    track.appendChild(d);
  });
  // 2 ghost spacers bottom
  for(let g=0;g<2;g++){ const d=document.createElement('div'); d.className='drum-item ghost'; d.style.height=IH+'px'; track.appendChild(d); }
}
buildDrum();
 
let offset=0, dragging=false, dragY0=0, dragOff0=0;
 
function clampOff(o){ return Math.max(0, Math.min((THEMES.length-1)*IH, o)); }
 
function render(off){
  const ci = off/IH;
  track.querySelectorAll('.drum-item[data-i]').forEach((el,i)=>{
    const dist = Math.abs(i-ci);
    el.classList.remove('active','near');
    if(dist<0.5) el.classList.add('active');
    else if(dist<1.45) el.classList.add('near');
    if(dist<0.5) applyTheme(parseInt(el.dataset.i));
  });
  track.style.transform=`translateY(${-off}px)`;
}
 
function snap(){
  const i=Math.round(offset/IH);
  offset=clampOff(i*IH);
  track.classList.add('snap');
  render(offset);
  setTimeout(()=>track.classList.remove('snap'),450);
}
 
const outer=document.getElementById('drumOuter');
outer.addEventListener('mousedown',e=>{ dragging=true; dragY0=e.clientY; dragOff0=offset; track.classList.remove('snap'); e.preventDefault(); });
window.addEventListener('mousemove',e=>{ if(!dragging)return; offset=clampOff(dragOff0+(dragY0-e.clientY)); render(offset); });
window.addEventListener('mouseup',()=>{ if(dragging){ dragging=false; snap(); } });
outer.addEventListener('touchstart',e=>{ dragging=true; dragY0=e.touches[0].clientY; dragOff0=offset; track.classList.remove('snap'); },{passive:false});
window.addEventListener('touchmove',e=>{ if(!dragging)return; offset=clampOff(dragOff0+(dragY0-e.touches[0].clientY)); render(offset); },{passive:false});
window.addEventListener('touchend',()=>{ if(dragging){ dragging=false; snap(); } });
outer.addEventListener('wheel',e=>{ e.preventDefault(); offset=clampOff(offset+e.deltaY*.45); render(offset); clearTimeout(outer._wt); outer._wt=setTimeout(snap,130); },{passive:false});
 
render(0);
 
document.getElementById('enterBtn').addEventListener('click',()=>{
  applyTheme(Math.round(offset/IH), true);
  document.getElementById('main').scrollIntoView({behavior:'smooth'});
});
 
// ─── STARS ────────────────────────────────────────────────
const starsEl=document.getElementById('stars');
for(let i=0;i<200;i++){
  const s=document.createElement('div'); s.className='star';
  const sz=Math.random()*2.4+0.5;
  const dur=Math.random()*5+3;
  s.style.cssText=`width:${sz}px;height:${sz}px;left:${Math.random()*100}%;top:${Math.random()*100}%;animation-duration:${dur}s;animation-delay:${-Math.random()*dur}s;opacity:${Math.random()*.6+.1}`;
  starsEl.appendChild(s);
}
// Shooting stars
for(let i=0;i<5;i++){
  const sh=document.createElement('div'); sh.className='shoot';
  const dur=Math.random()*8+6;
  sh.style.cssText=`top:${Math.random()*50}%;left:${Math.random()*70}%;animation-duration:${dur}s;animation-delay:${-Math.random()*dur}s;width:${Math.random()*60+50}px`;
  starsEl.appendChild(sh);
}
 
// ─── MOON (Canvas, Fixed to Viewport) ─────────────────────
const moonCanvas = document.getElementById('moonCanvas');
const ctx = moonCanvas.getContext('2d');
 
function resizeCanvas(){
  moonCanvas.width  = window.innerWidth;
  moonCanvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);
 
// Arc: moon travels a semicircle. Centre of arc is below the bottom of screen.
// t=0: bottom-left  t=0.5: top-centre  t=1: bottom-right
function moonXY(t) {
  const W = moonCanvas.width, H = moonCanvas.height;
  // Arc centre is below screen; radius spans from bottom corners to top-centre
  const cx = W * 0.5;
  const cy = H * 1.08;           // just below screen bottom
  const rx = W * 0.52;
  const ry = H * 1.02;
  const angle = Math.PI - t * Math.PI;  // π → 0
  return {
    x: cx + rx * Math.cos(angle),
    y: cy - ry * Math.sin(angle)
  };
}
 
function drawMoon(t) {
  const W = moonCanvas.width, H = moonCanvas.height;
  ctx.clearRect(0, 0, W, H);
 
  t = Math.max(0, Math.min(1, t));
  const { x, y } = moonXY(t);
  const phase = Math.sin(t * Math.PI);          // 0 → 1 → 0
  const R = Math.min(W, H) * (0.045 + phase * 0.022); // radius: ~4-6% of screen
 
  // Edge fade so moon ghosts in/out at horizons
  const edge = t < 0.06 ? t / 0.06 : t > 0.94 ? (1 - t) / 0.06 : 1;
 
  // ── Outer atmospheric halo ──
  const haloR = R * 2.8;
  const haloGrad = ctx.createRadialGradient(x, y, R * 0.5, x, y, haloR);
  haloGrad.addColorStop(0,   `rgba(255,251,220,${(0.12 + phase * 0.22) * edge})`);
  haloGrad.addColorStop(0.4, `rgba(255,245,200,${(0.06 + phase * 0.1)  * edge})`);
  haloGrad.addColorStop(1,   'rgba(255,245,200,0)');
  ctx.beginPath();
  ctx.arc(x, y, haloR, 0, Math.PI * 2);
  ctx.fillStyle = haloGrad;
  ctx.fill();
 
  // ── Inner glow ──
  const glowR = R * 1.55;
  const glowGrad = ctx.createRadialGradient(x, y, R * 0.3, x, y, glowR);
  glowGrad.addColorStop(0,   `rgba(255,255,235,${(0.25 + phase * 0.35) * edge})`);
  glowGrad.addColorStop(1,   'rgba(255,245,200,0)');
  ctx.beginPath();
  ctx.arc(x, y, glowR, 0, Math.PI * 2);
  ctx.fillStyle = glowGrad;
  ctx.fill();
 
  // ── Moon body with crescent mask ──
  ctx.save();
  // Clip to moon circle
  ctx.beginPath();
  ctx.arc(x, y, R, 0, Math.PI * 2);
  ctx.clip();
 
  // Fill moon body
  const moonGrad = ctx.createRadialGradient(x - R*0.28, y - R*0.25, R*0.05, x, y, R);
  moonGrad.addColorStop(0,   '#fffdf5');
  moonGrad.addColorStop(0.55,'#fffbe8');
  moonGrad.addColorStop(1,   '#d8c890');
  ctx.fillStyle = moonGrad;
  ctx.fillRect(x - R - 2, y - R - 2, R * 2 + 4, R * 2 + 4);
 
  // Crescent shadow: a dark disc offset to one side cuts the crescent shape
  const crescentDepth = 1 - phase;
  const dir = t < 0.5 ? 1 : -1;   // shadow side flips at zenith
  const shadowX = x + dir * crescentDepth * R * 1.08;
  const shadowR  = R * (0.96 + crescentDepth * 0.08);
 
  // Use destination-out to punch the shadow hole = crescent
  ctx.globalCompositeOperation = 'destination-out';
  // Soft edge for shadow
  const shadowGrad = ctx.createRadialGradient(shadowX - dir*shadowR*0.08, y, shadowR*0.1, shadowX, y, shadowR);
  shadowGrad.addColorStop(0,   `rgba(0,0,0,${0.04 + crescentDepth * 0.94})`);
  shadowGrad.addColorStop(0.7, `rgba(0,0,0,${crescentDepth * 0.98})`);
  shadowGrad.addColorStop(1,   'rgba(0,0,0,0)');
  ctx.beginPath();
  ctx.arc(shadowX, y, shadowR, 0, Math.PI * 2);
  ctx.fillStyle = shadowGrad;
  ctx.fill();
 
  ctx.restore();
 
  // ── Craters (visible near full moon) ──
  const craterAlpha = Math.max(0, (phase - 0.42) / 0.58) * 0.55 * edge;
  if (craterAlpha > 0.01) {
    const craters = [
      { ox: -0.3, oy: -0.2, r: 0.14 },
      { ox:  0.22,oy:  0.1, r: 0.09 },
      { ox: -0.06,oy:  0.3, r: 0.11 },
      { ox:  0.35,oy: -0.35,r: 0.07 },
    ];
    craters.forEach(c => {
      const cx2 = x + c.ox * R, cy2 = y + c.oy * R, cr = c.r * R;
      ctx.beginPath();
      ctx.arc(cx2, cy2, cr, 0, Math.PI * 2);
      ctx.strokeStyle = `rgba(160,135,80,${craterAlpha})`;
      ctx.lineWidth = R * 0.03;
      ctx.stroke();
      // inner shadow
      const cg = ctx.createRadialGradient(cx2, cy2, 0, cx2, cy2, cr);
      cg.addColorStop(0,   `rgba(100,85,50,${craterAlpha * 0.4})`);
      cg.addColorStop(1,   'rgba(100,85,50,0)');
      ctx.fillStyle = cg;
      ctx.fill();
    });
  }
 
  // ── Shimmer highlight (full moon only) ──
  const shimAlpha = Math.max(0, (phase - 0.55) / 0.45) * 0.45 * edge;
  if (shimAlpha > 0.01) {
    ctx.save();
    ctx.beginPath(); ctx.arc(x, y, R, 0, Math.PI * 2); ctx.clip();
    const sg = ctx.createLinearGradient(x - R*0.6, y - R*0.1, x + R*0.6, y + R*0.1);
    sg.addColorStop(0,   'rgba(255,255,255,0)');
    sg.addColorStop(0.5, `rgba(255,255,255,${shimAlpha})`);
    sg.addColorStop(1,   'rgba(255,255,255,0)');
    ctx.fillStyle = sg;
    ctx.fillRect(x - R, y - R * 0.25, R * 2, R * 0.5);
    ctx.restore();
  }
 
  // ── Subtle "Made by ME" text — only near full moon, curved along bottom arc ──
  const textAlpha = Math.max(0, (phase - 0.45) / 0.55) * 0.52 * edge;
  if (textAlpha > 0.005) {
    ctx.save();
    ctx.beginPath(); ctx.arc(x, y, R, 0, Math.PI * 2); ctx.clip();
    const txt = 'Made by ME';
    const fontSize = R * 0.22;
    ctx.font = `italic ${fontSize}px 'Cormorant Garamond', serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const arcR   = R * 0.6;
    const startA = Math.PI * 0.68;
    const endA   = Math.PI * 1.32;
    const totalA = endA - startA;
    ctx.fillStyle = `rgba(90,65,20,${textAlpha})`;
    const charWidths = txt.split('').map(c => ctx.measureText(c).width);
    const totalW = charWidths.reduce((a,b)=>a+b,0);
    const totalAngle = totalW / arcR;
    let charAngle = startA + (totalA - totalAngle) / 2;
    txt.split('').forEach((ch, i) => {
      const halfW = charWidths[i] / 2;
      charAngle += halfW / arcR;
      ctx.save();
      ctx.translate(x + arcR * Math.cos(charAngle), y + arcR * Math.sin(charAngle));
      ctx.rotate(charAngle + Math.PI / 2);
      ctx.fillText(ch, 0, 0);
      ctx.restore();
      charAngle += halfW / arcR;
    });
    ctx.restore();
  }
}
 
let moonT = 0;
function setMoon(t) { moonT = t; drawMoon(t); }
 
// ─── SCROLL ───────────────────────────────────────────────
const prog    = document.getElementById('prog');
const mainSec = document.getElementById('main');
 
function onScroll(){
  const sy    = window.scrollY;
  const total = document.body.scrollHeight - window.innerHeight;
  prog.style.width = (total ? sy / total * 100 : 0) + '%';
 
  // Show moon only when main section is in view
  const mTop  = mainSec.offsetTop;
  const mBot  = mTop + mainSec.offsetHeight;
  const inMain = sy + window.innerHeight > mTop && sy < mBot;
  moonCanvas.classList.toggle('visible', inMain);
 
  // t = 0 at top of #main, 1 at bottom of #main
  // We scroll through (mainSec.offsetHeight - window.innerHeight) pixels worth
  const scrollable = mainSec.offsetHeight - window.innerHeight;
  const moonT = scrollable > 0 ? Math.max(0, Math.min(1, (sy - mTop) / scrollable)) : 0;
  setMoon(moonT);
}
window.addEventListener('scroll', onScroll, { passive: true });
window.addEventListener('resize', () => { resizeCanvas(); drawMoon(moonT); });
onScroll();
 
// ══════════════════════════════════════════════════════════
//  SPLASH + MUSIC PLAYER
// ══════════════════════════════════════════════════════════
const splashEl      = document.getElementById('splash');
const splashBtn     = document.getElementById('splashBtn');
const musicPlayerEl = document.getElementById('musicPlayer');
const vinylEl       = document.getElementById('vinyl');
const eqBarsEl      = document.getElementById('eqBars');
const musicToggleEl = document.getElementById('musicToggle');
const ytPlayerWrap  = document.getElementById('ytPlayerWrap');
const ytFrame       = document.getElementById('ytFrame');
 
let splashDismissed = false;
let isPlaying = true;
 
function dismissSplash() {
  if (splashDismissed) return;
  splashDismissed = true;
  // Open the song in a new tab
  window.open('https://youtu.be/exUQkIkyBBI', '_blank');
  splashEl.classList.add('gone');
  musicPlayerEl.classList.remove('hidden');
  ytPlayerWrap.style.display = 'none';
  setPlayUI(true);
}
 
function setPlayUI(playing) {
  isPlaying = playing;
  vinylEl.classList.toggle('paused', !playing);
  eqBarsEl.classList.toggle('paused', !playing);
  musicToggleEl.innerHTML = playing ? '&#10074;&#10074;' : '&#9654;';
  musicToggleEl.title = playing ? 'Pause' : 'Play';
}
 
splashBtn.addEventListener('click', dismissSplash);
splashEl.addEventListener('click',  dismissSplash);
 
// Toggle hides/shows the yt player wrap (mute effect)
musicToggleEl.addEventListener('click', e => {
  e.stopPropagation();
  if (!splashDismissed) return;
  if (isPlaying) {
    ytPlayerWrap.style.opacity = '0';
    ytPlayerWrap.style.pointerEvents = 'none';
    ytFrame.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
    setPlayUI(false);
  } else {
    ytPlayerWrap.style.opacity = '1';
    ytPlayerWrap.style.pointerEvents = 'auto';
    ytFrame.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
    setPlayUI(true);
  }
});
 
// ─── INIT THEME ───────────────────────────────────────────
applyTheme(0);
 
// ══════════════════════════════════════════════════════════
//  K-DRAMA SECTION
// ══════════════════════════════════════════════════════════
 
const DRAMAS = {
  dots: {
    title: 'Descendants of the Sun',
    tagline: '사랑하면 지켜야 한다 — If you love, you must protect',
    symbol: '☀',
    facts: [
      { label: 'Year', value: '2016' },
      { label: 'Genre', value: 'Romance · Military · Action' },
      { label: 'Episodes', value: '16 Episodes' },
      { label: 'Network', value: 'KBS2' },
      { label: 'Stars', value: 'Song Joong-ki · Song Hye-kyo' },
      { label: 'Filming', value: 'Greece · South Korea' },
    ],
    dialogues: [
      { text: '"I thought about what I would do if I only had one day left to live. And I realised — I would want to spend it by your side."', speaker: 'Yoo Si-jin' },
      { text: '"In my world, the priority is the country first, then the mission, then my men, and lastly... myself. But you, you have become my exception."', speaker: 'Yoo Si-jin' },
      { text: '"I\'m not afraid of death. I\'m afraid of a life where I can\'t protect the people I love."', speaker: 'Yoo Si-jin' },
      { text: '"A doctor exists to save lives. A soldier exists to protect lives. We are not that different after all."', speaker: 'Kang Mo-yeon' },
      { text: '"Don\'t die. That\'s my one condition."', speaker: 'Kang Mo-yeon' },
    ],
    floatQuotes: [
      'If you love, you must protect',
      '사랑해 — I love you',
      'Stay alive. Come back.',
      'My priority, my exception',
      'Love forged under fire',
      'Two hearts, two duties',
      'Beyond the battlefield',
      'You are my exception',
    ]
  },
  dearest: {
    title: 'My Dearest',
    tagline: '내 사랑아 — My beloved, across every lifetime',
    symbol: '❀',
    facts: [
      { label: 'Year', value: '2023' },
      { label: 'Genre', value: 'Historical · Romance · War' },
      { label: 'Episodes', value: '20 Episodes' },
      { label: 'Network', value: 'MBC' },
      { label: 'Stars', value: 'Namkoong Min · Ahn Eun-jin' },
      { label: 'Era', value: 'Joseon · Qing Invasion' },
    ],
    dialogues: [
      { text: '"Even if I am reborn a hundred times, I will find you every single time. That is my vow."', speaker: 'Lee Jang-hyun' },
      { text: '"You are the one thing the war could not take from me."', speaker: 'Lee Jang-hyun' },
      { text: '"I do not ask you to love me. I only ask that you let me love you — quietly, from wherever I am."', speaker: 'Yoo Gil-chae' },
      { text: '"A heart that has loved you once can never be returned to how it was before."', speaker: 'Lee Jang-hyun' },
      { text: '"History may forget our names, but it cannot erase what we felt."', speaker: 'Yoo Gil-chae' },
    ],
    floatQuotes: [
      '내 사랑아 — My beloved',
      'A love older than kingdoms',
      'Find me in every lifetime',
      'The war took everything but you',
      'Joseon blooms in winter',
      'Vow across a hundred lives',
      'Even history cannot forget love',
      'I will find you again',
    ]
  },
  translate: {
    title: 'Can This Be Translated',
    tagline: '마음은 번역이 필요 없다 — The heart needs no translation',
    symbol: '◈',
    facts: [
      { label: 'Year', value: '2024' },
      { label: 'Genre', value: 'Romance · Comedy · Drama' },
      { label: 'Episodes', value: 'Ongoing Series' },
      { label: 'Vibe', value: 'Warm · Witty · Tender' },
      { label: 'Theme', value: 'Language · Culture · Connection' },
      { label: 'Heart', value: 'Lost in translation, found in love' },
    ],
    dialogues: [
      { text: '"There are feelings that no dictionary in the world can define. Yours is one of them."', speaker: 'Translator' },
      { text: '"I don\'t care what language you speak. When you laugh, I understand everything."', speaker: 'Lead' },
      { text: '"The most honest things people say are the ones they think no one will translate."', speaker: 'Lead' },
      { text: '"Some things aren\'t lost in translation. Some things are only found there."', speaker: 'Narrator' },
      { text: '"You taught me that home is not a place. It is the sound of someone who understands you."', speaker: 'Lead' },
    ],
    floatQuotes: [
      'The heart needs no translation',
      '말하지 않아도 알아 — I know without words',
      'Lost in translation, found in love',
      'Every language has a word for longing',
      'Understand me in silence',
      'Some feelings resist all dictionaries',
      'Words cross borders, hearts cross worlds',
      '번역 — translation · connection · love',
    ]
  }
};
 
// ── Floating background quotes ──────────────────────────
const kdramaSection = document.getElementById('kdrama');
let floatInterval = null;
let activeFloaters = [];
 
function clearFloaters() {
  activeFloaters.forEach(el => el.remove());
  activeFloaters = [];
  if(floatInterval) clearInterval(floatInterval);
}
 
function spawnFloater(text) {
  const el = document.createElement('div');
  el.className = 'float-quote';
  const drift = (Math.random() - 0.5) * 80;
  el.style.cssText = `
    left: ${Math.random() * 85 + 5}%;
    top: ${Math.random() * 80 + 10}%;
    --drift: ${drift}px;
    animation-duration: ${Math.random() * 18 + 14}s;
    animation-delay: ${-Math.random() * 10}s;
    transform: rotate(${(Math.random()-0.5)*6}deg);
    font-size: ${Math.random()*0.25 + 0.68}rem;
  `;
  el.textContent = text;
  kdramaSection.appendChild(el);
  activeFloaters.push(el);
}
 
function launchFloaters(drama) {
  clearFloaters();
  const quotes = DRAMAS[drama].floatQuotes;
  // Spawn 12–16 floaters from the pool
  const count = 14;
  for(let i = 0; i < count; i++) {
    spawnFloater(quotes[i % quotes.length]);
  }
  // Keep adding fresh ones periodically
  floatInterval = setInterval(() => {
    if(activeFloaters.length > 22) {
      const old = activeFloaters.shift();
      old.remove();
    }
    spawnFloater(quotes[Math.floor(Math.random() * quotes.length)]);
  }, 3500);
}
 
// ── Panel renderer ──────────────────────────────────────
let activeDrama = null;
const dramaPanel  = document.getElementById('dramaPanel');
const panelInner  = document.getElementById('panelInner');
const panelTitle  = document.getElementById('panelTitle');
const panelTagline= document.getElementById('panelTagline');
const factsGrid   = document.getElementById('factsGrid');
const dialogueList= document.getElementById('dialogueList');
 
function showDramaPanel(key) {
  const d = DRAMAS[key];
  activeDrama = key;
 
  // Update panel content
  panelTitle.textContent   = d.title;
  panelTagline.textContent = d.tagline;
  panelInner.dataset.symbol = d.symbol;
 
  factsGrid.innerHTML = d.facts.map(f =>
    `<div class="fact-chip"><strong>${f.label}</strong>${f.value}</div>`
  ).join('');
 
  dialogueList.innerHTML = d.dialogues.map((dl, i) =>
    `<div class="dialogue-card" style="transition-delay:${i*0.12}s">
      <div class="dialogue-text">${dl.text}</div>
      <div class="dialogue-speaker">— ${dl.speaker}</div>
    </div>`
  ).join('');
 
  // Animate panel in
  dramaPanel.classList.remove('show');
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      dramaPanel.classList.add('show');
      // Stagger dialogue cards
      setTimeout(() => {
        dialogueList.querySelectorAll('.dialogue-card').forEach((c,i) => {
          setTimeout(() => c.classList.add('visible'), i * 130);
        });
      }, 350);
    });
  });
 
  // Scroll panel into view
  setTimeout(() => dramaPanel.scrollIntoView({ behavior: 'smooth', block: 'start' }), 200);
 
  // Launch floaters
  launchFloaters(key);
}
 
// ── Card click handlers ─────────────────────────────────
document.querySelectorAll('.drama-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.drama-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    showDramaPanel(card.dataset.drama);
  });
  card.addEventListener('keydown', e => {
    if(e.key === 'Enter' || e.key === ' ') card.click();
  });
});
 
// ── Intersection Observer: animate cards on scroll ──────
const cardObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if(e.isIntersecting) {
      e.target.style.animationPlayState = 'running';
    }
  });
}, { threshold: 0.2 });
 
document.querySelectorAll('.drama-card').forEach(c => {
  c.style.animationPlayState = 'paused';
  cardObserver.observe(c);
});
 
</script>
 
<!-- ══ BIRTHDAY SECTION ══ -->
<style>
/* ── Birthday page ── */
#bday {
  position: relative;
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  overflow: hidden;
  padding: 5rem 2rem 6rem;
  z-index: 1;
}
 
/* confetti canvas behind everything */
#confettiCanvas {
  position: absolute; inset: 0;
  pointer-events: none; z-index: 0;
}
 
.bday-inner {
  position: relative; z-index: 5;
  display: flex; flex-direction: column;
  align-items: center; text-align: center;
  max-width: 780px;
}
 
/* ── Big birthday text ── */
.bday-top-emoji { font-size: clamp(2.5rem,7vw,4.5rem); animation: emojiPop 1.2s cubic-bezier(.34,1.72,.64,1) both; }
@keyframes emojiPop { from{transform:scale(0) rotate(-20deg);opacity:0} to{transform:scale(1) rotate(0);opacity:1} }
 
.bday-title {
  font-family: 'Cinzel Decorative', serif;
  font-size: clamp(2rem, 7vw, 5rem);
  font-weight: 900; letter-spacing: .15em;
  color: var(--accent);
  margin: .6rem 0 .3rem;
  animation: bdaySlide .9s .2s cubic-bezier(.34,1.56,.64,1) both;
  text-shadow: 0 0 60px var(--glow), 0 0 120px var(--glow);
}
.bday-name {
  font-family: 'Cinzel Decorative', serif;
  font-size: clamp(2.8rem, 9vw, 6.5rem);
  font-weight: 900; letter-spacing: .22em;
  color: var(--accent);
  animation: bdaySlide .9s .35s cubic-bezier(.34,1.56,.64,1) both;
  text-shadow: 0 0 80px var(--glow), 0 0 180px var(--glow);
  position: relative;
}
.bday-name::after {
  content: attr(data-n);
  position: absolute; inset: 0;
  color: transparent; -webkit-text-stroke: 1px var(--accent);
  opacity: .2; transform: translate(4px,4px); pointer-events: none;
}
@keyframes bdaySlide { from{opacity:0;transform:translateY(40px)} to{opacity:1;transform:translateY(0)} }
 
.bday-age {
  font-family: 'Bodoni Moda', serif;
  font-size: clamp(1rem,2.5vw,1.5rem);
  letter-spacing: .5em; opacity: .55;
  margin: .8rem 0 2rem;
  animation: bdaySlide .9s .5s both;
}
 
.bday-divider {
  width: 1px; height: 60px;
  background: linear-gradient(to bottom, transparent, var(--accent), transparent);
  margin: .5rem auto 2rem; opacity: .4;
}
 
/* ── Paragraph ── */
.bday-para {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(1rem, 2vw, 1.25rem);
  line-height: 2; letter-spacing: .04em;
  opacity: .82; max-width: 660px;
  animation: bdaySlide .9s .65s both;
  color: var(--accent); transition: color 1.1s;
}
.bday-para em { font-style: italic; opacity: 1; }
.bday-para strong { font-weight: 700; opacity: 1; }
 
/* ── Celebrate button ── */
.celebrate-wrap {
  margin-top: 3rem;
  animation: bdaySlide .9s .85s both;
}
.celebrate-btn {
  position: relative; cursor: pointer;
  background: transparent; border: none; outline: none;
  padding: 0; font-size: 0;
}
.celebrate-btn-inner {
  position: relative; overflow: hidden;
  padding: 18px 58px;
  border: 2px solid var(--accent);
  font-family: 'Cinzel Decorative', serif;
  font-size: clamp(.85rem, 2vw, 1.1rem);
  letter-spacing: .4em; text-transform: uppercase;
  color: var(--accent);
  transition: color .35s, border-color 1.1s;
  background: transparent;
  cursor: pointer;
  animation: btnFlash 1.8s ease-in-out infinite;
}
@keyframes btnFlash {
  0%,100% { box-shadow: 0 0 12px var(--glow), 0 0 30px var(--glow), inset 0 0 12px transparent; }
  50%      { box-shadow: 0 0 30px var(--glow), 0 0 70px var(--glow), inset 0 0 20px var(--glow); }
}
.celebrate-btn-inner::before {
  content:''; position:absolute; inset:0;
  background: var(--accent); transform:scaleX(0);
  transform-origin:left; transition:transform .4s cubic-bezier(.4,0,.2,1); z-index:0;
}
.celebrate-btn-inner:hover::before { transform:scaleX(1); }
.celebrate-btn-inner:hover { color: var(--bg); }
.celebrate-btn-inner span { position:relative; z-index:1; }
 
/* little light dots around button */
.btn-light {
  position: absolute;
  border-radius: 50%;
  background: var(--accent);
  animation: blink ease-in-out infinite;
  pointer-events: none;
}
@keyframes blink {
  0%,100%{ opacity:.15; transform:scale(.6); }
  50%    { opacity:1;   transform:scale(1.3); }
}
 
/* ══ DISCO OVERLAY ══ */
#discoOverlay {
  position: fixed; inset: 0; z-index: 8000;
  display: none; flex-direction: column;
  align-items: center; justify-content: flex-start;
  overflow-y: auto; overflow-x: hidden;
  background: #050508;
  padding: 0 0 4rem;
}
#discoOverlay.show { display: flex; }
 
/* disco background flash */
#discoOverlay::before {
  content:''; position:fixed; inset:0; z-index:0; pointer-events:none;
  animation: discoFlash 0.38s linear infinite;
}
@keyframes discoFlash {
  0%  { background: rgba(255,0,120,.04); }
  14% { background: rgba(0,200,255,.05); }
  28% { background: rgba(255,255,0,.04); }
  42% { background: rgba(120,0,255,.05); }
  57% { background: rgba(255,100,0,.04); }
  71% { background: rgba(0,255,150,.05); }
  85% { background: rgba(255,0,200,.04); }
  100%{ background: rgba(255,0,120,.04); }
}
 
/* disco balls */
.disco-ball-wrap {
  position: fixed; z-index: 8010; pointer-events: none;
}
.disco-ball-wrap.left  { bottom: 2rem; left:  2rem; }
.disco-ball-wrap.right { bottom: 2rem; right: 2rem; }
.disco-ball-wrap canvas { display:block; }
 
/* disco content */
.disco-content {
  position: relative; z-index: 8020;
  width: 100%; max-width: 820px;
  padding: 4rem 2rem 3rem;
  text-align: center;
}
 
.disco-close {
  position: fixed; top: 1.4rem; right: 1.8rem;
  z-index: 8050; background: transparent;
  border: 1px solid rgba(255,255,255,.3); color: rgba(255,255,255,.7);
  font-size: 1.1rem; padding: .5rem 1rem; cursor: pointer;
  font-family: 'Bodoni Moda', serif; letter-spacing: .2em;
  transition: border-color .3s, color .3s;
}
.disco-close:hover { border-color: #fff; color: #fff; }
 
.disco-title {
  font-family: 'Cinzel Decorative', serif;
  font-size: clamp(1.5rem, 5vw, 3rem);
  font-weight: 900; letter-spacing: .18em;
  margin-bottom: .5rem;
  animation: rainbowText 3s linear infinite;
}
.disco-sub {
  font-style: italic; font-size: clamp(.8rem,1.8vw,1rem);
  letter-spacing: .3em; opacity: .5; color: #fff; margin-bottom: 2.5rem;
}
@keyframes rainbowText {
  0%  { color: #ff6b8a; text-shadow:0 0 30px #ff6b8a,0 0 60px #ff6b8a; }
  16% { color: #ffb347; text-shadow:0 0 30px #ffb347,0 0 60px #ffb347; }
  33% { color: #fffb5c; text-shadow:0 0 30px #fffb5c,0 0 60px #fffb5c; }
  50% { color: #5cffa0; text-shadow:0 0 30px #5cffa0,0 0 60px #5cffa0; }
  66% { color: #5cc8ff; text-shadow:0 0 30px #5cc8ff,0 0 60px #5cc8ff; }
  83% { color: #c45cff; text-shadow:0 0 30px #c45cff,0 0 60px #c45cff; }
  100%{ color: #ff6b8a; text-shadow:0 0 30px #ff6b8a,0 0 60px #ff6b8a; }
}
 
.song-list {
  list-style: none; width: 100%;
  display: flex; flex-direction: column; gap: .7rem;
}
.song-item {
  display: flex; align-items: center; gap: 1rem;
  padding: 1rem 1.5rem;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.03);
  transition: background .25s, border-color .25s, transform .25s;
  cursor: default;
  animation: songSlide .5s both;
}
.song-item:hover {
  background: rgba(255,255,255,.09);
  border-color: rgba(255,255,255,.35);
  transform: translateX(6px);
}
@keyframes songSlide { from{opacity:0;transform:translateX(-22px)} to{opacity:1;transform:translateX(0)} }
.song-num {
  font-family: 'Bodoni Moda', serif;
  font-size: .75rem; letter-spacing: .35em;
  color: rgba(255,255,255,.3); min-width: 2.2rem; flex-shrink: 0;
}
.song-note { font-size: 1.2rem; flex-shrink: 0; animation: noteBounce 1s ease-in-out infinite alternate; }
@keyframes noteBounce { from{transform:translateY(0)} to{transform:translateY(-4px)} }
.song-info { text-align: left; flex: 1; }
.song-title {
  font-family: 'Bodoni Moda', serif;
  font-size: clamp(.85rem,1.8vw,1rem);
  letter-spacing: .12em; color: #fff; margin-bottom: .15rem;
  animation: rainbowText 3s linear infinite;
}
.song-film {
  font-style: italic; font-size: .72rem;
  letter-spacing: .1em; color: rgba(255,255,255,.4);
}
</style>
 
<!-- Confetti canvas (behind birthday section) -->
<section id="bday">
  <canvas id="confettiCanvas"></canvas>
 
  <div class="bday-inner" id="bdayInner">
    <div class="bday-top-emoji">🥳🎂🥳</div>
    <h2 class="bday-title">Happy 19th Birthday</h2>
    <h2 class="bday-name" data-n="Penduuu">Penduuu !!!</h2>
    <div class="bday-age">✦ &nbsp; XIX &nbsp; ✦</div>
    <div class="bday-divider"></div>
 
    <p class="bday-para">
      Okay Pendu, nineteen years of you on this planet and the universe is still trying to recover 🌍✨<br><br>
      <em>Here's the thing — you're stepping into the year where everything starts to matter.</em>
      The syllabus isn't going to read itself (trust me, I checked), and those dreams of yours?
      They've got an <strong>expiry date only if you let them.</strong><br><br>
      So open those books, attend those classes — yes, even the 8 AMs —
      and know that every small effort today is secretly building the version of you
      that your future self will be <em>embarrassingly proud of.</em><br><br>
      But more than all of that — <strong>keep that smile alive.</strong>
      The ridiculous, full-face, eyes-disappearing kind.
      Because that smile? That's the best thing about you,
      and the world genuinely does not deserve it, but please give it anyway. 💫<br><br>
      <em>Here's to 19 — may your grades be high and your stress be low.</em> 🎉
    </p>
 
    <div class="celebrate-wrap">
      <button class="celebrate-btn" id="celebrateBtn" aria-label="Let's Celebrate">
        <div class="celebrate-btn-inner" id="celebrateBtnInner">
          <span>🎉 &nbsp; Let's Celebrate &nbsp; 🎉</span>
        </div>
      </button>
    </div>
  </div>
</section>
 
<!-- ══ DISCO OVERLAY ══ -->
<div id="discoOverlay">
  <button class="disco-close" id="discoClose">✕ close</button>
 
  <!-- Disco balls (canvas, rendered by JS) -->
  <div class="disco-ball-wrap left">
    <canvas id="ballLeft" width="130" height="130"></canvas>
  </div>
  <div class="disco-ball-wrap right">
    <canvas id="ballRight" width="130" height="130"></canvas>
  </div>
 
  <div class="disco-content">
    <h2 class="disco-title">🪩 Penduuu's Playlist 🪩</h2>
    <p class="disco-sub">20 bops · no skips · full send</p>
 
    <ul class="song-list" id="songList"></ul>
  </div>
</div>
 
<script>
// ══════════════════════════════════════════════════════════
//  BIRTHDAY SECTION
// ══════════════════════════════════════════════════════════
 
// ── Confetti ──────────────────────────────────────────────
const confCv  = document.getElementById('confettiCanvas');
const confCtx = confCv.getContext('2d');
 
function resizeConf(){
  confCv.width  = confCv.parentElement.offsetWidth;
  confCv.height = confCv.parentElement.offsetHeight;
}
resizeConf();
window.addEventListener('resize', resizeConf);
 
const COLORS = ['#ff6b8a','#ffb347','#fffb5c','#5cffa0','#5cc8ff','#c45cff','#ff8c42','#e0aaff'];
const pieces = [];
for(let i=0;i<120;i++){
  pieces.push({
    x: Math.random(),
    y: Math.random() * -1.5,
    r: Math.random()*6+3,
    color: COLORS[Math.floor(Math.random()*COLORS.length)],
    speed: Math.random()*.004+.001,
    wobble: Math.random()*Math.PI*2,
    wSpeed: (Math.random()-.5)*.06,
    rot: Math.random()*Math.PI*2,
    rSpeed: (Math.random()-.5)*.06,
    type: Math.floor(Math.random()*3), // 0=circle, 1=rect, 2=star
    size: Math.random()*8+4,
  });
}
 
function drawConf(){
  const W=confCv.width, H=confCv.height;
  confCtx.clearRect(0,0,W,H);
  pieces.forEach(p=>{
    p.y += p.speed;
    p.wobble += p.wSpeed;
    p.rot += p.rSpeed;
    if(p.y > 1.1) { p.y = -0.12; p.x = Math.random(); }
    const px = p.x*W + Math.sin(p.wobble)*30;
    const py = p.y*H;
    confCtx.save();
    confCtx.translate(px,py);
    confCtx.rotate(p.rot);
    confCtx.globalAlpha = .85;
    confCtx.fillStyle = p.color;
    if(p.type===0){
      confCtx.beginPath(); confCtx.arc(0,0,p.r,0,Math.PI*2); confCtx.fill();
    } else if(p.type===1){
      confCtx.fillRect(-p.size/2,-p.size/4,p.size,p.size/2);
    } else {
      // little star
      confCtx.beginPath();
      for(let s=0;s<5;s++){
        const a=s*Math.PI*2/5 - Math.PI/2;
        const b=a+Math.PI/5;
        confCtx.lineTo(Math.cos(a)*p.r,Math.sin(a)*p.r);
        confCtx.lineTo(Math.cos(b)*p.r*.45,Math.sin(b)*p.r*.45);
      }
      confCtx.closePath(); confCtx.fill();
    }
    confCtx.restore();
  });
  requestAnimationFrame(drawConf);
}
 
// Start confetti when birthday section is visible
const bdayObserver = new IntersectionObserver(entries=>{
  if(entries[0].isIntersecting) drawConf();
}, {threshold:0.1});
bdayObserver.observe(document.getElementById('bday'));
 
// ── Button light dots ──────────────────────────────────────
(function(){
  const wrap = document.querySelector('.celebrate-wrap');
  const lights = [
    {top:'-8px',left:'20%'},{top:'-8px',left:'50%'},{top:'-8px',left:'80%'},
    {bottom:'-8px',left:'20%'},{bottom:'-8px',left:'50%'},{bottom:'-8px',left:'80%'},
    {top:'50%',left:'-8px'},{top:'50%',right:'-8px'},
  ];
  lights.forEach((pos,i)=>{
    const d=document.createElement('div'); d.className='btn-light';
    Object.assign(d.style,{...pos,width:'7px',height:'7px',
      animationDuration:.8+i*.15+'s',animationDelay:i*.1+'s'});
    wrap.appendChild(d);
  });
})();
 
// ── Celebrate button ───────────────────────────────────────
document.getElementById('celebrateBtn').addEventListener('click', openDisco);
document.getElementById('celebrateBtnInner').addEventListener('click', openDisco);
 
// ══════════════════════════════════════════════════════════
//  DISCO OVERLAY
// ══════════════════════════════════════════════════════════
const SONGS = [
  { title:'Balam Pichkari',      film:'Yeh Jawaani Hai Deewani (2013)' },
  { title:'Badtameez Dil',       film:'Yeh Jawaani Hai Deewani (2013)' },
  { title:'Gallan Goodiyaan',    film:'Dil Dhadakne Do (2015)' },
  { title:'Senorita',            film:'Zindagi Na Milegi Dobara (2011)' },
  { title:'Ainvayi Ainvayi',     film:'Band Baaja Baaraat (2010)' },
  { title:'Desi Girl',           film:'Dostana (2008)' },
  { title:'London Thumakda',     film:'Queen (2014)' },
  { title:'Nagada Sang Dhol',    film:'Ram-Leela (2013)' },
  { title:'Ghagra',              film:'Yeh Jawaani Hai Deewani (2013)' },
  { title:'Tune Maari Entriyaan',film:'Gunday (2014)' },
  { title:'Shake It Like Shamur',film:'Noor (2017)' },
  { title:'Dilliwali Girlfriend',film:'Yeh Jawaani Hai Deewani (2013)' },
  { title:'Morni Banke',         film:'Badhaai Do (2022)' },
  { title:'Radha',               film:'Student of the Year (2012)' },
  { title:'Dance Ka Bhoot',      film:'Brahmastra (2022)' },
  { title:'Zingaat (Hindi)',      film:'Dhadak (2018)' },
  { title:'Kala Chashma',        film:'Baar Baar Dekho (2016)' },
  { title:'Kar Gayi Chull',      film:'Kapoor & Sons (2016)' },
  { title:'Param Sundari',       film:'Mimi (2021)' },
  { title:'Wakhra Swag',         film:'Judgementall Hai Kya (2019)' },
];
 
const NOTES = ['🎵','🎶','🎸','🎤','🥁','🎹','🪗','🎺','🪩','🕺','💃','🔥'];
 
function buildSongList(){
  const ul = document.getElementById('songList');
  ul.innerHTML = '';
  SONGS.forEach((s,i)=>{
    const li = document.createElement('li');
    li.className = 'song-item';
    li.style.animationDelay = (i*0.06)+'s';
    li.innerHTML = `
      <span class="song-num">0${i<9?'':''}${i+1}</span>
      <span class="song-note" style="animation-delay:${i*.08}s">${NOTES[i%NOTES.length]}</span>
      <div class="song-info">
        <div class="song-title">${s.title}</div>
        <div class="song-film">${s.film}</div>
      </div>`;
    ul.appendChild(li);
  });
}
 
// ── Disco Ball Canvas ──────────────────────────────────────
function makeDiscoBall(canvasId, angleOffset){
  const cv  = document.getElementById(canvasId);
  const ctx = cv.getContext('2d');
  const W = cv.width, H = cv.height;
  const R = W*0.36;
  const cx = W/2, cy = H/2;
  let angle = angleOffset;
  const ROWS=10, COLS=16;
  const TILE_COLORS=['#ffffff','#ffe0f0','#c8e8ff','#fffbe0','#e0c8ff','#c8ffe0','#ffd6c8'];
  let t=0;
 
  function drawBall(){
    ctx.clearRect(0,0,W,H);
    t += .012;
    angle += .008;
 
    // Shadow under ball
    const shg = ctx.createRadialGradient(cx+R*.2,cy+R*.85,2,cx+R*.2,cy+R*.85,R*.8);
    shg.addColorStop(0,'rgba(0,0,0,.5)'); shg.addColorStop(1,'rgba(0,0,0,0)');
    ctx.beginPath(); ctx.ellipse(cx+R*.15,cy+R*.9,R*.7,R*.2,0,0,Math.PI*2);
    ctx.fillStyle=shg; ctx.fill();
 
    // Ball sphere clip
    ctx.save();
    ctx.beginPath(); ctx.arc(cx,cy,R,0,Math.PI*2); ctx.clip();
 
    // Dark base
    const bg=ctx.createRadialGradient(cx-R*.3,cy-R*.3,R*.05,cx,cy,R);
    bg.addColorStop(0,'#555'); bg.addColorStop(1,'#111');
    ctx.fillStyle=bg; ctx.fillRect(cx-R,cy-R,R*2,R*2);
 
    // Tiles
    for(let row=0;row<ROWS;row++){
      for(let col=0;col<COLS;col++){
        // spherical mapping
        const phi   = (row/(ROWS-1))*Math.PI;       // 0→π (top→bottom)
        const theta = (col/COLS)*Math.PI*2 + angle;  // rotating azimuth
        const sx = cx + R*Math.sin(phi)*Math.cos(theta);
        const sy = cy + R*(-Math.cos(phi))*.88;       // slight vert squish
        const sz = Math.sin(phi)*Math.sin(theta);     // depth (-1..1)
 
        if(sz < -0.15) continue; // back face cull
 
        const tileW = Math.max(2, (R*.36)*(Math.sin(phi)+.2)*(0.4+sz*.6));
        const tileH = Math.max(2, R*.11*(0.4+sz*.6));
        // brightness from depth + animated shimmer
        const shimmer = Math.sin(theta*3+t*4+row*.8)>.6 ? 1.6 : 1;
        const bright  = (.5 + sz*.5) * shimmer;
 
        const base = TILE_COLORS[(row*3+col*2+Math.floor(t*2))%TILE_COLORS.length];
        ctx.save();
        ctx.translate(sx,sy);
        ctx.rotate(theta*.25);
        // glow on bright tiles
        if(bright>1.1){
          ctx.shadowColor='rgba(255,255,255,.9)'; ctx.shadowBlur=8;
        }
        ctx.globalAlpha = Math.min(1, bright*.9);
        ctx.fillStyle = base;
        ctx.fillRect(-tileW/2,-tileH/2,tileW,tileH);
        ctx.globalAlpha=1; ctx.shadowBlur=0;
        ctx.restore();
      }
    }
    ctx.restore();
 
    // Specular highlight
    const hl=ctx.createRadialGradient(cx-R*.28,cy-R*.3,0,cx-R*.28,cy-R*.3,R*.45);
    hl.addColorStop(0,'rgba(255,255,255,.55)');hl.addColorStop(1,'rgba(255,255,255,0)');
    ctx.save(); ctx.beginPath(); ctx.arc(cx,cy,R,0,Math.PI*2); ctx.clip();
    ctx.fillStyle=hl; ctx.fillRect(cx-R,cy-R,R*2,R*2); ctx.restore();
 
    // Top mount
    ctx.beginPath(); ctx.rect(cx-4,cy-R-18,8,20);
    ctx.fillStyle='rgba(180,180,180,.6)'; ctx.fill();
    ctx.beginPath(); ctx.arc(cx,cy-R-18,5,0,Math.PI*2);
    ctx.fillStyle='rgba(200,200,200,.5)'; ctx.fill();
 
    // Hanging rope
    ctx.beginPath(); ctx.moveTo(cx,cy-R-18); ctx.lineTo(cx,0);
    ctx.strokeStyle='rgba(160,160,160,.3)'; ctx.lineWidth=1.5; ctx.stroke();
 
    requestAnimationFrame(drawBall);
  }
  drawBall();
}
 
function openDisco(){
  const overlay = document.getElementById('discoOverlay');
  buildSongList();
  overlay.classList.add('show');
  document.body.style.overflow='hidden';
  // Init disco balls
  makeDiscoBall('ballLeft',  0);
  makeDiscoBall('ballRight', Math.PI);
}
