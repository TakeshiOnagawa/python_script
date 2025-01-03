import pyvisa
import time
import numpy as np

rm = pyvisa.ResourceManager()

#接続されているデバイスを取得する
visa_list = rm.list_resources()
print(visa_list)

#ここはprint結果によって各自書き換える
hdm3065 = rm.open_resource('USB0::0x049F::0x606E::CN2303013001068::INSTR')

#IDN?は機器情報を取得するコマンド
hdm3065.write('*IDN?')

#タイムアウト指定
hdm3065.timeout = 25000

#init
hdm3065.write('*RST')
time.sleep(1)
hdm3065.write('*CLS')
time.sleep(1)

values = []
for i in range(208):
    hdm3065.write('CONF:VOLT:AC 100 mV')
    currentValue = np.array(hdm3065.query_ascii_values('READ?'))
    print(str(i)+':'+str(currentValue))
    values.append(currentValue)

print('max value is : ' + str(np.max(values)))
print('min value is : ' + str(np.min(values)))
print('average value is : ' + str(np.average(values)))
print('standard deviartion is : ' + str(np.std(values)))
print(len(values))
