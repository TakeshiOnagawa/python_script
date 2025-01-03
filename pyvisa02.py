import pyvisa
import time
import numpy as np

rm = pyvisa.ResourceManager()

#接続されているデバイスを取得する
visa_list = rm.list_resources()
print(visa_list)

#オシロスコープのSCPIオープン
scope = rm.open_resource('USB0::0x1AB1::0x0515::MS5A223805228::0::INSTR')
scope.timeout = 30000

# #*IDN?で機種情報を取得
scope.write('*IDN?')
print(scope.read())
time.sleep(1)


#横軸を2uS/divに設定
scope.write(':TIMebase:MAIN:SCALe 0.000002')

#CH1の設定
scope.write(':CHANnel1:DISPlay ON')             #CH1を有効
scope.write(':CHANnel1:SCALe 0.1')             #縦軸を100mV/divに設定
scope.write(':CHANnel1:BWLimit 20M')            #帯域制限20MHz
scope.write(':CHANnel1:COUPling AC')            #ACカップリング

#トリガーの設定
scope.write(':TRIGger:EDGE:SOURce CHAN1')       #トリガーソースをCH1に設定
scope.write(':TRIGger:MODE EDGE')               #トリガーをEDGEに設定
scope.write(':TRIGger:EDGE:SLOPe POSitive')     #トリガーをEDGE(positive)に設定
scope.write(':TRIGger:EDGE:LEVel 0.01')         #トリガーレベルを10mVに設定
scope.write(':TRIGger:SWEep SINGle')            #トリガーをSINGLEモードに設定
scope.write(':SYSTem:KEY:PRESs MOFF')           #MENUバーを消す
scope.write(':SYSTem:KEY:PRESs MOFF')           #MENUバーを消す


for i in range(10):
    
    scope.write(':SYSTem:KEY:PRESs SINGle')     #SINGLEボタン(トリガ待機)
    time.sleep(5)
    scope.write(':SAVE:IMAGe C:Scope'+str(i)+'.png')#画像保存
    time.sleep(20)
