import csv

def create_csv(file_name, array):
    """
    ファイル名とCSVにしたい2次元配列を渡すことでCSVを生成する関数
    file_name = 任意のファイル名
    array = [
        [2], 
        [4], 
        [hoge], 
        [piyo]
    ]
    """
    with open(file_name, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(array)