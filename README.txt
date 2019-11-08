First I created  QrCreater.py file which creates qr code according to given content,I saved this as a QR.png. 
Then, I created Scanner.py file which opens a web camera and scan the qr code. 
After scaning qr code, it parse the content and finds thenpathof the image which is hidden in qr code.
Then, it opens up a image which located in the given path.
I put a sample image "runner.jpg" and also i added its path inside the qr code. 
You can test it with run QrCreater.py file first and then you can scan the output of this run in the Scanner.py file.
