#!/usr/bin/env python3
import re
import inspect 
#from tqdm import tqdm
#from pymatgen.phasediagram.pdmaker import PhaseDiagram
#from pymatgen.phasediagram.plotter import PDPlotter
import sys
#sys.path.insert(0,'/home/gebhardtj/thidwick/scripts')
from libs.my_python_functions import *
#from my_qm_code_functions import *
import matplotlib.pyplot as plt 

#import roman #convert roman numbers to integer


# read radii and save them for each element, oxidation state, and coordination number (exclude
# high/low spin cases for now
#
# also remove IVSQ entries, no idea what those are
#
def compute_t(r_A,r_B,r_X):
    t=(r_A+r_X)/(m.sqrt(2)*(r_B+r_X))
    return t

ions=dict()

class ion:
    def __init__(self, label=None, ox=[], cn=[], r_c=[], r_ir=[], errors=[]):
        self.label=label
        self.ox=ox
        self.cn=cn
        self.r_c=r_c
        self.r_ir=r_ir
        self.errors=errors


def get_ionic_radii(filename):
    print (filename)

    lines,n=read_file(filename)
    #lines,n=read_file('test.dat')

    old_label=''
    old_ox=''
    na=-1
    no=-1
    radii=[]
    errors=[]
    # 0: list of 
    #   0 = atom label
    #   1 = list with oxidation states
    #       2 = list with coordination numbers for each oxidation state
    #       3 = list with r_c values for each ox. state 
    #       4 = list with r_ir values for each ox. state 
    for i in range(n):
        shift=0
        tmp=lines[i].split()
        label=tmp[0]
        ox=int(tmp[1])
        cn=tmp[2]
        r_c=tmp[3]
        # check for high spin/low spin
        check=is_float(r_c)
        if check == False:
            shift=2
            continue
        else:
            r_c=float(tmp[3+shift])
            r_ir=float(tmp[4+shift])

            if cn in ['IVSQ','IIIPY','IVPY']:
                continue
            elif cn in ['I','II','III','IIII','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV']:
                cn=roman.fromRoman(cn)
            else:
                cn=float(cn)
            #    print (label,ox,cn,r_c,r_ir)

            
            # now check for error est.
            if tmp[5+shift] != None:
                if tmp[5+shift] == 'None':
                    errors=None
                    #print('no float',errors)
                elif is_float(tmp[5+shift]) == True:
                    errors=float(tmp[5+shift])
                    #print('found float',errors)
                else:
                    errors=str(tmp[5+shift])
                    #print('no float',errors)
            else:
                errors=None
                #print('no float',errors)



            if label != old_label:
                ions[label] = ion(label)
                ions[label].ox = [ox]
                ions[label].cn = [[cn]]
                ions[label].r_c = [[r_c]]
                ions[label].r_ir = [[r_ir]]
                ions[label].errors = [[errors]]
                no=0
            else:
                if ox != old_ox:
#                        if label == 'Pb':
#                            print('new ox', ox, old_ox, no)
                    no=no+1
                    ions[label].ox.append(ox)
                    ions[label].cn.append([cn])
                    ions[label].r_c.append([r_c])
                    ions[label].r_ir.append([r_ir])
                    ions[label].errors.append([errors])
                else:
#                        if label == 'Pb':
#                           print('old ox', ox, old_ox, no)
                #    print(cn,label,no)
                    ions[label].cn[no].append(cn)
                    ions[label].r_c[no].append(r_c)
                    ions[label].r_ir[no].append(r_ir)
                    ions[label].errors[no].append(errors)
            #print (label,cn,ions[label],ions[label].cn,ions[label].r_c)
            old_ox=ox
            old_label=label


    #print (ions['Pa'].label)
    #print (ions['Pa'].ox)
    #print (ions['Pa'].cn)
    #exit()
    return ions


