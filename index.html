<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sémantický barman</title>
    <style>
        :root {
            --bg: #12100e;
            --surface: #1b1815;
            --surface-2: #24201c;
            --ink: #f3ece0;
            --muted: #a39787;
            --line: #36302a;
            --accent: #df8d2d;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: var(--bg);
            color: var(--ink);
            font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px;
        }

        .shell {
            width: 100%;
            max-width: 980px;
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 14px;
            overflow: hidden;
        }

        .top {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding: 14px 20px;
            background: var(--surface-2);
            border-bottom: 1px solid var(--line);
        }

        .title-wrap {
            display: flex;
            align-items: baseline;
            gap: 10px;
        }

        h1 {
            margin: 0;
            font-size: 1.18rem;
            font-weight: 700;
        }

        .meta-tag {
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
            font-size: 0.76rem;
            color: var(--muted);
        }

        .actions {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .round-txt {
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
            font-size: 0.82rem;
            color: var(--accent);
        }

        .btn-sub {
            background: transparent;
            color: var(--ink);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 6px 11px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
        }

        .btn-sub:hover:not(:disabled) {
            border-color: #5a5046;
            background: rgba(255, 255, 255, 0.03);
        }

        .grid {
            display: grid;
            grid-template-columns: 1.28fr 0.92fr;
        }

        @media (max-width: 820px) {
            .grid {
                grid-template-columns: 1fr;
            }
        }

        .stage-col {
            border-right: 1px solid var(--line);
            display: flex;
            flex-direction: column;
        }

        @media (max-width: 820px) {
            .stage-col {
                border-right: none;
                border-bottom: 1px solid var(--line);
            }
        }

        canvas#bar-canvas {
            display: block;
            width: 100%;
            height: 400px;
            background: #161210;
        }

        .caption {
            padding: 12px 18px;
            background: #161412;
            border-top: 1px solid var(--line);
            display: flex;
            flex-direction: column;
            gap: 3px;
        }

        #status-main {
            font-size: 0.94rem;
            font-weight: 600;
        }

        #status-sub {
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
            font-size: 0.78rem;
            color: var(--muted);
        }

        .side-col {
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .desc {
            margin: 0;
            font-size: 0.88rem;
            line-height: 1.45;
            color: var(--muted);
        }

        .form-row {
            display: flex;
            gap: 8px;
        }

        input[type="text"] {
            flex: 1;
            min-width: 0;
            padding: 11px 13px;
            font-size: 0.96rem;
            color: var(--ink);
            background: var(--bg);
            border: 1px solid var(--line);
            border-radius: 8px;
            outline: none;
        }

        input[type="text"]:focus {
            border-color: var(--accent);
        }

        .btn-main {
            padding: 11px 16px;
            font-size: 0.92rem;
            font-weight: 700;
            color: #16110c;
            background: var(--accent);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            white-space: nowrap;
        }

        .btn-main:hover:not(:disabled) {
            filter: brightness(1.07);
        }

        button:disabled {
            opacity: 0.45;
            cursor: not-allowed;
        }

        #err-box {
            min-height: 18px;
            font-size: 0.82rem;
            color: #f06d6d;
        }

        .log-head {
            display: flex;
            justify-content: space-between;
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
            font-size: 0.75rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding-bottom: 6px;
            border-bottom: 1px solid var(--line);
        }

        .log-list {
            flex: 1;
            max-height: 220px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .log-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            padding: 8px 10px;
            border-radius: 7px;
            background: var(--surface-2);
            border: 1px solid rgba(255, 255, 255, 0.04);
            font-size: 0.85rem;
        }

        .log-word {
            font-weight: 700;
        }

        .log-drink {
            color: var(--muted);
            font-size: 0.78rem;
        }

        .log-score {
            font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
            font-size: 0.8rem;
            font-weight: 600;
            white-space: nowrap;
        }
    </style>
</head>
<body>
<div class="shell">
    <div class="top">
        <div class="title-wrap">
            <h1>Sémantický barman</h1>
            <span class="meta-tag">2D profil · kosínusová podobnosť</span>
        </div>
        <div class="actions">
            <span class="round-txt" id="round-txt">Kolo #1</span>
            <button class="btn-sub" id="new-word-btn" type="button" onclick="manualNewRound()">Nové slovo</button>
        </div>
    </div>

    <div class="grid">
        <div class="stage-col">
            <canvas id="bar-canvas" width="560" height="400"></canvas>
            <div class="caption">
                <div id="status-main">Zadaj slovo a barman namieša prvý drink.</div>
                <div id="status-sub">Čaká na tip · kvalita 0–100</div>
            </div>
        </div>

        <div class="side-col">
            <p class="desc">
                Tipni slovo. Čím bližšie je vo vektorovom priestore k tajnému slovu, tým lepší drink barman namieša. Po uhádnutí sa automaticky spustí ďalšie kolo.
            </p>

            <form class="form-row" onsubmit="event.preventDefault(); submitGuess();">
                <input
                    id="word-input"
                    type="text"
                    autocomplete="off"
                    placeholder="Napr. bager, auto, voda, čaj..."
                />
                <button class="btn-main" id="mix-btn" type="submit">Namiešať</button>
            </form>

            <div id="err-box"></div>

            <div class="log-head">
                <span>Pokusy v kole</span>
                <span>Skóre / #</span>
            </div>
            <div class="log-list" id="log-list"></div>
        </div>
    </div>
