# 19/10/2023
# SP - Script to genereate psp with LDA in psp8 and upf format

import numpy as np
import os

#oncvpsp_dir = "/home/ponce/program/oncvpsp-4.0.1/"
oncvpsp_dir = "/Users/mverstra/CODES/ONCVPSP/oncvpsp_libxc6/src/"
binary = "oncvpspr.x"
oncvpsp_path = oncvpsp_dir+binary

elements = ['Ag','Al','Ar','As','At','Au','Ba','Be','B','Bi','Br',
'Ca','Cd','Ce','C','Cl','Co','Cr','Cs','Cu','Dy','Er','Eu','Fe',
'F','Ga','Gd','Ge','He','Hf','H','Hg',
'Ho','I','In','Ir','K','Kr','La','Li',
'Lu','Mg','Mn','Mo','Na','Nb','Nd','Ne',
'N','Ni','O','Os','Pb','Pd','P','Pm','Po','Pr','Pt',
'Rb','Re','Rh','Rn','Ru','Sb','Sc','Se',
'S','Si','Sm','Sn','Sr','Ta','Tb','Tc',
'Te','Ti','Tl','Tm','V','W','Xe','Yb',
'Y','Zn','Zr']

nb = len(elements)

# Update input files
#for ii in np.arange(100):
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-sp_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-spd_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-fsp_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-d_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-low_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-high_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-sp-high_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/3 both/g\' '+str(elements[ii])+'-spd-high_r.in && cd ../')

# Run and copy
for ii in np.arange(nb):
    input = str(elements[ii])+'_r.in'
    output = str(elements[ii])+'.out'
    psp8 = str(elements[ii])+'.psp8'
    upf = str(elements[ii])+'.upf' 
    if (os.path.isfile(str(elements[ii])+'/'+input)):  
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+' < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-sp_r.in'
    output = str(elements[ii])+'-sp.out'
    psp8 = str(elements[ii])+'-sp.psp8'
    upf = str(elements[ii])+'-sp.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+' < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-spd_r.in'
    output = str(elements[ii])+'-spd.out'
    psp8 = str(elements[ii])+'-spd.psp8'
    upf = str(elements[ii])+'-spd.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+' < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-fsp_r.in'
    output = str(elements[ii])+'-fsp.out'
    psp8 = str(elements[ii])+'-fsp.psp8'
    upf = str(elements[ii])+'-fsp.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-d_r.in'
    output = str(elements[ii])+'-d.out'
    psp8 = str(elements[ii])+'-d.psp8'
    upf = str(elements[ii])+'-d.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )
    
for ii in np.arange(nb):
    input = str(elements[ii])+'-low_r.in'
    output = str(elements[ii])+'-low.out'
    psp8 = str(elements[ii])+'-low.psp8'
    upf = str(elements[ii])+'-low.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-high_r.in'
    output = str(elements[ii])+'-high.out'
    psp8 = str(elements[ii])+'-high.psp8'
    upf = str(elements[ii])+'-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-sp-high_r.in'
    output = str(elements[ii])+'-sp-high.out'
    psp8 = str(elements[ii])+'-sp-high.psp8'
    upf = str(elements[ii])+'-sp-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-spd-high_r.in'
    output = str(elements[ii])+'-spd-high.out'
    psp8 = str(elements[ii])+'-spd-high.psp8'
    upf = str(elements[ii])+'-spd-high.upf'    
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && '+oncvpsp_path+'< '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )





