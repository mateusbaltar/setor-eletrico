import os
import datetime
import numpy
import xlrd

ACPH_TABLE_D = "acomph_q_d.csv"
ACPH_TABLE_S = "acomph_q_s.csv"
HDR = 0
PST = 1
Q = 2

def dt_today(ofst = 0):
    #d = datetime.datetime(2020, 1, 19)
    d = datetime.datetime.today()
    return (d + datetime.timedelta(days=+ofst)).strftime("%Y%m%d")

def dt_conv_smn(d, ofst = 0):
    # Converte p/ número da semana uma data passada no formato YYYYMMDD
    # ofst = offset dado em dias
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    d1 = d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + 6)
    di = datetime.datetime(d1.year, 1, 1)
    d2 = di + datetime.timedelta(days=-wd[di.weekday()])
    return [((d1 - d2).days // 7) + 1, d1.year]

def dt_conv_so_dt(smn, an):
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(an, 1, 1)
    d_tmp = d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + (smn - 1) * 7)
    return [d_tmp.strftime("%Y%m%d"), (d_tmp + datetime.timedelta(days=+6)).strftime("%Y%m%d")]

def dt_get_so_ini(d, ofst = 0):
    # Retorna o inicio da SO de uma data passada no formato YYYYMMDD
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    return (d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()])).strftime("%Y%m%d")

