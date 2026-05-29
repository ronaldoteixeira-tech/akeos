import json

slides_data = [
    {
        "type": "cover",
        "label": "Capa",
        "title": "Aprovação<br><span class='text-transparent bg-clip-text bg-gradient-to-r from-akeos-yellow to-yellow-200'>Inteligente</span>",
        "subtitle": "Estratégias Jurídicas, Gestão Emocional e Alta Performance para a OAB",
        "footer_items": ["📍 Oficina ESMAC + Akeos", "📍 Lara Ferreira dos Santos"]
    },
    {
        "type": "content",
        "label": "Introdução",
        "title": "A grande virada de chave",
        "bullets": [
            "A OAB não é uma competição",
            "Você não precisa acertar tudo",
            "Você precisa atingir a pontuação mínima"
        ],
        "emphasis": "Estudar estrategicamente é mais importante do que estudar exaustivamente."
    },
    {
        "type": "cards",
        "label": "O que veremos hoje",
        "title": "3 PILARES DA APROVAÇÃO",
        "cards": [
            {"label": "Pilar 1", "text": "Rotina ajustada"},
            {"label": "Pilar 2", "text": "Domínio do conteúdo"},
            {"label": "Pilar 3", "text": "Mentalidade e inteligência emocional"}
        ],
        "footer_emphasis": "Estratégias para o dia da prova"
    },
    {
        "type": "section",
        "label": "Pilar 1",
        "title": "ROTINA AJUSTADA",
        "subtitle": "Aprovação exige organização sustentável."
    },
    {
        "type": "content",
        "label": "Pilar 1",
        "title": "Estratégia sem individualidade não funciona",
        "subtitle": "Cada aluno possui uma realidade",
        "bullets": ["trabalho", "estágio", "filhos", "faculdade", "pouco tempo disponível"],
        "emphasis": "O melhor cronograma é o que funciona para sua rotina."
    },
    {
        "type": "content_red",
        "label": "Pilar 1",
        "title": "Metas reais",
        "subtitle": "Constância > intensidade exagerada",
        "bullets": ["Estudar 12h sem conseguir manter", "Estudar todas as matérias ao mesmo tempo", "Criar metas impossíveis"],
        "emphasis": "O melhor plano é aquele que você consegue cumprir."
    },
    {
        "type": "content",
        "label": "Pilar 1",
        "title": "Flexibilidade inteligente",
        "subtitle": "Disciplina não é rigidez",
        "bullets": ["Imprevistos acontecem:", "cansaço", "ansiedade", "problemas pessoais", "desgaste mental"],
        "emphasis": "Um dia ruim não pode virar abandono da preparação."
    },
    {
        "type": "section",
        "label": "Pilar 2",
        "title": "DOMÍNIO DO CONTEÚDO",
        "subtitle": "A OAB cobra interpretação e aplicação prática."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "O foco maior deve estar na lei seca",
        "subtitle": "A banca cobra muito texto de lei",
        "bullets": ["A banca explora:", "prazos", "exceções", "competências", "detalhes legais"],
        "emphasis": "Não basta assistir aula.<br>É preciso ler legislação."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "Saber aplicar o conteúdo ao caso concreto",
        "subtitle": "A prova quer raciocínio jurídico",
        "bullets": ["A OAB cobra:", "interpretação", "identificação de institutos", "aplicação da lei", "resolução prática"],
        "emphasis": "Não basta decorar conceitos."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "Questões são treinamento",
        "subtitle": "Resolver questões acelera aprovação",
        "bullets": ["Questões ajudam a:", "identificar padrões da banca", "melhorar interpretação", "fixar conteúdo", "descobrir pontos fracos"],
        "emphasis": "Questão também é método de aprendizagem."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "Estudar o que é relevante",
        "subtitle": "Estudo estratégico",
        "text": "Nem todas as matérias possuem o mesmo peso.",
        "bullets": ["Priorize:", "assuntos mais cobrados", "temas mais recorrentes", "conteúdos de maior incidência"],
        "emphasis": "A OAB exige pontuação mínima, não perfeição."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "Sair da zona de conforto",
        "subtitle": "Crescimento acontece no desconforto",
        "bullets": ["A aprovação exige enfrentar:", "matérias difíceis", "assuntos cansativos", "conteúdos que geram insegurança"],
        "emphasis": "Evoluir exige enfrentar dificuldades."
    },
    {
        "type": "content",
        "label": "Pilar 2",
        "title": "Simulados são indispensáveis",
        "subtitle": "O simulado aproxima você da prova real",
        "bullets": ["Treine:", "tempo", "resistência mental", "emocional", "ansiedade", "estratégia"],
        "emphasis": "Treinar comportamento também é preparação."
    },
    {
        "type": "section",
        "label": "Pilar 3",
        "title": "MENTALIDADE E INTELIGÊNCIA EMOCIONAL",
        "subtitle": "Aprovação também é emocional."
    },
    {
        "type": "content",
        "label": "Pilar 3",
        "title": "Aprovação também é emocional",
        "subtitle": "A preparação mexe com o psicológico",
        "bullets": ["Em alguns momentos você vai:", "duvidar de si", "sentir medo", "achar que não está evoluindo", "comparar sua evolução com a dos outros"],
        "emphasis": "Inteligência emocional também é preparação."
    },
    {
        "type": "content",
        "label": "Pilar 3",
        "title": "Autoconfiança construída através da evolução real",
        "subtitle": "Confiança vem da evolução",
        "bullets": ["Acompanhe:", "percentual de acertos", "desempenho por matéria", "simulados", "evolução nos resultados"],
        "emphasis": "Quem monitora resultados estuda com estratégia."
    },
    {
        "type": "content",
        "label": "Pilar 3",
        "title": "Pare de se comparar",
        "subtitle": "Cada aluno possui uma trajetória diferente",
        "bullets": ["rotina diferente", "dificuldades diferentes", "base diferente", "tempo diferente de evolução"],
        "emphasis": "Compare-se apenas com sua versão anterior."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "Como funciona a 1ª fase?",
        "subtitle": "",
        "bullets": ["80 questões", "múltipla escolha", "5 horas de duração"],
        "emphasis": "📌 Estratégia de execução importa."
    },
    {
        "type": "list_cols",
        "label": "ESTRUTURA DA PROVA",
        "title": "Questões e disciplinas",
        "subtitle": "Onde estão a maioria das questões?",
        "text": "As disciplinas:",
        "bullets": [
            "• Ética → 8 questões (10% da prova);",
            "• Constitucional → 6 questões (7,5%);",
            "• Civil → 6 questões (7,5%);",
            "• Processo Civil → 6 questões (7,5%);",
            "• Penal → 6 questões (7,5%);",
            "• Processo Penal → 6 questões (7,5%);",
            "• Trabalho → 5 questões (6,25%);",
            "• Processo do Trabalho → 5 questões (6,25%);",
            "• Administrativo → 5 questões (6,25%);",
            "• Tributário → 5 questões (6,25%)."
        ],
        "emphasis": "Representam aproximadamente 72,5% da prova."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "Por onde começar?",
        "subtitle": "Estratégia de resolução",
        "bullets": ["Faça a prova na ordem", "Resolva primeiro o que você sabe", "Pule questões difíceis", "Volte depois nas dúvidas"],
        "emphasis": "A primeira volta serve para garantir pontos."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "E o que fazer com as questões difíceis?",
        "subtitle": "Técnica de eliminação",
        "bullets": ["Quando estiver em dúvida:", "elimine alternativas absurdas", "descarte opções incompatíveis com a lei", "reduza entre 2 alternativas"],
        "emphasis": "Eliminar alternativas aumenta suas chances de acerto."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "Terminou a questão 80? Agora sim você volta",
        "subtitle": "Revisão inteligente",
        "bullets": ["Volte apenas:", "nas questões em branco", "nas questões com dúvida"],
        "text": "Não revise questões já marcadas com segurança.<br>Não troque gabarito por nervosismo."
    },
    {
        "type": "content_alert",
        "label": "ESTRUTURA DA PROVA",
        "title": "Expressões problemáticas",
        "subtitle": "Palavras que merecem atenção",
        "bullets": ["⚠️ sempre", "⚠️ nunca", "⚠️ jamais", "⚠️ sem exceção", "⚠️ obrigatoriamente", "⚠️ exclusivamente", "⚠️ em nenhuma hipótese"],
        "emphasis": "Alternativas muito absolutas possuem maior chance de erro."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "Quanto tempo separar para o cartão-resposta?",
        "subtitle": "Administração do tempo",
        "text": "Reserve os últimos 40 minutos",
        "bullets": ["Ideal:", "finalizar a prova em até 4h20", "preencher o cartão apenas no final"],
        "emphasis": "Não fique passando respostas ao longo da prova."
    },
    {
        "type": "content",
        "label": "ESTRUTURA DA PROVA",
        "title": "Fazer pausas estratégicas durante a prova",
        "subtitle": "Controle emocional durante a prova",
        "bullets": ["Durante a prova:", "respire", "tome água", "desacelere alguns segundos", "reorganize o raciocínio"],
        "emphasis": "📌 Pequenas pausas ajudam a recuperar concentração."
    },
    {
        "type": "cover",
        "label": "Conclusão",
        "title": "OAB não é sorte.<br>OAB é estratégia.",
        "subtitle": "A aprovação depende de:<br>constância • treino • inteligência emocional • preparação estratégica<br><br>Você não precisa ser perfeito. Você precisa ser consistente.",
        "footer_items": ["Akeos + ESMAC", "Instagram: @akeos.oab", "WhatsApp: (91) 99373-0730"]
    }
]

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akeos | Aprovação Inteligente</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        akeos: {
                            purple: '#5B21B6',
                            dark: '#1E1B4B',
                            yellow: '#EAB308',
                            gray: '#F3F4F6',
                            text: '#1F2937',
                            muted: '#6B7280'
                        }
                    },
                    fontFamily: {
                        'head': ['Montserrat', 'sans-serif'],
                        'body': ['Poppins', 'sans-serif']
                    },
                    boxShadow: {
                        'premium': '0 10px 40px -10px rgba(91,33,182,0.1)',
                        'glow': '0 0 20px rgba(234, 179, 8, 0.4)'
                    }
                }
            }
        }
    </script>
    <style>
        body, html { margin: 0; padding: 0; overflow: hidden; background-color: #1E1B4B; }
        .slide-container {
            display: flex;
            width: 100vw;
            height: 100vh;
            transition: transform 0.6s cubic-bezier(0.65, 0, 0.35, 1);
        }
        .slide {
            min-width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            overflow: hidden;
            box-sizing: border-box;
        }
        .hero-pattern {
            background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 30px 30px;
        }
        .controls {
            position: fixed;
            bottom: 30px;
            right: 30px;
            display: flex;
            gap: 15px;
            z-index: 50;
        }
        .btn-control {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-control:hover { transform: scale(1.1); }
        .progress-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            height: 5px;
            background: #EAB308;
            transition: width 0.3s;
            z-index: 50;
        }
        .slide-number {
            position: fixed;
            bottom: 30px;
            left: 30px;
            color: rgba(255,255,255,0.5);
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            z-index: 50;
            font-weight: 500;
        }
        .slide.active .animate-up {
            animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .animate-up {
            opacity: 0;
            transform: translateY(40px);
        }
        .delay-100 { animation-delay: 0.1s; }
        .delay-200 { animation-delay: 0.2s; }
        .delay-300 { animation-delay: 0.3s; }
        .delay-400 { animation-delay: 0.4s; }
        @keyframes slideUpFade {
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="antialiased selection:bg-akeos-yellow selection:text-akeos-dark font-body text-akeos-text">
    <div class="progress-bar" id="progress"></div>
    <div class="slide-number" id="slideNum">1</div>
    <div class="controls">
        <button class="btn-control shadow-premium" id="prevBtn" onclick="prevSlide()">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <button class="btn-control shadow-premium" id="nextBtn" onclick="nextSlide()">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
        </button>
    </div>
    <div class="slide-container" id="slider">
{slides_html}
    </div>
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const slider = document.getElementById('slider');
        const progress = document.getElementById('progress');
        const slideNum = document.getElementById('slideNum');
        
        function updateSlide() {
            slider.style.transform = `translateX(-${currentSlide * 100}vw)`;
            progress.style.width = `${((currentSlide + 1) / slides.length) * 100}%`;
            slideNum.textContent = `${currentSlide + 1} / ${slides.length}`;
            
            const activeSlide = slides[currentSlide];
            const isDark = activeSlide.classList.contains('bg-akeos-dark') || activeSlide.classList.contains('bg-akeos-purple');
            
            if(isDark) {
                slideNum.style.color = 'rgba(255,255,255,0.5)';
                document.querySelectorAll('.btn-control').forEach(b => {
                    b.style.border = '1px solid rgba(255,255,255,0.2)';
                    b.style.color = 'white';
                    b.style.background = 'rgba(255,255,255,0.1)';
                });
            } else {
                slideNum.style.color = 'rgba(0,0,0,0.4)';
                document.querySelectorAll('.btn-control').forEach(b => {
                    b.style.border = '1px solid rgba(0,0,0,0.1)';
                    b.style.color = '#5B21B6';
                    b.style.background = 'white';
                });
            }
            slides.forEach((s, i) => {
                if(i === currentSlide) s.classList.add('active');
                else s.classList.remove('active');
            });
        }
        function nextSlide() { if (currentSlide < slides.length - 1) { currentSlide++; updateSlide(); } }
        function prevSlide() { if (currentSlide > 0) { currentSlide--; updateSlide(); } }
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'Enter') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
        updateSlide();
    </script>
</body>
</html>"""

slides_html = ""

for slide in slides_data:
    if slide['type'] == 'cover':
        footers = ""
        for f in slide.get('footer_items', []):
            footers += f'<div class="flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10">{f}</div>\n'
        
        slides_html += f"""
        <div class="slide bg-akeos-dark text-white p-12 lg:p-24">
            <div class="absolute inset-0 bg-gradient-to-br from-akeos-dark via-akeos-purple to-[#4C1D95]"></div>
            <div class="absolute inset-0 hero-pattern opacity-30"></div>
            <img src="./logo-akeos.webp" class="absolute top-12 left-12 h-10 object-contain filter brightness-0 invert opacity-90 z-20">
            <div class="relative z-10 max-w-5xl animate-up">
                <span class="uppercase tracking-widest text-akeos-yellow font-bold text-sm mb-4 block">{slide['label']}</span>
                <h1 class="text-6xl lg:text-8xl font-head font-bold leading-tight mb-6 tracking-tight">{slide['title']}</h1>
                <p class="text-2xl text-purple-100 font-body leading-relaxed max-w-4xl mb-12 font-light delay-100 animate-up">
                    {slide['subtitle']}
                </p>
                <div class="flex flex-wrap gap-4 delay-200 animate-up text-sm font-medium">
                    {footers}
                </div>
            </div>
        </div>
        """
    elif slide['type'] == 'section':
        slides_html += f"""
        <div class="slide bg-akeos-purple text-white p-12 lg:p-24 text-center">
            <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')] opacity-50"></div>
            <img src="./logo-akeos.webp" class="absolute top-12 left-12 h-8 object-contain filter brightness-0 invert opacity-60 z-20">
            <div class="relative z-10 flex flex-col items-center justify-center h-full animate-up">
                <span class="px-5 py-2 bg-akeos-yellow text-akeos-dark font-bold rounded-full text-sm tracking-widest uppercase mb-8 shadow-glow">{slide['label']}</span>
                <h1 class="text-6xl lg:text-8xl font-head font-bold mb-6 tracking-tight">{slide['title']}</h1>
                <p class="text-2xl text-purple-200 font-body font-light delay-100 animate-up">{slide['subtitle']}</p>
            </div>
        </div>
        """
    elif slide['type'] == 'cards':
        cards_html = ""
        for c in slide.get('cards', []):
            cards_html += f"""
            <div class="p-8 border border-gray-100 rounded-2xl bg-white shadow-sm hover:shadow-premium transition-all group">
                <span class="text-xs font-bold text-akeos-purple bg-purple-50 px-3 py-1 rounded uppercase tracking-wider">{c['label']}</span>
                <h4 class="font-head font-bold text-2xl mt-5 text-akeos-dark group-hover:text-akeos-purple transition-colors">{c['text']}</h4>
            </div>
            """
        slides_html += f"""
        <div class="slide bg-gray-50 text-akeos-text p-12 lg:p-24">
            <img src="./logo-akeos.webp" class="absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20">
            <div class="relative z-10 max-w-6xl mx-auto w-full">
                <span class="uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up">{slide['label']}</span>
                <h2 class="text-4xl lg:text-5xl font-head font-bold mb-16 text-akeos-dark animate-up delay-100">{slide['title']}</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 animate-up delay-200">
                    {cards_html}
                </div>
                <div class="flex items-center gap-4 bg-akeos-dark text-white p-6 rounded-xl animate-up delay-300 w-max shadow-glow">
                    <div class="text-akeos-yellow text-2xl">⚡</div>
                    <p class="font-head font-semibold text-lg">{slide.get('footer_emphasis', '')}</p>
                </div>
            </div>
        </div>
        """
    elif slide['type'] in ['content', 'content_red', 'content_alert']:
        bullets_html = ""
        icon = "✓"
        icon_bg = "bg-purple-100"
        icon_color = "text-akeos-purple"
        if slide['type'] == 'content_red':
            icon = "✕"
            icon_bg = "bg-red-100"
            icon_color = "text-red-600"
        if slide['type'] == 'content_alert':
            icon = "!"
            icon_bg = "bg-yellow-100"
            icon_color = "text-yellow-600"

        for b in slide.get('bullets', []):
            bullets_html += f'''
            <div class="flex items-start gap-4">
                <div class="w-8 h-8 rounded-full {icon_bg} {icon_color} flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm">{icon}</div>
                <p class="text-xl font-body text-akeos-text">{b}</p>
            </div>
            '''
            
        subtitle_html = f'<p class="text-2xl text-akeos-muted font-body mb-10 animate-up delay-100">{slide["subtitle"]}</p>' if slide.get("subtitle") else ''
        text_html = f'<p class="text-xl text-akeos-text font-body mb-8 animate-up delay-100">{slide["text"]}</p>' if slide.get("text") else ''
        
        emphasis_html = ""
        if slide.get('emphasis'):
            emphasis_html = f'''
            <div class="bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12">
                <p class="text-2xl font-head font-semibold">{slide['emphasis']}</p>
            </div>
            '''
            
        slides_html += f"""
        <div class="slide bg-white text-akeos-text p-12 lg:p-24">
            <img src="./logo-akeos.webp" class="absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20">
            <div class="relative z-10 max-w-5xl mx-auto w-full">
                <span class="uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up">{slide['label']}</span>
                <h2 class="text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100">{slide['title']}</h2>
                {subtitle_html}
                {text_html}
                <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200">
                    {bullets_html}
                </div>
                {emphasis_html}
            </div>
        </div>
        """
    elif slide['type'] == 'list_cols':
        bullets_html = ""
        for b in slide.get('bullets', []):
            bullets_html += f'<li class="text-lg font-body text-akeos-muted mb-2">{b}</li>'
            
        slides_html += f"""
        <div class="slide bg-white text-akeos-text p-12 lg:p-24">
            <img src="./logo-akeos.webp" class="absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20">
            <div class="relative z-10 max-w-5xl mx-auto w-full">
                <span class="uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up">{slide['label']}</span>
                <h2 class="text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100">{slide['title']}</h2>
                <p class="text-2xl text-akeos-muted font-body mb-8 animate-up delay-100">{slide['subtitle']}</p>
                <p class="text-xl font-bold font-body mb-4 animate-up delay-200">{slide['text']}</p>
                <ul class="columns-1 md:columns-2 gap-8 animate-up delay-200 list-none">
                    {bullets_html}
                </ul>
                <div class="bg-akeos-yellow text-akeos-dark p-6 rounded-xl shadow-glow animate-up delay-300 max-w-4xl mt-12 inline-block">
                    <p class="text-xl font-head font-bold">{slide['emphasis']}</p>
                </div>
            </div>
        </div>
        """

final_html = html_template.replace('{slides_html}', slides_html)

with open('generator.py', 'w', encoding='utf-8') as f:
    f.write(f'''
import codecs
content = """{final_html.replace('"', '\\"')}"""
with codecs.open('apresentacao_akeos.html', 'w', 'utf-8') as f_out:
    f_out.write(content)
''')
