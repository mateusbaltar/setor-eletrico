import os
import shutil

pst_smp = [1,6,14,17,18,24,25,31,33,47,57,61,63,71,73,74,77,92,93,102,117,119,
           156,158,160,161,205,209,211,215,216,220,237,239,242,266,270,286]

pst_pvv = [[34, "INC"], [98, "INC"], [99, "INC"], [101, "INC"], [111, "NAT"], [115, "INC"], [120, "INC"],
           [121, "INC"], [125, "NAT"], [130, "NAT"], [134, "INC"], [144, "NAT"], [145, "INC"], [149, "INC"],
           [168, "PVV"], [188, "NAT"], [190, "INC"], [196, "INC"], [197, "INC"], [201, "INC"], [229, "NAT"],
           [243, "INC"], [245, "INC"], [246, "PVV"], [247, "INC"], [254, "INC"], [255, "INC"], [257, "NAT"],
           [259, "INC"], [262, "INC"], [269, "INC"], [271, "NAT"], [275, "NAT"], [277, "INC"], [278, "INC"],
           [279, "INC"], [280, "NAT"], [281, "NAT"], [283, "INC"], [287, "NAT"], [288, "INC"], [290, "INC"],
           [291, "INC"], [294, "INC"], [295, "INC"], [296, "INC"]]

def pvv_up(posto, ano, semana, vq):
    fnin_inp = os.path.join(os.getcwd(), "Previvaz_In", str(posto) + ".inp")
    fnin_str = os.path.join(os.getcwd(), "Previvaz_In", str(posto) + "_str.dat")
    fnout_inp = os.path.join(os.getcwd(), "Previvaz_Out", str(posto) + ".inp")
    fnout_str = os.path.join(os.getcwd(), "Previvaz_Out", str(posto) + "_str.dat")
    if (os.path.exists(fnin_inp) and os.path.exists(fnin_str)):
        pvv_file = open(fnin_str, 'rt')
        pvv_lns = pvv_file.readlines()
        pvv_file.close()
        for i in range(0, len(vq)):
            if semana + i > 52:
                s_tmp = semana + i -52
                a_tmp = ano + 1
            else:
                s_tmp = semana + i
                a_tmp = ano
            ano_ini = int(pvv_lns[1][1:5])
            ano_fim = int(pvv_lns[1][6:10])
            col_ano = (s_tmp - 1) % 9
            ln_ano = (s_tmp - 1) // 9
            ln_f = ((a_tmp - ano_ini) * 6) + 2 + ln_ano
            ln_idx_ini = col_ano * 8
            if ln_f == len(pvv_lns) - 1:
                pvv_lns.append("")
            if pvv_lns[ln_f].strip() == "":
                if ln_ano == 5:
                    pvv_lns.insert(ln_f, "      0.      0.      0.      0.      0.      0.      0.\n")
                else:
                    pvv_lns.insert(ln_f, "      0.      0.      0.      0.      0.      0.      0.      0.      0.    " + str(a_tmp) + "\n")
            pvv_lns[ln_f] = pvv_lns[ln_f][:ln_idx_ini] + ("       " + str(vq[i]))[-7:] + "." + pvv_lns[ln_f][ln_idx_ini + 8:]
        pvv_lns[1] = pvv_lns[1][:6] + str(a_tmp) + pvv_lns[1][10:]
        #fn_str = os.path.join(os.getcwd(), pvv_path, str(posto) + "_str_.dat")
        pvv_file = open(fnout_str, 'wt')
        for ln_idx in range(0, len(pvv_lns)):
            pvv_file.write(pvv_lns[ln_idx])
        pvv_file.close()
        # Edita o arquivo .inp
        pvv_file = open(fnin_inp, 'rt')
        pvv_lines = pvv_file.readlines()
        pvv_file.close()
        #fn_inp = os.path.join(os.getcwd(), pvv_path, str(posto) + "_.inp")
        pvv_file = open(fnout_inp, 'wt')
        s_tmp += 1
        if s_tmp > 52:
            s_tmp = 1
            a_tmp = a_tmp + 1
        for ln in range(0, len(pvv_lines)):
            if (ln == 8):
                pvv_file.write(str(s_tmp) + "\n")
            elif (ln == 9):
                pvv_file.write(str(a_tmp) + "\n")
            elif (ln == 12):
                pvv_file.write(str(a_tmp - 1) + "\n")
            else:
                pvv_file.write(pvv_lines[ln])
        pvv_file.close()
    else:
        print("pvv_up() - Posto não encontrado:", posto)

# Atualiza os arquivos do previvaz com os postos do Smap
file = open(os.path.join(os.getcwd(), "smp_q_sem.csv"), 'rt')
fl = file.readlines()
file.close()
l_idx = 0
smpv = []
for l in range(0, len(fl)):
    ls = fl[l].split(";")
    smpv.append([])
    for c in range(0, len(ls)):
        if c == len(ls) - 1:
            if ls[c].strip() != "":
                smpv[l_idx].append(ls[c].strip())
        else:
            smpv[l_idx].append(ls[c].strip())
    l_idx += 1
ai = int(smpv[0][1][3:7])
si = int(smpv[0][1][0:2])
for p in pst_smp:
    found = 1
    for a in range(1, len(smpv)):
        if(int(smpv[a][0]) == p):
            vt = []
            for b in range(1, len(smpv[a])):
                vt.append(int(smpv[a][b]))
            pvv_up(p, ai, si, vt)
            found = 0
    if found:
        print("pvv() - Posto não encontrado:", p)

# Atualiza os arquivos do previvaz com os postos do Acomph
file = open(os.path.join(os.getcwd(), "acomph_q_s.csv"), 'rt')
fl = file.readlines()
file.close()
l_idx = 0
smpv = []
for l in range(0, len(fl)):
    ls = fl[l].split(";")
    smpv.append([])
    for c in range(0, len(ls)):
        if c == len(ls) - 1:
            if ls[c].strip() != "":
                smpv[l_idx].append(ls[c].strip())
        else:
            smpv[l_idx].append(ls[c].strip())
    l_idx += 1
ai = int(smpv[0][2][3:7])
si = int(smpv[0][2][0:2])
for p in pst_pvv:
    found = 1
    for a in range(1, len(smpv)):
        if int(smpv[a][0]) == int(p[0]) and smpv[a][1] == p[1]:
            vt = []
            for b in range(2, len(smpv[a])):
                vt.append(int(round(float(smpv[a][b].replace(",", ".")), 0)))
            pvv_up(p[0], ai, si, vt)
            found = 0
    if found:
        print("pvv() - Posto não encontrado:", p)


# Copia os arquivos .lim pra pasta de saída
folder_list = os.listdir(os.path.join(os.getcwd(), "Previvaz_In"))
for fn in folder_list:
    if fn[-4:].lower() == '.lim':
        pth_1 = os.path.join(os.getcwd(), "Previvaz_In", fn)
        pth_2 = os.path.join(os.getcwd(), "Previvaz_Out", fn)
        shutil.copyfile(pth_1, pth_2)



