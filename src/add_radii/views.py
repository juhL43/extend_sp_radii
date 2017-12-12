from django.shortcuts import render

from .models import db_ions

# Create your views here.
def home(request):
    ions = db_ions.objects.all()
    #context = locals()
    template = 'home.html'
    H = db_ions.objects.get(label='H')
    Li = db_ions.objects.get(label='Li')
    Be = db_ions.objects.get(label='Be')
    B = db_ions.objects.get(label='B')
    C = db_ions.objects.get(label='C')
    N = db_ions.objects.get(label='N')
    O = db_ions.objects.get(label='O')
    F = db_ions.objects.get(label='F')
    Na = db_ions.objects.get(label='Na')
    Mg = db_ions.objects.get(label='Mg')
    Al = db_ions.objects.get(label='Al')
    Si = db_ions.objects.get(label='Si')
    P = db_ions.objects.get(label='P')
    S = db_ions.objects.get(label='S')
    Cl = db_ions.objects.get(label='Cl')
    K = db_ions.objects.get(label='K')
    Ca = db_ions.objects.get(label='Ca')
    Sc = db_ions.objects.get(label='Sc')
    Ti = db_ions.objects.get(label='Ti')
    V = db_ions.objects.get(label='V')
    Cr = db_ions.objects.get(label='Cr')
    Mn = db_ions.objects.get(label='Mn')
    Fe = db_ions.objects.get(label='Fe')
    Co = db_ions.objects.get(label='Co')
    Ni = db_ions.objects.get(label='Ni')
    Cu = db_ions.objects.get(label='Cu')
    Zn = db_ions.objects.get(label='Zn')
    Ga = db_ions.objects.get(label='Ga')
    Ge = db_ions.objects.get(label='Ge')
    As = db_ions.objects.get(label='As')
    Se = db_ions.objects.get(label='Se')
    Br = db_ions.objects.get(label='Br')
    Rb = db_ions.objects.get(label='Rb')
    Sr = db_ions.objects.get(label='Sr')
    Y = db_ions.objects.get(label='Y')
    Zr = db_ions.objects.get(label='Zr')
    Nb = db_ions.objects.get(label='Nb')
    Mo = db_ions.objects.get(label='Mo')
    Tc = db_ions.objects.get(label='Tc')
    Ru = db_ions.objects.get(label='Ru')
    Rh = db_ions.objects.get(label='Rh')
    Pd = db_ions.objects.get(label='Pd')
    Ag = db_ions.objects.get(label='Ag')
    Cd = db_ions.objects.get(label='Cd')
    In = db_ions.objects.get(label='In')
    Sn = db_ions.objects.get(label='Sn')
    Sb = db_ions.objects.get(label='Sb')
    Te = db_ions.objects.get(label='Te')
    I = db_ions.objects.get(label='I')
    Cs = db_ions.objects.get(label='Cs')
    Ba = db_ions.objects.get(label='Ba')
    Lu = db_ions.objects.get(label='Lu')
    Hf = db_ions.objects.get(label='Hf')
    Ta = db_ions.objects.get(label='Ta')
    W = db_ions.objects.get(label='W')
    Re = db_ions.objects.get(label='Re')
    Os = db_ions.objects.get(label='Os')
    Ir = db_ions.objects.get(label='Ir')
    Pt = db_ions.objects.get(label='Pt')
    Au = db_ions.objects.get(label='Au')
    Hg = db_ions.objects.get(label='Hg')
    Tl = db_ions.objects.get(label='Tl')
    Pb = db_ions.objects.get(label='Pb')
    Bi = db_ions.objects.get(label='Bi')
    Po = db_ions.objects.get(label='Po')
    At = db_ions.objects.get(label='At')
    Fr = db_ions.objects.get(label='Fr')
    Ra = db_ions.objects.get(label='Ra')
    #Lr = db_ions.objects.get(label='Lr')
    #Rf = db_ions.objects.get(label='Rf')
    #Db = db_ions.objects.get(label='Db')
    #Sg = db_ions.objects.get(label='Sg')
    #Bh = db_ions.objects.get(label='Bh')
    #Hs = db_ions.objects.get(label='Hs')
    #Mt = db_ions.objects.get(label='Mt')
    #Ds = db_ions.objects.get(label='Ds')
    #Rg = db_ions.objects.get(label='Rg')
    #Cn = db_ions.objects.get(label='Cn')
    #Nh = db_ions.objects.get(label='Nh')
    #Fl = db_ions.objects.get(label='Fl')
    #Mc = db_ions.objects.get(label='Mc')
    #Lv = db_ions.objects.get(label='Lv')
    #Ts = db_ions.objects.get(label='Ts')
    La = db_ions.objects.get(label='La')
    Ce = db_ions.objects.get(label='Ce')
    Pr = db_ions.objects.get(label='Pr')
    Nd = db_ions.objects.get(label='Nd')
    Pm = db_ions.objects.get(label='Pm')
    Sm = db_ions.objects.get(label='Sm')
    Eu = db_ions.objects.get(label='Eu')
    Gd = db_ions.objects.get(label='Gd')
    Tb = db_ions.objects.get(label='Tb')
    Dy = db_ions.objects.get(label='Dy')
    Ho = db_ions.objects.get(label='Ho')
    Er = db_ions.objects.get(label='Er')
    Tm = db_ions.objects.get(label='Tm')
    Yb = db_ions.objects.get(label='Yb')
    Ac = db_ions.objects.get(label='Ac')
    Th = db_ions.objects.get(label='Th')
    Pa = db_ions.objects.get(label='Pa')
    U = db_ions.objects.get(label='U')
    Np = db_ions.objects.get(label='Np')
    Pu = db_ions.objects.get(label='Pu')
    Am = db_ions.objects.get(label='Am')
    Cm = db_ions.objects.get(label='Cm')
    Bk = db_ions.objects.get(label='Bk')
    Cf = db_ions.objects.get(label='Cf')
    #Es = db_ions.objects.get(label='Es')
    #Fm = db_ions.objects.get(label='Fm')
    #Md = db_ions.objects.get(label='Md')
    #No = db_ions.objects.get(label='No')
    return render(request,template, {'ions' : ions, \
    'H' : H,\
    'Li' : Li, \
    'Be' : Be, \
    'B' : B, \
    'C' : C, \
    'N' : N, \
    'O' : O, \
    'F' : F, \
    'Na' : Na, \
    'Mg' : Mg, \
    'Al' : Al, \
    'Si' : Si, \
    'P' : P, \
    'S' : S, \
    'Cl' : Cl, \
    'K' : K, \
    'Ca' : Ca, \
    'Sc' : Sc, \
    'Ti' : Ti, \
    'V' : V, \
    'Cr' : Cr, \
    'Mn' : Mn, \
    'Fe' : Fe, \
    'Co' : Co, \
    'Ni' : Ni, \
    'Cu' : Cu, \
    'Zn' : Zn, \
    'Ga' : Ga, \
    'Ge' : Ge, \
    'As' : As, \
    'Se' : Se, \
    'Br' : Br, \
    'Rb' : Rb, \
    'Sr' : Sr, \
    'Y' : Y, \
    'Zr' : Zr, \
    'Nb' : Nb, \
    'Mo' : Mo, \
    'Tc' : Tc, \
    'Ru' : Ru, \
    'Rh' : Rh, \
    'Pd' : Pd, \
    'Ag' : Ag, \
    'Cd' : Cd, \
    'In' : In, \
    'Sn' : Sn, \
    'Sb' : Sb, \
    'Te' : Te, \
    'I' : I, \
    'Cs' : Cs, \
    'Ba' : Ba, \
    'Lu' : Lu, \
    'Hf' : Hf, \
    'Ta' : Ta, \
    'W' : W, \
    'Re' : Re, \
    'Os' : Os, \
    'Ir' : Ir, \
    'Pt' : Pt, \
    'Au' : Au, \
    'Hg' : Hg, \
    'Tl' : Tl, \
    'Pb' : Pb, \
    'Bi' : Bi, \
    'Po' : Po, \
    'At' : At, \
    'Fr' : Fr, \
    'Ra' : Ra, \
    #'Lr' : Lr, \
    #'Rf' : Rf, \
    #'Db' : Db, \
    #'Sg' : Sg, \
    #'Bh' : Bh, \
    #'Hs' : Hs, \
    #'Mt' : Mt, \
    #'Ds' : Ds, \
    #'Rg' : Rg, \
    #'Cn' : Cn, \
    #'Nh' : Nh, \
    #'Fl' : Fl, \
    #'Mc' : Mc, \
    #'Lv' : Lv, \
    #'Ts' : Ts, \
    'La' : La, \
    'Ce' : Ce, \
    'Pr' : Pr, \
    'Nd' : Nd, \
    'Pm' : Pm, \
    'Sm' : Sm, \
    'Eu' : Eu, \
    'Gd' : Gd, \
    'Tb' : Tb, \
    'Dy' : Dy, \
    'Ho' : Ho, \
    'Er' : Er, \
    'Tm' : Tm, \
    'Yb' : Yb, \
    'Ac' : Ac, \
    'Th' : Th, \
    'Pa' : Pa, \
    'U' : U, \
    'Np' : Np, \
    'Pu' : Pu, \
    'Am' : Am, \
    'Cm' : Cm, \
    'Bk' : Bk, \
    'Cf' : Cf, \
    #'Es' : Es, \
    #'Fm' : Fm, \
    #'Md' : Md, \
    #'No' : No, \
    })


