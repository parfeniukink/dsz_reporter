# Generated by Django 4.0.1 on 2022-01-21 12:38

from core.models import Url
from django.contrib.auth import get_user_model
from django.db import migrations

User = get_user_model()

USER_DATA = {"username": "admin", "password": "admin"}

source = [
    "https://mfa.gov.ua",
    "https://mon.gov.ua",
    "https://sport.gov.ua",
    "https://minagro.gov.ua",
    "https://mva.gov.ua",
    "https://nads.gov.ua",
    "https://snriu.gov.ua",
    "https://dotacii2019.minagro.gov.ua",
    "https://www.rv.gov.ua",
    "https://carpathia.gov.ua",
    "https://dn.gov.ua",
    "https://forest.gov.ua",
    "https://mspu.gov.ua",
    "https://mukachevo-rada.gov.ua",
    "https://new.dfrr.minregion.gov.ua",
    "https://numo.mon.gov.ua",
    "https://www.ispf.gov.ua",
    "https://teplo.org.ua",
    "https://amcu.gov.ua",
    "https://paralympic.org.ua",
    "https://morrichservice.marad.gov.ua",
    "https://marad.gov.ua",
    "https://adm.dp.gov.ua",
    "https://otg.dp.gov.ua",
    "https://www.ucrf.gov.ua",
    "https://treasury.gov.ua",
    "https://nato.mfa.gov.ua",
    "https://zakordonniukrainci.mfa.gov.ua",
    "https://germany.mfa.gov.ua",
    "https://kazakhstan.mfa.gov.ua",
    "https://denmark.mfa.gov.ua",
    "https://india.mfa.gov.ua",
    "https://egypt.mfa.gov.ua",
    "https://cyprus.mfa.gov.ua",
    "https://frankfurt.mfa.gov.ua",
    "https://coe.mfa.gov.ua",
    "https://hungary.mfa.gov.ua",
    "https://japan.mfa.gov.ua",
    "https://ireland.mfa.gov.ua",
    "https://geneva.mfa.gov.ua",
    "https://belarus.mfa.gov.ua",
    "https://syria.mfa.gov.ua",
    "https://council.mfa.gov.ua",
    "https://iran.mfa.gov.ua",
    "https://dubai.mfa.gov.ua",
    "https://sweden.mfa.gov.ua",
    "https://finland.mfa.gov.ua",
    "https://edinburgh.mfa.gov.ua",
    "https://usa.mfa.gov.ua",
    "https://chg.treasury.gov.ua",
    "https://chk.treasury.gov.ua",
    "https://chv.treasury.gov.ua",
    "https://cry.treasury.gov.ua",
    "https://dnp.treasury.gov.ua",
    "https://don.treasury.gov.ua",
    "https://ifr.treasury.gov.ua",
    "https://kha.treasury.gov.ua",
    "https://khe.treasury.gov.ua",
    "https://khm.treasury.gov.ua",
    "https://kid.treasury.gov.ua",
    "https://kyivr.treasury.gov.ua",
    "https://kyiv.treasury.gov.ua",
    "https://lug.treasury.gov.ua",
    "https://lviv.treasury.gov.ua",
    "https://myk.treasury.gov.ua",
    "https://ode.treasury.gov.ua",
    "https://pol.treasury.gov.ua",
    "https://riv.treasury.gov.ua",
    "https://sev.treasury.gov.ua",
    "https://sum.treasury.gov.ua",
    "https://ter.treasury.gov.ua",
    "https://vol.treasury.gov.ua",
    "https://vyn.treasury.gov.ua",
    "https://www.treasury.gov.ua",
    "https://zak.treasury.gov.ua",
    "https://zap.treasury.gov.ua",
    "https://zhy.treasury.gov.ua",
    "https://crimea-platform.org",
    "https://www.nerc.gov.ua",
    "https://sies.gov.ua",
    "https://court.gov.ua",
    "https://eastmtv.amcu.gov.ua",
    "https://southeastmtv.amcu.gov.ua",
    "https://dsns.gov.ua",
    "https://diia.gov.ua",
    "http://mova.gov.ua",
    "https://bukoda.gov.ua",
    "https://www.rada.gov.ua",
    "https://mkrada.gov.ua",
    "https://design.gov.ua",
    "https://www.kmu.gov.ua",
    "https://www.spfu.gov.ua",
    "https://dpss.gov.ua",
    "https://msp.gov.ua",
    "http://www.vin.gov.ua",
    "https://voladm.gov.ua",
    "http://adm.dp.gov.ua",
    "https://dn.gov.ua",
    "https://oda.zht.gov.ua",
    "http://www.carpathia.gov.ua",
    "http://www.zoda.gov.ua",
    "http://www.if.gov.ua",
    "http://koda.gov.ua",
    "http://www.kr-admin.gov.ua",
    "http://www.loda.gov.ua",
    "http://loda.gov.ua",
    "http://www.mk.gov.ua",
    "https://oda.odessa.gov.ua",
    "http://www.adm-pl.gov.ua",
    "http://www.rv.gov.ua",
    "http://sm.gov.ua",
    "http://www.oda.te.gov.ua",
    "http://kharkivoda.gov.ua",
    "http://khoda.gov.ua",
    "http://www.adm.km.ua",
    "http://ck-oda.gov.ua",
    "https://bukoda.gov.ua",
    "http://cg.gov.ua",
    "http://kievcity.gov.ua",
    "https://asvpweb.minjust.gov.ua",
    "https://rase.minjust.gov.ua",
    "https://regdracs.minjust.gov.ua",
    "https://dzmi.minjust.gov.ua",
    "https://orm.minjust.gov.ua",
    "https://kap.minjust.gov.ua",
    "https://apostille.minjust.gov.ua",
    "https://usr.minjust.gov.ua",
    "https://corruptinfo.nazk.gov.ua",
    "https://lustration.minjust.gov.ua",
    "https://ak.minjust.gov.ua",
    "https://rgf.minjust.gov.ua",
    "https://ern.minjust.gov.ua",
    "https://rnb.nais.gov.ua",
    "https://kap.minjust.gov.ua",
    "https://erpv.minjust.gov.ua",
    "https://rgo.minjust.gov.ua",
    "https://rmpse.minjust.gov.ua",
    "https://tax.gov.ua",
    "https://public.nazk.gov.ua",
    "https://www.drv.gov.ua",
    "https://arma.gov.ua",
    "https://hsc.gov.ua",
    "https://agroregisters.com.ua",
    "http://www.drlz.com.ua",
    "https://ehealth.gov.ua",
    "https://e.land.gov.ua",
    "https://info.edbo.gov.ua",
    "https://e-construction.gov.ua",
    "https://policy-web.mtsbu.ua",
    "https://ek-cbi.msp.gov.ua",
    "https://data.gov.ua",
    "https://ics.gov.ua/ics/about/acts/",
    "https://dsa.court.gov.ua/dsa/",
    "https://id.court.gov.ua",
    "https://www.kyivgaz.ua/",
    "https://kv.dsoua.com/ua/",
    "https://vn.dsoua.com/ua/",
    "http://gazovik.biz.ua/",
    "https://vl.dsoua.com/ua/",
    "https://dpgor.dsoua.com/ua/",
    "https://dp.dsoua.com/ua/",
    "https://kr.dsoua.com/ua/",
    "https://oblgaz.donetsk.ua/",
    "https://www.abonentinfo.com/",
    "https://margaz.com.ua/",
    "https://cabinet.margaz.com.ua",
    "https://zt.dsoua.com/ua/",
    "http://korostyshivgaz.com.ua/",
    "https://zk.dsoua.com/ua/",
    "https://zp.dsoua.com/ua/",
    "http://melgaz.com.ua/",
    "https://if.dsoua.com/ua/",
    "https://ts.dsoua.com/ua/",
    "https://kirgas.com/",
    "http://luggas.com.ua/",
    "https://lc.luggas.com.ua",
    "https://lv.dsoua.com/ua/",
    "http://nrsirka.com.ua/sample-page/",
    "https://mk.dsoua.com/ua/",
    "https://odgaz.odessa.ua/",
    "http://gadyachgas.at.ua",
    "http://kgaz.com.ua/",
    "http://billing.kgaz.com.ua/aut",
    "https://lubnygaz.com.ua/",
    "https://poltavagaz.com.ua/",
    "https://rv.dsoua.com/ua/ ",
    "https://sm.dsoua.com/ua/",
    "http://kuprg.org.ua/",
    "https://tgaz.te.ua/",
    "http://tmgaz.te.ua/",
    "https://kh.dsoua.com/ua/",
    "https://khgor.dsoua.com/ua/",
    "http://gaz.kherson.ua/",
    "http://194.79.22.199:8080/abonent/",
    "https://km.dsoua.com/ua/",
    "http://shepetivkagaz.ucoz.ua/",
    "https://umangaz.com.ua/",
    "http://www.chergas.ck.ua/",
    "http://abon1.chergas.ck.ua",
    "https://cv.dsoua.com/ua/",
    "https://cn.dsoua.com/ua",
    "https://www.agsynthesis.com/",
    "https://app.agsynthesis.com/register/step-one",
    "http://www.azovgaz.com.ua",
    "https://ascania.energy/",
    "https://www.vek.energy/",
    "https://teplobud-pcf.com/",
    "https://cabinet.teplobud-pcf.com/",
    "https://vlgaszbut.com.ua/",
    "https://elektro.volyn.ua/",
    "https://ok.elektro.volyn.ua/home/",
    "https://vngaszbut.com.ua/",
    "http://gazpostach.te.ua/",
    "https://account.gazpostach.te.ua/login",
    "http://gaspostach.com/",
    "https://gazprompostach.com.ua/",
    "http://cabinet.gazprompostach.com.ua/login.php",
    "https://www.okko.ua/okko-gas",
    "http://energy.glasscomerce.com",
    "https://yasno.com.ua/",
    "https://dpgaszbut.com.ua/",
    "https://yasno.com.ua/",
    "https://erupeople.com.ua/",
    "http://www.eru.com.ua/",
    "https://evodatrade.com.ua/",
    "http://vin.enera.ua/",
    "https://vn.e-svitlo.com.ua/",
    "https://lg.enera.ua/",
    "https://lg.e-svitlo.com.ua/",
    "https://energogarantiya.com/",
    "https://etg.ua/",
    "https://ztgaszbut.com.ua/",
    "https://www.ztoek.com.ua/",
    "https://zkgaszbut.com.ua/",
    "https://zakarpatzbut.energy/",
    "https://zpgaszbut.com.ua/",
    "https://ifgaszbut.com.ua/",
    "https://je.com.ua/ua/",
    "https://energy.kyivgaz.ua/",
    "https://kvgaszbut.com.ua/",
    "https://yasno.com.ua/",
    "https://kgaz-trading.com.ua/",
    "https://my.kgaz-trading.com.ua/auth",
    "https://ltke.com.ua/ua/",
    "http://176.37.146.52:3000/users/sign_in",
    "https://www.lgtrading.com.ua/",
    "http://www.zbut.luggas.com.ua/",
    "https://lc.luggas.com.ua/",
    "https://lvgaszbut.com.ua/",
    "https://lez.com.ua/",
    "https://info.lez.com.ua/",
    "http://www.mgas.com.ua",
    "http://tovmargaz.com.ua/",
    "http://cabinet.tov-margaz.com.ua/",
    "https://megawatt.com.ua/",
    "https://cabinet.megawatt.com.ua/",
    "https://mkgaszbut.com.ua/",
    "https://gas.ua/",
    "https://my.gas.ua/login",
    "https://gas.ua/uk/home/slr",
    "https://gazpostach.od.ua/",
    "http://poltavagazzbut.com.ua/",
    "https://cabinet.poltavagazzbut.com.ua/index.php",
    "https://pret.com.ua/",
    "https://my.pret.com.ua/",
    "https://www.gazps.com/",
    "https://rvgaszbut.com.ua/",
    "https://svitlogas.ua/",
    "https://sviy.com",
    "https://struinaftogaz.com.ua/",
    "https://smgaszbut.com.ua/",
    "https://gaz.tasenergy.com.ua/login",
    "http://teroblgaz.com.ua/",
    "http://zbutoblgaz.com.ua/",
    "https://tek.energy/",
    "https://my.tek.energy/",
    "https://td.lubnygaz.com.ua/",
    "https://umangazzbut.com.ua/",
    "https://khgaszbut.com.ua/",
    "https://khersonregiongas.com.ua/",
    "http://gaz.ukrcom.kherson.ua:8080/Abonent/",
    "https://khoek.ks.ua/",
    "https://kmgaszbut.com.ua/",
    "https://energo.km.ua/",
    "https://ienergo.com.ua/",
    "http://gas-zbut.ck.ua/",
    "http://ek.cv.ua/",
    "https://www.myenergy.cv.ua/uk/customer/login",
    "https://cvgaszbut.com.ua/",
    "https://cngaszbut.com.ua/",
    "https://dpgazshep.ucoz.ua/",
    "https://www.universegas.com.ua/",
]


def populate_urls():
    if Url.objects.all().exists():
        return
    for url in source:
        Url.objects.create(path=url)


def populate_db(*args, **kwargs):
    if not User.objects.all().exists():
        User.objects.create_superuser(**USER_DATA)
    populate_urls()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [migrations.RunPython(populate_db)]
