import os
import datetime

smp_inc_pst = []
smp_inc_q = []

d_acph = "20200218"
d_smap = "20200218"

#Funções auxiliares


def dt_delta(di, df):
    # Retorna a diferença, em dias, entre duas datas passadas no formato YYYYMMDD
    d_tmp = datetime.datetime(int(df[0:4]), int(df[4:6]), int(df[6:8])) - datetime.datetime(int(di[0:4]), int(di[4:6]), int(di[6:8]))
    return d_tmp.days + 1

def dt_offset(d, ofst):
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=+ofst)
    return d_tmp.strftime("%Y%m%d")

def dt_conv_smn(d, ofst = 0):
    # Converte p/ número da semana uma data passada no formato YYYYMMDD
    # ofst = offset dado em dias
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    d1 = d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + 6)
    di = datetime.datetime(d1.year, 1, 1)
    d2 = di + datetime.timedelta(days=-wd[di.weekday()])
    return [((d1 - d2).days // 7) + 1, d1.year]

def dt_get_so_ini(d, ofst = 0):
    # Retorna o inicio da SO de uma data passada no formato YYYYMMDD
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    return (d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()])).strftime("%Y%m%d")

def dt_hdr(d, ofst = 0):
    d_tmp = dt_conv_smn(d, ofst)
    return str(d_tmp[0]) + "_" + str(d_tmp[1])

def avr(val):
    #Calcula média aritimética dos elementos de uma matriz
    avr = 0
    for x in val:
        avr += x
    return round(avr/len(val), 2)

def opr(a1, a2, op):
    #Realiza operações aritméticas entre vetores e/ou constante
    ret = []
    if (len(a1) == len(a2)):
        if (op == "+"):
            for i in range(0, len(a1)):
                ret.append(a1[i] + a2[i])
        elif (op == "-"):
            for i in range(0, len(a1)):
                ret.append(a1[i] - a2[i])
        elif (op == "*"):
            for i in range(0, len(a1)):
                ret.append(a1[i] * a2[i])
        elif (op == "/"):
            for i in range(0, len(a1)):
                ret.append(a1[i] / a2[i])
    elif (len(a1) == 1):
        if (op == "+"):
            for i in range(0, len(a2)):
                ret.append(a1[0] + a2[i])
        elif (op == "-"):
            for i in range(0, len(a2)):
                ret.append(a1[0] - a2[i])
        elif (op == "*"):
            for i in range(0, len(a2)):
                ret.append(a1[0] * a2[i])
        elif (op == "/"):
            for i in range(0, len(a2)):
                ret.append(a1[0] / a2[i])
    elif (len(a2) == 1):
        if (op == "+"):
            for i in range(0, len(a1)):
                ret.append(a1[i] + a2[0])
        elif (op == "-"):
            for i in range(0, len(a1)):
                ret.append(a1[i] - a2[0])
        elif (op == "*"):
            for i in range(0, len(a1)):
                ret.append(a1[i] * a2[0])
        elif (op == "/"):
            for i in range(0, len(a1)):
                ret.append(a1[i] / a2[0])
    else:
        print("Erro opr(): Arrays com tamanhos diferente para calculo.")
    return ret

