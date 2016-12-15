# Author: Ahmed mahmoud 8/10/2016
# parse  outputted json file to output variants with specific coverage and frequency thresholds.
import json, os, sys, csv,shutil
from Tkinter import *
import Tkinter as tk




master = Tk()
cwgt=Canvas(master)
cwgt.pack(expand=True, fill=BOTH)

##############################################################################
###############loads file and accepts parameters from user input##############
def openfile():
   filename = tkFileDialog.askopenfilename(parent=cwgt,title='Choose a file')
   custName.set(filename)

custName = StringVar(None)
initname = Entry(cwgt, textvariable=custName)
initname.grid(column=1,row=0)

Button(cwgt, text='Browse', command=openfile).grid(row=0)
Label(cwgt, text=" Minumum Coverage Threshold:").grid(row=1)
Label(cwgt, text=" Minumum Frequency for NS5:").grid(row=2)
Label(cwgt, text=" Minumum Frequency for NS3:").grid(row=3)

e2 = Entry(cwgt)
e3 = Entry(cwgt)
e4 = Entry(cwgt)

e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

cov = e2.get()
NS5freq = e3.get()
NS3freq = e4.get()
###############################################################################
def quit_script():
   master.destroy()
   sys.exit()
###############################################################################
### Calculates percentages for variants from json and Parses based on region,##
#### cov and frequency#########################################################
def run():
    print initname.get()
    print e2.get()
    print e3.get()
    f = open(initname.get())
    data = json.load(f)
    f.close()
    out = open('/PATH_TO_DIRECTORY/file.csv', 'wb+')
    f = csv.writer(out)
    i = csv.reader(out)
    for item in data:
        f.writerow( [item['accept'], item['pValue'],item['amplicon'], item['genotype'], item['pos'],item['aaChange'], item['totalCover'], item['refCover'], item['altCover']])
    out.close()
    outs = open ('/PATH_TO_DIRECTORY/file.csv', 'r')
    outz = open('/PATH_TO_DIRECTORY/data_percentage.csv', 'w')
    i = csv.reader(outs)
    o = csv.writer(outz)
    for row in i:
        percentage = float((float(row[8])/float(row[6])))
        o.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],float(percentage)])
    outz.close()
    datapin = open ('/PATH_TO_DIRECTORY/data_percentage.csv', 'r')
    datapout_NS5A = open('/PATH_TO_DIRECTORY/"NS5A_1a.csv', 'w')
    datapout_NS5B = open('/PATH_TO_DIRECTORY/NS5B_1a.csv', 'w')
    datapout_NS3 = open('/PATH_TO_DIRECTORY/NS3_1a.csv', 'w')
    datapout_NS5A1b = open('/PATH_TO_DIRECTORY/NS5A_1b.csv', 'w')
    datapout_NS5B1b = open('/PATH_TO_DIRECTORY/NS5B_1b.csv', 'w')
    datapout_NS31b = open('/PATH_TO_DIRECTORY/NS3_1b.csv', 'w')
    datapin_NS5A = open('/PATH_TO_DIRECTORY/"NS5A_1a.csv', 'r')
    datapin_NS5B = open('/PATH_TO_DIRECTORY/NS5B_1a.csv', 'r')
    datapin_NS3 = open('/PATH_TO_DIRECTORY/NS3_1a.csv', 'r')
    datapin_NS5A1b = open('/PATH_TO_DIRECTORY/NS5A_1b.csv', 'r')
    datapin_NS5B1b = open('/PATH_TO_DIRECTORY/NS5B_1b.csv', 'r')
    datapin_NS31b = open('/PATH_TO_DIRECTORY/NS3_1b.csv', 'r')
    ins = csv.reader(datapin)
    outfile = csv.writer(datapout_NS5A)
    outfile2 = csv.writer(datapout_NS5B)
    outfile3 = csv.writer(datapout_NS3)
    outfile4 = csv.writer(datapout_NS5A1b)
    outfile5 = csv.writer(datapout_NS5B1b)
    outfile6 = csv.writer(datapout_NS31b)

