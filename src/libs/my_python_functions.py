#!/usr/bin/env python3
# this is the only way to keep this portable 
# you can check the python version using 
# print (sys.version) (after import sys)
#
#
# python functions for fast(er) programming
# generall functions only, all scripts are supposed to be able to use those functions
# thus, whenever changes are done compatibility will be lost with all old scripts
# usually on then get's lacy and old scripts don't work anymore
# thus try to kepp this as CLEAN AND GENERAL as possible

# don't put stuff of any quantum chemistry code in here, make an extra, similar general file for that

#


##------------------- IMPORT MODULES
import sys                      #enable system calls
import re
import os               #os.path.isfile , .stat
import inspect 
#import roman            # convert roman numbers to arabics
#import fileinput
#import argparse
#import glob
#import shutil          #enabling shutil.copy
#import subprocess      #enables using bash commands
#import time
#import math
#import string
#
#import matplotlib.pyplot as plt
import numpy as np
##------------------- 

# unfortunately this does not work
## check if a string can be converted into roman number
### return True or False
#def is_roman(s):
#    func_name=inspect.stack()[0][3]
#    try:
#        roman.fromRoman(s)
#        return True
#    except ValueError:
#        warning(func_name, "Not a Roman number")
#        return False

## check if a string can be converted into float
## return True or False
def is_float(s):
    func_name=inspect.stack()[0][3]
    try:
        float(s)
        return True
    except ValueError:
        vprint(func_name, "Not a float")
        return False

def warning(function, message):
    print ("! W ! A ! R ! N ! I ! N ! G !: ")
    print (function, ": ", message)

def error(function, message):
    print ("! E ! R ! R ! O ! R !: ")
    print (function, ": ", message)
    print ("E X I T")
    sys.exit()

## search regexp in list and return indexes of every match
## s=pattern, list=list to be searched, list with indexes and number of hits is returned
def list_idxs_from_pattern(s,list):
        p=re.compile(s)
        hits=[]
        for i in range(len(list)):
                if re.search(p, list[i]):
                        hits.append(i)
        return hits, len(hits)

## check if file exists, return error if not
## read file, return lines as list and number of entries
def read_file(filename):
    func_name=inspect.stack()[0][3]
    if check_file(filename) == True:
        #file = open(filename, "r+")
        file = open(filename, "r+", encoding="utf-8")
        lines = (file.read().splitlines())
        file.close()

        num_lines = len(lines)
    else:
        print(os.fspath(filename))
        filename=os.fsencode(filename)
        filename=filename.replace('b','')
        file = open(filename, "r+", encoding="utf-8")
        lines = (file.read().splitlines())
        file.close()

        num_lines = len(lines)
        #error(func_name,'file not found')
   
    return lines, num_lines

def check_file(PATH):
    #print ('testing',PATH)
    if os.path.isfile(PATH):
            if os.stat(PATH).st_size > 0:
                    return True
            else:
                    return False
    else:
            return False

## return the norm (i.e.,length) of a vector in form of a np.array
def norm(u):
        norm=np.linalg.norm(u)
        return norm

## return the angle between two vectors in degrees
# use vec_length
def angle(u,v):
        c_alpha=np.dot(u,v)/norm(u)/norm(v)
        alpha=np.arccos(np.clip(c_alpha,-1,1))
        alpha=np.degrees(alpha)
        return alpha

## verboseprint statement, prints all statemens only if -v argument is set
def vprint(v_flag,*args):
    #print(args)
    if v_flag == True:
        s=''
        for arg in args:
            s=s+str(arg)
        print (s)
    else:
        pass

## strip comma from the end of a string (for numbers)
def strip_comma(s):
        if s.endswith(','):
                s=s[:-1]
        return s

def printline(length):
        str="-"
        for i in range(length):
                str=str+"-"

        print (str)

