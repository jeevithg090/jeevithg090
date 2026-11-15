<a href="https://jeevithg.dev">
  <img src="./assets/header.svg" width="100%" alt="Jeevith Gangadhara: AI security, adversarial AI and LLM agents. The model proposes; code and humans decide." />
</a>

<p align="center">
  <a href="https://jeevithg.dev"><img src="https://img.shields.io/badge/jeevithg.dev-0F766E?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website: jeevithg.dev" /></a>
  <a href="https://www.linkedin.com/in/jeevith-gangadhara-782b21311"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:g.jeevith090@gmail.com"><img src="https://img.shields.io/badge/Email-111827?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<h3 align="center">I work where offensive security meets AI,<br/>and I build AI agents that ask before they act.</h3>

<br/>

<img src="./assets/whoami.svg" width="100%" alt="whoami: final-year BSc Computer Science at the University of Hertfordshire. Focus: agent security, prompt injection, tool permissions, adversarial robustness, AI control and evals. First-author adversarial-ML paper, HTB CPTS, #1 global TraceBash CTF 2026. Working on UofT AI Project X; looking for AI security research." />

## By the numbers

<table>
  <tr>
    <td align="center" width="33%" colspan="2"><h2>#1</h2>globally at <b>TraceBash CTF 2026</b><br/><sub>plus #2 RIFFHACK, 1st BushBash (ANU)</sub></td>
    <td align="center" width="33%" colspan="2"><h2>487,523</h2>URLs in <b>MultiPhishDB</b><br/><sub>six script families, bilingual labels, κ = 0.91</sub></td>
    <td align="center" width="33%" colspan="2"><h2>350 ms</h2>end-to-end <b>voice agent</b>, 7 languages<br/><sub>Whisper + LLaMA 3.2 + Piper, under 2¢ a minute</sub></td>
  </tr>
  <tr>
    <td align="center" width="50%" colspan="3"><h2>0 → ~10k</h2>users at V1 launch<br/><sub>tech lead, multi-tenant Postgres with RLS</sub></td>
    <td align="center" width="50%" colspan="3"><h2>45+</h2><b>hackathons and CTFs</b><br/><sub>HackMIT, Junction, OxHack, Meta, London × AI Science</sub></td>
  </tr>
</table>

## Activity

<a href="https://github.com/jeevithg090">
  <img src="https://ghchart.rshah.org/jeevithg090" width="100%" alt="GitHub contribution calendar for the last year, updated live" />
</a>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=jeevithg090&hide_border=true&background=0D1117&stroke=1F2937&ring=2DD4BF&fire=F59E0B&currStreakNum=F8FAFC&sideNums=F8FAFC&currStreakLabel=5EEAD4&sideLabels=99F6E4&dates=94A3B8" height="170" alt="Total contributions, current streak and longest streak, updated live" />
</p>

