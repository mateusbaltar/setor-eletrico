import os
import datetime
import numpy
import xlrd

QINCD_TABLE = "smp_inc_q_dia.csv"

smp_inc_hdr = []
smp_inc_pst = []
smp_inc_q = []

smp_pst = []
smp_q = []

def dt(op, ofs = 0):
    # 0 - Objeto
    # 1 - AAAAMMDD
    # 2 - DD/MM/AA
    # 3 - ACOMPH_DD.MM.AAAA.xls
    # 4 - Semana operativa
    # 5 - Ano corrente
    #d = datetime.datetime(2019, 9, 3)
    d = datetime.datetime.today()
    if(op == 0):
        return d
    elif op == 1:
        return (d + datetime.timedelta(days=+ofs)).strftime("%Y%m%d")
    elif (op == 2):
        return d.strftime("%d/%m/%Y")
    elif (op == 3):
        return "ACOMPH_" + d.strftime("%d.%m.%Y") + ".xls"
    elif (op == 4):
        wd = [2, 3, 4, 5, 6, 0, 1]
        d1 = d + datetime.timedelta(days= - wd[d.weekday()])
        di = datetime.datetime(d.year, 1, 1)
        d2 = di + datetime.timedelta(days= - wd[di.weekday()])
        return ((d1 - d2).days // 7) + 1
    elif (op == 5):
        return d.year
    elif op == 6:
        wd = [2, 3, 4, 5, 6, 0, 1]
        return (d + datetime.timedelta(days=ofs - wd[dt(0).weekday()])).strftime("%Y%m%d")
    elif op == 7:
        wd = [2, 3, 4, 5, 6, 0, 1]
        d1 = d + datetime.timedelta(days=ofs + -wd[d.weekday()])
        di = datetime.datetime(d1.year, 1, 1)
        d2 = di + datetime.timedelta(days=-wd[di.weekday()])
        return str(((d1 - d2).days // 7) + 1) + "_" + str(d1.year)
    else:
        print("Erro dt(): Argumento não econtrado")
        return 0

def so(offset):
    # Retorna data do inicio da semana operativa no formato YYYYMMDD
    d = [2, 3, 4, 5, 6, 0, 1]
    dt_tmp = dt(0) + datetime.timedelta(days = offset - d[dt(0).weekday()])
    return str(dt_tmp.year) + ("0" + str(dt_tmp.month))[-2:] + ("0" + str(dt_tmp.day))[-2:]

def avr(val):
    #Calcula média aritimética dos elementos de uma matriz
    avr = 0
    for x in val:
        avr += x
    return round(avr/len(val), 2)

def apx(v1):
    #Aproxima elementos de um vetor para número inteiro
    otp = []
    for i in v1:
        otp.append(round(i, 2))
        #otp.append(i)
    return otp

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

def smap_tmp_vg(v1, t):
    #Calcula vazão para um dado "tempo de viagem" da água
    otp = []
    dias = int((t//24)) + 1
    p1 = t % 24
    p2 = 24 - p1
    for a in range(0, dias):
        otp.append(0)
    for i in range(dias, len(v1)):
        otp.append(((v1[i - dias] * p1) + (v1[i - dias + 1] * p2))/24)
    if t > 0:
        return otp
    else:
        return v1

def smap_q_calc(vls):
    #vls = [[posto, tempo de viagem][. . .][. . .] . . .]
    #Soma vazões incrementais de postos passados como vetor de argumento
    otp = []
    array_init = 1
    for pst in vls:
        found = 1
        if(pst[1] == 0):
            for p_idx in range(0, len(smp_inc_pst)):
                if(pst[0] == smp_inc_pst[p_idx]):
                    if(array_init):
                        otp = smap_tmp_vg(smp_inc_q[p_idx], pst[2])
                        array_init = 0
                    else:
                        otp += numpy.array(smap_tmp_vg(smp_inc_q[p_idx], pst[2]))
                    found = 0
                    break
        elif(pst[1] == 1):
            for p_idx in range(0, len(smp_pst)):
                if(pst[0] == smp_pst[p_idx]):
                    if(array_init):
                        otp = smap_tmp_vg(smp_q[p_idx], pst[2])
                        array_init = 0
                    else:
                        otp += numpy.array(smap_tmp_vg(smp_q[p_idx], pst[2]))
                    found = 0
                    break
        if(found):
            print("q_soma() erro: Posto " + str(pst[0]) + " não encontrado")
    return otp

def smp_qincd_load():
    global smp_inc_hdr
    global smp_inc_pst
    global smp_inc_q
    #Faz leitura da tabela de vazoes incrementais
    qtable_pth = os.path.join(os.getcwd(), QINCD_TABLE)
    if os.path.exists(qtable_pth):
        table_file = open(qtable_pth, 'rt')
        table_rl = table_file.readlines()
        ls = table_rl[0].split(";")
        for a in range(1, len(ls)):
            if(ls[a].strip() != ""):
                smp_inc_hdr.append(ls[a].strip())
        vinc_idx = 0
        for a in range(1, len(table_rl)):
            ls = table_rl[a].split(";")
            if (ls[0].strip() != ""):
                smp_inc_pst.append(int(ls[0].strip()))
                smp_inc_q.append([])
                #print(table_rl[a])
                for b in range(1, len(smp_inc_hdr) + 1):
                    smp_inc_q[vinc_idx].append(float(ls[b].strip().replace(",", ".")))
                vinc_idx += 1
        table_file.close()
        #for a in range(0, len(smp_inc_pst)):
        #    print(smp_inc_pst[a], apx(smp_inc_q[a]))
        return 1
    else:
        print("Erro smp_qincd_load(): Tabela não encontrada")
        exit(0)

def smap_q():
    smp_qincd_load()
    # Posto 1 - GRANDE
    smp_pst.append(1)
    smp_q.append(smap_q_calc([[1, 0, 0]]))
    # Posto 211 - GRANDE
    smp_pst.append(211)
    smp_q.append(smap_q_calc([[1, 0, 13], [211, 0, 0]]))
    #smp_q.append(smap_q_calc([[1, 0, 0], [211, 0, 0]]))
    # Posto 6 - GRANDE
    smp_pst.append(6)
    smp_q.append(smap_q_calc([[211, 1, 36], [6, 0, 0]]))
    #smp_q.append(smap_q_calc([[211, 1, 0], [6, 0, 0]]))
    # Posto 7 - GRANDE
    smp_pst.append(7)
    smp_q.append(smap_q_calc([[6, 1, 23], [7, 0, 0]]))
    #smp_q.append(smap_q_calc([[6, 1, 0], [7, 0, 0]]))
    # Posto 8 - GRANDE
    smp_pst.append(8)
    smp_q.append(smap_q_calc([[7, 1, 7], [8, 0, 0]]))
    # Posto 9 - GRANDE
    smp_pst.append(9)
    smp_q.append(smap_q_calc([[8, 1, 5], [9, 0, 0]]))
    # Posto 10 - GRANDE
    smp_pst.append(10)
    smp_q.append(smap_q_calc([[9, 1, 10], [10, 0, 0]]))
    # Posto 11 - GRANDE
    smp_pst.append(11)
    smp_q.append(smap_q_calc([[10, 1, 12], [11, 0, 0]]))
    # Posto 12 - GRANDE
    smp_pst.append(12)
    smp_q.append(smap_q_calc([[11, 1, 11], [12, 0, 0]]))
    # Posto 14 - GRANDE
    smp_pst.append(14)
    smp_q.append(smap_q_calc([[14, 0, 0]]))
    # Posto 15 - GRANDE
    smp_pst.append(15)
    smp_q.append(smap_q_calc([[14, 1, 12], [15, 0, 0]]))
    # Posto 16 - GRANDE
    smp_pst.append(16)
    smp_q.append(smap_q_calc([[15, 1, 3], [16, 0, 0]]))
    # Posto 17 - GRANDE
    smp_pst.append(17)
    smp_q.append(smap_q_calc([[16, 1, 72], [12, 1, 20], [17, 0, 0]]))
    # Posto 18 - GRANDE
    smp_pst.append(18)
    smp_q.append(smap_q_calc([[17, 1, 28], [18, 0, 0]]))
    # Posto 22 - PARANAÍBA
    smp_pst.append(22)
    smp_q.append(smap_q_calc([[22, 0, 0]]))
    # Posto 251 - PARANAÍBA
    smp_pst.append(251)
    smp_q.append(smap_q_calc([[22, 1, 0], [251, 0, 0]]))
    # Posto 24 - PARANAÍBA
    smp_pst.append(24)
    smp_q.append(smap_q_calc([[251, 1, 0], [24, 0, 0]]))
    # Posto 25 - PARANAÍBA
    smp_pst.append(25)
    smp_q.append(smap_q_calc([[25, 0, 0]]))
    # Posto 206 - PARANAÍBA
    smp_pst.append(206)
    smp_q.append(smap_q_calc([[25, 1, 11], [206, 0, 0]]))
    # Posto 207 - PARANAÍBA
    smp_pst.append(207)
    smp_q.append(smap_q_calc([[206, 1, 5], [207, 0, 0]]))
    # Posto 28 - PARANAÍBA
    smp_pst.append(28)
    smp_q.append(smap_q_calc([[207, 1, 12], [28, 0, 0]]))
    # Posto 205 - PARANAÍBA
    smp_pst.append(205)
    smp_q.append(smap_q_calc([[205, 0, 0]]))
    # Posto 23 - PARANAÍBA
    smp_pst.append(23)
    smp_q.append(smap_q_calc([[205, 1, 12], [23, 0, 0]]))
    # Posto 209 - PARANAÍBA
    smp_pst.append(209)
    smp_q.append(smap_q_calc([[23, 1, 24], [209, 0, 0]]))
    # Posto 31 - PARANAÍBA
    smp_pst.append(31)
    smp_q.append(smap_q_calc([[209, 1, 17], [24, 1, 17], [28, 1, 17], [31, 0, 0]]))
    # Posto 32 - PARANAÍBA
    smp_pst.append(32)
    smp_q.append(smap_q_calc([[31, 1, 8], [32, 0, 0]]))
    # Posto 33 - PARANAÍBA
    smp_pst.append(33)
    smp_q.append(smap_q_calc([[32, 1, 15], [33, 0, 0]]))

    # Posto 47 - PARANAPANEMA (SE)
    smp_pst.append(47)
    smp_q.append(smap_q_calc([[47, 0, 0]]))
    # Posto 48 - PARANAPANEMA (SE)
    smp_pst.append(48)
    smp_q.append(smap_q_calc([[47, 1, 5.1], [48, 0, 0]]))
    # Posto 49 - PARANAPANEMA (SE)
    smp_pst.append(49)
    smp_q.append(smap_q_calc([[48, 1, 10.52], [49, 0, 0]]))
    # Posto 249 - PARANAPANEMA (SE)
    smp_pst.append(249)
    smp_q.append(smap_q_calc([[49, 1, 3], [249, 0, 0]]))
    # Posto 50 - PARANAPANEMA (SE)
    smp_pst.append(50)
    smp_q.append(smap_q_calc([[249, 1, 3], [50, 0, 0]]))
    # Posto 51 - PARANAPANEMA (SE)
    smp_pst.append(51)
    smp_q.append(smap_q_calc([[50, 1, 2.8], [51, 0, 0]]))
    # Posto 52 - PARANAPANEMA (SE)
    smp_pst.append(52)
    smp_q.append(smap_q_calc([[51, 1, 2.8], [52, 0, 0]]))
    # Posto 57 - PARANAPANEMA (S)
    smp_pst.append(57)
    smp_q.append(smap_q_calc([[57, 0, 0]]))
    # Posto 61 - PARANAPANEMA (SE)
    smp_pst.append(61)
    smp_q.append(smap_q_calc([[57, 1, 0], [52, 1, 17.2], [61, 0, 0]]))
    # Posto 62 - PARANAPANEMA (SE)
    smp_pst.append(62)
    smp_q.append(smap_q_calc([[61, 1, 9.2], [62, 0, 0]]))
    # Posto 63 - PARANAPANEMA (SE)
    smp_pst.append(63)
    smp_q.append(smap_q_calc([[62, 1, 13.9], [63, 0, 0]]))
    # Posto 71 - IGUAÇU
    smp_pst.append(71)
    smp_q.append(smap_q_calc([[71, 0, 0]]))
    # Posto 72 - IGUAÇU
    smp_pst.append(72)
    smp_q.append(smap_q_calc([[71, 1, 2], [72, 0, 0]]))
    # Posto 73 - IGUAÇU
    smp_pst.append(73)
    smp_q.append(smap_q_calc([[72, 1, 1.8], [73, 0, 0]]))
    # Posto 74 - IGUAÇU
    smp_pst.append(74)
    smp_q.append(smap_q_calc([[74, 0, 0]]))
    # Posto 76 - IGUAÇU
    smp_pst.append(76)
    smp_q.append(smap_q_calc([[74, 1, 12.7], [76, 0, 0]]))
    # Posto 77 - IGUAÇU
    smp_pst.append(77)
    smp_q.append(smap_q_calc([[73, 1, 9.6], [76, 1, 11.7], [77, 0, 0]]))

    # Posto 117 - ALTO TIETÊ
    smp_pst.append(117)
    smp_q.append(smap_q_calc([[117, 0, 0]]))
    # Posto 119 - ALTO TIETÊ
    smp_pst.append(119)
    smp_q.append(smap_q_calc([[119, 0, 0]]))
    # Posto 160 - ALTO TIETÊ
    smp_pst.append(160)
    smp_q.append(smap_q_calc([[160, 0, 0]]))
    # Posto 161 - ALTO TIETÊ
    smp_pst.append(161)
    smp_q.append(smap_q_calc([[117, 0, 6], [119, 0, 0], [160, 0, 15], [161, 0, 0]]))
    # Posto 237 - TIETÊ
    smp_pst.append(237)
    smp_q.append(smap_q_calc([[161, 1, 48], [237, 0, 0]]))
    # Posto 239 - TIETÊ
    smp_pst.append(239)
    smp_q.append(smap_q_calc([[238, 0, 0], [239, 0, 0]]))
    # Posto 240 - TIETÊ
    smp_pst.append(240)
    smp_q.append(smap_q_calc([[117, 0, 6], [119, 0, 0], [160, 0, 0], [161, 0, 0], [237, 0, 0], [238, 0, 0], [239, 0, 0], [240, 0, 0]]))
    # Posto 242 - TIETÊ
    smp_pst.append(242)
    smp_q.append(smap_q_calc([[240, 0, 13], [242, 0, 0]]))
    # Posto 155 - SÃO FRANCISCO (SE)
    smp_pst.append(155)
    smp_q.append(smap_q_calc([[155, 0, 0]]))
    # Posto 156 - SÃO FRANCISCO (SE)
    smp_pst.append(156)
    smp_q.append(smap_q_calc([[155, 1, 0], [156, 0, 0]]))
    # Posto 158 - SÃO FRANCISCO (SE)
    smp_pst.append(158)
    smp_q.append(smap_q_calc([[158, 0, 0]]))
    # Posto 89 - URUGUAI
    smp_pst.append(89)
    smp_q.append(smap_q_calc([[89, 0, 0]]))
    # Posto 216 - URUGUAI
    smp_pst.append(216)
    smp_q.append(smap_q_calc([[89, 1, 0], [216, 0, 0]]))
    # Posto 215 - URUGUAI
    smp_pst.append(215)
    smp_q.append(smap_q_calc([[215, 0, 0]]))
    # Posto 217 - URUGUAI
    smp_pst.append(217)
    smp_q.append(smap_q_calc([[216, 1, 1], [215, 1, 1], [217, 0, 0]]))
    # Posto 92 - URUGUAI
    smp_pst.append(92)
    smp_q.append(smap_q_calc([[217, 1, 2], [92, 0, 0]]))
    # Posto 93 - URUGUAI
    smp_pst.append(93)
    smp_q.append(smap_q_calc([[93, 0, 0]]))
    # Posto 220 - URUGUAI
    for a in range(0, len(smp_pst)):
        print(smp_pst[a], apx(smp_q[a]))
    print("\n\n")
    smp_pst.append(220)
    smp_q.append(smap_q_calc([[93, 1, 7.7], [220, 0, 0]]))
    for a in range(0, len(smp_pst)):
        print(smp_pst[a], apx(smp_q[a]))
    print("\n\n")
    # Posto 94 - URUGUAI
    smp_pst.append(94)
    smp_q.append(smap_q_calc([[92, 1, 20.9], [220, 1, 14.9]]))
    # Posto 102 - URUGUAI
    smp_pst.append(102)
    smp_q.append(smap_q_calc([[102, 0, 0]]))
    # Posto 286 - URUGUAI
    smp_pst.append(286)
    smp_q.append(smap_q_calc([[286, 0, 0]]))

    # Posto 266 - PARANÁ
    smp_pst.append(266)
    smp_q.append(smap_q_calc([[266, 0, 0]]))
    # Posto 270 - TOCANTINS (SE)
    smp_pst.append(270)
    smp_q.append(smap_q_calc([[270, 0, 0]]))

    # Imprime arquivo de vazoes diarias
    csv_file = open(os.path.join(os.getcwd(), "smp_q_dia.csv"), 'wt')
    csv_file.write("Posto / Data;")
    for a in range(-45, -45 + len(smp_q[0]), +1):
        csv_file.write(dt(1, a) + ";")
        if(dt(1, a) == dt(6, -35)):
            ci = a + 45
            #print("CI: ", ci)
    csv_file.write("\n")
    for a in range(0, len(smp_pst)):
        csv_file.write(str(smp_pst[a]) + ";")
        for b in range(0, len(smp_q[a])):
            csv_file.write(str(round(smp_q[a][b], 2)).replace(".", ",") + ";")
        csv_file.write("\n")
    csv_file.close()
    # Imprime arquivo de vazoes semanais
    csv_file = open(os.path.join(os.getcwd(), "smp_q_sem.csv"), 'wt')
    csv_file.write("Posto / Sem;" + str(dt(7,-35)) + ";" + str(dt(7,-28)) + ";" + str(dt(7,-21)) + ";" + str(dt(7,-14)) + ";" + str(dt(7,-7)) + ";" + str(dt(7,0)) + ";" + str(dt(7,7)) + ";\n")
    for a in range(0, len(smp_pst)):
        csv_file.write(str(smp_pst[a]) + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci:ci + 7]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 7:ci + 14]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 14:ci + 21]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 21:ci + 28]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 28:ci + 35]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 35:ci + 42]), 0))).replace(".", ",") + ";")
        csv_file.write(str(int(round(avr(smp_q[a][ci + 42:ci + 49]), 0))).replace(".", ",") + ";")
        csv_file.write("\n")
    csv_file.close()


#smp_qincd_load()
smap_q()