</div>

<script>
    let logs = [];
    let busy = false;

    const canvas = document.getElementById("bar-canvas");
    const ctx = canvas.getContext("2d");

    let phase = "idle"; // idle | shake | look | drink | bad | mid | good
    let phaseStart = performance.now();
    let mood = "idle"; // idle | bad | mid | good
    let drinkColor = "#d98a2b";
    let liquidRatio = 0.72;
    let particles = [];

    const INK = "#18120e";

    function resizeCanvas() {
        const rect = canvas.getBoundingClientRect();
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        const w = Math.max(300, Math.round(rect.width));
        const h = Math.max(240, Math.round(rect.height));
        if (canvas.width !== w * dpr || canvas.height !== h * dpr) {
            canvas.width = w * dpr;
            canvas.height = h * dpr;
        }
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function setPhase(nextPhase) {
        phase = nextPhase;
        phaseStart = performance.now();
    }

    function spawnParticles(color, count, originX, originY) {
        for (let i = 0; i < count; i++) {
            particles.push({
                x: originX + (Math.random() - 0.5) * 34,
                y: originY + (Math.random() - 0.5) * 24,
                vx: (Math.random() - 0.5) * 95,
                vy: -40 - Math.random() * 85,
                r: 2.5 + Math.random() * 3,
                life: 1.0,
                color
            });
        }
    }

    function drawBackgroundBottles(counterY, w) {
        // Jemná polička s fľašami v pozadí pre hĺbku scény
        const shelfY = counterY - 122;
        ctx.fillStyle = "#2b1d14";
        ctx.fillRect(28, shelfY, w - 56, 7);

        const bottleSpecs = [
            { x: 64, h: 52, w: 16, col: "#3d6b4c" },
            { x: 88, h: 44, w: 14, col: "#8c4a27" },
            { x: 112, h: 58, w: 17, col: "#2f4e6e" },
            { x: 410, h: 50, w: 15, col: "#7a3b2e" },
            { x: 434, h: 42, w: 14, col: "#5c6b3c" }
        ];

        for (const b of bottleSpecs) {
            ctx.fillStyle = b.col;
            ctx.strokeStyle = "#120c08";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(b.x - b.w / 2, shelfY - b.h, b.w, b.h, 3);
            ctx.fill();
            ctx.stroke();

            // Hrdlo fľaše
            ctx.fillRect(b.x - 4, shelfY - b.h - 10, 8, 10);
        }
    }

    // Ručne kreslený profil barmana otočeného doprava (smerom k pultu a shakeru)
    function drawBartenderProfile(x, y, headNod, headTurn, bodyTilt, bobY, armAngle, currentMood) {
        ctx.save();
        ctx.translate(x, y + bobY);
        ctx.rotate(bodyTilt);

        // Tieň na pulte
        ctx.fillStyle = "rgba(0, 0, 0, 0.45)";
        ctx.beginPath();
        ctx.ellipse(6, 2, 56, 9, 0, 0, Math.PI * 2);
        ctx.fill();

        // Trup / vesta + biela košeľa v bočnom profile
        ctx.fillStyle = "#252c34";
        ctx.strokeStyle = INK;
        ctx.lineWidth = 3;
        ctx.lineJoin = "round";
        ctx.beginPath();
        ctx.moveTo(-34, 0);
        ctx.quadraticCurveTo(-38, -58, -22, -96);
        ctx.quadraticCurveTo(4, -104, 24, -92);
        ctx.quadraticCurveTo(36, -54, 30, 0);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Predná biela košeľa a traky
        ctx.fillStyle = "#ebe3d5";
        ctx.beginPath();
        ctx.moveTo(8, -96);
        ctx.lineTo(25, -90);
        ctx.lineTo(28, -24);
        ctx.lineTo(12, -24);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Hlava v bočnom profile (s výrazným nosom, čelom, bradou a uchom)
        ctx.save();
        ctx.translate(4 + headTurn * 7, -112);
        ctx.rotate(headNod);

        // Krk
        ctx.fillStyle = "#dfa97d";
        ctx.strokeStyle = INK;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(-14, 14);
        ctx.lineTo(12, 14);
        ctx.lineTo(14, 28);
        ctx.lineTo(-16, 28);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