#################Filter by genotype #######################################
    def parse(genotype,coverage, varfrequency,fileout):
        if row[2] == genotype and row[6] >= coverage and float(row[9]) >= varfrequency:
            outfile = csv.writer(fileout)
            outfile.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]])
            print [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]

    for row in ins:
        parse ("AMP_G1a_NS5A",int(e2.get()),float(e3.get()),datapout_NS5A)
        parse ("AMP_G1a_NS5B",int(e2.get()),float(e3.get()),datapout_NS5B)
        parse ("AMP_G1a_NS3",int(e2.get()),float(e4.get()),datapout_NS3)
        parse ("AMP_G1b_NS5A",int(e2.get()),float(e3.get()),datapout_NS5A1b)
        parse ("AMP_G1b_NS3",int(e2.get()),float(e4.get()),datapout_NS31b)
        parse ("AMP_G1b_NS5B",int(e2.get()),float(e3.get()),datapout_NS5B1b)

###############Dictionary for Drug Resistance###############################
###############To be declared by USER ######################################
    NS31amuts = { <NS31A dictionary>}
    NS31bmuts = {<NS31b Dictionary>}
    NS34muts = {<NS3 genotype 4 Dictionary>}
    NS5A1amuts = {<NS5A1a dictionary>}
    NS5A1bmuts = {<NS5A1b dictionary>}
    NS5B1amuts = {<NS5B1a Dictionary}
    NS5B1bmuts = {<N5b 1b Dictionary>}
############################################################################


    datapin.close()
    datapout_NS5A.close()
    datapout_NS5B.close()
    datapout_NS3.close()
    datapout_NS5A1b.close()
    datapout_NS5B1b.close()
    datapout_NS31b.close()


    datapout_NS5Afinal = open('/PATH_TO_DIRECTORY/NS5A_1afinal.csv', 'w')
    datapout_NS5Bfinal = open('/PATH_TO_DIRECTORY/NS5B_1afinal.csv', 'w')
    datapout_NS3final = open('/PATH_TO_DIRECTORY/NS3_1afinal.csv', 'w')
    datapout_NS5A1bfinal = open('/PATH_TO_DIRECTORY/NS5A_1bfinal.csv', 'w')
    datapout_NS5B1bfinal = open('/PATH_TO_DIRECTORY/NS5B_1bfinal.csv', 'w')
    datapout_NS31bfinal = open('/PATH_TO_DIRECTORY/NS3_1bfinal.csv', 'w')

############## Drug Interpretation ############################################
    def mut(filetoberead, filetobewritten):
       mutcsv = csv.reader(filetoberead)
       out = csv.writer(filetobewritten)
       for row in mutcsv:
          if row[3] == "1a" and str(row[5]) in NS31amuts:
             print(row[5],NS31amuts[str(row[5])])
             out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS31amuts[str(row[5])]])
          elif row[3] == "1b" and str(row[5]) in NS31bmuts:
              print(row[5],NS31bmuts[str(row[5])])
              out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS31bmuts[str(row[5])]])
          elif row[3] == "1a" and str(row[5]) in NS5A1amuts:
              print(row[5],NS5A1amuts[str(row[5])])
              out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS5A1amuts[str(row[5])]])
          elif row[3] == "1a" and str(row[5]) in NS5A1bmuts:
              print(row[5],NS5A1bmuts[str(row[5])])
              out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS5A1bmuts[str(row[5])]])
          elif row[3] == "1a" and str(row[5]) in NS5B1amuts:
              print(row[5],NS5B1amuts[str(row[5])])
              out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS5B1amuts[str(row[5])]])
          elif row[3] == "1b" and str(row[5]) in NS5B1bmuts:
              print(row[5],NS5B1bmuts[str(row[5])])
              out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],NS5B1bmuts[str(row[5])]])
          else:
             out.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]])


    mut(datapin_NS5A,datapout_NS5Afinal)
    mut(datapin_NS5B,datapout_NS5Bfinal)
    mut(datapin_NS3,datapout_NS3final)
    mut(datapin_NS5A1b,datapout_NS5A1bfinal)
    mut(datapin_NS5B1b,datapout_NS5B1bfinal)
    mut(datapin_NS31b,datapout_NS31bfinal)
    datapout_NS5Afinal.close()
    datapout_NS5Bfinal.close()
    datapout_NS3final.close()




Button(cwgt, text='Quit', command=quit_script).grid(row=20, column=0, sticky=W, pady=4)
Button(cwgt, text='Parse', command=run).grid(row=20, column=1, sticky=W, pady=4)
master.minsize(800,400)
mainloop( )

