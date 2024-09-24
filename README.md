# description
The Xmind app utilizes a file cache to restore previous versions of Xmind files. However, as you save multiple times, the storage for these cache files can grow significantly(>1~100GB). This behavior leads to the accumulation of redundant file versions, making earlier versions increasingly irrelevant to the current one. 

To address this issue, I have implemented the following python code to delete unnecessary old version files and only leave the lastest 5 version.

Please execute by the Windows PowerShell and enter the following words: python <your py file path>