##------------------ general function put this in separate file
#
#
#
##exit script and print error string s      
#
#def printline(length):
#       str="-"
#       for i in range(length):
#               str=str+"-"
#
#       print (str)
#
#
#def warning(function, message):
#    print ("! W ! A ! R ! N ! I ! N ! G !: ")
#    print (function, ": ", message)
#
#def error(function, message):
#    print ("! E ! R ! R ! O ! R !: ")
#    print (function, ": ", message)
#    print ("E X I T")
#    sys.exit()
#
## !!!!!!!! this is not exclusive yet do this !!!!!!!
## change one word in a file exclusively and rewrite the changed file
## exclusively means it is checked how often the word is
## found and an error is given if it is found more then once
#def change_word_excl(OLD,NEW,filename):
#       for line in fileinput.input(filename, inplace=True):
#               print (line.replace(OLD,NEW), end = '')
#
##change one word in a file and rewrite the changed file
#def change_word(OLD,NEW,filename):
#       for line in fileinput.input(filename, inplace=True):
#               print (line.replace(OLD,NEW), end = '')
#
#
## search regexp in list and return indexes of every match
## s=pattern, list=list to be searched, list with indexes and number of hits is returned
#def list_indexes_from_pattern(s,list):
#       p=re.compile(s)
#       hits=[]
#       for i in range(len(list)):
#               if re.search(p, list[i]):
#                       hits.append(i)
#       return hits, len(hits)
#
## search regexp in list and return indexes of match
## check for number of hits, error if more then one
## s=pattern, list=list to be searched, list with indexes and number of hits is returned
#def list_indexes_from_pattern_excl(s,list):
#       func_name=inspect.stack()[0][3]
#       p=re.compile(s)
#       hits=[]
#       for i in range(len(list)):
#               if re.search(p, list[i]):
#                       hits.append(i)
#
#       if len(hits) > 1:
#               error(func_name,'found more then one hits')
#       elif len(hits) == 0:
#               error(func_name,'pattern not found')
#       else:
#               new_hit=hits[0]
#               return new_hit
#
#def list_indexes_from_pattern_no_case_excl(s,list):
#       func_name=inspect.stack()[0][3]
##      p=re.compile(s, re.IGNORECASE)
#
#       hits=[]
#       for i in range(len(list)):
#               if re.search(s, list[i], re.IGNORECASE):
#                       hits.append(i)
#
#       if len(hits) > 1:
#               error(func_name,'found more then one hits')
#       elif len(hits) == 0:
#               error(func_name,'pattern not found')
#       else:
#               new_hit=hits[0]
#               return new_hit
#
##get value to a key in file
##if key is not found, error
#def keyval_get(key, delim, filename):
#       func_name=inspect.stack()[0][3]
#
#       lines, num_lines=read_file(filename)
#
#       pattern=key+"[\s,\t]*"+delim
#
#       idx, num_hits=list_indexes_from_pattern(pattern, lines)
#
#       if num_hits > 1:
#               error(func_name,'Flag found more then once, exit, since I do not know what to do')
#
#       elif num_hits==1:
#               i=idx[0]
#               line=lines[i].split('=')
#               if len(line) == 2:
#                       value=line[1]
#                       #do this in order to get rid of some junk
#                       if ',' in value:
#                               value=value.replace(',','')
#                       return value
#
#               else:
#                       error(func_name,'Dont now what to do')
#       elif num_hits==0:
#               return None
#
#
##change value to a key in file
##if key is not found, add it with the new value
##if found more than once, error
#def keyval_change(key, new_value, delim, filename):
#       func_name=inspect.stack()[0][3]
#
#       lines, num_lines=read_file(filename)
#
#       pattern=key+"[\s,\t]*"+delim
#
#       indx, num_hits=list_indexes_from_pattern(pattern, lines)
#
#       if num_hits > 1:
#               error(func_name,'Flag found more then once, exit, since I do not know what to do')
#
#       elif num_hits==1:
#               file=open(filename, "w")
#               for i in range(num_lines):
#                       if i != indx[0]:
#                               file.write("%s\n" % lines[i])
#                       else:
#                               file.write ("%s = %s\n" % (key, new_value))
#               file.close()
#       elif num_hits==0:
#               file=open(filename, "w")
#               if code=='qe':
#                       # now we first need to find the correct block
#                       blocks=[['&control',['calculation','title','restart_mode','wf_collect','nstep','tstress','tprnfor','max_seconds','etot_conv_thr','forc_conv_thr','pseudo_dir']],['&system',['ecutwfc','ecutrho','ecutfock',]],['&electrons',['electron_maxstep']]]
#                       for i in range(len(blocks)):
#                               idx=list_indexes_from_pattern_no_case_excl(blocks[i][0],lines)
#                               blocks[i].append(idx)
#
#                       for i in range(len(blocks)):
#                               for blockkey in blocks[i][1]:
#                                       if blockkey == key.casefold():
#                                               target_block=i
#                                               break
#
#                       for i in range(num_lines):
#                               if i != blocks[target_block][2]:
#                                       file.write("%s\n" % lines[i])
#                               else:
#                                       file.write("%s\n" % lines[i])
#                                       file.write ("%s = %s\n" % (key, new_value))
#               else:
#                       file.write ("%s = %s\n" % (key, new_value))
#                       for i in range(num_lines):
#                               file.write("%s\n" % lines[i])
#               file.close()
#
#
##check if input path yields a file
##check if file is empty
##if input path is a not empty file return true
#def check_file(PATH):
#       if os.path.isfile(PATH):
#               if os.stat(PATH).st_size > 0:
#                       return True
#               else:
#                       return False
#       else:
#               return False
#
#
#
#
#
#def check_queue_for_job(jobid):
#
#       user=os.getenv('USER')
#
#       time.sleep(1)
#
#       while True:
#               p=subprocess.Popen('squeue', stdout=subprocess.PIPE)
#               result=str(p.communicate()[0])
#               lines=result.split('\\n')
#               #check if this split delimeter is different at other clusters!
#
#               hit_jobid, num_hits=list_indexes_from_pattern(jobid,lines)
#
#               if num_hits == 0:
#                       print ("%-30s : %-30s" % ('calculation status', 'finished'))
#                       break
#               elif num_hits == 1:
#                       job_status=lines[hit_jobid[0]]
#                       print (job_status)
#                       job_status=job_status.split()
#                       job_status=job_status[9]
#                       if job_status == cluster_R:
#                               print ("%-30s : %-30s" % ('calculation status', " running"))
#                       elif job_status == cluster_Q:
#                               print ("%-30s : %-30s" % ('calculation status', " queued"))
#                       elif job_status == "E":
#                               print ("%-30s : %-30s" % ('calculation status', "error"))
#
#               else:
#                       error(func_name, 'something strange goes on here')
#               time.sleep(5)
#               # make this time a command option !!!!!!
#
#def use_grep(pattern, path):
#       func_name=inspect.stack()[0][3]
#       p = subprocess.Popen(['grep', pattern, path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=-1)
#       output, error = p.communicate()
#
#       #found
#       if p.returncode == 0:
#               return output
#       #not found
#       elif p.returncode == 1:
#               return False
#       else:
#               assert p.returncode > 1
#               error(func_name, 'something strange with this grep')
#
#
#
##------------------- general function put this in separate file
#
##------------------- QM code related functions put this in separate file
## set some important stuff up depending on the used code
## stuff like input, output files ... 
#def setup_start():
#       func_name=inspect.stack()[0][3]
#       if code == "qe":
#               delim="="
#               cutoff_key='ecutwfc'
#               grid_key='ecutrho'
#               #input
#               if args.input is not None:
#                       input=args.input
#               else:
#                       possible_inputs=glob.glob('*.in')
#                       if len(possible_inputs) > 1:
#                               error(func_name, 'found multiple input files, please specify your input file using the -i option')
#                       else:
#                               input=possible_inputs[0]
#               print ("%-30s : %-30s" % ("input file", input))
#
#               #pseudo potentials
#
#               #input file list
##              file_list=[]
##              file_list.append(input)
##              file_list.append(pbs)
##
## that is probably not worth the effort, as different calcs require different input and so
## on, just copy everything in folder 
#
#               #main output
#               lines, num_lines=read_file(pbs)
#               idx=list_indexes_from_pattern_excl('< *'+str(input),lines)
#               tmp=lines[idx].split()
#               p=re.compile('\.out')
#               for i in range(len(tmp)):
#                       if re.search(p,tmp[i]):
#                               output=tmp[i]
#               try:
#                       output
#               except NameError:
#                       error(func_name,'failed to determine outfile')
#
#               output=re.sub('[>]','',output)
#               print ("%-30s : %-30s" % ("output file", output))
#
#       return input, output, delim, cutoff_key, grid_key
## enforce single-point, 
#def sp(file):
#       # QE
#       if code == "qe":
#               keyval_change('calculation', "'scf'", delim, file)
#               keyval_change('nstep', "1", delim, file)
#
## get kgrid 
## only automatic k-grids supported!
## store as k_gird[kx,ky,kz,wx,wy,wz]
#def kgrid_get(file):
#       kgrid=[]
#       func_name=inspect.stack()[0][3]
#       kgrid=[]
#       # QE
#       if code == "qe":
#               # read file
#               lines, num_lines=read_file(file)
#               # determine start
#               kstart=list_indexes_from_pattern_excl('K_POINTS',lines)
#               # get mode 
#               tmp=lines[kstart].split()
#               mode = tmp[1]
#               kmode_a=re.compile('(?i)auto')
#               kmode_g=re.compile("(?i)gamma")
#               
#               if re.search(kmode_a, mode):
#                       tmp=lines[kstart+1].split()
#                       kgrid.append(int(tmp[0]))
#                       kgrid.append(int(tmp[1]))
#                       kgrid.append(int(tmp[2]))
#                       kgrid.append(int(tmp[3]))
#                       kgrid.append(int(tmp[4]))
#                       kgrid.append(int(tmp[5]))
#               elif re.search(kmode_g, mode):
#                       kgrid.append(1)
#                       kgrid.append(1)
#                       kgrid.append(1)
#                       kgrid.append(1)
#                       kgrid.append(1)
#                       kgrid.append(1)
#               else:
#                       error(func_name, 'do not know this mode')
#
#               return mode, kgrid
#
## write kgrid 
#def kgrid_write(file):
#       func_name=inspect.stack()[0][3]
#       # QE
#       if code == "qe":
#               # read file
#               lines, num_lines=read_file(file)
#               kstart=list_indexes_from_pattern_excl('K_POINTS',lines)
#               outfile=open(file, "w")
#               for i in range(num_lines) :
#                       if i != kstart+1 :
#                               outfile.write ("%s \n" % lines[i])
#                       elif i == kstart+1 :
#                               for j in range(len(kgrid)):
#                                       outfile.write ("%-s " % str(kgrid[j]))
#                                       if j == len(kgrid)-1:
#                                               outfile.write ("%-s \n" % str(kgrid[j]))
#               outfile.close()
##def cp_files(path):
##      for file in file_list:
##              if os.path.exists('./'+str(file)) == True:
##                      shutil.copy(file, path)
##                      if os.path.exists('./'+path+'/'+str(file)) == False:
##                              error(func_name, 'something went wrong during copying files')
##              else:
##                      error(func_name, 'oh uh, cannot find required input file')
#
#def cp_all_files(dest):
#       print ("%-30s : " % ("copying files"))
#       for file in glob.glob("*"):
#               if os.path.isfile(file):
#                       print (file)
#                       shutil.copy(file, dest)
#       printline(60)
#
#def is_converged(file):
#       func_name=inspect.stack()[0][3]
#       if code == "qe":
#               lines, num_lines=read_file(file)
#               hits, n_hits=list_indexes_from_pattern('JOB DONE',lines)
#               if n_hits != 1:
#                       return False
#               else:
#                       hits, n_hits=list_indexes_from_pattern('convergence has been achieved in',lines)
#                       if n_hits != 1:
#                               return False
#                       else:
#                               return True
#
#def is_old(path):
#       func_name=inspect.stack()[0][3]
#       # check if path exists and is not empty
#       if os.path.isdir(path) == True:
#               # if yes check if outfile is found (code specific)
#               if os.path.exists(path+'/'+output) == True:
#                       # if yes check for convergence message (code specific)
#                       if is_converged(path+'/'+output) == True:
#                               print ("%-30s : %-30s" % ("calculation status", "already calculated"))
#                               return True
#                       else:
#                               error(func_name,'found some parts of an old calculation, require user care')
#               else:
#                       error(func_name,'found some parts of an old calculation, require user care')
#       else:
#               print ("%-30s : %-30s" % ('calculation status', 'new calc'))
#               return False
#
#
##qsub calc
#       # check for old calc
#       # if not found, submit
#       # after job is done, check calc
#def qsub(path):
#       func_name=inspect.stack()[0][3]
#       # qsub
#       os.chdir(path)
#       subprocess.call(['pwd'])
#
#       command=cluster_qsub+' '+pbs
#       out=subprocess.check_output(command, shell=True)
#       out=out.split()
#       jobid = str(out[3])
#       jobid=(jobid.lstrip(cluster_id_lstrip))
#       jobid=(jobid.rstrip(cluster_id_rstrip))
#       print ("%-30s : %-30s" % ("jobid", jobid))
#
#       os.chdir(workdir)
#       check_queue_for_job(jobid)
#
#       if is_converged(path_output) == True:
#               print ("%-30s : %-30s" % ("new calculation", "Done"))
#       else:
#               error(func_name,'Calculation not Converged')
#
#def energy_get(file):
#       func_name=inspect.stack()[0][3]
#       # QE
#       if code == "qe":
#               command="grep '!    total energy ' "+file
#               tmp=subprocess.check_output(command, shell=True)
#               tmp=tmp.split()
#               energy_Ry=float(tmp[4])
#               energy=energy_Ry*Ry2eV
#               return energy
#
## add 1 into every direction, except only one or only two start entries were 1, in that case
## assume 2d (1d) system and add only into the other directions
#def kgrid_increase():
##      kgrid[0]=2
##      kgrid[1]=2
##      kgrid[2]=2
#       if (kgrid[0] != 1 and kgrid[1] != 1 and kgrid[2] != 1 
#               or kgrid[0] == kgrid[1] == kgrid[2] == 1):
#               print ("%-30s : %-30s" % ("k-point increase", 'normal'))
#               for i in range(3):
#                       kgrid[i]=kgrid[i]+incr
#               print ("%-30s : %-9i x %-9i x %-9i" % ('new k grid:', kgrid[0], kgrid[1], kgrid[2]))
#
#       else:
#               print ("%-30s : %-30s" % ("k-point increase", '1D/2D dystem detected'))
#               for i in range(3):
#                       if kgrid[i] != 1:
#                               kgrid[i]=kgrid[i]+incr
#               print ("%-30s : %-i x %-9i x %-9i" % ('new k grid:', kgrid[0], kgrid[1], kgrid[2]))
#
#
#def nk_get():
#       func_name=inspect.stack()[0][3]
#       if code == "qe":
#               command="grep 'number of k points=' "+path_output
#               tmp=subprocess.check_output(command, shell=True)
#               tmp=tmp.split()
#               nk=int(tmp[4])
#               return nk
#
##------------------- QM code related functions put this in separate file
#
#
#
#
##================================================================================================
## START: grid_test
##================================================================================================
#
## do the same thing as kpt
#
#e_thr=0.01 # eV this is !
#func='grid_test'
#
#
## select code
## well here the functionality would come in, probably as option that is passed
#
#
#parser = argparse.ArgumentParser()
#parser.add_argument("-c","--code", choices=["qe"], help="specify the QM package, choose from list [qe=Quantum Espresso]", type=str,default="qe")
#parser.add_argument("-i","--input", help="specify the input file to set the energy opt_param_value", type=str)
#parser.add_argument("-p","--pbs", help="specify the pbs-file to run the job", type=str, default="pbs")
#parser.add_argument("-o","--output", help="specify the name of the output file", type=str,
#default="conv")
#parser.add_argument("-incr","--increment", 
#help="specify how much you want the grid to be increased in each step (Ry right now)",
#type=int)
#args = parser.parse_args()
#
#if check_file("./"+str(args.pbs)) == False:
#       error(func_name, 'found no pbs file, please specify your pbs file using the -p option')
#else:
#       pbs=args.pbs
#print ("%-30s : %-30s" % ("pbs file", pbs))
#
#outprefix=args.output
#code=args.code
#
#printline(60)
#
## establish workdir
#workdir=os.getcwd()
#
## define input
#input, output, delim, cutoff_key, grid_key =setup_start()
#
##opt_param is what we want to optimize here
#opt_param=grid_key
#
##get increment
#cutoff=float(keyval_get(cutoff_key,delim,input))
#incr=cutoff
#
## get value
#if keyval_get(opt_param,delim,input) is None:
#       warning('main',opt_param+' not found, using default')   
#       if code == "qe":
#               opt_param_value=4*cutoff
#else:
#       opt_param_value=float(keyval_get(opt_param,delim,input))
#
#opt_param_value_print=str(int(float(opt_param_value)))
#print ("%-30s : %-30s" % ('input '+opt_param, opt_param_value))
#opt_param_values=[]
#energies=[]
#errors_energy=[]
#
#loop=0
#while True:
#
#       if loop > 0:
#
#               opt_param_value=opt_param_value+incr
#               opt_param_value_print=str(int(float(opt_param_value)))
#               print ("%-30s : %-30s" % ('new '+opt_param, opt_param_value))
#
#       opt_param_values.append(opt_param_value)
#       # setup path
#       path='./'+func+'/'+opt_param_value_print
#
#       path_input=path+'/'+input
#       path_output=path+'/'+output
#
#       # check for old calc
#       if is_old(path) == False:
#               subprocess.call(['mkdir','-p', path])
#
#               # copy files (code specific) well, not any more
#               cp_all_files(path)
#
#               # change parameter
#               keyval_change(opt_param, opt_param_value, delim, path_input)
#
#               # enforce single-point, 
#               sp(path_input)
#
#               # compute
#               qsub(path)
#
#       # evaluate energy and grid 
#       energy=energy_get(path_output)
#       energies.append(energy)
#       
#       if loop > 0:
#
#               error_energy=math.fabs(energies[loop]-energies[loop-1]) 
#               errors_energy.append(error_energy)
#
#               if error_energy < e_thr:
#                       loop_conv=loop-1
#                       print ("%-30s : %-30s" % ('error in total energy ', error_energy))
#                       print ("%-30s : %-30s" % ('convergence in step ', loop_conv))
#                       printline(60)
#                       print ("%-30s : %-30s" % ('converged '+str(opt_param), opt_param_values[loop_conv]))
#                       errors_energy.append('0.0')
#                       loop=loop+1
#                       break
#               else:
#                       print ("%-30s : %-30s" % ('error in total energy ', error_energy))
#
#       loop=loop+1
#
#file='./'+func+'/'+outprefix+".dat"
#outfile=open(file, "w")
#outfile.write ("%-30s %-30s %-30s %-30s \n" % ('step', str(opt_param)+' / Ry', 'energy / eV', \
#'energy error / eV'))
#
#steps=[]
#for i in range(loop):
#       outfile.write ("%-30s %-30s %-30s %-30s \n" % (i, opt_param_values[i], energies[i],
#       errors_energy[i]))
#       steps.append(i)
#
#outfile.close()
#
## no point in plotting it when there is only one data point...
#if loop_conv>0:
#       plt.plot(opt_param_values, errors_energy, marker='o')
#       plt.xlabel(str(opt_param_value)+' / Ry')
#       plt.ylabel('Delta E0 / eV')
#       plt.ylim([0,0.1])
#       plt.xlim([opt_param_values[0],opt_param_values[loop_conv]])
#       plt.axhline(e_thr,color='red',linestyle='dashed')
#       plt.savefig('./'+func+'/'+outprefix+".png")
#       plt.show()
##================================================================================================
## END: opt_param_value_test
##================================================================================================
#
