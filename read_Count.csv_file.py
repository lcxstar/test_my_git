import pandas as pd
def readCount(file_path):
    #file_path为文件的绝对路径，读取Count.csv文件，跳过前四行，将表头设置为默认值
    raw_count= pd.read_csv(file_path,skiprows=4,header=None)
    #从DataFrame中选择需要的几列数据
    count = raw_count[[0, 1, 2, 3, 6, 7]]
    #表头重新命名，并设置索引列
    count.columns = ['name', 'Ns', 'A(cm^2)', 'RhoS(tracks/cm^2)', 'Ni', 'RhoI(tracks/cm^2)']
    count = count.set_index('name')
    #删除Ns为零的行
    count = count[~count['Ns'].isin([0])]
    #改变列的分布顺序
    count = count[['Ns', 'Ni', 'A(cm^2)', 'RhoS(tracks/cm^2)', 'RhoI(tracks/cm^2)']]
    return(count)
