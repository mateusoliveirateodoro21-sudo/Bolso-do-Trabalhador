import os, sys, zipfile
SITE = sys.argv[1] if len(sys.argv) > 1 else "https://SEUDOMINIO.com.br"
EMAIL = sys.argv[2] if len(sys.argv) > 2 else "contato@SEUDOMINIO.com.br"
NAME = "Bolso do Trabalhador"
OUT = "site"
os.makedirs(OUT, exist_ok=True)

CSS = """:root{--bg:#fff;--sf:#fff;--ink:#111;--mut:#4d4d4d;--ln:#e2e2e2;--nt:#111;--sun:#ffd400;--fc:#111}
@media(prefers-color-scheme:dark){:root{--bg:#111;--sf:#1c1c1c;--ink:#fff;--mut:#b8b8b8;--ln:#333;--nt:#000;--fc:#ffd400}}
*{box-sizing:border-box}html{padding-top:env(safe-area-inset-top,0)}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 "Bricolage Grotesque",system-ui,-apple-system,"Segoe UI",sans-serif;padding-bottom:env(safe-area-inset-bottom,0)}
.w{max-width:960px;margin:0 auto;padding:0 20px}
header{display:flex;justify-content:space-between;align-items:center;padding:16px 0}
.logo{font-weight:800;font-size:22px;color:var(--ink);text-decoration:none;display:flex;gap:10px;align-items:center}
.logo i{width:24px;height:24px;border-radius:50%;background:linear-gradient(90deg,var(--sun) 50%,#111 50%);border:2px solid var(--ink)}
nav{display:flex;gap:18px;font-size:15px}nav a,footer a,.t a{color:var(--mut)}nav a:hover{color:var(--ink)}
h1{font-size:clamp(1.9rem,5vw,3rem);line-height:1.08;letter-spacing:-.03em;margin:12px 0 14px;font-weight:800}
h2{font-size:1.3rem;margin:28px 0 8px}.lead{color:var(--mut);max-width:60ch}
.g{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:start;padding:12px 0 24px}
.calc{background:var(--sf);border:1.5px solid var(--ink);border-radius:16px;padding:20px;box-shadow:6px 6px 0 var(--sun)}
label{display:block;font-size:14px;color:var(--mut);margin:12px 0 4px}
input,select{width:100%;font:inherit;padding:10px 12px;border:1.5px solid var(--ln);border-radius:10px;background:var(--bg);color:var(--ink)}
:focus-visible{outline:3px solid var(--fc);outline-offset:2px}
dl{display:grid;grid-template-columns:1fr auto;gap:6px 12px;margin:16px 0 0;border-top:1.5px dashed var(--ln);padding-top:14px;font-size:15px}
dt{color:var(--mut)}dd{margin:0;text-align:right;font-variant-numeric:tabular-nums}
.total{display:flex;justify-content:space-between;align-items:baseline;margin-top:12px;padding:12px 14px;background:var(--nt);color:#fff;border-radius:12px}
.total strong{font-size:1.6rem;color:var(--sun)}
.note{font-size:13px;color:var(--mut);margin:12px 0 0}
.ad{margin:8px 0 28px;min-height:90px;border:1.5px dashed var(--ln);border-radius:12px;display:grid;place-items:center;color:var(--mut);font-size:13px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0 32px}
.cards a{display:block;padding:18px;background:var(--sf);border:1.5px solid var(--ln);border-radius:14px;color:var(--ink);text-decoration:none}
.cards a:hover{border-color:var(--ink)}.cards b{display:block}.cards span{color:var(--mut);font-size:15px}
.t{max-width:68ch}.t p{margin:0 0 12px}
footer{border-top:1.5px solid var(--ln);margin-top:36px;padding:20px 0 30px;font-size:14px;color:var(--mut)}
@media(max-width:760px){.g,.cards{grid-template-columns:1fr}nav{display:none}}
"""

