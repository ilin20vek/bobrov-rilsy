# Страница рилсов Боброва из подкаста с Игорем Малининым (WIVcEjFK47k), 8 роликов, без предложения и цен.
# Прохор, 04.11.2026, задача 1384, по образцу otdacha/stranicy/bobrov/sobrat.py. Собирает index.html из dannye.json; ролики - v/, обложки - o/.
import json, html, os
B = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(B, "dannye.json"), encoding="utf-8"))
for r in D:
    r["est"] = os.path.exists(os.path.join(B, "v", r["id"] + ".mp4"))
TEG = "#бизнес #предприниматель #маркетинг #ИИ #нейросети #shorts"
def tekst(r):
    return f"{r['nazv']}\n\n{r['opis']}\n\nПолное видео: https://youtu.be/WIVcEjFK47k?t={r['t']}\n\n{TEG}"
plitki = "".join(f'''
      <button class="pl" onclick="otkryt({i})"><img src="o/{r['id']}.jpg" alt="" loading="lazy">
        <span class="nz">{html.escape(r['nazv'])}</span></button>''' for i, r in enumerate(D) if r["est"])
dannye = json.dumps([{"id": r["id"], "nazv": r["nazv"], "opis": r["opis"], "tekst": tekst(r)} for r in D], ensure_ascii=False)
stranica = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ilin20vek.github.io/bobrov-rilsy/">
<meta property="og:title" content="Дмитрий Бобров и Игорь Малинин: 8 коротких роликов">
<meta property="og:description" content="ИИ-агенты, продажи, маркетплейсы, ошибка собственника, личный бренд - короткие ролики из подкаста.">
<meta property="og:image" content="https://ilin20vek.github.io/bobrov-rilsy/o/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="noindex, nofollow">
<title>Бобров и Малинин - рилсы</title>
<style>
:root{{--bg:#0e0e0f;--pl:#1c1c1e;--li:#2c2c2e;--tx:#f2f2f2;--mut:#a7a7ad;--ak:#ff6a00}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--tx);font:16px/1.55 Roboto,Arial,sans-serif}}
.w{{max-width:1120px;margin:0 auto;padding:0 16px}}
.hero{{text-align:center;padding:48px 16px 24px}}
.emb{{width:180px;height:180px;display:block;margin:0 auto 10px}}
.bpr{{font-size:15px;letter-spacing:.32em;text-transform:uppercase;color:var(--mut)}}
.metka{{display:inline-block;margin:28px 0 10px;background:var(--ak);color:#111;font-weight:800;border-radius:20px;padding:5px 16px;font-size:13px;letter-spacing:.06em;text-transform:uppercase}}
h1{{font-size:clamp(28px,5vw,46px);line-height:1.12;margin:0 0 14px}}
.lead{{max-width:720px;margin:0 auto;color:#d6d6da;font-size:18px}}
.ot{{display:flex;gap:12px;align-items:center;justify-content:center;margin:22px 0 0;color:var(--mut)}}
.ot img{{width:52px;height:52px;border-radius:50%;object-fit:cover;object-position:50% 20%}}
h2{{font-size:clamp(22px,3.4vw,30px);margin:46px 0 8px}} .pod{{color:var(--mut);margin:0 0 18px}}
.setka{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:18px 12px}}
.pl{{all:unset;cursor:pointer;display:block}}
.pl img{{width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:12px;display:block;background:#222}}
.pl:hover img{{outline:2px solid var(--ak)}} .nz{{display:block;margin:8px 2px 0;font-weight:500;line-height:1.3}}
.sovet{{background:var(--pl);border-radius:16px;padding:18px 20px;margin-top:22px;color:#ddd}} .sovet b{{color:var(--tx)}}
.tri{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}}
.tri div{{background:var(--pl);border-radius:14px;padding:16px 18px}} .tri b{{display:block;font-size:17px;margin-bottom:6px}}
.akciya{{margin-top:46px;border:2px solid var(--ak);border-radius:20px;padding:26px 24px;background:linear-gradient(160deg,#241307,#141414 60%)}}
.akciya .m{{color:var(--ak);font-weight:800;letter-spacing:.08em;text-transform:uppercase;font-size:13px}}
.akciya h2{{margin:8px 0 6px}} .cena{{font-size:clamp(34px,6vw,54px);font-weight:900;margin:6px 0}} .cena small{{font-size:18px;color:var(--mut);font-weight:500}}
.akciya ul{{padding-left:20px;color:#ddd}} .star{{color:var(--mut);font-size:.55em;font-weight:600;margin-right:8px}} .itogo{{font-size:20px;font-weight:700;margin:2px 0 6px}} .proba{{background:#ffffff14;border-radius:12px;padding:10px 14px;margin:8px 0 12px;color:#fff}} .akciya li{{margin:6px 0}}
.dalshe{{margin-top:22px;background:var(--pl);border-radius:16px;padding:20px 22px}} .dalshe p{{color:#ddd;margin:6px 0 0}}
.vstr{{text-align:center;margin:48px 0 20px}} .vstr .q{{font-size:clamp(22px,3.4vw,30px);font-weight:800;max-width:780px;margin:0 auto 18px}}
.b{{display:inline-block;background:#3a3a3c;color:var(--tx);border:0;border-radius:22px;padding:11px 20px;text-decoration:none;font:600 15px inherit;cursor:pointer;margin:4px}}
.b.ak{{background:var(--ak);color:#111}} .b:hover{{filter:brightness(1.15)}}
footer{{text-align:center;color:var(--mut);padding:24px 16px 56px;font-size:14px}}
.okno{{position:fixed;inset:0;background:rgba(0,0,0,.86);display:none;align-items:center;justify-content:center;padding:16px;z-index:9}} .okno.on{{display:flex}}
.vn{{background:var(--pl);border-radius:16px;max-width:860px;width:100%;max-height:94vh;overflow:auto;display:grid;grid-template-columns:minmax(220px,340px) 1fr;gap:18px;padding:16px}}
.vn video{{width:100%;aspect-ratio:9/16;border-radius:12px;background:#000}} .vn h3{{margin:2px 0 8px;font-size:20px}} .vn p{{color:#ddd;margin:0 0 10px}}
.vn textarea{{width:100%;height:130px;background:#141414;color:var(--mut);border:1px solid var(--li);border-radius:8px;padding:8px;font:13px/1.4 inherit}}
.zakr{{float:right;background:none;border:0;color:var(--mut);font-size:26px;cursor:pointer}} .zakr2{{position:fixed;top:10px;right:10px;z-index:10;background:#ffffffee;color:#111;border:0;border-radius:22px;padding:10px 16px;font:700 16px Roboto,Arial,sans-serif;cursor:pointer;box-shadow:0 2px 10px #0008}}
@media(max-width:640px){{.okno{{align-items:flex-start;padding-top:60px}} .vn{{grid-template-columns:1fr}} .vn video{{max-width:300px;margin:0 auto;display:block}} .setka{{grid-template-columns:repeat(2,1fr)}} .emb{{width:140px;height:140px}}}}
</style></head><body>
<header class="hero">
  <img class="emb" src="o/bpr-emblema.png" alt="Бизнес по-русски">
  <div class="bpr">Бизнес по-русски</div>
  <div class="metka">Короткие ролики</div>
  <h1>Дмитрий Бобров и Игорь Малинин</h1>
  <p class="lead">Восемь коротких роликов из подкаста: ИИ-агенты, продажи, маркетплейсы, ошибка собственника, личный бренд. С вопросом в первую секунду, титрами и обложкой.</p>
</header>
<main class="w">
  <h2>Восемь роликов</h2>
  <p class="pod">Нажмите на обложку: ролик запустится, рядом название, описание и кнопки «скачать».</p>
  <div class="setka">{plitki}
  </div>
</main>
<footer>Игорь Ильин · «Бизнес по-русски»</footer>
<div class="okno" id="okno" onclick="if(event.target===this)zakryt()"><button class="zakr2" onclick="zakryt()" aria-label="Закрыть">× Закрыть</button><div class="vn">
  <div><video id="vid" controls playsinline></video></div>
  <div><button class="zakr" onclick="zakryt()">×</button><h3 id="nz"></h3><p id="op"></p>
  <textarea id="tx" readonly></textarea>
  <div><a class="b" id="dv" download>Скачать ролик</a><a class="b" id="do" download>Скачать обложку</a><button class="b" onclick="kop(this)">Скопировать текст</button></div></div>
</div></div>
<script>
var D={dannye};
function otkryt(i){{var r=D[i];document.getElementById('nz').textContent=r.nazv;document.getElementById('op').textContent=r.opis;
document.getElementById('tx').value=r.tekst;var v=document.getElementById('vid');v.poster='o/'+r.id+'.jpg';v.src='v/'+r.id+'.mp4';
document.getElementById('dv').href='v/'+r.id+'.mp4';document.getElementById('do').href='o/'+r.id+'.jpg';document.getElementById('okno').classList.add('on');if(!history.state||!history.state.okno)history.pushState({{okno:1}},'');
var p=v.play();if(p&&p.catch)p.catch(function(){{v.muted=true;v.play()}})}}
function zakryt(iz){{var v=document.getElementById('vid');v.pause();document.getElementById('okno').classList.remove('on');if(!iz&&history.state&&history.state.okno)history.back()}}
window.addEventListener('popstate',function(){{if(document.getElementById('okno').classList.contains('on'))zakryt(1)}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')zakryt()}});
function kop(b){{var t=document.getElementById('tx');t.select();try{{navigator.clipboard.writeText(t.value)}}catch(e){{document.execCommand('copy')}}
b.textContent='Скопировано';setTimeout(function(){{b.textContent='Скопировать текст'}},1500)}}
</script>
</body></html>'''
open(os.path.join(B, "index.html"), "w", encoding="utf-8").write(stranica)
print("index.html", sum(r["est"] for r in D), "роликов")