## Featured work

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/UniPhish">UniPhish</a></h3>
      <p><sub><b>Unicode-native phishing detection</b> · first-author research, manuscript for IEEE TIFS</sub></p>
      <ul>
        <li>Byte-level model that reads every Unicode character, where ASCII-vocabulary detectors map Arabic, CJK, Devanagari and Hangul to a single unknown token.</li>
        <li>Built <b>MultiPhishDB</b> (487,523 URLs) and reproduced the source IEEE paper end to end, correcting its parameter count and overstated claims.</li>
        <li>Grew into a platform: explainable verdicts for URLs, pages, emails, files and QR codes, plus <b>AgentGuard</b>, an MCP layer that screens what AI agents read and send.</li>
      </ul>
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow" />
      <img src="https://img.shields.io/badge/adversarial_training-0F766E" alt="Adversarial training" />
      <img src="https://img.shields.io/badge/MCP-111827" alt="MCP" />
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/Steward">Steward</a></h3>
      <p><sub><b>Open-source personal AI agent</b> · OxHack 26, University of Oxford</sub></p>
      <ul>
        <li>An agent with its own browser, files and shell. Models plan; deterministic code decides every amount, permission and "yes".</li>
        <li>Governance on every tool call: deny rules, taint tracking that forces approval after untrusted input, outbound secret checks, an SSRF proxy and a hash-chained audit log.</li>
        <li>Red-teamed live: an injected "forward all invoices" email was refused, and signed mandates refused 10/10 forgery and scope attacks.</li>
      </ul>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
      <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
      <img src="https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white" alt="Playwright" />
      <img src="https://img.shields.io/badge/MCP-111827" alt="MCP" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/AlertForge">SentinelForge</a></h3>
      <p><sub><b>Autonomous SOC war room</b> · LLM agents with a human in charge</sub></p>
      <ul>
        <li>Folds alert storms into single incidents, then a team of LLM agents triages, investigates and plans containment.</li>
        <li>A human approver stands in front of every action that changes production.</li>
      </ul>
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/multi--agent-0F766E" alt="Multi-agent" />
      <img src="https://img.shields.io/badge/incident_response-B91C1C" alt="Incident response" />
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/IntentGuard">IntentGuard</a></h3>
      <p><sub><b>Risk-aware cross-chain treasury agent</b> · the AI decides, the chain enforces</sub></p>
      <ul>
        <li>Turns a goal like "move $5,000 USDC to the best safe yield, never above risk tier 2" into an ERC-7683-style cross-chain order.</li>
        <li>Scores every solver route on cited evidence, then runs an adversarial Proposer / Red Team / Arbiter review before anything moves.</li>
      </ul>
      <img src="https://img.shields.io/badge/Solidity-363636?logo=solidity&logoColor=white" alt="Solidity" />
      <img src="https://img.shields.io/badge/red_team_agents-B91C1C" alt="Red-team agents" />
      <img src="https://img.shields.io/badge/ERC--7683-111827" alt="ERC-7683" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/PromptAI">PromptForge</a></h3>
      <p><sub><b>Multi-agent GenAI platform</b> · automated evaluation built in</sub></p>
      <ul>
        <li>13 agents on a 13-state supervisor state machine, routing each step across Groq, Gemini, Cerebras and 345+ OpenRouter models.</li>
        <li>Every output scored on an auditable 8-dimension rubric, with fail-closed safety gates, citation-level RAG and bring-your-own-key envelope encryption.</li>
      </ul>
      <img src="https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white" alt="Next.js" />
      <img src="https://img.shields.io/badge/Hono-E36002?logo=hono&logoColor=white" alt="Hono" />
      <img src="https://img.shields.io/badge/pgvector-4169E1?logo=postgresql&logoColor=white" alt="pgvector" />
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/jeevithg090/Axi0N_Meta">Rulecam</a></h3>
      <p><sub><b>Plain-language rules for any camera</b> · Meta Global AI Developer Hackathon 2026</sub></p>
      <ul>
        <li>Describe what worries you in your own language; Rulecam says honestly what a camera can and can't check and proves each rule before it goes live.</li>
        <li>A second Meta model reviews every alert before anyone is bothered, and the evidence is kept so anyone can check it.</li>
      </ul>
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/computer_vision-7C3AED" alt="Computer vision" />
      <img src="https://img.shields.io/badge/Llama-0467DF?logo=meta&logoColor=white" alt="Llama" />
    </td>
  </tr>
</table>

<details>
<summary><b>More things I've built</b></summary>
<br/>

