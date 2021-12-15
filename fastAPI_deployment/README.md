# 使用 fastAPI 部署 YOLOv4 物件偵測模型

## 使用 Conda 建立 Python 虛擬環境

### 前置作業: 在電腦裡安裝 [conda](https://docs.conda.io/en/latest/)
我們會使用 Conda 作為環境管理系統，所有需要的函式庫相依都會存放在獨立的環境中。

### 1. 建立虛擬環境
假設我們已經成功安裝好 conda，第一步就是要建立一個新的開發環境。

使用以下指令建立一個包含 python 3.7 的環境：
```
conda create --name 2021ironman python=3.7
```
當環境成功建立好之後，使用以下指令啟動該環境：
```
conda activate 2021ironman
```
接下來我們會在這個環境中安裝所有需要的函式庫與進行開發，所以每次開啟時請確認已進入 `2021ironman` 環境。

### 2. 使用 PIP 安裝函式庫
繼續下去之前請再次確認是否在 `fastAPI_depolyment` 資料夾中，其中包含了 `requirements.txt` 檔案。

這個檔案列出了所有需要的函式庫與其對應的版本，使用以下指令進行安裝：
```
pip install -r requirements.txt
```
請耐心等待各個函式庫下載完成，這步驟完成後，我們就可以開始進行開發了。

阿，如果你是屬於先看完每個步驟再行動那一派的話，其實前兩步驟可以用以下指令抄捷徑：
```
conda env create -f requirements.yml
conda activate 2021ironman
```

### 3. 開啟 Jupyter Lab
在上一個步驟中，我們已經安裝了 Jupyter lab，可以使用以下指令開啟它：
```
jupyter lab
```
執行之後，可以看到終端機印出了許多訊息，而通常我們都需要使用 Token 對 Jupyter lab 進行授權。

這部分只需要到 http://localhost:8888/ 把 Token 貼上去即可，終端機的輸出可能看起來如下，紅框的部分就是 Token：

![Token](https://user-images.githubusercontent.com/43287234/134353956-798521ae-7486-47f0-ad32-05fd4cdf8c77.png)

### 4. 執行 notebook
此時 Jupyter lab 應該會位於執行上一步指令的資料夾中，點開 `server.ipynb` 就可以開始我們的冒險啦!!

如果想關閉 Jupyter lab 的話就連按兩次 Ctrl + C 即可。

## 方法2 使用Pipenv建立虛擬環境
1. 把專案`git clone`下來。
2. 建立pipenv虛擬環境，如未安裝pipenv請執行`pip3 install pipenv`。
    ```
    pipenv --three 
    或指定版本如下
    pipenv --python 3.8 
    ```
3. 安裝相依套件，執行以下指令安裝`requirements.txt`內套件，順利完成將產生`Pipfile.lock`，而`Pipfile`也記錄引入套件的資訊。
    ```
    pipenv install -r .\iThome-2021ironman\fastAPI_deployment\requirements.txt
    ```
4. 執行jupyter lab，如果您使用windows10系統，遇到ModuleNotFoundError: No module named 'pysqlite2'或sqlite3的問題，請參考此[issue](https://github.com/jupyter/notebook/issues/4332)，至 [sqlite官網](https://www.sqlite.org/download.html)下載壓縮檔，解壓縮將`sqlite3.dll`置於您的電腦`C:\Windows\System32\sqlite3.dll`中可解決。
    ```
    #啟動環境
    pipenv shell
    jupyter lab
    #或在pipenv shell外執行
    pipenv run jupyter lab
    ```





### 就這樣，祝大家部署模型愉快~~