def tmp_vg(v1, t):
    #Calcula vazão para um dado "tempo de viagem" da água
    otp = []
    dias = int((t//24)) + 1
    p1 = t%24
    p2 = 24 - p1
    for a in range(0, dias):
        otp.append(0)
    if (t > 0):
        for i in range(dias, len(v1)):
            otp.append(((float(v1[i - dias]) * p1) + (float(v1[i - dias + 1]) * p2))/24)
    else:
        for i in range(dias, len(v1)):
            otp.append(float(v1[i]))
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

def avr(val):
    #Calcula média aritimética dos elementos de uma matriz
    avr = 0
    for x in val:
        avr += x
    return str(round(avr/len(val), 3)).replace(".", ",")

def acph_fn(offset):
    d = dt_today(-offset)
    return "ACOMPH_" + d[6:8] + "." + d[4:6] + "." + d[0:4] + ".xls"

def acomph_table_load(qtable_fn):
    acph_hdr = []
    acph_pst = []
    acph_q = []
    qtable_pth = os.path.join(os.getcwd(), qtable_fn)
    if os.path.exists(qtable_pth):
        table_file = open(qtable_pth, 'rt')
        table_rl = table_file.readlines()
        ls = table_rl[0].split(";")
        for a in range(2, len(ls)):
            if(ls[a].strip() != ""):
                acph_hdr.append(ls[a].strip())
        acph_idx = 0
        for a in range(1, len(table_rl)):
            ls = table_rl[a].split(";")
            if (ls[0].strip() != ""):
                acph_pst.append([int(ls[0].strip()), ls[1].strip()])
                acph_q.append([])
                for b in range(2, len(acph_hdr) + 2):
                    acph_q[acph_idx].append(float(pxv(ls[b].strip(), ".")))
                acph_idx += 1
        table_file.close()
        #print(acph_hdr)
        #print(acph_pst)
        #print(acph_q)
        return [acph_hdr, acph_pst, acph_q]
    else:
        print("Erro acomph_table2(): Tabela não encontrada")
        return 0

def acomph_table_create(acph_fn):
    acph_pst = []
    acph_q = []
    header = []
    file_name = os.path.join(os.getcwd(), "Acomph", acph_fn)
    sis_conf = [
        ["Grande", 1, 211, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18],
        ["Paranaíba", 22, 251, 24, 25, 206, 207, 28, 205, 23, 209, 31, 32, 33, 99, 247, 248, 261, 294, 241],
        ["Tietê", 118, 117, 161, 237, 238, 239, 240, 242, 243],
        ["Paranapanema", 47, 48, 49, 249, 50, 51, 52, 57, 61, 62, 63],
        ["Paraná", 34, 245, 154, 246, 266],
        ["Iguaçu", 74, 76, 71, 72, 73, 77, 78, 222, 81],
        ["Uruguai", 215, 89, 216, 217, 92, 93, 220, 94, 286, 102, 103],
        ["Jacui", 110, 111, 112, 113, 114, 98, 97, 284],
        ["Outras Sul", 115, 101],
        ["Paraguai", 278, 259, 281, 295],
        ["Paraíba do Sul", 121, 122, 120, 123, 125, 197, 198, 129, 130, 201, 202],
        ["Doce", 262, 183, 134, 263, 149, 141, 148, 144],
        ["Outras Sudeste", 196, 283],
        ["São Francisco", 155, 156, 158, 169, 172, 173, 178],
        ["Outras Nordeste", 190, 255, 188, 254],
        ["Tocantins", 270, 191, 253, 257, 273, 271, 275],
        ["Amazonas", 296, 277, 279, 145, 291, 285, 287, 269, 290, 227, 228, 229, 230, 288],
        ["Araguari", 204, 280, 297]
    ]
    if os.path.exists(file_name):
        # Abre arquivo ACOMPH p/ leitura
        book = xlrd.open_workbook(file_name)
        vaz_idx = 0
        header_done = 1
        # Laço de leitura do arquivo ACOMPH (Bacias)
        for bacia_idx in range(0, len(sis_conf)):
            # Variável de controle de erro das bacias
            bacia_found = 1
            # Configura a aba que será lida
            try:
                sheet_tmp = book.sheet_by_name(sis_conf[bacia_idx][0])
            # Tratamento de erro caso a bacia não seja encontrada
            except:
                print("Erro read_acomph(): Bacia " + sis_conf[bacia_idx][0] + " não encontrada")
                bacia_found = 0
            if (bacia_found):
                # Constrói o cabeçalho do arquivo CSV
                if (header_done):
                    for ln_idx in range(5, 35):
                        date_tmp = datetime.datetime(
                            *xlrd.xldate_as_tuple(sheet_tmp.cell(ln_idx, 0).value, book.datemode))
                        header.append(date_tmp.strftime("%Y%m%d"))
                    header_done = 0
                # Faz a varredura, em cada bacia, no arquivo ACOMPH p/ encontrar o posto
                for posto_idx in range(1, len(sis_conf[bacia_idx])):
                    posto_found = 0
                    for cl_idx in range(0, sheet_tmp.ncols - 1):
                        # Encontra a posição do posto a ser lido
                        if (str(sheet_tmp.cell(0, cl_idx).value) == "Posto"):
                            # Armazena o número do posto encontrado
                            posto_tmp = int(sheet_tmp.cell(0, cl_idx + 1).value)
                            # Faz leitura dos dados de vazão no ACOMPH quando o posto é encontrado
                            if (posto_tmp == sis_conf[bacia_idx][posto_idx]):
                                acph_pst.append(int(posto_tmp))
                                acph_pst.append(int(posto_tmp))
                                acph_q.append([])
                                for ln_idx in range(5, 35):
                                    acph_q[vaz_idx].append(float(sheet_tmp.cell(ln_idx, cl_idx).value))
                                vaz_idx += 1
                                acph_q.append([])
                                for ln_idx in range(5, 35):
                                    acph_q[vaz_idx].append(float(sheet_tmp.cell(ln_idx, cl_idx + 1).value))
                                vaz_idx += 1
                                posto_found = 1
                    # Faz registro de erro de posto não encontrado
                    if (posto_found == 0):
                        print("Erro read_acomph(): Posto " + sis_conf[bacia_idx][posto_idx] + " não encontrado")
    else:
        print("Erro read_acomph(): Arquivo " + file_name + " não encontrado")
        exit(0)
    # Imprime arquivo
    csv_file = open(os.path.join(os.getcwd(), ACPH_TABLE_D), 'wt')
    csv_file.write("Posto;Tipo;")
    for a in range(0, len(header)):
        csv_file.write(header[a] + ";")
    csv_file.write("\n")
    leg = "NAT"
    for a in range(0, len(acph_pst)):
        csv_file.write(str(acph_pst[a]) + ";")
        if (leg == "NAT"):
            leg = "INC"
        elif (leg == "INC"):
            leg = "NAT"
        csv_file.write(leg + ";")
        for b in range(0, len(acph_q[a])):
            csv_file.write(str(round(acph_q[a][b], 3)).replace(".", ",") + ";")
        csv_file.write("\n")
    csv_file.close()

def acomph_table_update(acph_fn):
    HDR = 0
    PST = 1
    Q = 2
    tb = acomph_table_load(ACPH_TABLE_D)
    dt_ini = tb[HDR][0]
    dt_fim = tb[HDR][-1]
    sis_conf = [
        ["Grande", 1, 211, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18],
        ["Paranaíba", 22, 251, 24, 25, 206, 207, 28, 205, 23, 209, 31, 32, 33, 99, 247, 248, 261, 294, 241],
        ["Tietê", 118, 117, 161, 237, 238, 239, 240, 242, 243],
        ["Paranapanema", 47, 48, 49, 249, 50, 51, 52, 57, 61, 62, 63],
        ["Paraná", 34, 245, 154, 246, 266],
        ["Iguaçu", 74, 76, 71, 72, 73, 77, 78, 222, 81],
        ["Uruguai", 215, 89, 216, 217, 92, 93, 220, 94, 286, 102, 103],
        ["Jacui", 110, 111, 112, 113, 114, 98, 97, 284],
        ["Outras Sul", 115, 101],
        ["Paraguai", 278, 259, 281, 295],
        ["Paraíba do Sul", 121, 122, 120, 123, 125, 197, 198, 129, 130, 201, 202],
        ["Doce", 262, 183, 134, 263, 149, 141, 148, 144],
        ["Outras Sudeste", 196, 283],
        ["São Francisco", 155, 156, 158, 169, 172, 173, 178],
        ["Outras Nordeste", 190, 255, 188, 254],
        ["Tocantins", 270, 191, 253, 257, 273, 271, 275],
        ["Amazonas", 296, 277, 279, 145, 291, 285, 287, 269, 290, 227, 228, 229, 230, 288],
        ["Araguari", 204, 280, 297]
    ]
    # print(dt_ini)
    # print(dt_fim)
    file_name = os.path.join(os.getcwd(), "Acomph", acph_fn)
    if os.path.exists(file_name):
        # Abre arquivo ACOMPH p/ leitura
        book = xlrd.open_workbook(file_name)
        vaz_idx = 0
        header_done = 1
        pst_tb_idx = 0
        # Laço de leitura do arquivo ACOMPH (Bacias)
        for bacia_idx in range(0, len(sis_conf)):
            # Variável de controle de erro das bacias
            bacia_found = 1
            # Configura a aba que será lida
            try:
                sheet_tmp = book.sheet_by_name(sis_conf[bacia_idx][0])
            # Tratamento de erro caso a bacia não seja encontrada
            except:
                print("Erro read_acomph(): Bacia " + sis_conf[bacia_idx][0] + " não encontrada")
                bacia_found = 0
            if (bacia_found):
                if (header_done):
                    ini_idx = 0
                    stt_bef = -1
                    stp_bef = -1
                    stt_aft = -1
                    # Cria cabeçalho
                    for ln_idx in range(5, 35):
                        date_tmp = datetime.datetime(
                            *xlrd.xldate_as_tuple(sheet_tmp.cell(ln_idx, 0).value, book.datemode)).strftime(
                            "%Y%m%d")
                        if date_tmp < dt_ini:
                            tb[HDR].insert(ini_idx, date_tmp)
                            if (stt_bef == -1):
                                stt_bef = ln_idx
                            ini_idx += 1
                        elif date_tmp == dt_ini and stp_bef == -1:
                            stp_bef = ln_idx
                        elif date_tmp > dt_fim:
                            tb[HDR].append(date_tmp)
                            if stt_aft == -1:
                                stt_aft = ln_idx
                    header_done = 0
                # Faz a varredura, em cada bacia, no arquivo ACOMPH p/ encontrar o posto
                for posto_idx in range(1, len(sis_conf[bacia_idx])):
                    posto_found = 0
                    cl_idx = 0
                    while posto_found == 0 and cl_idx < (sheet_tmp.ncols - 1):
                        # Encontra a posição do posto a ser lido
                        if (str(sheet_tmp.cell(0, cl_idx).value) == "Posto"):
                            # Armazena o número do posto encontrado
                            posto_tmp = int(sheet_tmp.cell(0, cl_idx + 1).value)
                            # Faz leitura dos dados de vazão no ACOMPH quando o posto é encontrado
                            if posto_tmp == sis_conf[bacia_idx][posto_idx]:
                                # print(posto_tmp, tb[PST][pst_tb_idx][0], pst_tb_idx)
                                if posto_tmp == tb[PST][pst_tb_idx][0]:
                                    posto_found = 1
                                    # Trata sequencia de datas anteriores
                                    if stt_bef != -1 and stp_bef != -1:
                                        ins_idx = 0
                                        for ln_idx in range(5, stp_bef):
                                            tb[Q][pst_tb_idx].insert(ins_idx, float(sheet_tmp.cell(ln_idx, cl_idx).value))
                                            ins_idx += 1
                                        pst_tb_idx += 1
                                        ins_idx = 0
                                        for ln_idx in range(5, stp_bef):
                                            tb[Q][pst_tb_idx].insert(ins_idx, float(
                                                sheet_tmp.cell(ln_idx, cl_idx + 1).value))
                                            ins_idx += 1
                                        pst_tb_idx += 1
                                    # Trata sequencia de datas posteriores
                                    elif stt_bef == -1 and stp_bef == -1 and stt_aft != -1:
                                        for ln_idx in range(stt_aft, 35):
                                            tb[Q][pst_tb_idx].append(float(sheet_tmp.cell(ln_idx, cl_idx).value))
                                        pst_tb_idx += 1
                                        for ln_idx in range(stt_aft, 35):
                                            tb[Q][pst_tb_idx].append(
                                                float(sheet_tmp.cell(ln_idx, cl_idx + 1).value))
                                        pst_tb_idx += 1
                                else:
                                    print("Erro")
                        cl_idx += 1
                    # Faz registro de erro de posto não encontrado
                    if (posto_found == 0):
                        print(
                            "Erro read_acomph(): Posto " + str(sis_conf[bacia_idx][posto_idx]) + " não encontrado")
        # Imprime arquivo
        csv_file = open(os.path.join(os.getcwd(), ACPH_TABLE_D), 'wt')
        csv_file.write("Posto;Tipo;")
        for a in range(0, len(tb[HDR])):
            csv_file.write(tb[HDR][a] + ";")
        csv_file.write("\n")
        leg = "NAT"
        for a in range(0, len(tb[PST])):
            csv_file.write(str(tb[PST][a][0]) + ";")
            if (leg == "NAT"):
                leg = "INC"
            elif (leg == "INC"):
                leg = "NAT"
            csv_file.write(leg + ";")
            for b in range(0, len(tb[Q][a])):
                csv_file.write(str(round(tb[Q][a][b], 3)).replace(".", ",") + ";")
            csv_file.write("\n")
        csv_file.close()

def read_acph_q():
    mk_table = 0
    for a in range(0, 30):
        acph_pth = os.path.join(os.getcwd(), "Acomph", acph_fn(a))
        if os.path.exists(acph_pth):
            print(str(a) + " - read_acph_q() - Lendo dados de: " + acph_fn(a))
            if(mk_table):
                acomph_table_update(acph_pth)
            else:
                acomph_table_create(acph_pth)
                mk_table = 1
    tb = acomph_table_load(ACPH_TABLE_D)
    # Posto 119
    idx_118 = tb[PST].index([118, 'INC'])
    tb[PST].append([119, 'INC'])
    tb[PST].append([119, 'NAT'])
    tb[Q].append([])
    tb[Q].append([])
    idx_119 = tb[PST].index([119, 'INC'])
    for v in tb[Q][idx_118]:
        tb[Q][idx_119].append((v - 0.185)/0.8103)
        tb[Q][idx_119+1].append((v - 0.185)/0.8103)
    # Posto 168
    tb[PST].append([168, 'PVV'])
    tb[Q].append([])
    idx_168 = tb[PST].index([168, 'PVV'])
    idx_169 = tb[PST].index([169, 'INC'])
    tb[Q][idx_168] += tb[Q][idx_169]
    # Posto 246
    tb[PST].append([246, 'PVV'])
    tb[Q].append([])
    idx_246 = tb[PST].index([246, 'INC'])
    idx_154 = tb[PST].index([154, 'INC'])
    tb[Q][tb[PST].index([246, 'PVV'])] += opr(tmp_vg(tb[Q][idx_246], 0), tmp_vg(tb[Q][idx_154], 8), "+")

    # Imprime arquivo diario
    csv_file = open(os.path.join(os.getcwd(), ACPH_TABLE_D), 'wt')
    csv_file.write("Posto;Tipo;")
    for a in range(1, len(tb[HDR])):
        csv_file.write(tb[HDR][a] + ";")
    csv_file.write("\n")
    for a in range(0, len(tb[PST])):
        csv_file.write(str(tb[PST][a][0]) + ";")
        csv_file.write(tb[PST][a][1] + ";")
        for b in range(1, len(tb[Q][a])):
            csv_file.write(str(round(tb[Q][a][b], 3)).replace(".", ",") + ";")
        csv_file.write("\n")
    # Imprime arquivo semanal
    csv_file = open(os.path.join(os.getcwd(), ACPH_TABLE_S), 'wt')
    dti = dt_get_so_ini(tb[HDR][1], 6)
    # Encontra a data de inicio da primeira semana operativa
    dti_idx = tb[HDR].index(dti)
    # Inicia o cabeçalho do arquivo CSV
    csv_file.write("Posto;Tipo;")
    # Imprime o cabeçalho do arquivo CSV
    for a in range(dti_idx, len(tb[HDR]), 7):
        tt_tmp = dt_conv_smn(tb[HDR][a])
        csv_file.write(str(tt_tmp[0]) + "_" + str(tt_tmp[1]) + ";")
    csv_file.write("\n")
    # Calcula e imprime a média das vazões no arquivo CSV
    for a in range(0, len(tb[PST])):
        # Imprime o posto
        csv_file.write(str(tb[PST][a][0]) + ";")
        # Imprime o tipo INC / NAT
        csv_file.write(tb[PST][a][1] + ";")
        for b in range(dti_idx, len(tb[HDR]), 7):
            # Calcula a média de cada semana e imprime
            csv_file.write(avr(tb[Q][a][b:b + 7]) + ";")
        csv_file.write("\n")

read_acph_q()
input('Pressione uma tecla para continuar...')