| Project | What it is |
|---|---|
| [qPilot](https://github.com/jeevithg090/qpilot) | Open qPCR analysis with human-gated AI, co-built with a PhD scientist as a selected developer at London × AI Science. AI proposes, a deterministic engine checks, a scientist decides. |
| [Voice AI Model](https://github.com/jeevithg090/Voice-AI-Model) | Low-cost real-time voice agent for Hindi, Tamil, Telugu, Kannada and English, built only from open models on hardware you control. |
| [Apollo Omni-Indic](https://github.com/jeevithg090/Speech-to-Speech) | Research prototype of a speech-to-speech assistant for Indian hospital helplines, built around one transformer that both hears and speaks. |
| [Piper Tamil TTS](https://github.com/jeevithg090/FInal-Voice) | One resumable command that turns an AMD ROCm GPU server into a trained Tamil text-to-speech voice. |
| [GeoShardDB](https://github.com/jeevithg090/Distributed_System-Geo-Sharding) | Multi-region distributed database simulator: geo-sharded PostgreSQL, Redis caching and circuit-breaker failover. |
| [ComputerVision-Orchestra](https://github.com/jeevithg090/ComputerVision-Orchestra) | Multi-modal evidence review for damage claims: photos, chat and history in, an explained decision out. |
| [Keystone](https://github.com/jeevithg090/Prism) | AI agents read your syllabus, the job market and your code, and turn them into a roadmap from degree to industry. |

</details>

## Research

- **UniPhish: Unicode-native phishing URL detection.** First author, with Manipal faculty co-authors; manuscript for IEEE TIFS.
- **Project X, UofT AI (University of Toronto).** Selected for the global undergraduate ML research competition; cybersecurity research project, 2026–27, in progress.
- **Low-latency multilingual voice agent.** Research paper, Enigma, MAHE 2025: self-hosted Whisper + LLaMA 3.2 + Piper in six Indian languages plus English, benchmarked on an AMD Instinct MI300X.

**Interests:** agent security (prompt injection, tool-use permissions, sandboxing) · adversarial robustness and AI control · LLM evaluations · AI-enabled offensive security

## Experience

| | Role | When |
|---|---|---|
| **VoiceDots** | AI Voice Agent Developer: production GenAI voice agents (ASR → LLM → TTS over WebRTC) | Jul – Sep 2026 |
| **Ericsson** | Software Engineer Intern, Infrastructure & Network Security | May – Jul 2026 |
| **Colcord** | Full Stack Developer & Tech Lead: owned V1 from zero to ~10,000 users | Jul 2025 – Jan 2026 |
| **Kasturba Hospital** | AI Intern, Clinical ML: EHR pipelines and AI-versus-clinician agreement studies | Aug – Dec 2025 |

## Offensive security and awards

| | |
|---|---|
| 🥇 **TraceBash CTF 2026** | 1st place globally: reverse engineering, cryptography, web exploitation, binary analysis |
| 🥈 **RIFFHACK CTF 2026** | 2nd place globally: forensics, network exploitation, vulnerability research |
| 🥇 **BushBash CTF 2026** | 1st place, hosted by the Australian National University |
| 🛡️ **HTB CPTS** | Hack The Box Certified Penetration Testing Specialist |
| 🏛️ **HackMIT 2026** | 33rd worldwide in the admissions puzzle (top 50 earn entry); sponsor-track prize winner at MIT |
| ✨ **Selected** | London × AI Science developer cohort · Junction (Finland) travel grant · IIIT Hyderabad Hackathon finalist |

## Toolbox

<p>
  <img src="https://skillicons.dev/icons?i=py,cpp,ts,js,go,java,swift,solidity,pytorch,tensorflow,fastapi,react,nextjs,nodejs&perline=14" alt="Python, C++, TypeScript, JavaScript, Go, Java, Swift, Solidity, PyTorch, TensorFlow, FastAPI, React, Next.js, Node.js" />
  <br/>
  <img src="https://skillicons.dev/icons?i=docker,aws,postgres,redis,sqlite,linux,bash,git,githubactions,kali&perline=14" alt="Docker, AWS, PostgreSQL, Redis, SQLite, Linux, Bash, Git, GitHub Actions, Kali Linux" />
</p>

- **Security:** penetration testing (CPTS), reverse engineering, binary analysis, web and network exploitation, cryptography, threat modelling, prompt-injection defences
- **ML and research:** adversarial training, knowledge distillation, quantisation, ablations, dataset construction, evaluation design
- **LLMs and agents:** orchestration, tool use and MCP, RAG, automated evals, open models (LLaMA, Qwen, Whisper via Ollama)

## Education

- **BSc (Hons) Computer Science**, University of Hertfordshire, UK · 2026–2027 · expected First Class Honours · transferred on a Merit Scholarship, Student Representative
- **BSc Computer Science Engineering**, ICAS, Manipal Academy of Higher Education, India · 2024–2026

<br/>

<p align="center">
  <sub>Looking for empirical AI security research: agent security, adversarial robustness, evals.<br/>
  Say hello at <a href="https://jeevithg.dev">jeevithg.dev</a> or on <a href="https://www.linkedin.com/in/jeevith-gangadhara-782b21311">LinkedIn</a>.</sub>
</p>