JS = """(function(){
var F=new Intl.NumberFormat("pt-BR",{style:"currency",currency:"BRL"});
function v(i){return parseFloat(document.getElementById(i).value)||0}
var C={
noturno:function(){var h=v("sal")/v("div"),n=h*v("pct")/100*v("hn"),e=h*1.5*v("he");return{hora:h,not:n,he:e,tot:n+e}},
escala:function(){var h=v("sal")/v("div"),n=h*v("pct")/100*v("hn")*v("pl"),e=h*1.5*v("he");return{hm:v("pl")*12,hora:h,not:n,he:e,tot:n+e}},
hora:function(){var h=v("sal")/v("div");return{h50:h*1.5,h100:h*2,hora:h}},
ferias:function(){var b=v("sal")+v("med"),f=b/30*v("dias"),t=f/3,a=v("dias")==20?b/30*10*4/3:0;return{base:b,fer:f,terco:t,abono:a,tot:f+t+a}},
servidor:function(){var h=v("base")/v("div"),k=v("red")==1?60/52.5:1,pe=v("pe")/100,pn=v("pn")/100,a=h*(1+pe)*v("hed"),b=h*pn*v("hn")*k,c=h*(1+pe)*(1+pn)*v("hen")*k;return{hora:h,hed:a,adn:b,hen:c,tot:a+b+c}}
};
var k=document.body.getAttribute("data-calc");if(!k)return;
function run(){var r=C[k]();Object.keys(r).forEach(function(i){var e=document.getElementById("o-"+i);
e.textContent=e.getAttribute("data-f")=="h"?r[i].toLocaleString("pt-BR",{maximumFractionDigits:1})+" h":F.format(r[i])})}
Array.prototype.forEach.call(document.querySelectorAll("input,select"),function(e){e.addEventListener("input",run)});run();
})();
"""

