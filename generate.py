# 17/01/2022
# SP - Script to genereate psp without NLCC in psp8 and upf format
# 25/09/2025 - update to get FR LDA with PW. One need to update oncvpsp-4.0.1/src/upfout_r.f90 and upfout.f90
# with
# else if(iexc==-001012) then
#     write(6,'(t8,a)') &
#&        'functional="SLA  PW   NOGX NOGC"'

import numpy as np
import os

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
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-s_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-sp_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-spd_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-fsp_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-d_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-low_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-high_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-sp-high_r.in && cd ../')
#    os.system('cd '+str(elements[ii])+'/ && sed -i \'s/4 both/-001012 both/g\' '+str(elements[ii])+'-spd-high_r.in && cd ../')

# Run and copy
for ii in np.arange(nb):
    input = str(elements[ii])+'_r.in'
    output = str(elements[ii])+'_r.out'
    psp8 = str(elements[ii])+'_r.psp8'
    upf = str(elements[ii])+'_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-s_r.in'
    output = str(elements[ii])+'-s_r.out'
    psp8 = str(elements[ii])+'-s_r.psp8'
    upf = str(elements[ii])+'-s_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-sp_r.in'
    output = str(elements[ii])+'-sp_r.out'
    psp8 = str(elements[ii])+'-sp_r.psp8'
    upf = str(elements[ii])+'-sp_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-spd_r.in'
    output = str(elements[ii])+'-spd_r.out'
    psp8 = str(elements[ii])+'-spd_r.psp8'
    upf = str(elements[ii])+'-spd_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-fsp_r.in'
    output = str(elements[ii])+'-fsp_r.out'
    psp8 = str(elements[ii])+'-fsp_r.psp8'
    upf = str(elements[ii])+'-fsp_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-d_r.in'
    output = str(elements[ii])+'-d_r.out'
    psp8 = str(elements[ii])+'-d_r.psp8'
    upf = str(elements[ii])+'-d_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-low_r.in'
    output = str(elements[ii])+'-low_r.out'
    psp8 = str(elements[ii])+'-low_r.psp8'
    upf = str(elements[ii])+'-low_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )

for ii in np.arange(nb):
    input = str(elements[ii])+'-high_r.in'
    output = str(elements[ii])+'-high_r.out'
    psp8 = str(elements[ii])+'-high_r.psp8'
    upf = str(elements[ii])+'-high_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-sp-high_r.in'
    output = str(elements[ii])+'-sp-high_r.out'
    psp8 = str(elements[ii])+'-sp-high_r.psp8'
    upf = str(elements[ii])+'-sp-high_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )


for ii in np.arange(nb):
    input = str(elements[ii])+'-spd-high_r.in'
    output = str(elements[ii])+'-spd-high_r.out'
    psp8 = str(elements[ii])+'-spd-high_r.psp8'
    upf = str(elements[ii])+'-spd-high_r.upf'
    if (os.path.isfile(str(elements[ii])+'/'+input)):
      os.system('cd '+str(elements[ii])+'/ && /home/ponce/program/oncvpsp-4.0.1/src/oncvpspr.x < '+input+' > '+output+' && awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSPCODE8/{out=1}\' '+output+' > '+psp8+' &&  awk \'BEGIN{out=0};/END_PSP/{out=0} {if(out == 1) {print}};/PSP_UPF/{out=1}\' '+output+' >  '+upf+' && cd ../' )





