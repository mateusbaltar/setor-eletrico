import os
import datetime

prevs_pst = [[1, 1], [2, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [14, 1], [15, 1], [16, 1],
             [17, 1], [18, 1], [22, 1], [23, 1], [24, 1], [25, 1], [28, 1], [31, 1], [32, 1], [33, 1], [34, 0],
             [47, 1], [48, 1], [49, 1], [50, 1], [51, 1], [52, 1], [57, 1], [61, 1], [62, 1], [63, 1], [71, 1],
             [72, 1], [73, 1], [74, 1], [76, 1], [77, 1], [78, 1], [81, 0], [89, 1], [92, 1], [93, 1], [94, 1],
             [97, 0], [98, 0], [99, 0], [101, 0], [102, 1], [103, 1], [104, 0], [109, 0], [110, 0], [111, 0],
             [112, 0], [113, 0], [114, 0], [115, 0], [116, 0], [117, 1], [118, 0], [119, 1], [120, 0], [121, 0],
             [122, 0], [123, 0], [125, 0], [129, 0], [130, 0], [134, 0], [141, 0], [144, 0], [145, 0], [148, 0],
             [149, 0], [154, 0], [155, 0], [156, 0], [158, 0], [160, 1], [161, 1], [166, 0], [168, 0], [169, 0],
             [171, 0], [172, 0], [173, 0], [175, 0], [176, 0], [178, 0], [183, 0], [188, 0], [190, 0], [191, 0],
             [196, 0], [197, 0], [198, 0], [201, 0], [202, 0], [203, 0], [204, 0], [205, 1], [206, 1], [207, 1],
             [209, 1], [211, 1], [215, 1], [216, 1], [217, 1], [220, 1], [222, 1], [227, 0], [228, 0], [229, 0],
             [230, 0], [237, 1], [238, 1], [239, 1], [240, 1], [241, 0], [242, 1], [243, 0], [244, 0], [245, 0],
             [246, 0], [247, 0], [248, 0], [249, 1], [251, 1], [252, 0], [253, 0], [254, 0], [255, 0], [257, 0],
             [259, 0], [261, 0], [262, 0], [263, 0], [266, 1], [269, 0], [270, 1], [271, 0], [273, 0], [275, 0],
             [277, 0], [278, 0], [279, 0], [280, 0], [281, 0], [283, 0], [284, 0], [285, 0], [286, 1], [287, 0],
             [288, 0], [290, 0], [291, 0], [294, 0], [295, 0], [296, 0], [297, 0], [301, 1], [320, 1]]

def dt_today(ofst = 0):
    #d = datetime.datetime(2019, 9, 3)
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

def dt_get_so_fim(d, ofst = 0):
    # Retorna o final da SO de uma data passada no formato YYYYMMDD
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    return (d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + 6)).strftime("%Y%m%d")

def dt_prevs(d, ofst = 0):
    wd = [2, 3, 4, 5, 6, 0, 1]
    d_tmp = datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)
    d_tmp = d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + 6)
    d_ref = datetime.datetime(d_tmp.year, d_tmp.month, 1)
    d_ref = d_ref + datetime.timedelta(-wd[d_ref.weekday()])
    s0_0 = (d_ref + datetime.timedelta(days=0)).strftime("%Y%m%d")
    s0_1 = (d_ref + datetime.timedelta(days=6)).strftime("%Y%m%d")
    s0 = dt_conv_smn(d_ref.strftime(s0_0))
    s1_0 = (d_ref + datetime.timedelta(days=7)).strftime("%Y%m%d")
    s1_1 = (d_ref + datetime.timedelta(days=13)).strftime("%Y%m%d")
    s1 = dt_conv_smn(d_ref.strftime(s1_0))
    s2_0 = (d_ref + datetime.timedelta(days=14)).strftime("%Y%m%d")
    s2_1 = (d_ref + datetime.timedelta(days=20)).strftime("%Y%m%d")
    s2 = dt_conv_smn(d_ref.strftime(s2_0))
    s3_0 = (d_ref + datetime.timedelta(days=21)).strftime("%Y%m%d")
    s3_1 = (d_ref + datetime.timedelta(days=27)).strftime("%Y%m%d")
    s3 = dt_conv_smn(d_ref.strftime(s3_0))
    s4_0 = (d_ref + datetime.timedelta(days=28)).strftime("%Y%m%d")
    s4_1 = (d_ref + datetime.timedelta(days=34)).strftime("%Y%m%d")
    s4 = dt_conv_smn(d_ref.strftime(s4_0))
    s5_0 = (d_ref + datetime.timedelta(days=35)).strftime("%Y%m%d")
    s5_1 = (d_ref + datetime.timedelta(days=41)).strftime("%Y%m%d")
    s5 = dt_conv_smn(d_ref.strftime(s5_0))
    return [
        [s0[0], s0[1], s0_0, s0_1],
        [s1[0], s1[1], s1_0, s1_1],
        [s2[0], s2[1], s2_0, s2_1],
        [s3[0], s3[1], s3_0, s3_1],
        [s4[0], s4[1], s4_0, s4_1],
        [s5[0], s5[1], s5_0, s5_1]
    ]

