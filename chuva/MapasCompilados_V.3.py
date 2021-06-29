import datetime
import ftplib
import math
import os
import shutil
import struct
import time
import urllib
import urllib.request
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Na Versao 3.0:
# - Inserido o modelo de previsao ECMWF
# - Modificada a matriz do modelo de previsao ETA40, com compreensao de lista
# - Modificada a grade do modelo de previsao GEFS
# - Modelo GEFS nao mais por interpolacao
# - Inserido paradigma POO para os modelos de precipitacao

modelo_eta40 = Modelo('Prev_ETA40_ONS', xdef, ydef, grid, 'Eta40_precipitacao10d.zip') 
modelo_gefs = Modelo('Prev_GEFS_ONS', xdef, ydef, grid, '.zip') 
modelo_ecmwf = Modelo('Prev_ECMWF_ONS', xdef, ydef, grid, '.zip') 

class Modelos:

    def __init__(self, modelo, xdef, ydef, grid, url):

        self.nome = modelo
        self.xdef = xdef
        self.ydef = ydef
        self.grid = grid
        self.url = url

    def __repr__(self):

        print(self.nome)

    def conv_dat_to_bin(self):

        verify_folder(self.nome)

        if (log_date(self.nome) != today()):
            
            download_chuva_eta40_ons(self.nome, self.url) == 1):


            index_1 = tuple((x * a + i) for i in range(a) for x in range(b))
            index_2 = tuple(x for x in range(a*b))
            index = [eta_index, gefs_index]
            folder = modelo[2]
            path_list = os.listdir(folder)
            condicao = 0

            for file in path_list:
                if file.endswith('.dat'):
                    eta_file = open(os.path.join(os.path.dirname(__file__), folder, file), 'rt')
                    file_content = eta_file.readlines()
                    bin_file = open(os.path.join(os.path.dirname(__file__), folder, file[0:len(file) - 4] + '.bin'), 'wb')
                    cnt = 0
                    for _ in range(0, a):
                        for _ in range(0, b):
                            if not condicao:
                                # var = struct.pack('f', float(file_content[index[modelo[3]][cnt]][14:19]))
                                # print(var, len(var))
                                condicao += 1
                            bin_file.write(struct.pack('f', float(file_content[index[modelo[3]][cnt]][14:19])))
                            cnt += 1
                    eta_file.close()
                    bin_file.close()


            
            for i in range(1,2):
                soma_arq_bin(self.nome, create_name_list(i), 'soma_eta40_1.bin', self.xdef * self.ydef) == 1):
                #soma_arq_bin('Prev_ETA_ONS', create_name_list(2), 'Prev_ETA_ONS', 'soma_eta40_2.bin', self.xdef * self.ydef) == 1):

            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'Prev_ETA_ONS/soma_eta40_2.bin'), os.path.join(os.path.dirname(__file__), 'Prev_Quinta', nome_aux))
            print('Chuva ETA 40: OK')
            edit_log_file('Chuva ETA 40', '')





    def sum_arq_bin(self):

    def gera_mapas(self):

        if (log_date(f'Chuva_{self.nome}') == today() and log_date(f'Mapas_{self.nome}') != today()):
            
            leg = f'{self.nome}'
            t1 = 'Previsao Semana Operativa'
            t2 = d0 + ' a ' + d3
            gera_mapas(t1, t2, leg, 'Prev_ETA_ONS', 'soma_eta40_1.bin', os.path.join('.'), 'eta_1_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            t1 = 'Previsao Proxima Semana Operativa'
            t2 = d4 + ' a ' + d5
            gera_mapas(t1, t2, leg, 'Prev_ETA_ONS', 'soma_eta40_2.bin', os.path.join('.'), 'eta_2_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            print('      Mapas_ETA: OK')
            edit_log_file('Mapas_ETA', '')


def conv_100_100_x_40_40(path, arq_bin):
    #x_eta_init = -83.0
    #x_eta_step = 0.4
    #x_eta_size = 144
    #y_eta_init = -50.2
    #y_eta_step = 0.4
    #y_eta_size = 157

    x_eta_init = -82.6
    x_eta_step = 0.4
    x_eta_size = 121
    y_eta_init = -50.2
    y_eta_step = 0.4
    y_eta_size = 157

    x_gefs_init = -99.0
    x_gefs_step = 1.0
    #x_gefs_size = 80
    y_gefs_init = -60.0
    y_gefs_step = 1.0
    #y_gefs_size = 81

    gefs = open(os.path.join(os.path.dirname(__file__), path, arq_bin), 'rt')
    gefs_read = gefs.readlines()
    bin_file = open(os.path.join(os.path.dirname(__file__), path, arq_bin[0:len(arq_bin)-4] + '.bin'), 'wb')
    gefs_file = []
    for gefs_idx in range(0, len(gefs_read)):
        gefs_file.append([])
        gefs_file[gefs_idx].append(float(gefs_read[gefs_idx][0:6]))
        gefs_file[gefs_idx].append(float(gefs_read[gefs_idx][7:13]))
        gefs_file[gefs_idx].append(float(gefs_read[gefs_idx][14:19]))
    tst = 0
    for cnt_y in range(0, y_eta_size):
        for cnt_x in range(0, x_eta_size):
            eta_x = x_eta_init + (x_eta_step * float(cnt_x))
            eta_y = y_eta_init + (y_eta_step * float(cnt_y))
            x_gefs_coef = round((eta_x - x_gefs_init) / x_gefs_step, 0)
            y_gefs_coef = round((eta_y - y_gefs_init) / y_gefs_step, 0)
            x_gefs_prox = x_gefs_init + (x_gefs_step * x_gefs_coef)
            y_gefs_prox = y_gefs_init + (y_gefs_step * y_gefs_coef)
            if (abs(eta_x - x_gefs_prox) < 0.001 and abs(eta_y - y_gefs_prox) < 0.001):
                for gefs_idx in range(0, len(gefs_file)):
                    if (abs(gefs_file[gefs_idx][0] - x_gefs_prox) < 0.001 and abs(gefs_file[gefs_idx][1] - y_gefs_prox) < 0.001):
                        v = gefs_file[gefs_idx][2]
                        break
            elif (abs(eta_x - x_gefs_prox) < 0.001):
                if(eta_y > y_gefs_prox):
                    p_var_y_x = x_gefs_prox
                    p_var_y_y = y_gefs_prox + y_gefs_step
                else:
                    p_var_y_x = x_gefs_prox
                    p_var_y_y = y_gefs_prox - y_gefs_step
                check_v = 0
                for gefs_idx in range(0, len(gefs_file)):
                    if (abs(gefs_file[gefs_idx][0] - x_gefs_prox) < 0.001 and abs(gefs_file[gefs_idx][1] - y_gefs_prox) < 0.001):
                        v1 = gefs_file[gefs_idx][2]
                        check_v += 1
                    elif (abs(gefs_file[gefs_idx][0] - p_var_y_x) < 0.001 and abs(gefs_file[gefs_idx][1] - p_var_y_y) < 0.001):
                        v2 = gefs_file[gefs_idx][2]
                        check_v += 1
                    if(check_v == 2):
                        break
                d1 = math.sqrt((x_gefs_prox - eta_x) ** 2 + (y_gefs_prox - eta_y) ** 2)
                d2 = math.sqrt((p_var_y_x - eta_x) ** 2 + (p_var_y_y - eta_y) ** 2)
                v = ((1 / d1) * v1 + (1 / d2) * v2) / ((1 / d1) + (1 / d2))
            elif (abs(eta_y - y_gefs_prox) < 0.001):
                if(eta_x > x_gefs_prox):
                    p_var_x_x = x_gefs_prox + x_gefs_step
                    p_var_x_y = y_gefs_prox
                else:
                    p_var_x_x = x_gefs_prox - x_gefs_step
                    p_var_x_y = y_gefs_prox
                check_v = 0
                for gefs_idx in range(0, len(gefs_file)):
                    if (abs(gefs_file[gefs_idx][0] - x_gefs_prox) < 0.001 and abs(gefs_file[gefs_idx][1] - y_gefs_prox) < 0.001):
                        v1 = gefs_file[gefs_idx][2]
                        check_v += 1
                    elif (abs(gefs_file[gefs_idx][0] - p_var_x_x) < 0.001 and abs(gefs_file[gefs_idx][1] - p_var_x_y) < 0.001):
                        v2 = gefs_file[gefs_idx][2]
                        check_v += 1
                    if(check_v == 2):
                        break
                d1 = math.sqrt((x_gefs_prox - eta_x) ** 2 + (y_gefs_prox - eta_y) ** 2)
                d2 = math.sqrt((p_var_x_x - eta_x) ** 2 + (p_var_x_y - eta_y) ** 2)
                v = ((1 / d1) * v1 + (1 / d2) * v2) / ((1 / d1) + (1 / d2))
            else:
                if (eta_y > y_gefs_prox):
                    p_var_y_x = x_gefs_prox
                    p_var_y_y = y_gefs_prox + y_gefs_step
                else:
                    p_var_y_x = x_gefs_prox
                    p_var_y_y = y_gefs_prox - y_gefs_step
                if (eta_x > x_gefs_prox):
                    p_var_x_x = x_gefs_prox + x_gefs_step
                    p_var_x_y = y_gefs_prox
                else:
                    p_var_x_x = x_gefs_prox - x_gefs_step
                    p_var_x_y = y_gefs_prox
                p_var_d_x = p_var_x_x
                p_var_d_y = p_var_y_y
                check_v = 0
                for gefs_idx in range(0, len(gefs_file)):
                    if (abs(gefs_file[gefs_idx][0] - x_gefs_prox) < 0.001 and abs(gefs_file[gefs_idx][1] - y_gefs_prox) < 0.001):
                        v1 = gefs_file[gefs_idx][2]
                        check_v += 1
                    elif (abs(gefs_file[gefs_idx][0] - p_var_x_x) < 0.001 and abs(gefs_file[gefs_idx][1] - p_var_x_y) < 0.001):
                        v2 = gefs_file[gefs_idx][2]
                        check_v += 1
                    elif (abs(gefs_file[gefs_idx][0] - p_var_y_x) < 0.001 and abs(gefs_file[gefs_idx][1] - p_var_y_y) < 0.001):
                        v3 = gefs_file[gefs_idx][2]
                        check_v += 1
                    elif (abs(gefs_file[gefs_idx][0] - p_var_d_x) < 0.001 and abs(gefs_file[gefs_idx][1] - p_var_d_y) < 0.001):
                        v4 = gefs_file[gefs_idx][2]
                        check_v += 1
                    if(check_v == 4):
                        break
                d1 = math.sqrt((x_gefs_prox - eta_x) ** 2 + (y_gefs_prox - eta_y) ** 2)
                d2 = math.sqrt((p_var_x_x - eta_x) ** 2 + (p_var_x_y - eta_y) ** 2)
                d3 = math.sqrt((p_var_y_x - eta_x) ** 2 + (p_var_y_y - eta_y) ** 2)
                d4 = math.sqrt((p_var_d_x - eta_x) ** 2 + (p_var_d_y - eta_y) ** 2)
                v = ((1 / d1) * v1 + (1 / d2) * v2 + (1 / d3) * v3 + (1 / d4) * v4) / ((1 / d1) + (1 / d2) + (1 / d3) + (1 / d4))
            #print('%i / %.f' % (tst, v))
            bin_file.write(struct.pack('f', v))
            tst += 1

def gera_mapas(t1, t2, lgd, path, file_name, folder, img_name, x_def = str(), y_def = str()):
    #Cria arquivo CTL
    ctl = open(os.path.join(os.path.dirname(__file__), path, 'ctl.ctl'), 'wt')
    ctl.write('DSET %s\n' % os.path.join(os.path.dirname(__file__), path, file_name))
    ctl.write('UNDEF -9999.\n')
    ctl.write('TITLE 29help Days of Sample Model Output\n')
    ctl.write('%s\n' % x_def)
    ctl.write('%s\n' % y_def)
    ctl.write('ZDEF   1 LEVELS 1000\n')
    ctl.write('TDEF   1 LINEAR 12Z19Apr2017 24hr\n')
    ctl.write('VARS  1\n')
    ctl.write('PREC    0  99     Total  24h Precip.        (m)\n')
    ctl.write('ENDVARS\n')
    ctl.close()

    #Cria arquivo GS (Script)
    script_mapas =  open('C:/OpenGrADS-2.2/Contents/Resources/SampleDatasets/script_mapas.gs', 'wt')
    script_mapas.writelines("'reinit'\n")
    script_mapas.writelines("'open %s'\n" % os.path.join(os.path.dirname(__file__), path, 'ctl.ctl'))
    script_mapas.writelines("'set display color white'\n")  
    script_mapas.writelines("'set rgb 16 224 255 255'\n")
    script_mapas.writelines("'set rgb 17 179 239 251'\n")
    script_mapas.writelines("'set rgb 18 151 210 247'\n")
    script_mapas.writelines("'set rgb 19 35 132 238'\n")
    script_mapas.writelines("'set rgb 20 22 101 202'\n")
    script_mapas.writelines("'set rgb 21 103 253 131'\n")
    script_mapas.writelines("'set rgb 22 12 221 1'\n")
    script_mapas.writelines("'set rgb 23 26 181 27'\n")
    script_mapas.writelines("'set rgb 24 253 233 118'\n")
    script_mapas.writelines("'set rgb 25 255 187 66'\n")
    script_mapas.writelines("'set rgb 26 255 93 0'\n")
    script_mapas.writelines("'set rgb 27 228 18 0'\n")
    script_mapas.writelines("'set rgb 28 255 86 107'\n")
    script_mapas.writelines("'set vpage 0.2 8.5 0 11'\n")
    script_mapas.writelines("'set parea off'\n") 
    script_mapas.writelines("'set mpt 1 1 1 1'\n")
    script_mapas.writelines("'set mpdset amsulrp'\n")
    script_mapas.writelines("'clear'\n")
    script_mapas.writelines("'set timelab off'\n")
    script_mapas.writelines("'set grads off'\n")    
    script_mapas.writelines("'set lon -75 -34.6'\n") # Define marcacoes do eixo x do mapa
    script_mapas.writelines("'set lat -35 5'\n") # Define marcacoes do eixo y do mapa
    script_mapas.writelines("'set map 1 1 4'\n")
    script_mapas.writelines("'set mpdraw on'\n")
    script_mapas.writelines("'set csmooth on'\n")
    script_mapas.writelines("'set gxout shade2'\n")
    script_mapas.writelines("'set clevs  0 1 5 10 15 20 25 30 40 50 75 100 150 200'\n")
    script_mapas.writelines("'set ccols  0 16 17 18 19 20 21 22 23 24 25 26 27 28 15'\n")
    script_mapas.writelines("'d prec'\n")
    script_mapas.writelines("'cbarn 1 0'\n") # Define o tamano e posicao da barra de escala "run cbarn sf vert xmid ymid" , sf   - scale the whole bar 1.0 = original 0.5 half the size, etc., vert - 0 FORCES a horizontal bar = 1 a vertical bar
    script_mapas.writelines("'set lon -80 -35'\n")
    script_mapas.writelines("'set lat -40 10'\n")
    script_mapas.writelines("'set map 1 1 4'\n")
    script_mapas.writelines("'set mpdraw on'\n")
    script_mapas.writelines("'set csmooth on'\n")
    script_mapas.writelines("'set gxout shade2'\n")
    script_mapas.writelines("'set rgb 30 70 70 70'\n")
    script_mapas.writelines("'set line 30 1 1 0'\n") # Define a cor da linha das bacias hidrográficas
    script_mapas.writelines("'draw shp bacias-hidrograficas'\n") # Abre o arquivo bacias-hidrograficas.shp com o shape das bacias
    #script_mapas.writelines("'draw xlab %s'\n" % lgd)
    script_mapas.writelines("'draw title {}\ {}\{}'\n".format(lgd, t1, t2))
    script_mapas.writelines("'printim %s/%s.png x600 y800'\n" %(os.path.join(os.path.dirname(__file__), folder), img_name[0:len(img_name) - 4]))
    script_mapas.close()
    os.chdir('C:/OpenGrADS-2.2/Contents/Resources/SampleDatasets/')
    os.system('C:/OpenGrADS-2.2/Contents/Cygwin/Versions/2.2.1.oga.1/i686/gradsgui.exe -pcbx script_mapas.gs')
    #os.remove(os.path.join(os.path.dirname(__file__), path, 'ctl.ctl'))

def download_chuva():
    if(erro == 0):
        zip = zipfile.ZipFile(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        fn_list = zip.namelist()
        zip.extractall(os.path.join(os.path.dirname(__file__), out_path))
        zip.close()
        os.remove(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
        td = datetime.date.fromordinal(today())
        dt_comp = 'ETA40_p' + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'

def download_chuva_ocorrida_cptec(out_files_path):
    erro = 0
    servidor = "ftp1.cptec.inpe.br"
    pre_path = '/modelos/io/produtos/MERGE/'
    folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_files_path))
    for fn in folder_list:
        #if (fn[0:5] == 'prec_'):
        os.remove(os.path.join(os.path.dirname(__file__), out_files_path, fn))
    try:
        ftp = ftplib.FTP(servidor)
    except:
        erro += 1
        print("     Erro - download_chuva_ocorrida: Nao foi possivel encontrar o servidor")
    if (erro == 0):
        try:
            ftp.login()
        except:
            erro += 1
            print("     Erro - download_chuva_ocorrida: Nao foi possivel conectar ao servidor")
        if(erro == 0):
            ano_ini = 0
            for i in range(so_ini(), today()): #Alterar a condição para no sábado gerar o mapa com a chuva acumulada da Sem Op
                data_tmp = datetime.date.fromordinal(i)
                if(ano_ini != data_tmp.year):
                    folder_aux = pre_path + str(data_tmp.year)
                    try:
                        ftp.cwd(folder_aux)
                    except:
                        erro += 1
                        print("     Erro - download_chuva_ocorrida: Pasta %s nao encontrada" % folder_aux)
                        break
                    else:
                        ano_ini = data_tmp.year
                if (erro == 0):
                    filename = "prec_" + str(data_tmp.year) + ('0' + str(data_tmp.month))[-2:] + ('0' + str(data_tmp.day))[-2:] + ".bin"
                    file = open(os.path.join(os.path.dirname(__file__), out_files_path,  filename), 'wb')
                    try:
                        ftp.retrbinary('RETR ' + filename, file.write)
                    except:
                        erro += 1
                        print("     Erro - download_chuva_ocorrida: Arquivo %s nao esta pronto" % filename)
                        file.close()
                        os.remove(os.path.join(os.path.dirname(__file__), out_files_path + '/' + filename))
                        break
                    else:
                        #print("   Download arquivo chuva ocorrida: %s" % filename)
                        file.close()
                        file_w = open(os.path.join(os.path.dirname(__file__), out_files_path, 'tmp.bin'), 'wb')
                        file_r = open(os.path.join(os.path.dirname(__file__), out_files_path, filename), 'rb')
                        for a in range(1, 314):
                            for b in range(1, 246):
                                tmp = struct.unpack('f', file_r.read(4))[0]
                                if (b <= 242 and (b % 2) == 0 and (a % 2) != 0):
                                    file_w.write(struct.pack('f', tmp))
                        file_r.close()
                        file_w.close()
                        os.remove(os.path.join(os.path.dirname(__file__), out_files_path, filename))
                        os.rename(os.path.join(os.path.dirname(__file__), out_files_path, 'tmp.bin'), os.path.join(os.path.dirname(__file__), out_files_path, filename))
                        time.sleep(0.7)
        ftp.quit()
    if(erro == 0):
        return 1
    else:
        return 0

def download_chuva_eta40_ons(out_path, url_eta):
    eta_index = tuple((x * 157 + i) for i in range(156+1) for x in range(143+1))
    #url_eta = 'http://pactoenergia.com.br/mdl/mapas/' + url_eta
    #out_file_name = 'eta40.zip'
    erro = 0
    folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
    for fn in folder_list:
        os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
    try:
        os.path.isfile(os.path.join(os.path.dirname(__file__), out_path, fn))
    except:
        erro += 1
        print('Erro - arquivo_chuva: Nao foi possivel localizar o arquivo de chuva do ETA')
        print('   ' + url_eta)
    if(erro == 0):
        zip = zipfile.ZipFile(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        fn_list = zip.namelist()
        zip.extractall(os.path.join(os.path.dirname(__file__), out_path))
        zip.close()
        os.remove(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
        td = datetime.date.fromordinal(today())
        dt_comp = 'ETA40_p' + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'
        for fn in folder_list:
            if (fn[0:14] != dt_comp):
                erro += 1
                print('   Erro - download_chuva: Chuva nao atualizada')
                break
        if (erro == 0):
            #Converte os arquivos de texto para binario
            for fn in fn_list:
                eta = open(os.path.join(os.path.dirname(__file__), out_path, fn), 'rt')
                eta_read = eta.readlines()
                bin_file = open(os.path.join(os.path.dirname(__file__), out_path, fn[0:len(fn) - 4] + '.bin'), 'wb')
                
                ##########################################
                eta_cnt = 0
                for _ in range(0, 157):
                    for b in range(0, 144):
                        if (b >= 1 and b <= 121):
                            bin_file.write(struct.pack('f', float(eta_read[eta_index[eta_cnt]][14:19])))
                        eta_cnt += 1
                #########################################
                
                eta.close()
                bin_file.close()
                os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
                time.sleep(0.7)
    if(erro == 0):
        return 1
    else:
        return 0

def download_chuva_gefs_ons(out_path, url_gefs):
    url_gefs = 'http://pactoenergia.com.br/mdl/mapas/' + url_gefs
    out_file_name = 'gefs.zip'
    erro = 0
    folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
    for fn in folder_list:
        #if (fn[0:5] == 'GEFS_'):
        os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
    try:
        urllib.request.urlretrieve(url_gefs, os.path.join(os.path.dirname(__file__), out_path, out_file_name))
    except:
        erro += 1
        print('   Erro - download_chuva: Nao foi possivel acessar o link para chuva do GEFS')
        print('   ' + url_gefs)
    if(erro == 0):
        zip = zipfile.ZipFile(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        fn_list = zip.namelist()
        zip.extractall(os.path.join(os.path.dirname(__file__), out_path))
        zip.close()
        os.remove(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
        td = datetime.date.fromordinal(today())
        dt_comp = 'GEFS_p' + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'
        for fn in folder_list:
            if (fn[0:13] != dt_comp):
                erro += 1
                print('   Erro - download_chuva: Chuva nao atualizada')
                break
        if (erro == 0):
            # Converte os arquivos de texto para binario (Adicionar Alteração)
            for fn in fn_list:
                conv_100_100_x_40_40(out_path, fn)
                os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
    if(erro == 0):
        return 1
    else:
        return 0

def download_chuva_ecmwf_ons(out_path, url_ecmwf):
    ecmwf_index = tuple(x for x in range(301*376))
    url_ecmwf = 'http://pactoenergia.com.br/mdl/mapas/' + url_ecmwf
    out_file_name = 'ecmwf.zip'
    erro = 0
    folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
    for fn in folder_list:
        #if (fn[0:6] == 'ETA40_'):
        os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
    try:
        urllib.request.urlretrieve(url_ecmwf, os.path.join(os.path.dirname(__file__), out_path, out_file_name))
    except:
        erro += 1
        print('   Erro - download_chuva: Nao foi possivel acessar o link para chuva do ECMWF')
        print('   ' + url_ecmwf)
    if(erro == 0):
        zip = zipfile.ZipFile(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        fn_list = zip.namelist()
        zip.extractall(os.path.join(os.path.dirname(__file__), out_path))
        zip.close()
        os.remove(os.path.join(os.path.dirname(__file__), out_path, out_file_name))
        folder_list = os.listdir(os.path.join(os.path.dirname(__file__), out_path))
        td = datetime.date.fromordinal(today())
        dt_comp = 'ECMWF_p' + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'
        for fn in folder_list:
            if (fn[0:14] != dt_comp):
                erro += 1
                print('   Erro - download_chuva: Chuva nao atualizada')
                break
        if (erro == 0):
            #Converte os arquivos de texto para binario
            for fn in fn_list:
                eta = open(os.path.join(os.path.dirname(__file__), out_path, fn), 'rt')
                eta_read = eta.readlines()
                bin_file = open(os.path.join(os.path.dirname(__file__), out_path, fn[0:len(fn) - 4] + '.bin'), 'wb')
                ##########################################
                cnt = 0
                for _ in range(0, 301):
                    for _ in range(0, 376):
                        bin_file.write(struct.pack('f', float(eta_read[ecmwf_index[cnt]][14:22])))
                        cnt += 1
                #########################################
                eta.close()
                bin_file.close()
                os.remove(os.path.join(os.path.dirname(__file__), out_path, fn))
                time.sleep(0.7)
    if(erro == 0):
        return 1
    else:
        return 0

def soma_arq_bin(in_files_path, in_files_list, out_file_path, out_file_name, size):
    if(not os.path.exists(os.path.join(os.path.dirname(__file__), in_files_path))):
        print('   Erro - soma_arq_bin: Pasta com arquivos de entrada nao existe')
    else:
        os.chdir(os.path.join(os.path.dirname(__file__), in_files_path))
        not_found_error = 0
        for fn in in_files_list:
            if (not os.path.isfile(os.path.join(os.path.dirname(__file__), in_files_path, fn))):
                not_found_error += 1
                print('   Erro - soma_arq_bin: Arquivo %s nao encontrado' % fn)
        if(not_found_error > 0):
            return 0
        else:
            soma = []
            for a in range(size):
                soma.append(0)
            for fn in in_files_list:
                fbin = open(fn, "rb")
                for cnt_aux in range(0, size):
                    tmp = struct.unpack('f', fbin.read(4))[0]
                    soma[cnt_aux] += tmp
                fbin.close()
                #print('   Arquivo somado: %s' %fn)
            fsoma = open(os.path.join(os.path.dirname(__file__), out_file_path, out_file_name), "wb")
            for a in range(size):
                fsoma.write(struct.pack('f', soma[a]))
            fsoma.close()
            return 1

def create_name_list(opt):
    #Funcao que cria o titulo com o nome dos mapas e as semanas

    names_list = []
    td = datetime.date.fromordinal(today())
    if(opt == 0):
        #Chuva Ocorrida "0"
        for dt in range(so_ini(), today()):
            dt_aux = datetime.date.fromordinal(dt)
            name = 'prec_' + (str(dt_aux.year) + ('00' + str(dt_aux.month))[-2:] + ('00' + str(dt_aux.day))[-2:]) + '.bin'
            names_list.append(name)
    elif(opt == 1 or opt == 3 or opt == 5):
        #Chuva Primeira Semana ETA40 "1" / Chuva Primeira Semana GEFS "3"
        if(opt == 1):
            prefix = 'ETA40_p'
        elif(opt == 3):
            prefix = 'GEFS_p'
        else:
            prefix = 'ECMWF_p'
        p1 = prefix + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'
        for dt in range(today(), so_ini() + 7):
            dt_aux = datetime.date.fromordinal(dt + 1)
            p2 = (('00' + str(dt_aux.day))[-2:] + ('00' + str(dt_aux.month))[-2:] + str(dt_aux.year)[-2:]) + '.bin'
            name = p1 + p2
            names_list.append(name)
    elif (opt == 2 or opt == 4 or opt == 6):
        # Chuva Segunda Semana ETA40 "2" / Chuva Segunda Semana GEFS "4"
        if (opt == 2):
            prefix = 'ETA40_p'
        elif (opt == 4):
            prefix = 'GEFS_p'
        else:
            prefix = 'ECMWF_p'
        if(today() + 10 > so_ini() + 14):
            dt_aux_2 = so_ini() + 14
        else:
            dt_aux_2 = today() + 10
        p1 = prefix + (('00' + str(td.day))[-2:] + ('00' + str(td.month))[-2:] + str(td.year)[-2:]) + 'a'
        for dt in range(so_ini() + 7, dt_aux_2):
            dt_aux = datetime.date.fromordinal(dt + 1)
            p2 = (('00' + str(dt_aux.day))[-2:] + ('00' + str(dt_aux.month))[-2:] + str(dt_aux.year)[-2:]) + '.bin'
            name = p1 + p2
            names_list.append(name)
    return names_list

def str_dt(opt = 0):
    if(opt == 0):
        date_aux = datetime.date.fromordinal(today())
    else:
        date_aux = datetime.date.fromordinal(opt)
    return ('00' + str(date_aux.day))[-2:] + '/' + ('00' + str(date_aux.month))[-2:] + '/' + str(date_aux.year)

def verify_folder(folder):

    #Verifica se existe a pasta de execução e cria
    if not os.path.exists(os.path.join(os.path.dirname(__file__), folder)):
        os.makedirs(os.path.join(os.path.dirname(__file__), folder))

def upload_zips(path_name):
    time.sleep(30)
    folder_list = os.listdir(path_name)
    upload_list = [f for f in folder_list if f.endswith('.zip')]
    ftp = ftplib.FTP('pactoenergia.com.br', 'mdl@pactoenergia.com.br', '29!pAcTo+16')
    ftp.cwd('mapas')
    for f in upload_list:
        try:
            file = open(os.path.join(path_name, f), 'rb')
            ftp.storbinary('STOR ' + f, file)
            print("   Arquivo Uploaded: %s" %f)
            file.close()
        except IOError:
            continue
    ftp.quit()
    for fn in upload_list:
        os.remove(os.path.join(path_name, fn))

def upload_file(path, fn):
    ftp = ftplib.FTP('pactoenergia.com.br', 'mdl@pactoenergia.com.br', '29!pAcTo+16')
    ftp.cwd('mapas')
    file = open(os.path.join(os.path.dirname(__file__), path, fn), 'rb')
    ftp.storbinary('STOR ' + fn, file)
    file.close()
    ftp.quit()
    print("   Arquivo %s uploaded" %fn)

#Funcoes de data e hora
def today():
    #dia = 21
    #mes = 6
    #ano = 2017
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    ano = datetime.datetime.now().year
    return datetime.date.toordinal(datetime.date(ano, mes, dia))

def str_now():
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    return (('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:])

def week_day():
    dt_aux = datetime.date.fromordinal(today())
    return dt_aux.weekday()

def so_ini():
    d_semana = (2, 3, 4, 5, 6, 0, 1)
    date_aux = datetime.date.fromordinal(today())
    inicio_mes = datetime.date(date_aux.year, date_aux.month, date_aux.day)
    return datetime.date.toordinal(inicio_mes) - d_semana[inicio_mes.weekday()]

def hour():
    return  datetime.datetime.now().hour

def rev():
    d_semana = (2, 3, 4, 5, 6, 0, 1)
    dt_aux_1 = datetime.date.fromordinal(today())
    if (datetime.date.fromordinal(so_ini() + 6).month != datetime.date.fromordinal(so_ini()).month):
        rev = 0
        next_rev = 1
    elif(datetime.date.fromordinal(so_ini() + 13).month != datetime.date.fromordinal(so_ini() + 7).month or datetime.date.fromordinal(so_ini() + 7).day == 1):
        inicio_mes = datetime.date(dt_aux_1.year, dt_aux_1.month, 1)
        ini = datetime.date.toordinal(inicio_mes) - d_semana[inicio_mes.weekday()]
        rev = int((today() - ini) / 7)
        next_rev = 0
    else:
        inicio_mes = datetime.date(dt_aux_1.year, dt_aux_1.month, 1)
        ini = datetime.date.toordinal(inicio_mes) - d_semana[inicio_mes.weekday()]
        rev = int((today() - ini) / 7)
        next_rev = rev + 1
    return (rev, next_rev)

#Funcoes para arquivo de log
def edit_log_file(descrpt, info):
    file = open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'rt')
    file_tmp = open(os.path.join(os.path.dirname(__file__), 'log2.txt'), 'wt')
    file_buff = file.readlines()
    find = 0
    h = datetime.datetime.now()
    line_aux = descrpt + ',' + str(h.year) + '/' + ('0' + str(h.month))[-2:] + '/' + ('0' + str(h.day))[-2:] + ',' + ('0' + str(h.hour))[-2:] + ':' + ('0' + str(h.minute))[-2:] + ',' + info
    for i in range(0, len(file_buff)):
        id = file_buff[i].split(',')
        if (id[0] == descrpt):
            find = 1
            file_tmp.write(line_aux + '\n')
        elif(file_buff[i] != '\n'):
            file_tmp.write(file_buff[i])
    if(find == 0):
        file_tmp.write('\n' + line_aux)
    file.close()
    file_tmp.close()
    os.remove(os.path.join(os.path.dirname(__file__), 'log.txt'))
    os.rename(os.path.join(os.path.dirname(__file__), 'log2.txt'), os.path.join(os.path.dirname(__file__), 'log.txt'))
    #upload_file('', 'log.txt')

def read_log_file(descrpt):

    # Verifica existencia do arquivo de log
    if not os.path.isfile(os.path.join(os.path.dirname(__file__), 'log.txt')):
        open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'x')

    # Abre e le o arquivo de log
    file = open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'rt')
    file_buff = file.readlines()
    find = 0
    for i in range(0, len(file_buff)):
        id = file_buff[i].split(',')
        if (id[0] == descrpt):
            find = 1
            break
    file.close()
    if (find == 0):
        return 0
    else:
        return (id)

def log_date(descrpt):

    # Le o arquivo de log e retorna a data de atualizacao do modelo
    aux = read_log_file(descrpt)
    if(aux != 0):
        return datetime.date.toordinal(datetime.date(int(aux[1][0:4]), int(aux[1][5:7]), int(aux[1][8:10])))
    else:
        return 0

def log_error(descrpt):
    aux = read_log_file(descrpt)
    if(aux != 0):
        return aux[3][0:2]
    else:
        return 0

#Funcoes para upload
def upload_mapas():
    folder_list = os.listdir(os.path.join(os.path.dirname(__file__)))
    upload_list = [fn for fn in folder_list if fn.endswith('.png')]
    if upload_list:
        ftp = ftplib.FTP('pactoenergia.com.br', 'mdl@pactoenergia.com.br', '29!pAcTo+16')
        ftp.cwd('mapas')
        for fn in upload_list:
            file = open(os.path.join(os.path.dirname(__file__), fn), 'rb')
            ftp.storbinary('STOR ' + fn, file)
            #print("      Arquivo %s uploaded" %fn)
            file.close()
        ftp.quit()
        print('      Upload: {} OK'.format(fn))
        edit_log_file('Upload', '')
        for fn in upload_list:
            os.remove(os.path.join(os.path.dirname(__file__), fn))

#Funcoes para download
def mapas():
    if (log_date('Upload') != today() and hour() >= 7):
        print('   Rotina de atualizacao de chuvas' + ' - ' + str_dt() + ' - ' + str_now())
        print("   ---------------------------------------------------------------")

        #Limpar pasta de downloads
        # download_folder = 'C:/Users/Mateus Mendonca/Downloads'
        # for file in os.listdir(download_folder):
        #     os.remove(os.path.join(download_foler, file))

        #Baixar dados de previsão de chuva do ONS - SINtegre e carregar para PACTO
        options = Options()
        # options.add_argument('--window-position=10000,0')
        driver = webdriver.Chrome(executable_path='C:/Users/Mateus Mendonca/Downloads/chromedriver.exe', options=options)
        
        try:
            driver.get('https://sintegre.ons.org.br')
            #assert 'ONS' in driver.title

            usuario = 'mateus.mendonca'
            senha = 'EngEletrica2009'

            elem = driver.find_element_by_name('username')
            elem.send_keys(usuario + Keys.RETURN)
            elem = driver.find_element_by_name('password')
            elem.send_keys(senha + Keys.RETURN)

            PATH = 'https://sintegre.ons.org.br/sites/9/38/Documents/images/operacao_integrada/meteorologia/'
            driver.get(PATH + 'eta/Eta40_precipitacao10d.zip')
            driver.get(PATH + 'global/GEFS_precipitacao14d.zip')
            driver.get(PATH + 'ecmwf/ECMWF_precipitacao14d.zip')

            upload_zips('C:/Users/Mateus Mendonca/Downloads')
            driver.quit()
        except:
            driver.quit()
            print('Erro - acesso_SINtegre')

        verify_folder('Prev_Quinta')

        #Baixar e somar dados de chuva ocorrida
        if (log_date('Chuva Ocorrida') != today()):
            verify_folder('Ocorrida')
            if (download_chuva_ocorrida_cptec('Ocorrida') == 1):
                if (soma_arq_bin('Ocorrida', create_name_list(0), 'Ocorrida', 'soma_ocorrida.bin', 18997) == 1):
                    print('      Chuva Ocorrida: OK')
                    edit_log_file('Chuva Ocorrida', '')
        
        #Baixar e somar dados de previsão de chuva ETA 40Km
        if (log_date('Chuva ETA 40') != today()):
            verify_folder('Prev_ETA_ONS')
            if (download_chuva_eta40_ons('Prev_ETA_ONS', 'Eta40_precipitacao10d.zip') == 1):
                if (soma_arq_bin('Prev_ETA_ONS', create_name_list(1), 'Prev_ETA_ONS', 'soma_eta40_1.bin', 18997) == 1):
                    if (soma_arq_bin('Prev_ETA_ONS', create_name_list(2), 'Prev_ETA_ONS', 'soma_eta40_2.bin', 18997) == 1):
                        if(week_day() == 3):
                            nome_aux = 'ETA40_' + str(datetime.date.fromordinal(so_ini() + 7)) + '.bin'
                            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'Prev_ETA_ONS/soma_eta40_2.bin'), os.path.join(os.path.dirname(__file__), 'Prev_Quinta', nome_aux))
                        print('      Chuva ETA 40: OK')
                        edit_log_file('Chuva ETA 40', '')

        #Baixar e somar dados de previsão de chuva GEFS
        if (log_date('Chuva GEFS') != today()):
            verify_folder('Prev_GEFS_ONS')
            if (download_chuva_gefs_ons('Prev_GEFS_ONS', 'GEFS_precipitacao14d.zip') == 1):
                if (soma_arq_bin('Prev_GEFS_ONS', create_name_list(3), 'Prev_GEFS_ONS', 'soma_gefs_1.bin', 18997) == 1):
                    if (soma_arq_bin('Prev_GEFS_ONS', create_name_list(4), 'Prev_GEFS_ONS', 'soma_gefs_2.bin', 18997) == 1):
                        if (week_day() == 3):
                            nome_aux = 'GEFS_' + str(datetime.date.fromordinal(so_ini() + 7)) + '.bin'
                            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'Prev_GEFS_ONS/soma_gefs_2.bin'),os.path.join(os.path.dirname(__file__), 'Prev_Quinta', nome_aux))
                        print('      Chuva GEFS: OK')
                        edit_log_file('Chuva GEFS', '')

        #Baixar e somar dados de previsão de chuva ECMWF
        if (log_date('Chuva ECMWF') != today()):
            verify_folder('Prev_ECMWF_ONS')
            if (download_chuva_ecmwf_ons('Prev_ECMWF_ONS', 'ECMWF_precipitacao14d.zip') == 1):
                if (soma_arq_bin('Prev_ECMWF_ONS', create_name_list(5), 'Prev_ECMWF_ONS', 'soma_ecmwf_1.bin', 113176) == 1):
                    if (soma_arq_bin('Prev_ECMWF_ONS', create_name_list(6), 'Prev_ECMWF_ONS', 'soma_ecmwf_2.bin', 113176) == 1):
                        if (week_day() == 3):
                            nome_aux = 'ECMWF_' + str(datetime.date.fromordinal(so_ini() + 7)) + '.bin'
                            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'Prev_ECMWF_ONS/soma_ecmwf_2.bin'),os.path.join(os.path.dirname(__file__), 'Prev_Quinta', nome_aux))
                        print('      Chuva ECMWF: OK')
                        edit_log_file('Chuva ECMWF', '')

        d_str = date.today().strftime('%y%m%d')
        d0 = str_dt()
        if date.today().weekday() == 5:
            d1 = str_dt(today())
        else:
            d1 = str_dt(today() - 1)
        d2 = str_dt(so_ini())
        d3 = str_dt(so_ini() + 6)
        d4 = str_dt(so_ini() + 7)
        if today()+9 >= so_ini()+13:
            d5 = str_dt(so_ini() + 13)
        else:
            d5 = str_dt(today()+9)
            
        #Gera mapas Chuva Ocorrida
        if (log_date('Chuva Ocorrida') == today() and log_date('Mapas_Ocorrida') != today()):
            leg = 'Pacto Energia - Prec. Acumulada (mm)'
            t1 = 'Semana Operativa'
            t2 = d2 + ' a ' + d1
            gera_mapas(t1, t2, leg, 'Ocorrida', 'soma_ocorrida.bin', os.path.join('.'), 'prec_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            print('      Mapas_Ocorrida: OK')
            edit_log_file('Mapas_Ocorrida', '')

        #Gera mapas ETA 40Km
        if (log_date('Chuva ETA 40') == today() and log_date('Mapas_ETA') != today()):
            leg = 'Pacto Energia - Modelo ETA 40'
            t1 = 'Previsao Semana Operativa'
            t2 = d0 + ' a ' + d3
            gera_mapas(t1, t2, leg, 'Prev_ETA_ONS', 'soma_eta40_1.bin', os.path.join('.'), 'eta_1_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            t1 = 'Previsao Proxima Semana Operativa'
            t2 = d4 + ' a ' + d5
            gera_mapas(t1, t2, leg, 'Prev_ETA_ONS', 'soma_eta40_2.bin', os.path.join('.'), 'eta_2_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            print('      Mapas_ETA: OK')
            edit_log_file('Mapas_ETA', '')

        #Gera mapas GEFS
        if (log_date('Chuva GEFS') == today() and log_date('Mapas_GEFS') != today()):
            leg = 'Pacto Energia - Modelo GEFS'
            t1 = 'Previsao Semana Operativa'
            t2 = d0 + ' a ' + d3
            gera_mapas(t1, t2, leg, 'Prev_GEFS_ONS', 'soma_gefs_1.bin', os.path.join('.'), 'gefs_1_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            t1 = 'Previsao Proxima Semana Operativa'
            t2 = d4 + ' a ' + d5
            gera_mapas(t1, t2, leg, 'Prev_GEFS_ONS', 'soma_gefs_2.bin', os.path.join('.'), 'gefs_2_' + d_str + '.bin', 'XDEF  121 LINEAR  -82.60   0.40', 'YDEF  157 LINEAR  -50.20   0.40')
            print('      Mapas_GEFS: OK')
            edit_log_file('Mapas_GEFS', '')

        #Gera mapas ECMWF
        if (log_date('Chuva ECMWF') == today() and log_date('Mapas_ECMWF') != today()):
            leg = 'Pacto Energia - Modelo ECMWF'
            t1 = 'Previsao Semana Operativa'
            t2 = d0 + ' a ' + d3
            gera_mapas(t1, t2, leg, 'Prev_ECMWF_ONS', 'soma_ecmwf_1.bin', os.path.join('.'), 'ecmwf_1_' + d_str + '.bin', 'XDEF  301 LINEAR  -90.00   0.20', 'YDEF  376 LINEAR  -60.00   0.20')
            t1 = 'Previsao Proxima Semana Operativa'
            t2 = d4 + ' a ' + d5
            gera_mapas(t1, t2, leg, 'Prev_ECMWF_ONS', 'soma_ecmwf_2.bin', os.path.join('.'), 'ecmwf_2_' + d_str + '.bin', 'XDEF  301 LINEAR  -90.00   0.20', 'YDEF  376 LINEAR  -60.00   0.20')
            print('      Mapas_ECMWF: OK')
            edit_log_file('Mapas_ECMWF', '')

        #Faz o upload dos mapas gerados
        #upload_mapas() 

        #Atualiza log dos mapas
        condicoes = [
            log_date('Mapas_Ocorrida') == today(),
            log_date('Mapas_ETA') == today(),
            log_date('Mapas_GEFS') == today(),
            log_date('Mapas_ECMWF') == today(),
        ]
        if all(condicoes):
            print('      Mapas: OK')
            edit_log_file('Mapas', '')

def main():
    check_date = 0
    while (1):
        if (check_date != today()):
            print("   ---------------------------------------------------------------")
            print("   |  Pacto Energia - Pacto Comercializadora de Energia          |")
            print("   |  %s - São Paulo - SP                                |" % str_dt())
            print("   |  Contatos: + 55 (11) 4550 4601                              |")
            print("   |  www.pactoenergia.com.br / contato@pactoenergia.com.br      |")
            print("   |  Python Script   V 2.0                                      |")
            print("   |  Rev: %i  Prox. Rev: %i                                       |" % (rev()[0], rev()[1]))
            print("   ---------------------------------------------------------------")
            check_date = today()
        
        mapas()
        
        time.sleep(120)

main()




