#add new info to ions dictionary
#so far tested only for cases where i added new oxidation states
#r_c is a dummy here for now
def add_new_info(ions,label,ox,cn,r_c,r_ir,errors):
    func_name=inspect.stack()[0][3]
    if label in ions:
        #error(func_name,'cannot add, already existing ion')
        if ox in ions[label].ox:
            no=ions[label].ox.index(ox)
            #if cn in ions[label].cn[no]:
            #    error(func_name,'cannot add, already existing information')
            #else:
            #    ions[label].cn[no].append(cn)
            #    ions[label].r_c[no].append(r_c)
            #    ions[label].r_ir[no].append(r_ir)
            cn_old=False
            for i in range(len(cn)):
                #check if radius already exists
                # if so, for now this should be an original SP radius
                # for now we want to keep the originial values, i.e., we modify t of the linear fit so that the old SP radius is retained, scaling all new values
                if cn[i] in ions[label].cn[no]:
                    cn_old=True
                    print(ions[label].cn[no],i)
                    nc=ions[label].cn[no].index(cn[i])
                    warning(func_name,'already existing information')
                    print('OX: ',ions[label].ox[no],'CN: ', cn[i])
                    print('r(new)', r_ir[i], 'r(old)', ions[label].r_ir[no][nc])
                    #this case should not happen any more, since we shift it
                    #already above, however, the old implementation below is
                    #nonsense, since it shift all values according to the linear
                    #shift. if ever needed again, only shift the i-th value
                    if r_ir[i] != ions[label].r_ir[no][nc]:
                        error(func_name,'old and new r differ, reimplement me')
                    #m,t=np.polyfit(cn,r_ir,1)
                    #fit_fn=np.poly1d([m,t])
                    #interp_r=fit_fn(cn[i])
                    #print('Fit based on new data',fit_fn)
                    #r_old=ions[label].r_ir[no][nc]
                    #dt=interp_r-r_old
                    #t=t-dt
                    #fit_fn_adj=np.poly1d([m,t])
                    #print ('Adjusted fit to retain old data', fit_fn_adj)
                    #if fit_fn_adj(cn[i]) != ions[label].r_ir[no][nc]:
                    #    print (fit_fn_adj)
                    #    print (fit_fn_adj(cn[i]))
                    #    print (ions[label].r_ir[no][nc])
                    #    error(func_name,'something went wrong adjusting the fit')
                    #for j in range(len(cn)):
                    #    if j != i:
                    #        print ('Def. fit', fit_fn(cn[j]))
                    #        print ('Adjusted Fit', fit_fn_adj(cn[j]))
                    #        interp_r=fit_fn_adj(cn[j])
                    #        ions[label].cn[no].append(cn[j])
                    #        ions[label].r_c[no].append(r_c[j])
                    #        ions[label].r_ir[no].append(interp_r)
                    #        ions[label].errors[no].append(errors[j])
#                   #         print(ions[label].label)
#                   #         print(ions[label].ox)
#                   #         print(ions[label].cn)
#                   #         print(ions[label].r_ir)
                    #break
                    #else:
                    #    break
                else:
                    ions[label].cn[no].append(cn[i])
                    ions[label].r_c[no].append(r_c[i])
                    ions[label].r_ir[no].append(r_ir[i])
                    ions[label].errors[no].append(errors[i])

            #if cn_old==False:
            #    for i in range(len(cn)):
            #            ions[label].cn[no].append(cn[i])
            #            ions[label].r_c[no].append(r_c[i])
            #            ions[label].r_ir[no].append(r_ir[i])
            #            ions[label].errors[no].append(errors[i])
        else:
            cn_old=False
            ions[label].ox.append(ox)
            #for i in range(len(cn)):
            #    ions[label].cn[no].append(cn[i])
            #    ions[label].r_c[no].append(r_c[i])
            #    ions[label].r_ir[no].append(r_ir[i])
            ions[label].cn.append(cn)
            ions[label].r_c.append(r_c)
            ions[label].r_ir.append(r_ir)
            ions[label].errors.append(errors)
    else:
        ions[label] = ion(label)
        ions[label].ox = ox
        ions[label].cn = [cn]
        ions[label].r_c = [r_c]
        ions[label].r_ir = [r_ir]
        ions[label].errors = [errors]
    print('UPDATED:')
    print(ions[label].label)
    print(ions[label].ox)
    print(ions[label].cn)
    print(ions[label].r_ir)
    print(ions[label].errors)

# we dont shift here anymore, implement plot in main function
#    if cn_old==True:
#        # plot 
#        y=[]
#        yadj=[]
#        x=[]
#        for i in range(1,12):
#            y.append(fit_fn(i))
#            yadj.append(fit_fn_adj(i))
#            x.append(i)
#        plt.plot(x,y,'r-',label='Original Fit: '+str(fit_fn))
#        plt.plot(x,yadj,'b-',label='Adjusted Fit: '+str(fit_fn_adj))
#        plt.plot(cn,r_ir,'bo')
#        plt.plot(ions[label].cn[no][nc],ions[label].r_ir[no][nc],'ro',label='Original Data Point')
#        plt.title('Shift for: '+label+' '+str(ox))
#        plt.legend()
#        plt.savefig('add_to_sp/shiftedfit_'+label+'_'+str(ox)+'.pdf',format='pdf')
#        plt.show()