def dt_obj(d, ofst):
    return datetime.datetime(int(d[0:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=ofst)

def sem_calc(sem, ano, ofts):
    sem += ofts
    if sem > 52:
        sem = sem - 52
        ano += 1
    elif sem < 1:
        sem = 52 + sem
        ano -= 1
    return [sem, ano]

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

def avr(val):
    #Calcula média aritimética dos elementos de uma matriz
    avr = 0
    for x in val:
        avr += float(x.strip().replace(",", "."))
    return int(round(avr/len(val), 0))

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

def rgrs(pst, v_ref, ano, sem):
    wd = [2, 3, 4, 5, 6, 0, 1]
    A0 = [
        [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [10, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [11, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [15, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [16, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [22, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [251, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [206, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [207, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [28, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [23, 205, 0.8, -0.3, 2, 1.3, 2.2, 2.4, 2.7, 1.8, 1.1, 0.7, 1.3, 0.9],
        [32, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [248, 247, 1.1, 0.5, 1, 0.2, 0.5, 0.1, 0.3, -0.2, 0.1, -0.3, -0.2, 0.9],
        [261, 247, 1.8, 0.8, 3.2, 1.2, 0.4, 0.8, 1.1, 0.9, 0.6, 0.5, 1.1, 2.8],
        [241, 294, 0.1, -0.9, 0, -1.1, -0.4, -0.4, 0.8, 1, 0.2, -0.1, 0.1, 0.3],
        [118, 119, -0.5, -0.1, 1.8, 0.4, -0.4, 0.4, 0.3, -0.3, 1, 0.2, 1.3, -0.6],
        [301, 119, -0.5, -0.1, 1.8, 0.4, -0.4, 0.4, 0.3, -0.3, 1, 0.2, 1.3, -0.6],
        [320, 119, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [116, 117, -0.6, -0.4, -8.1, -2.1, 0.8, -1.8, -1.8, -2.5, -0.1, -2.7, 2.2, -0.2],
        [48, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [49, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [249, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [50, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [52, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [51, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [62, 63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [89, 216, -0.3, 3.5, 1.3, 0.9, 0.7, -3, -8, -3.5, -1.7, 1.2, -3, -0.2],
        [217, 92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [94, 92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [103, 102, -0.4, 0.7, -1.1, 0, 1.8, -2.8, 1.9, 0.4, -0.4, 0.7, 1.7, -0.2],
        [76, 74, 2.6, -6.8, 4.1, -5.5, 2.7, 17.8, 13.5, 18.3, 4.6, 12.4, 18.7, 20.9],
        [72, 71, 0, 0.4, 0.3, 0.1, 0.3, 0, 0.2, 0.1, 0, -0.1, 0.4, 0],
        [78, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [222, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [81, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [252, 259, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [110, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [112, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [113, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [114, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [97, 98, 1, -1.3, 11.6, -12.3, -4.8, 4, 5.5, 18.4, 10.7, -4.5, 4.2, 2.5],
        [284, 98, 1, -1.3, 11.4, -11.7, -7.2, 2.4, 5.1, 18.5, 9.7, -3.7, 4, 3.1],
        [303, 201, -3.5, -1.6, -2.9, -1.3, 0.4, -0.7, -0.5, -0.2, 0.2, -0.4, -1.2, 0],
        [123, 125, -7.9, -12.7, -10.2, -14, 6.9, -15.6, -6.1, -3.7, -2.1, -1.4, 6.1, -1.8],
        [129, 130, 19.6, 18.1, 22.6, 9.1, 7.5, 12.3, 11.1, 7.7, 10.1, 12.5, 15.2, 9.6],
        [202, 201, -3.2, -1.5, -2.8, -1.3, 0.1, -0.9, -0.6, -0.1, 0.2, -0.2, -0.8, 0.2],
        [306, 201, -3.5, -1.6, -2.9, -1.3, 0.4, -0.7, -0.5, -0.2, 0.2, -0.4, -1.2, 0],
        [203, 201, -0.4, 0.4, -0.2, 0.3, 1.7, 0.3, 0.2, 0, -0.1, -0.1, 0.1, 0.1],
        [122, 121, 3, 2.2, -3, -0.5, 0.2, -1.2, 3.7, 1.8, 0.4, 1.6, 1.9, -1.3],
        [129, 130, 19.6, 18.1, 22.6, 9.1, 7.5, 12.3, 11.1, 7.7, 10.1, 12.5, 15.2, 9.6],
        [198, 197, 21.7, 10.1, 15.6, 7.8, 13.8, 13.9, 8.1, 8.1, 3.6, 4.2, 10.5, 14.9],
        [263, 134, -0.6, -0.2, -0.3, -0.4, -0.2, 0.1, -0.3, -0.2, -0.2, 0, 0.6, 2],
        [141, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [148, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [183, 262, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [191, 270, 8.7, 11.5, 28.1, 22.2, 2.6, 4.2, -0.4, 1.3, 1.7, 8.9, 15.9, 12.1],
        [253, 270, 78.2, 81, 72, 42.2, 2.9, 9.2, 8.7, 7.5, 16.7, 22.5, 10.8, 34.8],
        [273, 257, 294.7, 549.2, 274.8, 493, 138, 43.2, 42.6, 41.1, 74.5, 0, -26.3, 272.5],
        [155, 156, 23.8, 36.9, 47.1, 38.9, 23.5, 8.5, 25.2, 17.8, 12.8, 26.6, 27.6, 61.5],
        [285, 287, 1.7, 13.7, 0.3, -1.8, -1.3, 3.4, -1.1, -0.2, -0.2, -0.4, -0.5, -1.3],
        [227, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [228, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [230, 229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [204, 280, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [297, 280, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    B0 = [
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [7, 6, 1.115, 1.126, 1.127, 1.129, 1.125, 1.117, 1.117, 1.116, 1.108, 1.109, 1.103, 1.104],
        [8, 6, 1.14, 1.157, 1.159, 1.165, 1.157, 1.147, 1.145, 1.143, 1.13, 1.131, 1.123, 1.122],
        [9, 6, 1.149, 1.17, 1.172, 1.182, 1.17, 1.158, 1.158, 1.155, 1.139, 1.141, 1.13, 1.127],
        [10, 6, 1.177, 1.207, 1.21, 1.225, 1.208, 1.195, 1.192, 1.19, 1.165, 1.165, 1.152, 1.147],
        [11, 6, 1.242, 1.286, 1.291, 1.317, 1.291, 1.272, 1.267, 1.261, 1.229, 1.227, 1.208, 1.2],
        [12, 6, 1.402, 1.47, 1.481, 1.523, 1.483, 1.452, 1.438, 1.431, 1.38, 1.38, 1.356, 1.343],
        [15, 14, 1.635, 1.633, 1.64, 1.61, 1.628, 1.639, 1.655, 1.708, 1.68, 1.613, 1.6, 1.623],
        [16, 14, 1.667, 1.663, 1.663, 1.644, 1.651, 1.667, 1.69, 1.708, 1.68, 1.645, 1.625, 1.652],
        [22, 24, 0.213, 0.218, 0.232, 0.241, 0.241, 0.24, 0.233, 0.229, 0.225, 0.219, 0.22, 0.221],
        [251, 24, 0.355, 0.358, 0.376, 0.388, 0.385, 0.377, 0.371, 0.365, 0.355, 0.353, 0.358, 0.368],
        [206, 25, 1.149, 1.152, 1.155, 1.166, 1.166, 1.167, 1.172, 1.189, 1.19, 1.182, 1.167, 1.154],
        [207, 25, 1.168, 1.173, 1.176, 1.19, 1.19, 1.192, 1.196, 1.22, 1.223, 1.203, 1.19, 1.173],
        [28, 25, 1.212, 1.223, 1.224, 1.245, 1.241, 1.247, 1.252, 1.28, 1.281, 1.257, 1.235, 1.216],
        [23, 205, 1.245, 1.242, 1.24, 1.229, 1.221, 1.217, 1.208, 1.213, 1.222, 1.241, 1.239, 1.244],
        [32, 31, 1.047, 1.05, 1.05, 1.053, 1.055, 1.056, 1.06, 1.062, 1.063, 1.054, 1.048, 1.046],
        [248, 247, 1.036, 1.039, 1.037, 1.04, 1.039, 1.04, 1.039, 1.042, 1.039, 1.043, 1.042, 1.036],
        [261, 247, 1.108, 1.112, 1.105, 1.112, 1.116, 1.114, 1.11, 1.111, 1.113, 1.114, 1.108, 1.101],
        [241, 294, 1.089, 1.092, 1.088, 1.095, 1.091, 1.091, 1.082, 1.08, 1.086, 1.088, 1.087, 1.086],
        [118, 119, 0.822, 0.812, 0.763, 0.806, 0.857, 0.75, 0.802, 0.833, 0.774, 0.8, 0.773, 0.823],
        [301, 119, 0.822, 0.812, 0.763, 0.806, 0.857, 0.75, 0.802, 0.833, 0.774, 0.8, 0.773, 0.823],
        [320, 119, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [116, 117, 0.33, 0.269, 0.605, 0.374, 0.167, 0.357, 0.451, 0.5, 0.314, 0.562, 0.173, 0.322],
        [48, 47, 1.021, 1.025, 1.026, 1.023, 1.026, 1.029, 1.022, 1.027, 1.025, 1.026, 1.022, 1.026],
        [49, 47, 1.551, 1.488, 1.452, 1.482, 1.569, 1.573, 1.573, 1.561, 1.609, 1.613, 1.565, 1.521],
        [249, 47, 1.569, 1.504, 1.471, 1.505, 1.59, 1.592, 1.596, 1.581, 1.627, 1.634, 1.586, 1.538],
        [50, 47, 2.012, 1.951, 1.946, 2.036, 2.133, 2.121, 2.101, 2.115, 2.137, 2.105, 2.081, 2.013],
        [52, 47, 2.114, 2.06, 2.064, 2.173, 2.267, 2.257, 2.23, 2.25, 2.261, 2.225, 2.21, 2.128],
        [51, 47, 2.042, 1.986, 1.984, 2.082, 2.174, 2.165, 2.146, 2.162, 2.174, 2.141, 2.124, 2.051],
        [62, 63, 0.905, 0.903, 0.891, 0.888, 0.893, 0.89, 0.889, 0.881, 0.891, 0.891, 0.885, 0.894],
        [89, 216, 0.925, 0.91, 0.92, 0.904, 0.897, 0.909, 0.922, 0.909, 0.906, 0.899, 0.916, 0.913],
        [217, 92, 0.735, 0.739, 0.731, 0.708, 0.694, 0.687, 0.706, 0.704, 0.71, 0.704, 0.701, 0.709],
        [94, 92, 1.211, 1.183, 1.205, 1.228, 1.236, 1.256, 1.24, 1.226, 1.207, 1.218, 1.255, 1.258],
        [103, 102, 1.042, 1.033, 1.048, 1.032, 1.027, 1.048, 1.033, 1.037, 1.037, 1.037, 1.036, 1.042],
        [76, 74, 1.136, 1.144, 1.12, 1.177, 1.174, 1.155, 1.141, 1.119, 1.145, 1.145, 1.135, 1.108],
        [72, 71, 1.048, 1.044, 1.045, 1.048, 1.046, 1.048, 1.046, 1.048, 1.048, 1.049, 1.045, 1.047],
        [78, 77, 1.042, 1.04, 1.045, 1.046, 1.05, 1.049, 1.047, 1.046, 1.041, 1.052, 1.054, 1.048],
        [222, 77, 1.293, 1.288, 1.291, 1.35, 1.4, 1.394, 1.35, 1.349, 1.322, 1.36, 1.368, 1.342],
        [81, 77, 1.397, 1.392, 1.395, 1.46, 1.512, 1.506, 1.458, 1.458, 1.429, 1.469, 1.478, 1.45],
        [252, 259, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [110, 111, 0.158, 0.16, 0.15, 0.147, 0.146, 0.138, 0.147, 0.148, 0.139, 0.146, 0.144, 0.142],
        [112, 111, 1.007, 1.008, 1.009, 1.014, 1.01, 1.008, 1.007, 1.007, 1.006, 1.006, 1.005, 1.011],
        [113, 111, 1.252, 1.256, 1.271, 1.287, 1.283, 1.279, 1.294, 1.269, 1.282, 1.279, 1.297, 1.256],
        [114, 111, 1.518, 1.552, 1.579, 1.636, 1.571, 1.623, 1.629, 1.55, 1.553, 1.546, 1.55, 1.517],
        [97, 98, 1.722, 1.712, 1.574, 1.871, 1.922, 1.817, 1.837, 1.752, 1.835, 1.939, 1.805, 1.833],
        [284, 98, 1.779, 1.768, 1.636, 1.919, 2, 1.886, 1.902, 1.814, 1.902, 2.002, 1.875, 1.888],
        [303, 201, 0.59, 0.48, 0.55, 0.47, 0.35, 0.47, 0.42, 0.39, 0.39, 0.46, 0.5, 0.43],
        [123, 125, 0.778, 0.801, 0.802, 0.821, 0.738, 0.843, 0.812, 0.8, 0.793, 0.79, 0.736, 0.766],
        [129, 130, 0.917, 0.924, 0.921, 0.935, 0.938, 0.923, 0.923, 0.932, 0.921, 0.915, 0.912, 0.92],
        [202, 201, 0.575, 0.475, 0.539, 0.465, 0.371, 0.485, 0.441, 0.369, 0.39, 0.43, 0.472, 0.413],
        [306, 201, 0.594, 0.484, 0.547, 0.47, 0.349, 0.469, 0.423, 0.387, 0.386, 0.46, 0.505, 0.426],
        [203, 201, 1.476, 1.449, 1.477, 1.453, 1.32, 1.419, 1.436, 1.462, 1.477, 1.467, 1.457, 1.457],
        [122, 121, 1.14, 1.161, 1.194, 1.155, 1.16, 1.203, 1.094, 1.139, 1.174, 1.144, 1.132, 1.178],
        [129, 130, 0.917, 0.924, 0.921, 0.935, 0.938, 0.923, 0.923, 0.932, 0.921, 0.915, 0.912, 0.92],
        [198, 197, 1.767, 1.963, 1.807, 1.913, 1.67, 1.594, 1.775, 1.772, 2.012, 2.027, 1.864, 1.878],
        [263, 134, 1.045, 1.044, 1.044, 1.046, 1.045, 1.044, 1.046, 1.046, 1.046, 1.043, 1.039, 1.034],
        [141, 144, 0.559, 0.586, 0.59, 0.598, 0.618, 0.629, 0.629, 0.635, 0.643, 0.617, 0.58, 0.554],
        [148, 144, 0.859, 0.862, 0.862, 0.862, 0.863, 0.867, 0.867, 0.869, 0.873, 0.869, 0.862, 0.858],
        [183, 262, 1.094, 1.097, 1.087, 1.095, 1.089, 1.083, 1.095, 1.081, 1.108, 1.085, 1.091, 1.093],
        [191, 270, 1.11, 1.107, 1.097, 1.097, 1.121, 1.116, 1.135, 1.14, 1.131, 1.108, 1.102, 1.103],
        [253, 270, 1.173, 1.178, 1.194, 1.225, 1.26, 1.214, 1.213, 1.224, 1.171, 1.151, 1.207, 1.195],
        [273, 257, 1.334, 1.301, 1.447, 1.403, 1.479, 1.386, 1.281, 1.206, 1.073, 1.252, 1.337, 1.247],
        [155, 156, 0.21, 0.181, 0.172, 0.16, 0.193, 0.24, 0.176, 0.2, 0.219, 0.169, 0.174, 0.171],
        [285, 287, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985, 0.985],
        [227, 229, 0.394, 0.376, 0.362, 0.357, 0.385, 0.451, 0.51, 0.564, 0.598, 0.55, 0.48, 0.425],
        [228, 229, 0.428, 0.41, 0.395, 0.391, 0.421, 0.488, 0.549, 0.602, 0.638, 0.591, 0.519, 0.462],
        [230, 229, 1.009, 1.009, 1.009, 1.009, 1.009, 1.009, 1.01, 1.009, 1.009, 1.009, 1.01, 1.009],
        [204, 280, 0.998, 0.998, 0.997, 0.997, 0.997, 0.997, 0.997, 0.997, 0.998, 0.996, 1, 1],
        [297, 280, 1.009, 1.009, 1.009, 1.009, 1.009, 1.009, 1.009, 1.009, 1.009, 1.011, 1.01, 1.009]
    ]
    for a in A0:
        if a[0] == pst:
            la = a
    for a in B0:
        if a[0] == pst:
            lb = a
    d_tmp = datetime.datetime(ano, 1, 1)
    d_tmp = d_tmp + datetime.timedelta(days=-wd[d_tmp.weekday()] + (sem - 1) * 7)
    m1 = d_tmp.month
    nm1 = 1
    m2 = 0
    nm2 = 0
    for b in range(1, 7):
        if (d_tmp + datetime.timedelta(days=b)).month == m1:
            nm1 += 1
        elif m2 == 0:
            m2 = (d_tmp + datetime.timedelta(days=b)).month
            nm2 = 1
        else:
            nm2 += 1
    return round((nm1*(la[m1 + 1]+(v_ref * lb[m1 + 1])) + nm2*(la[m2 + 1]+(v_ref * lb[m2 + 1])))/7, 2)

def pvv_load_(pst, ano, sem, ve):
    fn = os.path.join(os.getcwd(), "Previvaz_Done", str(pst), str(pst) + "_fut.dat")
    #fn = os.path.join(os.getcwd(), "Previvaz_Done", str(pst) + "_fut.dat")
    if os.path.exists(fn):
        pvv_file = open(fn, 'rt')
        pvv_lns = pvv_file.readlines()
        pvv_file.close()
        ano_load = int(pvv_lns[1][10:14])
        sem_load = int(pvv_lns[1][22:24])
        if ano > ano_load and sem < sem_load:
            position = (52 + sem) - sem_load
        else:
            position = sem - sem_load
        #print(ano, ano_load, sem, sem_load, position)
        if position >= 0 and position < 6:
            prev = float(pvv_lns[1 + ve][24 + (9 * position):33 + (9 * position)])
            return prev
        else:
            print("Erro pvv_load(" + str(pst) + ", " + str(ano) + ", " + str(sem) + ", " + str(ve) + ") - Datas dos arquivos são incompatíveis")
            return 0
            #exit(0)
    else:
        print("Erro pvv_load() - Posto " + str(pst) + " não encontrado")
        return 0
        #exit(0)

def pvv_load(pst, ano, sem, ve):
    fn = os.path.join(os.getcwd(), "Previvaz_Done", str(pst), str(pst) + "_fut.dat")
    #fn = os.path.join(os.getcwd(), "Previvaz_Done", str(pst) + "_fut.dat")
    if os.path.exists(fn):
        pvv_file = open(fn, 'rt')
        pvv_lns = pvv_file.readlines()
        pvv_file.close()
        ano_load = int(pvv_lns[1][10:14])
        sem_load = int(pvv_lns[1][22:24])
        if ano > ano_load and sem < sem_load:
            position = (52 + sem) - sem_load
        else:
            position = sem - sem_load
        if position >= 0 and position < 6:
            prev = float(pvv_lns[1 + ve][24 + (9 * position):33 + (9 * position)])
            return prev
        else:
            fn = os.path.join(os.getcwd(), "Previvaz_Out", str(pst) + "_str.dat")
            if os.path.exists(fn):
                pvv_file = open(fn, 'rt')
                pvv_lns = pvv_file.readlines()
                pvv_file.close()
                ano_ini = int(pvv_lns[1][1:5])
                ano_fim = int(pvv_lns[1][6:10])
                col_ano = (sem - 1) % 9
                ln_ano = (sem - 1) // 9
                ln_f = ((ano - ano_ini) * 6) + 2 + ln_ano
                ln_idx_ini = col_ano * 8
                if ln_f < len(pvv_lns):
                    return float(pvv_lns[ln_f][ln_idx_ini:ln_idx_ini + 8])
                else:
                    print("Erro pvv_load(1) - Posto " + str(pst) + " não encontrado")
                    return 0
                    # exit(0)
            else:
                print("Erro pvv_load(2) - Posto " + str(pst) + " não encontrado")
                return 0
                # exit(0)
    else:
        print("Erro pvv_load(3) - Posto " + str(pst) + " não encontrado")
        return 0
        #exit(0)

def smp_q_load(pst, sem, ano):
    fn = os.path.join(os.getcwd(), "smp_q_sem.csv")
    if os.path.exists(fn):
        fl = open(fn, 'rt')
        fl_lns = fl.readlines()
        fl.close()
        hdr = fl_lns[0].split(";")
        ttl = str(sem) + "_" + str(ano)
        if ttl in hdr:
            c_idx = hdr.index(ttl)
            for a in range(1, len(fl_lns)):
                lsplit = fl_lns[a].split(";")
                if(int(lsplit[0]) == pst):
                    return float(lsplit[c_idx].strip())
            print("Erro smp_q_load() - Posto " + str(pst) + " não encontrado")
            return 0
            #exit(0)
        else:
            print("Erro smp_q_load() - Posto: " + str(pst) + " Data: " + ttl + " não encontrada")
            return 0
            #exit(0)
    else:
        print("Erro smp_q_load() - Arquivo não encontrado")
        return 0
        #exit(0)

def smp_qinc_load(pst, sem, ano):
    fn = os.path.join(os.getcwd(), "smp_inc_q_sem.csv")
    if os.path.exists(fn):
        fl = open(fn, 'rt')
        fl_lns = fl.readlines()
        fl.close()
        hdr = fl_lns[0].split(";")
        ttl = str(sem) + "_" + str(ano)
        if ttl in hdr:
            c_idx = hdr.index(ttl)
            for a in range(1, len(fl_lns)):
                lsplit = fl_lns[a].split(";")
                if(int(lsplit[0]) == pst):
                    return float(lsplit[c_idx].strip())
            print("Erro smp_qinc_load() - Posto " + str(pst) + " não encontrado")
            return 0
            #exit(0)
        else:
            print("Erro smp_qinc_load() - Posto: " + str(pst) + " Data: " + ttl + " não encontrada")
            return 0
            #exit(0)
    else:
        print("Erro smp_q_load() - Arquivo não encontrado")
        return 0
        #exit(0)

def acph_qs_load_x(pst, sem, ano, tp):
    fn = os.path.join(os.getcwd(), "acomph_q_d.csv")
    if os.path.exists(fn):
        fl = open(fn, 'rt')
        fl_lns = fl.readlines()
        fl.close()
        hdr = fl_lns[0].split(";")
        ttl = dt_conv_so_dt(sem, ano)
        if ttl[0] in hdr and ttl[1] in hdr:
            c_ini = hdr.index(ttl[0])
            c_fim = hdr.index(ttl[1]) + 1
            for a in range(1, len(fl_lns)):
                lsplit = fl_lns[a].split(";")
                if(int(lsplit[0]) == pst):
                    lsplit = fl_lns[a + tp].split(";")
                    return avr(lsplit[c_ini:c_fim])
            print("Erro acph_q_load(" + str(pst) + ", " +  str(sem) + ", " + str(ano) + ", "  + str(tp) + ") - Posto não encontrado")
            #exit(0)
            return 0
        else:
            print("Erro acph_q_load(" + str(pst) + ", " +  str(sem) + ", " + str(ano) + ", "  + str(tp) + ") - Data não encontrada")
            #exit(0)
            return 0
    else:
        print("Erro acph_q_load(" + str(pst) + ", " +  str(sem) + ", " + str(ano) + ", "  + str(tp) + ") - Arquivo não encontrado")
        #exit(0)
        return 0

def acph_q_load_y(pst, dti, dtf, tp):
    fn = os.path.join(os.getcwd(), "acomph_q_d.csv")
    if os.path.exists(fn):
        fl = open(fn, 'rt')
        fl_lns = fl.readlines()
        fl.close()
        hdr = fl_lns[0].split(";")
        if dti in hdr and dtf in hdr:
            c_ini = hdr.index(dti)
            c_fim = hdr.index(dtf) + 1
            for a in range(1, len(fl_lns)):
                lsplit = fl_lns[a].split(";")
                if int(lsplit[0]) == pst:
                    lsplit = fl_lns[a + tp].split(";")
                    return lsplit[c_ini:c_fim]
            print("Erro acph_q_load(" + str(pst) + ", " + str(dti) + ", " + str(dtf) + ") - Posto não encontrado")
            #exit(0)
            return 0
        else:
            print("Erro acph_q_load(" + str(pst) + ", " + str(dti) + ", " + str(dtf) + ") - Data não encontrada")
            #exit(0)
            return 0
    else:
        print("Erro acph_q_load(" + str(pst) + ", " + str(dti) + ", " + str(dtf) + ") - Arquivo não encontrado")
        #exit(0)
        return 0

def acph_q_load(pst, sem, ano, tp):
    file = open(os.path.join(os.getcwd(), "acomph_q_s.csv"), 'rt')
    fl = file.readlines()
    file.close()
    l_tmp = fl[0].split(";")
    col_idx = l_tmp.index(str(sem) + "_" + str(ano))
    for ln_idx in range(1, len(fl)):
        l_tmp = fl[ln_idx].split(";")
        if int(l_tmp[0]) == pst and l_tmp[1] == tp:
            return float(pxv(l_tmp[col_idx].strip(), "."))
    print("pvv() - Posto não encontrado:", pst)
    return 0

def prv_ln(vl):
    #return ("          " + str(vl))[-10:]
    return ("          " + str(int(round(vl))))[-10:]

def prv_ln_ini(id, pst):
    ln = ("      " + str(id))[-6:]
    ln += ("     " + str(pst))[-5:]
    return ln

def past_v(pst, ano, sem):
    if pst == 2:
        return prv_ln(acph_q_load(1, sem, ano, "INC"))
    if pst == 160:
        return prv_ln(7)
    elif pst == 104:
        return prv_ln(acph_q_load(117, sem, ano, "NAT") + acph_q_load(118, sem, ano, "NAT"))
    elif pst == 109:
        return prv_ln(acph_q_load(118, sem, ano, "NAT"))
    elif pst == 116:
        v118 = acph_q_load(118, sem, ano, "NAT")
        return prv_ln(((v118*0.1897)-0.185)/0.8103)
    elif pst == 166:
        vtmp = acph_q_load(245, sem, ano, "INC")
        vtmp += acph_q_load(154, sem, ano, "INC")
        vtmp += acph_q_load(246, sem, ano, "INC")
        vtmp += acph_q_load(62, sem, ano, "INC")
        vtmp += acph_q_load(63, sem, ano, "INC")
        vtmp += acph_q_load(266, sem, ano, "INC")
        return prv_ln(vtmp)
    elif pst == 168:
        return prv_ln(acph_q_load(168, sem, ano, "PVV"))
    elif pst == 171:
        return prv_ln(acph_q_load(172, sem, ano, "INC"))
    elif pst == 175:
        return prv_ln(acph_q_load(172, sem, ano, "NAT"))
    elif pst == 176:
        return prv_ln(acph_q_load(172, sem, ano, "NAT"))
    elif pst == 203:
        return prv_ln(rgrs(203, acph_q_load(201, sem, ano, "NAT"), ano, sem))
    elif pst == 244:
        return prv_ln(acph_q_load(34, sem, ano, "NAT") + acph_q_load(243, sem, ano, "NAT"))
    elif pst == 252:
        return prv_ln(rgrs(252, acph_q_load(259, sem, ano, "NAT"), ano, sem))
    elif pst == 301:
        return prv_ln(acph_q_load(118, sem, ano, "NAT"))
    elif pst == 320:
        return prv_ln(acph_q_load(119, sem, ano, "INC"))
    else:
        return prv_ln(acph_q_load(pst, sem, ano, "NAT"))

def smp_v(pst, ano, sem):
    if pst == 2:
        return prv_ln(smp_q_load(1, sem, ano))
    elif pst == 78:
        return prv_ln(smp_qinc_load(71, sem, ano) +
                      smp_qinc_load(72, sem, ano) +
                      smp_qinc_load(73, sem, ano) +
                      smp_qinc_load(74, sem, ano) +
                      smp_qinc_load(76, sem, ano) +
                      smp_qinc_load(77, sem, ano) +
                      smp_qinc_load(78, sem, ano)
                      )
    elif pst == 81:
        return prv_ln(smp_qinc_load(71, sem, ano) +
                      smp_qinc_load(72, sem, ano) +
                      smp_qinc_load(73, sem, ano) +
                      smp_qinc_load(74, sem, ano) +
                      smp_qinc_load(76, sem, ano) +
                      smp_qinc_load(77, sem, ano) +
                      smp_qinc_load(78, sem, ano) +
                      smp_qinc_load(222, sem, ano) +
                      smp_qinc_load(81, sem, ano)
                      )
    elif pst == 94:
        return prv_ln(smp_qinc_load(89, sem, ano) +
                      smp_qinc_load(216, sem, ano) +
                      smp_qinc_load(215, sem, ano) +
                      smp_qinc_load(217, sem, ano) +
                      smp_qinc_load(93, sem, ano) +
                      smp_qinc_load(220, sem, ano) +
                      smp_qinc_load(92, sem, ano) +
                      smp_qinc_load(94, sem, ano)
                      )
    elif pst == 103:
        return prv_ln(smp_qinc_load(102, sem, ano) + smp_qinc_load(103, sem, ano))
    elif pst == 222:
        return prv_ln(smp_qinc_load(71, sem, ano) +
                      smp_qinc_load(72, sem, ano) +
                      smp_qinc_load(73, sem, ano) +
                      smp_qinc_load(74, sem, ano) +
                      smp_qinc_load(76, sem, ano) +
                      smp_qinc_load(77, sem, ano) +
                      smp_qinc_load(78, sem, ano) +
                      smp_qinc_load(222, sem, ano)
                      )
    elif pst == 237:
        return prv_ln(smp_qinc_load(117, sem, ano) +
                      smp_qinc_load(118, sem, ano) +
                      smp_qinc_load(160, sem, ano) +
                      smp_qinc_load(161, sem, ano) +
                      smp_qinc_load(237, sem, ano)
                      )
    elif pst == 238:
        return prv_ln(smp_qinc_load(117, sem, ano) +
                      smp_qinc_load(118, sem, ano) +
                      smp_qinc_load(160, sem, ano) +
                      smp_qinc_load(161, sem, ano) +
                      smp_qinc_load(237, sem, ano) +
                      smp_qinc_load(238, sem, ano)
                      )
    elif pst == 239:
        return prv_ln(smp_qinc_load(117, sem, ano) +
                      smp_qinc_load(118, sem, ano) +
                      smp_qinc_load(160, sem, ano) +
                      smp_qinc_load(161, sem, ano) +
                      smp_qinc_load(237, sem, ano) +
                      smp_qinc_load(238, sem, ano) +
                      smp_qinc_load(239, sem, ano)
                      )
    elif pst == 240:
        return prv_ln(smp_q_load(240, sem, ano))
    elif pst == 242:
        return prv_ln(smp_q_load(237, sem, ano) + smp_q_load(239,  sem, ano) + smp_q_load(242, sem, ano))
    elif pst == 251:
        return prv_ln(smp_qinc_load(251, sem, ano) + smp_qinc_load(22, sem, ano))
    elif pst == 266:
        return prv_ln(
            smp_qinc_load(47, sem, ano) +
            smp_qinc_load(48, sem, ano) +
            smp_qinc_load(49, sem, ano) +
            smp_qinc_load(50, sem, ano) +
            smp_qinc_load(51, sem, ano) +
            smp_qinc_load(52, sem, ano) +
            smp_qinc_load(57, sem, ano) +
            smp_qinc_load(61, sem, ano) +
            smp_qinc_load(62, sem, ano) +
            smp_qinc_load(63, sem, ano) +
            smp_qinc_load(249, sem, ano) +

            pvv_load(34, ano, sem, 0) +
            pvv_load(245, ano, sem, 0) +
            pvv_load(246, ano, sem, 0) +
            smp_qinc_load(266, sem, ano) +

            smp_qinc_load(1, sem, ano) +
            smp_qinc_load(211, sem, ano) +
            smp_qinc_load(6, sem, ano) +
            smp_qinc_load(7, sem, ano) +
            smp_qinc_load(8, sem, ano) +
            smp_qinc_load(9, sem, ano) +
            smp_qinc_load(10, sem, ano) +
            smp_qinc_load(11, sem, ano) +
            smp_qinc_load(12, sem, ano) +
            smp_qinc_load(17, sem, ano) +
            smp_qinc_load(18, sem, ano) +
            smp_qinc_load(14, sem, ano) +
            smp_qinc_load(15, sem, ano) +
            smp_qinc_load(16, sem, ano) +

            smp_qinc_load(22, sem, ano) +
            smp_qinc_load(23, sem, ano) +
            smp_qinc_load(24, sem, ano) +
            smp_qinc_load(25, sem, ano) +
            smp_qinc_load(28, sem, ano) +
            smp_qinc_load(31, sem, ano) +
            smp_qinc_load(32, sem, ano) +
            smp_qinc_load(33, sem, ano) +
            smp_qinc_load(205, sem, ano) +
            smp_qinc_load(206, sem, ano) +
            smp_qinc_load(207, sem, ano) +
            smp_qinc_load(209, sem, ano) +
            smp_qinc_load(251, sem, ano) +

            pvv_load(294, ano, sem, 0) +
            #pvv_load(241, ano, sem, 0) +
            pvv_load(247, ano, sem, 0) +
            #pvv_load(248, ano, sem, 0) +
            #rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            pvv_load(99, ano, sem, 0) +

            smp_qinc_load(117, sem, ano) +
            smp_qinc_load(119, sem, ano) +
            smp_qinc_load(160, sem, ano) +
            smp_qinc_load(161, sem, ano) +
            smp_qinc_load(237, sem, ano) +
            smp_qinc_load(238, sem, ano) +
            smp_qinc_load(239, sem, ano) +
            smp_qinc_load(240, sem, ano) +
            smp_qinc_load(242, sem, ano) +
            pvv_load(243, ano, sem, 0)

            # Paranapanema
            # smp_q_load(63, sem, ano) +
            # Paraná
            # pvv_load(34, ano, sem, 0) +
            # pvv_load(245, ano, sem, 0) +
            # pvv_load(246, ano, sem, 0) +
            # smp_q_load(266, sem, ano)
            # Grande
            # smp_q_load(18, sem, ano) +
            # Paranaíba
            # smp_q_load(33, sem, ano) +
            # pvv_load(99, ano, sem, 0) +
            # rgrs(241, pvv_load(294, ano, sem, 0), ano, sem) +
            # rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            # Tietê
            # smp_q_load(237, sem, ano) +
            # smp_q_load(239, sem, ano) +
            # smp_q_load(242, sem, ano) +
            # pvv_load(243, ano, sem, 0) +
        )
    elif pst == 301:
        return prv_ln(rgrs(301, smp_qinc_load(119, sem, ano), ano, sem))
    elif pst == 320:
        return prv_ln(smp_qinc_load(119, sem, ano))
    return prv_ln(smp_q_load(pst, sem, ano))

def pvv_v(pst, ano, sem):
    if pst == 2:
        return prv_ln(pvv_load(1, ano, sem, 0))
    elif pst == 7:
        return prv_ln(rgrs(7, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 8:
        return prv_ln(rgrs(8, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 9:
        return prv_ln(rgrs(9, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 10:
        return prv_ln(rgrs(10, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 11:
        return prv_ln(rgrs(11, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 12:
        return prv_ln(rgrs(12, pvv_load(6, ano, sem, 0), ano, sem))
    elif pst == 15:
        return prv_ln(rgrs(15, pvv_load(14, ano, sem, 0), ano, sem))
    elif pst == 16:
        return prv_ln(rgrs(16, pvv_load(14, ano, sem, 0), ano, sem))
    elif pst == 22:
        return prv_ln(rgrs(22, pvv_load(24, ano, sem, 0), ano, sem))
    elif pst == 23:
        return prv_ln(rgrs(23, pvv_load(205, ano, sem, 0), ano, sem))
    elif pst == 28:
        return prv_ln(rgrs(28, pvv_load(25, ano, sem, 0), ano, sem))
    elif pst == 32:
        return prv_ln(rgrs(32, pvv_load(31, ano, sem, 0), ano, sem))
    elif pst == 34:
        return prv_ln(
        pvv_load(34, ano, sem, 0)+
        pvv_load(18, ano, sem, 0)+
        pvv_load(33, ano, sem, 0)+
        pvv_load(99, ano, sem, 0)+
        rgrs(241, pvv_load(294, ano, sem, 0), ano, sem)+
        rgrs(261, pvv_load(247, ano, sem, 0), ano, sem)
        )
    elif pst == 48:
        return prv_ln(rgrs(48, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 49:
        return prv_ln(rgrs(49, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 50:
        return prv_ln(rgrs(50, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 51:
        return prv_ln(rgrs(51, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 52:
        return prv_ln(rgrs(52, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 62:
        return prv_ln(rgrs(62, pvv_load(63, ano, sem, 0), ano, sem))
    elif pst == 72:
        return prv_ln(rgrs(72, pvv_load(71, ano, sem, 0), ano, sem))
    elif pst == 76:
        return prv_ln(rgrs(76, pvv_load(74, ano, sem, 0), ano, sem))
    elif pst == 78:
        return prv_ln(rgrs(78, pvv_load(77, ano, sem, 0), ano, sem))
    elif pst == 81:
        return prv_ln(rgrs(81, pvv_load(77, ano, sem, 0), ano, sem))
    elif pst == 89:
        return prv_ln(rgrs(89, pvv_load(216, ano, sem, 0), ano, sem))
    elif pst == 94:
        return prv_ln(rgrs(94, pvv_load(92, ano, sem, 0), ano, sem))
    elif pst == 97:
        return prv_ln(rgrs(97, pvv_load(98, ano, sem, 0), ano, sem))
    elif pst == 103:
        return prv_ln(rgrs(103, pvv_load(102, ano, sem, 0), ano, sem))
    elif pst == 104:
        return prv_ln(pvv_load(117, ano, sem, 0) + rgrs(118, pvv_load(119, ano, sem, 0), ano, sem))
    elif pst == 109:
        return prv_ln(rgrs(118, pvv_load(119, ano, sem, 0), ano, sem))
    elif pst == 110:
        return prv_ln(rgrs(110, pvv_load(111, ano, sem, 0), ano, sem))
    elif pst == 112:
        return prv_ln(rgrs(112, pvv_load(111, ano, sem, 0), ano, sem))
    elif pst == 113:
        return prv_ln(rgrs(113, pvv_load(111, ano, sem, 0), ano, sem))
    elif pst == 114:
        return prv_ln(rgrs(114, pvv_load(111, ano, sem, 0), ano, sem))
    elif pst == 116:
        return prv_ln(rgrs(116, pvv_load(117, ano, sem, 0), ano, sem))
    elif pst == 118:
        return prv_ln(rgrs(118, pvv_load(119, ano, sem, 0), ano, sem))
    elif pst == 122:
        return prv_ln(rgrs(122, pvv_load(121, ano, sem, 0), ano, sem))
    elif pst == 123:
        return prv_ln(rgrs(123, pvv_load(125, ano, sem, 0), ano, sem))
    elif pst == 129:
        return prv_ln(rgrs(129, pvv_load(130, ano, sem, 0), ano, sem))
    elif pst == 141:
        return prv_ln(rgrs(141, pvv_load(144, ano, sem, 0), ano, sem))
    elif pst == 148:
        return prv_ln(rgrs(148, pvv_load(144, ano, sem, 0), ano, sem))
    elif pst == 154:
        return prv_ln(pvv_load(246, ano, sem, 0) * 0.152)
    elif pst == 155:
        return prv_ln(rgrs(155, pvv_load(156, ano, sem, 0), ano, sem))
    elif pst == 166:
        return prv_ln(
            pvv_load(63, ano, sem, 0) +
            pvv_load(245, ano, sem, 0) +
            pvv_load(246, ano, sem, 0) +
            pvv_load(266, ano, sem, 0) -
            pvv_load(61, ano, sem, 0)
            )
    elif pst == 183:
        return prv_ln(rgrs(183, pvv_load(262, ano, sem, 0), ano, sem))
    elif pst == 191:
        return prv_ln(rgrs(191, pvv_load(270, ano, sem, 0), ano, sem))
    elif pst == 198:
        return prv_ln(rgrs(198, pvv_load(197, ano, sem, 0), ano, sem))
    elif pst == 202:
        return prv_ln(rgrs(202, pvv_load(201, ano, sem, 0), ano, sem))
    elif pst == 203:
        return prv_ln(rgrs(203, pvv_load(201, ano, sem, 0), ano, sem))
    elif pst == 204:
        return prv_ln(rgrs(204, pvv_load(280, ano, sem, 0), ano, sem))
    elif pst == 206:
        return prv_ln(rgrs(206, pvv_load(25, ano, sem, 0), ano, sem))
    elif pst == 207:
        return prv_ln(rgrs(207, pvv_load(25, ano, sem, 0), ano, sem))
    elif pst == 217:
        return prv_ln(rgrs(217, pvv_load(92, ano, sem, 0), ano, sem))
    elif pst == 222:
        return prv_ln(rgrs(222, pvv_load(77, ano, sem, 0), ano, sem))
    elif pst == 227:
        return prv_ln(rgrs(227, pvv_load(229, ano, sem, 0), ano, sem))
    elif pst == 228:
        return prv_ln(rgrs(228, pvv_load(229, ano, sem, 0), ano, sem))
    elif pst == 230:
        return prv_ln(rgrs(230, pvv_load(229, ano, sem, 0), ano, sem))
    elif pst == 238:
        return prv_ln(pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) * 0.342)
    elif pst == 239:
        return prv_ln(pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0))
    elif pst == 240:
        v239 = pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0)
        v240 = pvv_load(242, ano, sem, 0) * 0.717
        return prv_ln(v239 + v240)
    elif pst == 241:
        return prv_ln(rgrs(241, pvv_load(294, ano, sem, 0), ano, sem))
    elif pst == 242:
        return prv_ln(pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) + pvv_load(242, ano, sem, 0))
    elif pst == 243:
        return prv_ln(pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) + pvv_load(242, ano, sem, 0) + pvv_load(243, ano, sem, 0))
    elif pst == 244:
        return prv_ln(
            pvv_load(34, ano, sem, 0) +
            pvv_load(18, ano, sem, 0) +
            pvv_load(33, ano, sem, 0) +
            pvv_load(99, ano, sem, 0) +
            rgrs(241, pvv_load(294, ano, sem, 0), ano, sem) +
            rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) + pvv_load(242, ano, sem, 0) + pvv_load(243, ano, sem, 0)
        )
    elif pst == 245:
        return prv_ln(
            pvv_load(34, ano, sem, 0) +
            pvv_load(18, ano, sem, 0) +
            pvv_load(33, ano, sem, 0) +
            pvv_load(99, ano, sem, 0) +
            rgrs(241, pvv_load(294, ano, sem, 0), ano, sem) +
            rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) + pvv_load(242, ano, sem, 0) + pvv_load(243, ano, sem, 0) +
            pvv_load(245, ano, sem, 0)
        )
    elif pst == 246:
        return prv_ln(
            pvv_load(34, ano, sem, 0) +
            pvv_load(18, ano, sem, 0) +
            pvv_load(33, ano, sem, 0) +
            pvv_load(99, ano, sem, 0) +
            rgrs(241, pvv_load(294, ano, sem, 0), ano, sem) +
            rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            pvv_load(237, ano, sem, 0) + pvv_load(239, ano, sem, 0) + pvv_load(242, ano, sem, 0) + pvv_load(243, ano, sem, 0) +
            pvv_load(245, ano, sem, 0) +
            pvv_load(246, ano, sem, 0)
        )
    elif pst == 248:
        return prv_ln(rgrs(248, pvv_load(247, ano, sem, 0), ano, sem))
    elif pst == 249:
        return prv_ln(rgrs(249, pvv_load(47, ano, sem, 0), ano, sem))
    elif pst == 251:
        return prv_ln(rgrs(251, pvv_load(24, ano, sem, 0), ano, sem))
    elif pst == 252:
        return prv_ln(rgrs(252, pvv_load(259, ano, sem, 0), ano, sem))
    elif pst == 253:
        return prv_ln(rgrs(253, pvv_load(270, ano, sem, 0), ano, sem))
    elif pst == 261:
        return prv_ln(rgrs(261, pvv_load(247, ano, sem, 0), ano, sem))
    elif pst == 266:
        return prv_ln(
            pvv_load(63, ano, sem, 0) +
            pvv_load(34, ano, sem, 0) +
            pvv_load(18, ano, sem, 0) +
            pvv_load(33, ano, sem, 0) +
            pvv_load(99, ano, sem, 0) +
            rgrs(241, pvv_load(294, ano, sem, 0), ano, sem) +
            rgrs(261, pvv_load(247, ano, sem, 0), ano, sem) +
            pvv_load(237, ano, sem, 0) +
            pvv_load(239, ano, sem, 0) +
            pvv_load(242, ano, sem, 0) +
            pvv_load(243, ano, sem, 0) +
            pvv_load(245, ano, sem, 0) +
            pvv_load(246, ano, sem, 0) +
            pvv_load(266, ano, sem, 0)
            )
    elif pst == 263:
        return prv_ln(rgrs(263, pvv_load(134, ano, sem, 0), ano, sem))
    elif pst == 273:
        return prv_ln(rgrs(273, pvv_load(257, ano, sem, 0), ano, sem))
    elif pst == 284:
        return prv_ln(rgrs(284, pvv_load(98, ano, sem, 0), ano, sem))
    elif pst == 285:
        return prv_ln(rgrs(285, pvv_load(287, ano, sem, 0), ano, sem))
    elif pst == 297:
        return prv_ln(rgrs(297, pvv_load(280, ano, sem, 0), ano, sem))
    elif pst == 301:
        return prv_ln(rgrs(301, pvv_load(119, ano, sem, 0), ano, sem))
    elif pst == 320:
        return prv_ln(pvv_load(119, ano, sem, 0))
    else:
        return prv_ln(pvv_load(pst, ano, sem, 0))





prevs_dt = dt_prevs(dt_today(), 7)
sem_atual = dt_conv_smn(dt_today())
#print(prevs_dt)
#print(sem_atual)
if sem_calc(sem_atual[0], sem_atual[1], 1) == sem_calc(prevs_dt[0][0], prevs_dt[0][1], 0):
    col_ini = 1
else:
    for s_idx in range(0, len(prevs_dt)):
        print(sem_atual, prevs_dt[s_idx])
        if sem_atual[0] == prevs_dt[s_idx][0] and sem_atual[1] == prevs_dt[s_idx][1]:
            col_ini = -s_idx
limite = 0
fn = os.path.join(os.getcwd(), "prevs.txt")
pf = open(fn, 'wt')
for p_idx in range(0, len(prevs_pst)):
    pf.write(prv_ln_ini(p_idx + 1, prevs_pst[p_idx][0]))
    posto = prevs_pst[p_idx][0]
    tipo = prevs_pst[p_idx][1]
    for s_idx in range(col_ini, col_ini + 6):
        s_tmp = sem_calc(sem_atual[0], sem_atual[1], s_idx)
        semana = s_tmp[0]
        ano = s_tmp[1]
        print("Posto: ", posto, "Tipo: ", tipo, "Indice: ", s_idx, "Ano: ", ano, "Semana: ", semana)
        # Atualiza as colunas do prevs com valores do Acomph
        if s_idx < 0:
            #print("1")
            # Retorna valor do Acomph
            v_tmp = past_v(posto, ano, semana)
        # Atualiza as colunas do prevs com valores do Acomph ou Smap
        elif s_idx == 0:
            if tipo == 0:
                #print("2")
                # Retorna valor do Acomph
                v_tmp = past_v(posto, ano, semana)
            else:
                #print("3")
                # Retorna valor do Smap
                v_tmp = smp_v(posto, ano, semana)
        # Atualiza as colunas do prevs com valores do Smap ou Previvaz
        elif s_idx == 1:
            if tipo == 0:
                #print("4")
                # Retorna valor do Previvaz
                v_tmp = pvv_v(posto, ano, semana)
            else:
                #print("5")
                # Retorna valor do Smap
                v_tmp = smp_v(posto, ano, semana)
        # Atualiza as colunas do prevs com valores do Previvaz
        else:
            #print("6")
            v_tmp = pvv_v(posto, ano, semana)
        pf.write(v_tmp)
    pf.write("\n")


