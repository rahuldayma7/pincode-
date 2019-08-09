# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:00:37 2019

@author: rahul.dayma
"""

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


import time

import requests
from tqdm import tqdm
def get_address(link):
    r=requests.get(link)
    text=r.text
    temp=text.split('Address:')[1].split('State:')[0].replace('</b>','').replace('<b>','').replace('<br>','')
    return temp
data=pd.read_excel('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/New folder/68774_Cleaned.xlsm' ,sheet_name='Lot 2')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver=webdriver.Chrome('C:/Users/rahul.dayma/Downloads/chromedriver_win32/chromedriver.exe',options=options)

x=[]
y=[]
df8=pd.DataFrame()
address=[]

for i,j in tqdm(enumerate(data['ADDRESS 1'])):
    driver.get('https://ifsc.bankifsccode.com/{}'.format(j))
#r=requests.get('https://ifsc.bankifsccode.com/')
#soup=BeautifulSoup(r.text, 'html.parser')
#df=soup.find_all("b")
#A=data['IFSC']
#df=A.loc[0:5]


#columns=['Bank','State','District','Branch','IFSC','MICR','Address']


#for i,j in tqdm(enumerate(data['IFSC'][28175:40000])):
    #data['IFSC'][26180]
    
    y=[]
    #driver.find_element_by_id("ifsccode").send_keys(j)
    #driver.find_element_by_name("submit").click()
    time.sleep(1)
    
        
       
    #headers=driver.find_elements_by_tag_name("b")
    try:
        data1=driver.find_elements_by_tag_name("a")
    #for m,n in enumerate(headers):
     #   ac=n.text
      #  x.append(ac)
        for p,q in enumerate(data1):
            ad=q.text
            y.append(ad)
        
        address=(get_address(driver.current_url))
        columns=['Bank','State','District','Branch','IFSC','Address']
        df1=pd.DataFrame(columns=columns)
        df1[columns[0]]=y[8::44]
        df1[columns[1]]=y[9::44]
        df1[columns[2]]=y[10::44]
        df1[columns[3]]=y[12::44] 
        df1[columns[4]]=y[13::44]
        df1[columns[5]]=address
        #driver.back()
        time.sleep(1)
        #driver.refresh()
        df8=df8.append(df1,ignore_index=True)
        #main_df=main_df.append(df8, ignore_index=True)
    except StaleElementReferenceException:
        time.sleep(40)
        driver.quit()
        driver = webdriver.Chrome("C:/Users/rahul.dayma/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get('https://ifsc.bankifsccode.com/')
    
    except NoSuchElementException:
        time.sleep(40)
        driver.quit()
        driver = webdriver.Chrome("C:/Users/rahul.dayma/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get('https://ifsc.bankifsccode.com/')

    except IndexError:
        time.sleep(40)
        driver.quit()
        driver = webdriver.Chrome("C:/Users/rahul.dayma/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get('https://ifsc.bankifsccode.com/')

#df40_43268=df8
#df_10=pd.read_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/0-26659.csv')
#df_10=df_10.append(df40_43268,ignore_index=True)
#df_10=df_10.drop('Unnamed: 0',axis=1)
#df_10.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/ifsc_data')
#
#
#
#data_ap=pd.read_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/ifsc_data1.csv')
#data_ap=data_ap.append(df8,ignore_index=True)
#data_ap.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/main_df.csv')
#
#main_data=pd.read_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/main_df.csv')
#
#main_data=main_data.append(df8,ignore_index=True)
#main_data.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/main_data.csv')
#final_data=pd.read_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/main_data.csv')
#final_data=final_data.append(df8,ignore_index=True)
#final_data=final_data.drop('Unnamed: 0.1.1',axis=1)
#final_data.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/final_data.csv')
#df_43000=df8
#final_data=final_data.append(df8,ignore_index=True)
#final_data.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/final_data1.csv')
#final_data=final_data.drop('Unnamed: 0',axis=1)





