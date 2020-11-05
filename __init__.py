# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import tarfile
import os.path

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'tgz_files' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import gzip_service

module = GetParams("module")

if module == "compress":
    source_file = GetParams("path_file")
    source_dir = GetParams("path_folder")
    add_folder = GetParams("add_folder")
    #add_folder = eval(add_folder)
    output_filename = GetParams("output_path")
    try:
        source = source_file if bool(source_file) else source_dir
        files = []
        if not add_folder:
            files.append(source_dir)
        else:
            for file in os.listdir(source_dir):
                file = os.path.join(source_dir, file)
                files.append(file)
        if output_filename.endswith(".tar"):
            with tarfile.open(output_filename, "w") as tar:
                for file in files:
                    tar.add(file, arcname=os.path.basename(file))
        if output_filename.endswith(".tgz") or output_filename.endswith(".tar.gz"):
            with tarfile.open(output_filename, "w:gz") as tar:
                for file in files:
                    tar.add(file, arcname=os.path.basename(file))
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e


if module == "unzip":
    try: 
        tar_url = GetParams("tar_url")
        extract_path = GetParams("extract_path")
        if tar_url.find('.gz') > 0:
            ext_file = tar_url[:len(tar_url)-3]
            gzip_service.gunzip_shutil(tar_url, ext_file)
        if tar_url.find('.gz') < 0:
            tar = tarfile.open(tar_url, 'r')
            for item in tar:
                tar.extract(item, extract_path)
                if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
                    extract(item.name, "./" + item.name[:item.name.rfind('/')])
            try:
                extract(sys.argv[1] + '.tgz')
                print ('Done.')
            except:
                name = os.path.basename(sys.argv[0])
                print (name[:name.rfind('.')], '<filename>')
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e