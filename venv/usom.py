import requests
response=requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)#SSL Sertifikasını göz ardı etmek için kullanıyoruz
dosya=open("usom.txt","w")
dosya.write(str(response.content))
dosya.close()