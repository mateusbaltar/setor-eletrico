import os
import struct

ETA_ONS = (157, 121,  './Prev_ETA_ONS', 0)
GEFS_ONS = (80, 81,  './Prev_GEFS_ONS', 1)
TOK30 = (131, 155,  './Prev_TOK30_TOK', 0)
ECMWF_TOK = (152, 167, './Prev_ECMWF_TOK', 0)
ECMWF_ONS = (301, 376,  './Prev_ECMWF_ONS', 1)
GEFS_TOK = (152, 167, './Prev_GEFS_TOK', 0)
GEFS1_TOK = (152, 167, './Prev_GEFS1_TOK', 0)

modelo = GEFS_ONS

def dat_to_bin():

    a = modelo[0]
    b =  modelo[1]

    eta_index = tuple((x * a + i) for i in range(a) for x in range(b))
    gefs_index = tuple(x for x in range(a*b))
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

    soma_arq_bin(modelo[2], modelo[2][2:], 'soma.bin', modelo[0] * modelo[1])

def soma_arq_bin(in_files_path, out_file_path, out_file_name, size):
    
    # Lista com os arquivos da semana operativa
    in_files_list = [f for f in os.listdir(os.path.join('.', in_files_path)) if f.endswith('.bin')]

    if(not os.path.exists(os.path.join(os.path.dirname(__file__), in_files_path))):
        print('   Erro - soma_arq_bin: Pasta com arquivos de entrada nao existe')
    else:
        os.chdir(os.path.join(os.path.dirname(__file__), in_files_path))
        found_error = 0
        for fn in in_files_list:
            if (not os.path.isfile(os.path.join(os.path.dirname(__file__), in_files_path, fn))):
                found_error += 1
                print('   Erro - soma_arq_bin: Arquivo %s nao encontrado' % fn)
        if(found_error > 0):
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
                print('   Arquivo somado: %s' %fn)
            fsoma = open(os.path.join(os.path.dirname(__file__), out_file_path, out_file_name), "wb")
            for a in range(size):
                fsoma.write(struct.pack('f', soma[a]))
            fsoma.close()
            return 1

dat_to_bin()
#soma_arq_bin(modelo[2], modelo[2][2:], 'soma.bin', modelo[0] * modelo[1])