#from existing data, get the specified label, ox, and cn by linear interpolation if possible
#return
#   interpolated radius    
def interpolate_r_ir(ions,label,ox,cn):
    func_name=inspect.stack()[0][3]
    interp=True
    if label not in ions:
        warning(func_name,'cannot interpolate, ion not known')
        interp=False
    print('ox',ox,ions[label].ox)
    if ox not in ions[label].ox:
        warning(func_name,'cannot interpolate, oxidation state not known')
        interp=False

    no=ions[label].ox.index(ox)
    print(ions[label].cn[no])

    if len(ions[label].cn[no]) <= 1:
        warning(func_name,'cannot interpolate, only one data point')
        interp=False

    if interp==False:
        interp_r=interpolate_hack_r_ir(ions,label,ox,cn)
    else:

        #get data for ox state

        tmp_cn=ions[label].cn[no]
        tmp_r=ions[label].r_ir[no]

        fit=np.polyfit(tmp_cn,tmp_r,1)
        fit_fn=np.poly1d(fit)
        #for the anions and can happen that interp does not work since the slope becomes negative, catch this case
        if fit[0]<0:
            interp=False

        interp_r=float(fit_fn(cn))
        print (fit)
        print (fit_fn)
        print (interp_r)



    return interp_r


#if interpolation is not possible, reduce r by some percentage, print warning
#hack if we know the ion and ox, just not the CN:
#   in this case we shouldnt be here unless the interpolation fails because of a negative slope, thus 
#   average the CN and r info we have, and compute the wanted r/cn pair based by changing the r by a percentage
def interpolate_hack_r_ir(ions,label,ox,cn):
    func_name=inspect.stack()[0][3]
    warning(func_name,'interpolation was not succesful, hack instead')
    if label not in ions:
        error(func_name,'cannot hack, ion not known')
    if ox not in ions[label].ox:
        error(func_name,'cannot hack, oxidation state not known')

    #get data for ox state
    no=ions[label].ox.index(ox)
    tmp_cn=np.mean(ions[label].cn[no])
    tmp_r=np.mean(ions[label].r_ir[no])

    #scale by 2% per CN
    #perc=0.02
    #for anions between cn=6 and cn=12 typical scaling is ~0.04, thus for our purpose use 0.04/6 for now
    perc=0.007
    scale=perc*(tmp_cn-cn)
    r=tmp_r-scale*tmp_r
#    print (tmp_cn)
    print ('%-10s %-10s %-10s %-10s' % ('CN', 'CN(interp)', 'r', 'r_interp'))
    print ('%-10i %-10i %-10.5f %-10.5f' % (tmp_cn, cn, tmp_r, r))
#    print (r)
    return r


#  reprint the ions list 
def update_radii_database(ions,filename):
    func_name=inspect.stack()[0][3]
    o=open(filename, "w")
    for i in ions:
        no=len(ions[i].ox)
        for j in range(no):
            nc=len(ions[i].cn[j])
            for k in range(nc):
#                print(ions[i].label,ions[i].ox[j],ions[i].cn[j][k],ions[i].r_c[j][k],ions[i].r_ir[j][k])
                #if i == 'Pb':
                #    print(ions[i].cn)
                if isinstance(ions[i].errors[j], float) == True:
                    o.write("%-3s %-3i %-6.2f %-10.4f %-10.4f %-10.4f\n"% \
                    (ions[i].label,ions[i].ox[j],ions[i].cn[j][k],ions[i].r_c[j][k],ions[i].r_ir[j][k],ions[i].errors[j][k]))
                else:
                    o.write("%-3s %-3i %-6.2f %-10.4f %-10.4f %-10s\n"% \
                    (ions[i].label,ions[i].ox[j],ions[i].cn[j][k],ions[i].r_c[j][k],ions[i].r_ir[j][k],ions[i].errors[j][k]))

    o.close()

# Polynomial Regression
def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
#    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    ssres = np.sum((y-yhat)**2)   # or sum([ (yi - yihat)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
#    results['determination'] = ssreg / sstot
    results['determination'] = 1- ssres / sstot

    return results

