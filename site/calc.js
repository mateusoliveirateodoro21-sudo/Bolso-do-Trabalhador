(function(){
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
