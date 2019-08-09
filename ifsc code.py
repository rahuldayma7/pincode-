# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:02:35 2019

@author: rahul.dayma
"""

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
def get_address(link):
    r=requests.get(link)
    text=r.text
    temp=text.split('Address:')[1].split('State:')[0].replace('</b>','').replace('<b>','').replace('<br>','')
    return temp
data=pd.read_excel('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/New folder/68774_Cleaned.xlsm' ,sheet_name='Lot 2')
driver=webdriver.Chrome('C:/Users/rahul.dayma/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://ifsc.bankifsccode.com/')
#r=requests.get('https://ifsc.bankifsccode.com/')
#soup=BeautifulSoup(r.text, 'html.parser')
#df=soup.find_all("b")
#A=data['IFSC']
#df=A.loc[0:5]


x=[]
y=[]
#columns=['Bank','State','District','Branch','IFSC','MICR','Address']

df8=pd.DataFrame()
address=[]

for i,j in tqdm(enumerate(data['IFSC'][1058:])):
    
    y=[]
    driver.find_element_by_id("ifsccode").send_keys(j)
    driver.find_element_by_name("submit").click()
    time.sleep(3)
    
        
       
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
        time.sleep(2)
        driver.refresh()
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
    
        
        
main_df=df8            
    
main_df     
main_df.to_csv('C:/Users/rahul.dayma/Desktop/New folder/work rahul_dayma/IFSC/ifsc1000.csv')
   












































    
#columns=['ifsc','bank','branch','Bns hours','MOP','Contact','Bank Dtls','R services','Location','city','district','state','pincode','country','address']
#columns=['IFSC code','bank','branch','Location','city','district','state','pincode','address']

#df1=pd.DataFrame(columns=columns)
#df1[columns[0]]=y[5::34]
#df1[columns[1]]=y[7::34]
#df1[columns[2]]=y[9::34]
#df1[columns[3]]=y[21::34] 
#df1[columns[4]]=y[23::34]
#df1[columns[5]]=y[25::34]   
#df1[columns[6]]=y[27::34]
#df1[columns[7]]=y[29::34]
#df1[columns[8]]=y[33::34]

#df1.to_csv('C:/Users/rahul.dayma/Desktop/New folder/final_marketwatch/bonds/zipppppqq.csv')

#df3=df1.copy
        
        
        
        
#address=(get_address(driver.current_url))
#           columns=['IFSC code','bank','branch','Location','city','district','state','pincode','address']
  #          df1=pd.DataFrame(columns=columns)
   #3         df1[columns[0]]=y[5::34]
    #        df1[columns[1]]=y[7::34]
      #      df1[columns[2]]=y[9::34]
       #     df1[columns[3]]=y[21::34] 
       # 3    df1[columns[4]]=y[23::34]
          #  df1[columns[5]]=y[25::34]   
          #  df1[columns[6]]=y[27::34]
           # df1[columns[7]]=y[29::34]
            #df1[columns[8]]=y[33::34]            
            #df1[columns[9]]=address