def plot_cn_vs_r(ax,X,OX,symbol):
    ions=get_ionic_radii('radii_updated.dat')

    print('Element:', ions[X].label)
    print('OXs:', ions[X].ox)
    print('Radii:', ions[X].r_ir)
    print('CNs:', ions[X].cn)
    print('Errors:', ions[X].errors)

    no=ions[X].ox.index(OX)

    x=[]
    y=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    x4=[]
    y4=[]
    y4_err=[]
    x5=[]
    y5=[]
        
    for j in range(len(ions[X].cn[no])):
        print(j,ions[X].errors[no][j])
        x.append(ions[X].cn[no][j])
        y.append(ions[X].r_ir[no][j])
        if ions[X].errors[no][j] == 'SP':
            x2.append(ions[X].cn[no][j])
            y2.append(ions[X].r_ir[no][j])
        elif ions[X].errors[no][j] in ['Interp','Merged']:
            x3.append(ions[X].cn[no][j])
            y3.append(ions[X].r_ir[no][j])
        elif ions[X].errors[no][j] in ['None',None]:
            x5.append(ions[X].cn[no][j])
            y5.append(ions[X].r_ir[no][j])
        else:
            x4.append(ions[X].cn[no][j])
            y4.append(ions[X].r_ir[no][j])
            y4_err.append(ions[X].errors[no][j])

    #m,t=np.polyfit(x,y,1)
    #fit=np.poly1d([m,t])
    #print('Fit',fit)

    fit_result=polyfit(x,y,1)
    fit=np.poly1d(fit_result['polynomial'])

    print('Fit',fit)
    print('Determination (R^2)', fit_result['determination'])

    x_fit=[]
    y_fit=[]
    for i in range(1,13):
        y_fit.append(fit(i))
        x_fit.append(i)

    print('x-data (CN)',x,x2,x3,x4)
    print('y-data (r_ir)',y,y2,y3,y4)
    print('y-error',y4_err)

    #plot
    #plt.plot(x,y,'bo')
    ax.plot(x2,y2, symbol, color='black', label=X)
    ax.plot(x3,y3, symbol, color='green', label='')
    ax.plot(x5,y5, symbol, color='red', label='')
    ax.errorbar(x4,y4,yerr=y4_err, fmt=symbol, color='blue',\
            ecolor='black',capsize=5)
    #plt.plot(x_fit,y_fit,'--', color='gray', label=r'Fit('+str(X)+'): '+str(fit)+'\
    #        $R^2$:'+"{:.4f}".format(fit_result['determination']))
    ax.plot(x_fit,y_fit,'--', color='gray',\
            label=r'$R^2$:'+"{:.4f}".format(fit_result['determination']))

    #plt.show()
                

def plot_ox_vs_r(ax,X,CN,symbol):
    ions=get_ionic_radii('radii_updated.dat')

    print('Element:', ions[X].label)
    print('OXs:', ions[X].ox)
    print('Radii:', ions[X].r_ir)
    print('CNs:', ions[X].cn)
    print('Errors:', ions[X].errors)

    x=[]
    y=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    x4=[]
    y4=[]
    y4_err=[]
    x5=[]
    y5=[]
    for i in range(len(ions[X].ox)):
        for j in range(len(ions[X].cn[i])):
            print(i,j,ions[X].errors[i][j])
            if ions[X].cn[i][j] == CN:
                x.append(ions[X].ox[i])
                y.append(ions[X].r_ir[i][j])
                if ions[X].errors[i][j] == 'SP':
                    x2.append(ions[X].ox[i])
                    y2.append(ions[X].r_ir[i][j])
                elif ions[X].errors[i][j] in ['Interp','Merged']:
                    x3.append(ions[X].ox[i])
                    y3.append(ions[X].r_ir[i][j])
                elif ions[X].errors[i][j] in ['None',None]:
                    x5.append(ions[X].ox[i])
                    y5.append(ions[X].r_ir[i][j])
                else:
                    x4.append(ions[X].ox[i])
                    y4.append(ions[X].r_ir[i][j])
                    y4_err.append(ions[X].errors[i][j])

    fit_result=polyfit(x,y,1)
    fit=np.poly1d(fit_result['polynomial'])

    print('Fit',fit)
    print('Determination (R^2)', fit_result['determination'])

    x_fit=[]
    y_fit=[]
    for i in range(-2,7):
        y_fit.append(fit(i))
        x_fit.append(i)

    print('x-data (OX)',x,x2,x3,x4)
    print('y-data (r_ir)',y,y2,y3,y4)
    print('y-error',y4_err)

    #plot
    #plt.plot(x,y,'bo')
    ax.plot(x2,y2, symbol, color='black', label=X)
    ax.plot(x3,y3, symbol, color='green', label='')
    ax.plot(x5,y5, symbol, color='red', label='')
    plt.errorbar(x4,y4,yerr=y4_err, fmt=symbol, color='blue')
    #ax.plot(x_fit,y_fit,'--', color='gray', label=r'Fit('+str(X)+'): '+str(fit)+'\
    #        $R^2$:'+"{:.4f}".format(fit_result['determination']))
    ax.plot(x_fit,y_fit,'--', color='gray',\
            label=r'$R^2$:'+"{:.4f}".format(fit_result['determination']))

    #plt.show()