def details(request, ion_label):
    sel_ion = db_ions.objects.get(label=ion_label)
    ions = db_ions.objects.all()
    #return render(request,'details.html', {'sel_ion' : sel_ion})
    oxrange=range(len(sel_ion.ox))
    ox=sel_ion.ox
    cnrange=[]
    for i in range(len(sel_ion.ox)):
        cnrange.append(range(len(sel_ion.cn[i])))
    H = db_ions.objects.get(label='H')
    Li = db_ions.objects.get(label='Li')
    Be = db_ions.objects.get(label='Be')
    B = db_ions.objects.get(label='B')
    C = db_ions.objects.get(label='C')
    N = db_ions.objects.get(label='N')
    O = db_ions.objects.get(label='O')
    F = db_ions.objects.get(label='F')
    Na = db_ions.objects.get(label='Na')
    Mg = db_ions.objects.get(label='Mg')
    Al = db_ions.objects.get(label='Al')
    Si = db_ions.objects.get(label='Si')
    P = db_ions.objects.get(label='P')
    S = db_ions.objects.get(label='S')
    Cl = db_ions.objects.get(label='Cl')
    K = db_ions.objects.get(label='K')
    Ca = db_ions.objects.get(label='Ca')
    Sc = db_ions.objects.get(label='Sc')
    Ti = db_ions.objects.get(label='Ti')
    V = db_ions.objects.get(label='V')
    Cr = db_ions.objects.get(label='Cr')
    Mn = db_ions.objects.get(label='Mn')
    Fe = db_ions.objects.get(label='Fe')
    Co = db_ions.objects.get(label='Co')
    Ni = db_ions.objects.get(label='Ni')
    Cu = db_ions.objects.get(label='Cu')
    Zn = db_ions.objects.get(label='Zn')
    Ga = db_ions.objects.get(label='Ga')
    Ge = db_ions.objects.get(label='Ge')
    As = db_ions.objects.get(label='As')
    Se = db_ions.objects.get(label='Se')
    Br = db_ions.objects.get(label='Br')
    Rb = db_ions.objects.get(label='Rb')
    Sr = db_ions.objects.get(label='Sr')
    Y = db_ions.objects.get(label='Y')
    Zr = db_ions.objects.get(label='Zr')
    Nb = db_ions.objects.get(label='Nb')
    Mo = db_ions.objects.get(label='Mo')
    Tc = db_ions.objects.get(label='Tc')
    Ru = db_ions.objects.get(label='Ru')
    Rh = db_ions.objects.get(label='Rh')
    Pd = db_ions.objects.get(label='Pd')
    Ag = db_ions.objects.get(label='Ag')
    Cd = db_ions.objects.get(label='Cd')
    In = db_ions.objects.get(label='In')
    Sn = db_ions.objects.get(label='Sn')
    Sb = db_ions.objects.get(label='Sb')
    Te = db_ions.objects.get(label='Te')
    I = db_ions.objects.get(label='I')
    Cs = db_ions.objects.get(label='Cs')
    Ba = db_ions.objects.get(label='Ba')
    Lu = db_ions.objects.get(label='Lu')
    Hf = db_ions.objects.get(label='Hf')
    Ta = db_ions.objects.get(label='Ta')
    W = db_ions.objects.get(label='W')
    Re = db_ions.objects.get(label='Re')
    Os = db_ions.objects.get(label='Os')
    Ir = db_ions.objects.get(label='Ir')
    Pt = db_ions.objects.get(label='Pt')
    Au = db_ions.objects.get(label='Au')
    Hg = db_ions.objects.get(label='Hg')
    Tl = db_ions.objects.get(label='Tl')
    Pb = db_ions.objects.get(label='Pb')
    Bi = db_ions.objects.get(label='Bi')
    Po = db_ions.objects.get(label='Po')
    At = db_ions.objects.get(label='At')
    Fr = db_ions.objects.get(label='Fr')
    Ra = db_ions.objects.get(label='Ra')
    #Lr = db_ions.objects.get(label='Lr')
    #Rf = db_ions.objects.get(label='Rf')
    #Db = db_ions.objects.get(label='Db')
    #Sg = db_ions.objects.get(label='Sg')
    #Bh = db_ions.objects.get(label='Bh')
    #Hs = db_ions.objects.get(label='Hs')
    #Mt = db_ions.objects.get(label='Mt')
    #Ds = db_ions.objects.get(label='Ds')
    #Rg = db_ions.objects.get(label='Rg')
    #Cn = db_ions.objects.get(label='Cn')
    #Nh = db_ions.objects.get(label='Nh')
    #Fl = db_ions.objects.get(label='Fl')
    #Mc = db_ions.objects.get(label='Mc')
    #Lv = db_ions.objects.get(label='Lv')
    #Ts = db_ions.objects.get(label='Ts')
    La = db_ions.objects.get(label='La')
    Ce = db_ions.objects.get(label='Ce')
    Pr = db_ions.objects.get(label='Pr')
    Nd = db_ions.objects.get(label='Nd')
    Pm = db_ions.objects.get(label='Pm')
    Sm = db_ions.objects.get(label='Sm')
    Eu = db_ions.objects.get(label='Eu')
    Gd = db_ions.objects.get(label='Gd')
    Tb = db_ions.objects.get(label='Tb')
    Dy = db_ions.objects.get(label='Dy')
    Ho = db_ions.objects.get(label='Ho')
    Er = db_ions.objects.get(label='Er')
    Tm = db_ions.objects.get(label='Tm')
    Yb = db_ions.objects.get(label='Yb')
    Ac = db_ions.objects.get(label='Ac')
    Th = db_ions.objects.get(label='Th')
    Pa = db_ions.objects.get(label='Pa')
    U = db_ions.objects.get(label='U')
    Np = db_ions.objects.get(label='Np')
    Pu = db_ions.objects.get(label='Pu')
    Am = db_ions.objects.get(label='Am')
    Cm = db_ions.objects.get(label='Cm')
    Bk = db_ions.objects.get(label='Bk')
    Cf = db_ions.objects.get(label='Cf')
    #Es = db_ions.objects.get(label='Es')
    #Fm = db_ions.objects.get(label='Fm')
    #Md = db_ions.objects.get(label='Md')
    #No = db_ions.objects.get(label='No')
    return render(request,'home.html', {'sel_ion' : sel_ion, 'ox' : sel_ion.ox, 'oxrange' : oxrange, 'cnrange' : cnrange, \
    'H' : H,\
    'Li' : Li, \
    'Be' : Be, \
    'B' : B, \
    'C' : C, \
    'N' : N, \
    'O' : O, \
    'F' : F, \
    'Na' : Na, \
    'Mg' : Mg, \
    'Al' : Al, \
    'Si' : Si, \
    'P' : P, \
    'S' : S, \
    'Cl' : Cl, \
    'K' : K, \
    'Ca' : Ca, \
    'Sc' : Sc, \
    'Ti' : Ti, \
    'V' : V, \
    'Cr' : Cr, \
    'Mn' : Mn, \
    'Fe' : Fe, \
    'Co' : Co, \
    'Ni' : Ni, \
    'Cu' : Cu, \
    'Zn' : Zn, \
    'Ga' : Ga, \
    'Ge' : Ge, \
    'As' : As, \
    'Se' : Se, \
    'Br' : Br, \
    'Rb' : Rb, \
    'Sr' : Sr, \
    'Y' : Y, \
    'Zr' : Zr, \
    'Nb' : Nb, \
    'Mo' : Mo, \
    'Tc' : Tc, \
    'Ru' : Ru, \
    'Rh' : Rh, \
    'Pd' : Pd, \
    'Ag' : Ag, \
    'Cd' : Cd, \
    'In' : In, \
    'Sn' : Sn, \
    'Sb' : Sb, \
    'Te' : Te, \
    'I' : I, \
    'Cs' : Cs, \
    'Ba' : Ba, \
    'Lu' : Lu, \
    'Hf' : Hf, \
    'Ta' : Ta, \
    'W' : W, \
    'Re' : Re, \
    'Os' : Os, \
    'Ir' : Ir, \
    'Pt' : Pt, \
    'Au' : Au, \
    'Hg' : Hg, \
    'Tl' : Tl, \
    'Pb' : Pb, \
    'Bi' : Bi, \
    'Po' : Po, \
    'At' : At, \
    'Fr' : Fr, \
    'Ra' : Ra, \
    #'Lr' : Lr, \
    #'Rf' : Rf, \
    #'Db' : Db, \
    #'Sg' : Sg, \
    #'Bh' : Bh, \
    #'Hs' : Hs, \
    #'Mt' : Mt, \
    #'Ds' : Ds, \
    #'Rg' : Rg, \
    #'Cn' : Cn, \
    #'Nh' : Nh, \
    #'Fl' : Fl, \
    #'Mc' : Mc, \
    #'Lv' : Lv, \
    #'Ts' : Ts, \
    'La' : La, \
    'Ce' : Ce, \
    'Pr' : Pr, \
    'Nd' : Nd, \
    'Pm' : Pm, \
    'Sm' : Sm, \
    'Eu' : Eu, \
    'Gd' : Gd, \
    'Tb' : Tb, \
    'Dy' : Dy, \
    'Ho' : Ho, \
    'Er' : Er, \
    'Tm' : Tm, \
    'Yb' : Yb, \
    'Ac' : Ac, \
    'Th' : Th, \
    'Pa' : Pa, \
    'U' : U, \
    'Np' : Np, \
    'Pu' : Pu, \
    'Am' : Am, \
    'Cm' : Cm, \
    'Bk' : Bk, \
    'Cf' : Cf, \
    #'Es' : Es, \
    #'Fm' : Fm, \
    #'Md' : Md, \
    #'No' : No, \
    })

