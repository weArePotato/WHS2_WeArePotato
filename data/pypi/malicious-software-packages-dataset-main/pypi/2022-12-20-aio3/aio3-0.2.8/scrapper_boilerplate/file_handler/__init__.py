import json
import pandas as pd
import os


def remove_duplicates():
    print('Terminado! Verificando se existe linhas duplicadas...')
    lines_seen = set()
    with open('profiles.txt', "w") as output_file:
        for each_line in open('raw_profile.txt', "r"):
            if each_line not in lines_seen:  # check if line is not duplicate
                output_file.write(each_line)
                lines_seen.add(each_line)

    print('Terminado! link duplicados removidos')


def save_to_json(data, filename):
    """
    Save data to json file
    """
    print('Salvando os dados em JSON')
    with open(f'{filename}', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_links(file_text):
    print('Iniciando leitura de links...')
    with open(f'{file_text}.txt', 'r') as text:
        return text.readlines()


def JSONtoExcel(filename):
    try:
        print('Iniciando convensão...')
        # temp_df = pd.read_json(f'{filename}.json')
        temp_df = load_json(filename)
        df = pd.json_normalize(temp_df)
        df.to_excel(f'{filename}.xlsx')
        print('Convensão realizada com sucesso!')

    except Exception as error:
        print('Falha na conversão, Arquivo incorreto ou não existe...')


def CSVtoExcel(filename:str):
    """
    convert csv to excel
    filename: str
    return: void
    """
    df = pd.read_csv(filename)
    df.to_excel(filename.replace('.csv', '.xlsx'))
    print('Convensão realizada com sucesso!')


def load_json(json_name:str="data.json"):
    """
    Loads a json file and returns a dataframe
    return: python dictionary
    """
    with open(f'{json_name}','r', encoding="utf-8") as file:
        data = json.load(file)

    return data


def save_to_html(data:str, filename:str='coment.html', mode='w'):
    """
    save data to html

    data: str: data to save
    filename: str: filename to save
    mode: str: append file ou write file
    return: void"""
    with open(filename, mode, encoding='utf8') as file:
        file.write(str(data))


def dataToCSV(dataDict:dict, filename:str):
    """
    convert dict to dataframe and save to csv
    dataDict: dict
    filename: str
    """
    compressed_data = { k: [v] for k, v in dataDict.items() }
    df = pd.DataFrame(compressed_data)
    df.to_csv(filename, mode="a", index=False, header=not os.path.exists(filename))


def dataToExcel(dataDict:dict, filename:str):
    """
    convert dict to dataframe and save to excel
    dataDict: dict
    filename: str

    return: void
    """

    compressed_data = { k: [v] for k, v in dataDict.items() }
    df = pd.DataFrame(compressed_data)
    df.to_excel(filename, index=False, header=not os.path.exists(filename))
