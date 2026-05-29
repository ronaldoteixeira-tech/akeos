
import codecs
content = """<!DOCTYPE html>
<html lang=\"pt-BR\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Akeos | Aprovação Inteligente</title>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap\" rel=\"stylesheet\">
    <script src=\"https://cdn.tailwindcss.com\"></script>
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
<body class=\"antialiased selection:bg-akeos-yellow selection:text-akeos-dark font-body text-akeos-text\">
    <div class=\"progress-bar\" id=\"progress\"></div>
    <div class=\"slide-number\" id=\"slideNum\">1</div>
    <div class=\"controls\">
        <button class=\"btn-control shadow-premium\" id=\"prevBtn\" onclick=\"prevSlide()\">
            <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M15 18l-6-6 6-6\"/></svg>
        </button>
        <button class=\"btn-control shadow-premium\" id=\"nextBtn\" onclick=\"nextSlide()\">
            <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M9 18l6-6-6-6\"/></svg>
        </button>
    </div>
    <div class=\"slide-container\" id=\"slider\">

        <div class=\"slide bg-akeos-dark text-white p-12 lg:p-24\">
            <div class=\"absolute inset-0 bg-gradient-to-br from-akeos-dark via-akeos-purple to-[#4C1D95]\"></div>
            <div class=\"absolute inset-0 hero-pattern opacity-30\"></div>
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-10 object-contain filter brightness-0 invert opacity-90 z-20\">
            <div class=\"relative z-10 max-w-5xl animate-up\">
                <span class=\"uppercase tracking-widest text-akeos-yellow font-bold text-sm mb-4 block\">Capa</span>
                <h1 class=\"text-6xl lg:text-8xl font-head font-bold leading-tight mb-6 tracking-tight\">Aprovação<br><span class='text-transparent bg-clip-text bg-gradient-to-r from-akeos-yellow to-yellow-200'>Inteligente</span></h1>
                <p class=\"text-2xl text-purple-100 font-body leading-relaxed max-w-4xl mb-12 font-light delay-100 animate-up\">
                    Estratégias Jurídicas, Gestão Emocional e Alta Performance para a OAB
                </p>
                <div class=\"flex flex-wrap gap-4 delay-200 animate-up text-sm font-medium\">
                    <div class=\"flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10\">📍 Oficina ESMAC + Akeos</div>
<div class=\"flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10\">📍 Lara Ferreira dos Santos</div>

                </div>
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Introdução</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">A grande virada de chave</h2>
                
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">A OAB não é uma competição</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Você não precisa acertar tudo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Você precisa atingir a pontuação mínima</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Estudar estrategicamente é mais importante do que estudar exaustivamente.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-gray-50 text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-6xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">O que veremos hoje</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-16 text-akeos-dark animate-up delay-100\">3 PILARES DA APROVAÇÃO</h2>
                <div class=\"grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 animate-up delay-200\">
                    
            <div class=\"p-8 border border-gray-100 rounded-2xl bg-white shadow-sm hover:shadow-premium transition-all group\">
                <span class=\"text-xs font-bold text-akeos-purple bg-purple-50 px-3 py-1 rounded uppercase tracking-wider\">Pilar 1</span>
                <h4 class=\"font-head font-bold text-2xl mt-5 text-akeos-dark group-hover:text-akeos-purple transition-colors\">Rotina ajustada</h4>
            </div>
            
            <div class=\"p-8 border border-gray-100 rounded-2xl bg-white shadow-sm hover:shadow-premium transition-all group\">
                <span class=\"text-xs font-bold text-akeos-purple bg-purple-50 px-3 py-1 rounded uppercase tracking-wider\">Pilar 2</span>
                <h4 class=\"font-head font-bold text-2xl mt-5 text-akeos-dark group-hover:text-akeos-purple transition-colors\">Domínio do conteúdo</h4>
            </div>
            
            <div class=\"p-8 border border-gray-100 rounded-2xl bg-white shadow-sm hover:shadow-premium transition-all group\">
                <span class=\"text-xs font-bold text-akeos-purple bg-purple-50 px-3 py-1 rounded uppercase tracking-wider\">Pilar 3</span>
                <h4 class=\"font-head font-bold text-2xl mt-5 text-akeos-dark group-hover:text-akeos-purple transition-colors\">Mentalidade e inteligência emocional</h4>
            </div>
            
                </div>
                <div class=\"flex items-center gap-4 bg-akeos-dark text-white p-6 rounded-xl animate-up delay-300 w-max shadow-glow\">
                    <div class=\"text-akeos-yellow text-2xl\">⚡</div>
                    <p class=\"font-head font-semibold text-lg\">Estratégias para o dia da prova</p>
                </div>
            </div>
        </div>
        
        <div class=\"slide bg-akeos-purple text-white p-12 lg:p-24 text-center\">
            <div class=\"absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')] opacity-50\"></div>
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain filter brightness-0 invert opacity-60 z-20\">
            <div class=\"relative z-10 flex flex-col items-center justify-center h-full animate-up\">
                <span class=\"px-5 py-2 bg-akeos-yellow text-akeos-dark font-bold rounded-full text-sm tracking-widest uppercase mb-8 shadow-glow\">Pilar 1</span>
                <h1 class=\"text-6xl lg:text-8xl font-head font-bold mb-6 tracking-tight\">ROTINA AJUSTADA</h1>
                <p class=\"text-2xl text-purple-200 font-body font-light delay-100 animate-up\">Aprovação exige organização sustentável.</p>
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 1</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Estratégia sem individualidade não funciona</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Cada aluno possui uma realidade</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">trabalho</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">estágio</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">filhos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">faculdade</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">pouco tempo disponível</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">O melhor cronograma é o que funciona para sua rotina.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 1</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Metas reais</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Constância > intensidade exagerada</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-red-100 text-red-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✕</div>
                <p class=\"text-xl font-body text-akeos-text\">Estudar 12h sem conseguir manter</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-red-100 text-red-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✕</div>
                <p class=\"text-xl font-body text-akeos-text\">Estudar todas as matérias ao mesmo tempo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-red-100 text-red-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✕</div>
                <p class=\"text-xl font-body text-akeos-text\">Criar metas impossíveis</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">O melhor plano é aquele que você consegue cumprir.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 1</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Flexibilidade inteligente</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Disciplina não é rigidez</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Imprevistos acontecem:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">cansaço</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">ansiedade</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">problemas pessoais</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">desgaste mental</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Um dia ruim não pode virar abandono da preparação.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-akeos-purple text-white p-12 lg:p-24 text-center\">
            <div class=\"absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')] opacity-50\"></div>
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain filter brightness-0 invert opacity-60 z-20\">
            <div class=\"relative z-10 flex flex-col items-center justify-center h-full animate-up\">
                <span class=\"px-5 py-2 bg-akeos-yellow text-akeos-dark font-bold rounded-full text-sm tracking-widest uppercase mb-8 shadow-glow\">Pilar 2</span>
                <h1 class=\"text-6xl lg:text-8xl font-head font-bold mb-6 tracking-tight\">DOMÍNIO DO CONTEÚDO</h1>
                <p class=\"text-2xl text-purple-200 font-body font-light delay-100 animate-up\">A OAB cobra interpretação e aplicação prática.</p>
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">O foco maior deve estar na lei seca</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">A banca cobra muito texto de lei</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">A banca explora:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">prazos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">exceções</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">competências</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">detalhes legais</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Não basta assistir aula.<br>É preciso ler legislação.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Saber aplicar o conteúdo ao caso concreto</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">A prova quer raciocínio jurídico</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">A OAB cobra:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">interpretação</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">identificação de institutos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">aplicação da lei</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">resolução prática</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Não basta decorar conceitos.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Questões são treinamento</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Resolver questões acelera aprovação</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Questões ajudam a:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">identificar padrões da banca</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">melhorar interpretação</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">fixar conteúdo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">descobrir pontos fracos</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Questão também é método de aprendizagem.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Estudar o que é relevante</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Estudo estratégico</p>
                <p class=\"text-xl text-akeos-text font-body mb-8 animate-up delay-100\">Nem todas as matérias possuem o mesmo peso.</p>
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Priorize:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">assuntos mais cobrados</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">temas mais recorrentes</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">conteúdos de maior incidência</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">A OAB exige pontuação mínima, não perfeição.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Sair da zona de conforto</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Crescimento acontece no desconforto</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">A aprovação exige enfrentar:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">matérias difíceis</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">assuntos cansativos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">conteúdos que geram insegurança</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Evoluir exige enfrentar dificuldades.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 2</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Simulados são indispensáveis</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">O simulado aproxima você da prova real</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Treine:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">tempo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">resistência mental</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">emocional</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">ansiedade</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">estratégia</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Treinar comportamento também é preparação.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-akeos-purple text-white p-12 lg:p-24 text-center\">
            <div class=\"absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNSkiLz48L3N2Zz4=')] opacity-50\"></div>
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain filter brightness-0 invert opacity-60 z-20\">
            <div class=\"relative z-10 flex flex-col items-center justify-center h-full animate-up\">
                <span class=\"px-5 py-2 bg-akeos-yellow text-akeos-dark font-bold rounded-full text-sm tracking-widest uppercase mb-8 shadow-glow\">Pilar 3</span>
                <h1 class=\"text-6xl lg:text-8xl font-head font-bold mb-6 tracking-tight\">MENTALIDADE E INTELIGÊNCIA EMOCIONAL</h1>
                <p class=\"text-2xl text-purple-200 font-body font-light delay-100 animate-up\">Aprovação também é emocional.</p>
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 3</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Aprovação também é emocional</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">A preparação mexe com o psicológico</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Em alguns momentos você vai:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">duvidar de si</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">sentir medo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">achar que não está evoluindo</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">comparar sua evolução com a dos outros</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Inteligência emocional também é preparação.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 3</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Autoconfiança construída através da evolução real</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Confiança vem da evolução</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Acompanhe:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">percentual de acertos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">desempenho por matéria</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">simulados</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">evolução nos resultados</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Quem monitora resultados estuda com estratégia.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">Pilar 3</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Pare de se comparar</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Cada aluno possui uma trajetória diferente</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">rotina diferente</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">dificuldades diferentes</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">base diferente</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">tempo diferente de evolução</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Compare-se apenas com sua versão anterior.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Como funciona a 1ª fase?</h2>
                
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">80 questões</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">múltipla escolha</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">5 horas de duração</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">📌 Estratégia de execução importa.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Questões e disciplinas</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-8 animate-up delay-100\">Onde estão a maioria das questões?</p>
                <p class=\"text-xl font-bold font-body mb-4 animate-up delay-200\">As disciplinas:</p>
                <ul class=\"columns-1 md:columns-2 gap-8 animate-up delay-200 list-none\">
                    <li class=\"text-lg font-body text-akeos-muted mb-2\">• Ética → 8 questões (10% da prova);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Constitucional → 6 questões (7,5%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Civil → 6 questões (7,5%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Processo Civil → 6 questões (7,5%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Penal → 6 questões (7,5%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Processo Penal → 6 questões (7,5%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Trabalho → 5 questões (6,25%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Processo do Trabalho → 5 questões (6,25%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Administrativo → 5 questões (6,25%);</li><li class=\"text-lg font-body text-akeos-muted mb-2\">• Tributário → 5 questões (6,25%).</li>
                </ul>
                <div class=\"bg-akeos-yellow text-akeos-dark p-6 rounded-xl shadow-glow animate-up delay-300 max-w-4xl mt-12 inline-block\">
                    <p class=\"text-xl font-head font-bold\">Representam aproximadamente 72,5% da prova.</p>
                </div>
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Por onde começar?</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Estratégia de resolução</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Faça a prova na ordem</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Resolva primeiro o que você sabe</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Pule questões difíceis</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Volte depois nas dúvidas</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">A primeira volta serve para garantir pontos.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">E o que fazer com as questões difíceis?</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Técnica de eliminação</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Quando estiver em dúvida:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">elimine alternativas absurdas</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">descarte opções incompatíveis com a lei</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">reduza entre 2 alternativas</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Eliminar alternativas aumenta suas chances de acerto.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Terminou a questão 80? Agora sim você volta</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Revisão inteligente</p>
                <p class=\"text-xl text-akeos-text font-body mb-8 animate-up delay-100\">Não revise questões já marcadas com segurança.<br>Não troque gabarito por nervosismo.</p>
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Volte apenas:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">nas questões em branco</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">nas questões com dúvida</p>
            </div>
            
                </div>
                
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Expressões problemáticas</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Palavras que merecem atenção</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ sempre</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ nunca</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ jamais</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ sem exceção</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ obrigatoriamente</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ exclusivamente</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-yellow-100 text-yellow-600 flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">!</div>
                <p class=\"text-xl font-body text-akeos-text\">⚠️ em nenhuma hipótese</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Alternativas muito absolutas possuem maior chance de erro.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Quanto tempo separar para o cartão-resposta?</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Administração do tempo</p>
                <p class=\"text-xl text-akeos-text font-body mb-8 animate-up delay-100\">Reserve os últimos 40 minutos</p>
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Ideal:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">finalizar a prova em até 4h20</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">preencher o cartão apenas no final</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">Não fique passando respostas ao longo da prova.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-white text-akeos-text p-12 lg:p-24\">
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-8 object-contain mix-blend-multiply opacity-60 z-20\">
            <div class=\"relative z-10 max-w-5xl mx-auto w-full\">
                <span class=\"uppercase tracking-widest text-akeos-purple font-bold text-xs mb-4 block animate-up\">ESTRUTURA DA PROVA</span>
                <h2 class=\"text-4xl lg:text-5xl font-head font-bold mb-4 text-akeos-dark animate-up delay-100\">Fazer pausas estratégicas durante a prova</h2>
                <p class=\"text-2xl text-akeos-muted font-body mb-10 animate-up delay-100\">Controle emocional durante a prova</p>
                
                <div class=\"grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-6 animate-up delay-200\">
                    
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">Durante a prova:</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">respire</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">tome água</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">desacelere alguns segundos</p>
            </div>
            
            <div class=\"flex items-start gap-4\">
                <div class=\"w-8 h-8 rounded-full bg-purple-100 text-akeos-purple flex items-center justify-center font-bold shrink-0 mt-0.5 text-sm\">✓</div>
                <p class=\"text-xl font-body text-akeos-text\">reorganize o raciocínio</p>
            </div>
            
                </div>
                
            <div class=\"bg-akeos-purple text-white p-8 rounded-2xl shadow-premium animate-up delay-300 max-w-4xl border-l-4 border-akeos-yellow mt-12\">
                <p class=\"text-2xl font-head font-semibold\">📌 Pequenas pausas ajudam a recuperar concentração.</p>
            </div>
            
            </div>
        </div>
        
        <div class=\"slide bg-akeos-dark text-white p-12 lg:p-24\">
            <div class=\"absolute inset-0 bg-gradient-to-br from-akeos-dark via-akeos-purple to-[#4C1D95]\"></div>
            <div class=\"absolute inset-0 hero-pattern opacity-30\"></div>
            <img src=\"./logo-akeos.webp\" class=\"absolute top-12 left-12 h-10 object-contain filter brightness-0 invert opacity-90 z-20\">
            <div class=\"relative z-10 max-w-5xl animate-up\">
                <span class=\"uppercase tracking-widest text-akeos-yellow font-bold text-sm mb-4 block\">Conclusão</span>
                <h1 class=\"text-6xl lg:text-8xl font-head font-bold leading-tight mb-6 tracking-tight\">OAB não é sorte.<br>OAB é estratégia.</h1>
                <p class=\"text-2xl text-purple-100 font-body leading-relaxed max-w-4xl mb-12 font-light delay-100 animate-up\">
                    A aprovação depende de:<br>constância • treino • inteligência emocional • preparação estratégica<br><br>Você não precisa ser perfeito. Você precisa ser consistente.
                </p>
                <div class=\"flex flex-wrap gap-4 delay-200 animate-up text-sm font-medium\">
                    <div class=\"flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10\">Akeos + ESMAC</div>
<div class=\"flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10\">Instagram: @akeos.oab</div>
<div class=\"flex items-center gap-2 bg-white/10 px-5 py-3 rounded-lg backdrop-blur border border-white/10\">WhatsApp: (91) 99373-0730</div>

                </div>
            </div>
        </div>
        
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
with codecs.open('apresentacao_akeos.html', 'w', 'utf-8') as f_out:
    f_out.write(content)