def tmp_vg(v1, t):
    #Calcula vazão para um dado "tempo de viagem" da água
    otp = []
    dias = int((t//24)) + 1
    p1 = t % 24
    p2 = 24 - p1
    if t > 0:
        for a in range(0, dias):
            otp.append(0)
        for i in range(dias, len(v1)):
            otp.append(((v1[i - dias] * p1) + (v1[i - dias + 1] * p2))/24)
        return otp
    else:
        return v1

def pxv(v, op):
    if op == ",":
        if "." in v:
            return v.replace(".", ",")
        else:
            return v
    elif op == ".":
        if "," in v:
            return v.replace(",", ".")
        else:
            return v
    else:
        print("Erro pxv()")
        exit(0)

#Funções Smap
def smp_read_sbb(sbb, dti, dtf):
    smp_path = "Smap"
    #Faz a leitura nos arquivos de saída do SMAP da vazão incremental da sub-bacia passada como argumento
    if(sbb == "AVERMELHA" or sbb == "CAMARGOS" or sbb == "CAPESCURO" or sbb == "EDACUNHA" or sbb == "FURNAS" or sbb == "MARIMBONDO" or sbb == "PARAGUACU" or sbb == "PASSAGEM" or sbb == "PBUENOS" or sbb == "PCOLOMBIA" or sbb == "FUNIL MG"):
        bc = "Grande"
    elif(sbb == "FOA" or sbb == "JORDSEG" or sbb == "SCAXIAS" or sbb == "STACLARA" or sbb == "UVITORIA"):
        bc = "Iguacu"
    elif (sbb == "BALSA" or sbb == "FLOR+ESTRA" or sbb == "ITAIPU" or sbb == "IVINHEMA" or sbb == "PTAQUARA"):
        bc = "Itaipu"
    elif (sbb == "CORUMBA1" or sbb == "CORUMBAIV" or sbb == "EMBORCACAO" or sbb == "ITUMBIARA" or sbb == "NOVAPONTE" or sbb == "RVERDE" or sbb == "SDOFACAO" or sbb == "SSIMAO2"):
        bc = "Paranaiba"
    elif (sbb == "CANOASI" or sbb == "CAPIVARA" or sbb == "CHAVANTES" or sbb == "JURUMIRIM" or sbb == "MAUA" or sbb == "ROSANA"):
        bc = "Paranapanema"
    elif (sbb == "QM" or sbb == "RB-SMAP" or sbb == "SFR2" or sbb == "SRM2" or sbb == "TM-SMAP"):
        bc = "SaoFrancisco"
    elif (sbb == "BBONITA" or sbb == "ESOUZA" or sbb == "IBITINGA" or sbb == "NAVANHANDA"):
        bc = "Tiete"
    elif (sbb == "SMESA"):
        bc = "Tocantins"
    elif (sbb == "BG" or sbb == "CN" or sbb == "FOZCHAPECO" or sbb == "ITA" or sbb == "MACHADINHO" or sbb == "MONJOLINHO" or sbb == "QQUEIXO" or sbb == "SJOAO"):
        bc = "Uruguai"
    #Leitura arquivo de entrada
    f_tmp = open(os.path.join(os.getcwd(), smp_path, bc, "ARQ_ENTRADA", sbb + ".txt"), 'rt', encoding='utf-8')
    f_lines = f_tmp.readlines()
    f_tmp.close
    vz = []
    dt_init = 0
    for l in range(0, len(f_lines)):
        if(f_lines[l].strip() != ""):
            dt_tmp = f_lines[l][20:24] + f_lines[l][25:27] + f_lines[l][28:30]
            if dt_tmp == dti:
                dt_init = 1
            if(dt_init):
                vz.append(round(float(f_lines[l][40:]), 2))
            if dt_tmp == dtf:
                dt_init = 0
                break
    # Leitura do arquivo de saida
    f_tmp = open(os.path.join(os.getcwd(), smp_path, bc, "ARQ_SAIDA", sbb + "_PMEDIA_ORIG_PREVISAO.txt"), 'rt', encoding='utf-8')
    f_lines = f_tmp.readlines()
    f_tmp.close()
    for l_idx in range(1, len(f_lines)):
        if f_lines[l_idx].strip() != "":
            dt_tmp = f_lines[l_idx][6:10] + f_lines[l_idx][3:5] + f_lines[l_idx][0:2]
            if dt_tmp == dti:
                dt_init = 1
            if(dt_init):
                vz.append(float(f_lines[l_idx][11:20]))
            if dt_tmp == dtf:
                break
    if len(vz) == dt_delta(dti, dtf):
        return vz
    else:
        print("Erro smp_read_sbb(" + sbb + ", " + dti + ", " + dtf + ") " + " - Intervalo não encontrado")
        exit(0)

def acph_q_load(pst, tp, dti, dtf):
    fn = os.path.join(os.getcwd(), "acomph_q_d.csv")
    if os.path.exists(fn):
        f = open(fn, 'rt')
        f_lns = f.readlines()
        f.close()
        hdr = f_lns[0].split(";")
        if dti in hdr and dtf in hdr:
            ci_idx = hdr.index(dti)
            cf_idx = hdr.index(dtf) + 1
            for a in range(1, len(f_lns)):
                lsplit = f_lns[a].split(";")
                if int(lsplit[0]) == pst and lsplit[1] == tp:
                    otp = []
                    for b in range(ci_idx, cf_idx):
                        otp.append(float(pxv(lsplit[b], ".")))
                    return otp
            else:
                print("Erro acph_q_load(" + str(pst) + "," + tp + "," + dti + "," + dtf + ") - Posto não encontrado")
                return 0
        else:
            print("Erro acph_q_load(" + str(pst) + ","  + tp + "," + dti + "," +  dtf + ") - Período não encontrado")
            exit(0)
        print("Erro acph_q_load() - Arquivo não encontrado: " + fn)
        exit(0)

def q_calc(di, df, inpt):
    #inpt = [subbacia, operação, fator]
    otp = []
    n = dt_delta(di, df)
    for i in range(0, n):
        otp.append(0)
    for i in inpt:
        if i[1] == "tv":
            otp = opr(otp, tmp_vg(smp_read_sbb(i[0], di, df), i[2]), "+")
        elif i[1] == "*":
            otp = opr(otp, opr(smp_read_sbb(i[0], di, df), [i[2]], "*"), "+")
    return otp

def calc_postos():
    # Posto 1 - Camargos
    p = 1
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CAMARGOS", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 6 - Furnas
    p = 6
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PBUENOS", "tv", 12], ["FURNAS", "*", 1], ["PARAGUACU", "tv", 10]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 7 - M. Moraes
    p = 7
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PCOLOMBIA", "*", 0.377]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 8 - L. C. Barreto
    p = 8
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PCOLOMBIA", "*", 0.087]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 9 - Jaguara
    p = 9
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PCOLOMBIA", "*", 0.036]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 10 - Igarapava
    p = 10
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PCOLOMBIA", "*", 0.103]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 11 - Volta Grande
    p = 11
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["PCOLOMBIA", "*", 0.23]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 12 - P. Colombia
    p = 12
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CAPESCURO", "tv", 8], ["PCOLOMBIA", "*", 0.167]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 14 - Caconde
    p = 14
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["EDACUNHA", "*", 0.61]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 15 - E. da Cunha
    p = 15
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["EDACUNHA", "*", 0.39]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 16 - Limoeiro
    p = 16
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MARIMBONDO", "*", 0.004]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 17 - Marimbondo
    p = 17
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MARIMBONDO", "*", 0.996], ["PASSAGEM", "tv", 16]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 18 - A. Vermelha
    p = 18
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["AVERMELHA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 22 - Batalha
    p = 22
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SDOFACAO", "*", 0.615]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 23 - Batalha
    p = 23
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CORUMBA1", "*", 0.1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 24 - EMBORCACAO
    p = 24
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["EMBORCACAO", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 25 - Nova Ponte
    p = 25
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["NOVAPONTE", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 28 - C. Branco-2
    p = 28
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITUMBIARA", "*", 0.012]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 31 - Itumbiara
    p = 31
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITUMBIARA", "*", 0.943]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 32 - C. Dourada
    p = 32
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SSIMAO2", "*", 0.109]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 33 - São Simão
    p = 33
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["RVERDE", "tv", 8], ["SSIMAO2", "*", 0.891]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 47 - Jurumirim
    p = 47
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["JURUMIRIM", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 48 - Piraju
    p = 48
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CHAVANTES", "*", 0.046]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 49 - Chavantes
    p = 49
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CHAVANTES", "*", 0.954]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 50 - Salto Grande CS
    p = 50
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CANOASI", "*", 0.778]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 51 - Canoas II
    p = 51
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CANOASI", "*", 0.061]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 52 - Canoas I
    p = 52
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CANOASI", "*", 0.13]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 57 - Maua
    p = 57
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MAUA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 61 - Capivara
    p = 61
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CAPIVARA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 62 - Taquaruçu
    p = 62
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ROSANA", "*", 0.299]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 63 - Rosana
    p = 63
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ROSANA", "*", 0.701]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 71 - Santa Clara-PR
    p = 71
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["STACLARA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 72 - Fundão
    p = 72
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["JORDSEG", "*", 0.039]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 73 - Jordao
    p = 73
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["JORDSEG", "*", 0.157]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 74 - G. B. Munhoz
    p = 74
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["FOA", "*", 1], ["UVITORIA", "tv", 17.4]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 76 - Segredo
    p = 76
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["JORDSEG", "*", 0.804]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 77 - Salto Santiago
    p = 77
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SCAXIAS", "*", 0.258]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 78 - Salto Osório
    p = 78
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SCAXIAS", "*", 0.102]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 89 - Garibaldi
    p = 89
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CN", "*", 0.910]])[3:]
    smp_inc_q.append(q_tmp)
     # Posto 92 - Itá
    p = 92
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 93 - Passo Fundo
    p = 93
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MONJOLINHO", "*", 0.586]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 94 - Foz Chapecó
    p = 94
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["FOZCHAPECO", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 102 - São José
    p = 102
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SJOAO", "*", 0.963]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 103 - São José
    p = 103
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SJOAO", "*", 0.037]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 117 - Guarapiranga
    p = 117
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ESOUZA", "*", 0.12]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 119 - Guarapiranga
    p = 119
    smp_inc_pst.append(p)
    q_tmp = []
    q_118 = acph_q_load(118, "INC", dt_acph_i, dt_acph_f)
    for v in range(0, len(q_118)):
        q_tmp.append((q_118[v] - 0.185) / 0.8103)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ESOUZA", "*", 0.183]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 155 - Retiro Baixo
    p = 155
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["RB-SMAP", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 156 - Tres Marias
    p = 156
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["TM-SMAP", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 158 - Queimado
    p = 158
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["QM", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 160 - Ponte Nova
    p = 160
    smp_inc_pst.append(p)
    #q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp = q_calc(dt_acph_i, dt_smp_f, [["ESOUZA", "*", 0.073]])
    smp_inc_q.append(q_tmp)
    # Posto 161 - E. S. Pinheiros
    p = 161
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ESOUZA", "*", 0.624]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 205 - Corumba-4
    p = 205
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CORUMBAIV", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 206 - Miranda
    p = 206
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITUMBIARA", "*", 0.04]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 207 - C. Branco-1
    p = 207
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITUMBIARA", "*", 0.005]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 209 - Corumba
    p = 209
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CORUMBA1", "*", 0.9]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 211 - Funil - MG
    p = 211
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["FUNIL MG", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 215 - Barra Grande
    p = 215
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["BG", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 216 - Campos Novos
    p = 216
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CN", "*", 0.09]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 217 - Machadinho
    p = 217
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MACHADINHO", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 220 - Monjolinho
    p = 220
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["MONJOLINHO", "*", 0.414]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 222 - Salto Caxias
    p = 222
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SCAXIAS", "*", 0.640]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 237 - B. Bonita
    p = 237
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["BBONITA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 238 - Bariri
    p = 238
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["IBITINGA", "*", 0.344]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 239 - Ibitinga
    p = 239
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["IBITINGA", "*", 0.656]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 240 - Promissão
    p = 240
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["NAVANHANDA", "*", 0.719]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 242 - N. Avanhandava
    p = 242
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["NAVANHANDA", "*", 0.281]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 249 - Ourinhos
    p = 249
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["CANOASI", "*", 0.031]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 251 - S. do Facão
    p = 251
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SDOFACAO", "*", 0.385]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 266 - Itaipu
    p = 266
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["ITAIPU", "*", 1], ["BALSA", "tv", 32], ["FLOR+ESTRA", "tv", 33], ["IVINHEMA", "tv", 45], ["PTAQUARA", "tv", 36]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 270 - Serra da Mesa
    p = 270
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["SMESA", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)
    # Posto 286 - Quebra Queixo
    p = 286
    smp_inc_pst.append(p)
    q_tmp = acph_q_load(p, "INC", dt_acph_i, dt_acph_f)
    q_tmp += q_calc(dt_smp_i, dt_smp_f, [["QQUEIXO", "*", 1]])[3:]
    smp_inc_q.append(q_tmp)

def print_files():
    # Imprime arquivo de vazoes incrementais diarias
    csv_file = open(os.path.join(os.getcwd(), "smp_inc_q_dia.csv"), 'wt')
    csv_file.write("Posto / Data;")
    ci = 0
    d = dt_delta(dt_acph_i, dt_smp_f)
    for a in range(0, d):
        csv_file.write(dt_offset(dt_acph_i, a) + ";")
        if dt_offset(dt_acph_i, a) == dt_get_so_ini(d_smap, -35):
            ci = a
    csv_file.write("\n")
    for a in range(0, len(smp_inc_pst)):
        csv_file.write(str(smp_inc_pst[a]) + ";")
        for b in range(0, len(smp_inc_q[a])):
            csv_file.write(str(round(smp_inc_q[a][b], 2)).replace(".", ",") + ";")
        csv_file.write("\n")
    csv_file.close()
    # Imprime arquivo de vazoes semanais
    csv_file = open(os.path.join(os.getcwd(), "smp_inc_q_sem.csv"), 'wt')
    csv_file.write("Posto / Sem;" + dt_hdr(dt_get_so_ini(d_smap, -35)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap, -28)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap, -21)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap, -14)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap, -7)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap)) + ";")
    csv_file.write(dt_hdr(dt_get_so_ini(d_smap, 7)) + ";\n")
    for a in range(0, len(smp_inc_pst)):
        csv_file.write(str(smp_inc_pst[a]) + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci:ci + 7]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 7:ci + 14]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 14:ci + 21]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 21:ci + 28]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 28:ci + 35]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 35:ci + 42]), 0))),",") + ";")
        csv_file.write(pxv(str(int(round(avr(smp_inc_q[a][ci + 42:ci + 49]), 0))),",") + ";")
        csv_file.write("\n")
    csv_file.close()

dt_acph_i = dt_offset(d_acph, -45)
dt_acph_f = dt_offset(d_acph, -1)
dt_smp_i = dt_offset(d_acph, -3)
dt_smp_f = dt_offset(d_smap, 11)

calc_postos()
print_files()




