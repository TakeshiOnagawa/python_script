import pyvisa
import time
import numpy as np

rm = pyvisa.ResourceManager()

#接続されているデバイスを取得する
visa_list = rm.list_resources()
print(visa_list)

#Hantek HDM3065のSCPIをオープンする(ここはprint結果によって各自書き換える)
hdm3065 = rm.open_resource('USB0::0x049F::0x606E::CN2303013001068::INSTR')

#IDN?は機器情報を取得するコマンド
hdm3065.write('*IDN?')

#タイムアウト指定[ms]
#これがないとREAD命令で
hdm3065.timeout = 25000

#HDM3065のInit
hdm3065.write('*RST')                   #キューのRESET命令
time.sleep(3)
hdm3065.write('*CLS')                   #キューのCLEAR命令
time.sleep(0.3)
hdm3065.write('CONF:VOLT:AC 100 mV')    #機器のCONF命令
time.sleep(3)
hdm3065.write('SAMP:COUN 1')            #サンプル数指定
time.sleep(0.3)

#デジタルマルチメータから連続でREADする
values = []
for i in range(10):
    currentValue = np.array(hdm3065.query_ascii_values('READ?'))
    print(str(i)+':'+str(currentValue))
    values.append(currentValue)

#取得後の統計値を出力
print('max value is : ' + str(np.max(values)))
print('min value is : ' + str(np.min(values)))
print('average value is : ' + str(np.average(values)))
print('standard deviartion is : ' + str(np.std(values)))
print(len(values))