LAYOUT = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
<link rel="canonical" href="@@SITE@@/@@FILE@@">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,800&display=swap">
<link rel="stylesheet" href="style.css">
<!-- AdSense: cole aqui o script da conta depois da aprovação -->
</head>
<body@@ATTR@@>
<div class="w">
<header><a class="logo" href="index.html"><i></i>@@NAME@@</a>
<nav aria-label="Principal"><a href="index.html#calculadoras">Calculadoras</a><a href="sobre.html">Sobre</a><a href="contato.html">Contato</a></nav></header>
<main>@@BODY@@</main>
<footer><p>@@NAME@@ é um projeto independente. Os cálculos são estimativas e não substituem o RH, o sindicato ou um advogado.</p>
<p><a href="privacidade.html">Política de privacidade</a> · <a href="contato.html">Contato</a> · <a href="sobre.html">Sobre</a></p></footer>
</div>
@@SCRIPT@@
</body>
</html>
"""

CALCS = {
"adicional-noturno.html": dict(key="noturno", title="Calculadora de adicional noturno e hora extra",
 desc="Calcule o adicional noturno e as horas extras do mês a partir do salário. Grátis, com a conta explicada.",
 fields=[("sal", "Salário mensal (R$)", "n", 2200), ("div", "Divisor da hora", [(220, "220 horas"), (180, "180 horas")], 220),
  ("pct", "Adicional noturno (%)", [(20, "20%"), (30, "30%"), (40, "40%")], 20), ("hn", "Horas noturnas no mês", "n", 105), ("he", "Horas extras no mês", "n", 4)],
 outs=[("hora", "Valor da hora", "r"), ("not", "Adicional noturno", "r"), ("he", "Horas extras (50%)", "r"), ("tot", "Total a mais no mês", "r")],
 text="<h2>Como a conta é feita</h2><p>Valor da hora = salário ÷ divisor. Adicional noturno = valor da hora × percentual × horas noturnas. Hora extra = valor da hora × 1,5 × horas extras.</p><p>O trabalho noturno urbano vai das 22h às 5h, e o adicional mínimo é de 20%. Algumas convenções coletivas pagam mais, então confira a sua.</p><p>Esta calculadora não aplica a hora noturna reduzida (52 min 30 s) nem os reflexos em férias e 13º. O resultado é bruto, antes de INSS e IR.</p>"),
"escala-12x36.html": dict(key="escala", title="Calculadora da escala 12x36",
 desc="Veja as horas do mês, o valor da hora e o adicional noturno na escala 12x36. Grátis e com a conta explicada.",
 fields=[("sal", "Salário mensal (R$)", "n", 2200), ("div", "Divisor da hora", [(220, "220 horas"), (180, "180 horas")], 220),
  ("pl", "Plantões no mês", "n", 15), ("hn", "Horas noturnas por plantão", "n", 5), ("pct", "Adicional noturno (%)", [(20, "20%"), (30, "30%"), (40, "40%")], 20), ("he", "Horas extras no mês", "n", 0)],
 outs=[("hm", "Horas trabalhadas no mês", "h"), ("hora", "Valor da hora", "r"), ("not", "Adicional noturno", "r"), ("he", "Horas extras (50%)", "r"), ("tot", "Total a mais no mês", "r")],
 text="<h2>Como funciona a 12x36</h2><p>São 12 horas de plantão e 36 de descanso. Dentro das 12 horas não existe hora extra: ela só começa se você passar do fim do turno ou se o intervalo de refeição não for concedido.</p><p>A remuneração mensal já cobre os descansos semanais e os feriados trabalhados. O adicional noturno continua devido sobre as horas entre 22h e 5h.</p><p>Muitas convenções usam divisor 220, outras 180. Veja o que vale na sua categoria. Esta calculadora não aplica a hora noturna reduzida.</p>"),
"valor-da-hora.html": dict(key="hora", title="Calculadora do valor da hora de trabalho",
 desc="Descubra quanto vale a sua hora de trabalho e o valor da hora extra de 50% e de 100%.",
 fields=[("sal", "Salário mensal (R$)", "n", 2200), ("div", "Divisor da hora", [(220, "220 horas"), (200, "200 horas"), (180, "180 horas"), (150, "150 horas")], 220)],
 outs=[("h50", "Hora extra a 50%", "r"), ("h100", "Hora extra a 100%", "r"), ("hora", "Valor da hora normal", "r")],
 text="<h2>De onde vem o divisor</h2><p>O divisor de 220 horas corresponde a uma jornada de 44 horas por semana. Quem trabalha 40 horas semanais costuma usar 200, e o divisor de 180 aparece em escalas como a 12x36 de algumas convenções.</p><p>O valor da hora é a base de tudo: adicional noturno, hora extra e reflexos. Use o divisor que está no seu contrato ou na convenção da categoria.</p>"),
"servidor-publico.html": dict(key="servidor", title="Calculadora de hora extra e adicional noturno do servidor público",
 desc="Calcule hora extra e adicional noturno de servidor público com percentuais editáveis, no modelo da Lei 8.112/90.",
 fields=[("base", "Remuneração-base de cálculo (R$)", "n", 3000), ("div", "Divisor da hora (horas por mês)", "n", 200),
  ("pe", "Adicional de hora extra (%)", "n", 50), ("pn", "Adicional noturno (%)", "n", 25),
  ("hed", "Horas extras diurnas no mês", "n", 6), ("hn", "Horas noturnas da jornada normal (relógio)", "n", 0),
  ("hen", "Horas extras noturnas (relógio)", "n", 0), ("red", "Hora noturna reduzida (52 min 30 s)", [(1, "Aplicar"), (0, "Não aplicar")], 1)],
 outs=[("hora", "Valor da hora normal", "r"), ("hed", "Horas extras diurnas", "r"), ("adn", "Adicional noturno (jornada normal)", "r"), ("hen", "Horas extras noturnas", "r"), ("tot", "Total a mais no mês", "r")],
 text="<h2>Como o modelo federal funciona</h2><p>Para servidores civis da União, a Lei 8.112/90 prevê hora extra com acréscimo de 50%, limitada a 2 horas por jornada e só em situações excepcionais e temporárias. O serviço noturno, das 22h às 5h, recebe 25% a mais, e cada hora vale 52 minutos e 30 segundos.</p><p>Quando a hora extra é noturna, os dois acréscimos se acumulam: o 25% incide sobre a hora já acrescida de 50%. A calculadora faz essa conta.</p><p>Estados e municípios têm estatuto próprio, e os percentuais, o divisor e as regras de hora reduzida podem ser diferentes. Por isso os percentuais e o divisor são campos editáveis. Use os valores da lei do seu ente e o divisor informado pelo RH do seu órgão.</p><p>Em regra, ocupantes de cargo em comissão ou função de confiança não recebem esses adicionais. O resultado é bruto, antes dos descontos de previdência e imposto de renda.</p>"),
"ferias-com-horas-extras.html": dict(key="ferias", title="Calculadora de férias com média de horas extras",
 desc="Calcule as férias com o terço constitucional, a venda de 10 dias e a média das horas extras.",
 fields=[("sal", "Salário mensal (R$)", "n", 2200), ("med", "Média mensal de horas extras (R$)", "n", 300), ("dias", "Como tirar as férias", [(30, "30 dias de descanso"), (20, "20 dias + vender 10")], 30)],
 outs=[("base", "Base de cálculo", "r"), ("fer", "Férias", "r"), ("terco", "Um terço constitucional", "r"), ("abono", "Abono (venda de 10 dias)", "r"), ("tot", "Total bruto", "r")],
 text="<h2>O que entra na conta</h2><p>As horas extras habituais entram na base das férias pela média. A base é o salário mais essa média. As férias valem a base ÷ 30 × os dias, mais um terço.</p><p>Ao vender 10 dias, o abono também recebe o terço. O resultado é bruto, antes dos descontos de INSS e IR. Confirme a média com o seu RH.</p>"),
}

def write(name, content):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(content)

def page(file, title, desc, body, attr="", script=""):
    h = LAYOUT
    for k, v in {"@@TITLE@@": title + " | " + NAME, "@@DESC@@": desc, "@@SITE@@": SITE, "@@FILE@@": file, "@@NAME@@": NAME,
                 "@@BODY@@": body, "@@ATTR@@": attr, "@@SCRIPT@@": script}.items():
        h = h.replace(k, v)
    write(file, h)

AD = '<div class="ad" role="complementary" aria-label="Espaço publicitário"><!-- AdSense: bloco de anúncio --></div>'
urls = ["index.html"]
for f, p in CALCS.items():
    fs = ""
    for fid, lab, kind, d in p["fields"]:
        if kind == "n":
            inp = '<input id="%s" type="number" inputmode="decimal" min="0" step="any" value="%s">' % (fid, d)
        else:
            inp = '<select id="%s">' % fid + "".join('<option value="%s"%s>%s</option>' % (a, " selected" if a == d else "", b) for a, b in kind) + "</select>"
        fs += '<label for="%s">%s</label>%s' % (fid, lab, inp)
    rows = "".join('<dt>%s</dt><dd id="o-%s" data-f="%s">–</dd>' % (l, i, fm) for i, l, fm in p["outs"][:-1])
    i, l, fm = p["outs"][-1]
    body = ('<div class="g"><div><h1>%s</h1><p class="lead">%s</p></div><div class="calc">%s<dl aria-live="polite">%s</dl>'
            '<div class="total"><span>%s</span><strong id="o-%s" data-f="%s">–</strong></div>'
            '<p class="note">Estimativa bruta, antes de INSS e IR. Confira a sua convenção coletiva.</p></div></div>%s<div class="t">%s</div>'
            '<p><a href="index.html#calculadoras">Ver todas as calculadoras</a></p>') % (p["title"], p["desc"], fs, rows, l, i, fm, AD, p["text"])
    page(f, p["title"], p["desc"], body, ' data-calc="%s"' % p["key"], '<script src="calc.js"></script>')
    urls.append(f)

import glob
GUIDES = []
for g in sorted(glob.glob("guias/*.html")):
    t, d, b = open(g, encoding="utf-8").read().split("\n", 2)
    fn = "guia-" + os.path.basename(g)
    page(fn, t, d, '<article class="t">' + b + "</article>" + AD)
    GUIDES.append((fn, t, d))
    urls.append(fn)
gcards = "".join('<a href="%s"><b>%s</b><span>%s</span></a>' % x for x in GUIDES)
cards = "".join('<a href="%s"><b>%s</b><span>%s</span></a>' % (f, p["title"], p["desc"]) for f, p in CALCS.items())
home = ('<h1>Confira quanto você deveria receber pelo seu trabalho.</h1>'
        '<p class="lead">Calculadoras gratuitas para quem trabalha em escala, à noite ou faz hora extra. Digite os números do holerite e veja a conta passo a passo.</p>'
        '<h2 id="calculadoras">Calculadoras</h2><div class="cards">%s</div>%s'
        '<div class="t"><h2>Como usar</h2><p>Escolha a calculadora, digite o salário e as horas do mês e leia o resultado. Cada página explica a fórmula usada, para você conferir o valor com o RH ou o sindicato.</p></div>') % (cards, AD)
if GUIDES:
    home = home.replace('<div class="t"><h2>Como usar', '<h2>Guias</h2><div class="cards">' + gcards + '</div><div class="t"><h2>Como usar')
page("index.html", "Calculadoras para quem trabalha em escala, à noite e com hora extra",
     "Calculadoras gratuitas de adicional noturno, hora extra, escala 12x36 e férias, com a conta explicada.", home)

page("sobre.html", "Sobre", "Quem faz o %s e como as calculadoras funcionam." % NAME,
     '<h1>Sobre</h1><div class="t"><p>%s reúne calculadoras gratuitas para trabalhadores que fazem plantão, trabalham à noite ou recebem hora extra. A ideia é mostrar a conta, e não só o resultado.</p><p>As fórmulas seguem regras gerais da CLT e são estimativas. Convenções coletivas e acordos podem mudar os valores. Em caso de dúvida, procure o RH, o sindicato ou um advogado.</p><p>Encontrou um erro? Escreva para <a href="mailto:%s">%s</a>.</p></div>' % (NAME, EMAIL, EMAIL))
page("contato.html", "Contato", "Fale com a equipe do %s." % NAME,
     '<h1>Contato</h1><div class="t"><p>Sugestões, correções e dúvidas sobre as calculadoras: <a href="mailto:%s">%s</a>.</p><p>Não damos orientação jurídica individual. Para isso, procure um advogado ou o sindicato da sua categoria.</p></div>' % (EMAIL, EMAIL))
page("privacidade.html", "Política de privacidade", "Como o %s trata dados e cookies." % NAME,
     '<h1>Política de privacidade</h1><div class="t"><p>Os valores digitados nas calculadoras são processados no seu navegador e não são enviados nem guardados por nós.</p><p>Este site pode usar o Google AdSense para exibir anúncios. O Google e parceiros podem usar cookies para mostrar anúncios com base nas suas visitas a este e a outros sites. Você pode gerenciar a personalização de anúncios nas configurações de anúncios do Google.</p><p>Podemos usar ferramentas de estatística de acesso, como o Google Search Console e o Google Analytics, para entender quais páginas são mais úteis.</p><p>Conforme a LGPD, você pode pedir informações sobre dados pessoais tratados por nós pelo e-mail <a href="mailto:%s">%s</a>.</p><p>Esta política pode ser atualizada. Última revisão: outubro de 2026.</p></div>' % (EMAIL, EMAIL))
urls += ["sobre.html", "contato.html", "privacidade.html"]

write("style.css", CSS)
write("calc.js", JS)
write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join("<url><loc>%s/%s</loc></url>\n" % (SITE, u if u != "index.html" else "") for u in urls) + "</urlset>\n")

os.makedirs("/mnt/user-data/outputs", exist_ok=True)
with zipfile.ZipFile("/mnt/user-data/outputs/bolso-do-trabalhador-mvp.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for fn in sorted(os.listdir(OUT)):
        z.write(os.path.join(OUT, fn), "site/" + fn)
    z.write("build.py", "build.py")
print(sorted(os.listdir(OUT)))
