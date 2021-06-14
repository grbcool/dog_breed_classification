import base64
 
with open('008b1271ed1addaccf93783b39deab45.jpg','rb') as bytes_file:
    encoding = base64.b64encode(bytes_file.read())

with open('base64.txt','wb') as f:
    f.write(encoding)    
