# 實踐資料飛輪 (鳥兒分類網頁)
## Prerequisites
為了讓接下來的步驟可以順利進行，我們首先要完成以下的前置作業，但因為每個人的作業系統不同 (當然最好是使用 Linux) 所以這裡不額外做說明，請自行進入參考連結並跟著其中的步驟安裝即可：
- 建立 [Google Cloud](https://cloud.google.com/gcp) 帳號與 [Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

    **注意這部份是要收費的，但可以使用$300美元的抵免額並免費試用90天 (免費試用期結束後不會自動收費)!**
- 安裝 [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (後面會用到 gcloud CLI)
- - [訓練好的模型](https://github.com/eatPizza311/iThome-2021ironman/blob/main/build_dataflywheel/model_training.ipynb)，我們的 App 會使用影像分類模型 (以 [Kaggle 300 Bird Species - Classification](https://www.kaggle.com/gpiosenka/100-bird-species) 種的幾種鳥類作為訓練集)。
   
  訓練資料已由 GCP 的值區移到此 Repo 並用 Git LFS 儲存，需要可以自行下載。
  
- 安裝 [Docker](https://docs.docker.com/get-docker/)
- 安裝 [Anaconda](https://www.anaconda.com/products/individual) (如果不想也沒關係!)

## 建立虛擬環境
1. 克隆 Repo
    ```bash
    git clone https://github.com/eatPizza311/iThome-2021ironman.git
    ```
2. 進入 `build_dataflywheel/ironbird/` 資料夾
    ```bash
    cd iThome-2021ironman/build_dataflywheel/ironbird/
    ```
3. 建立虛擬環境與處理函式庫相依 (Streamlit, TensorFlow, etc)

    如果在前置作業時沒有安裝 Anaconda 的話，請使用以下指令建立虛擬環境與安裝函式庫：
    ```bash
    pip install virtualenv
    virtualenv <ENV-NAME>
    source <ENV-NAME>/bin/activate
    pip install -r requirement.txt
    ```
    如果有 Anaconda 則可以使用以下指令：
    ```bash
    conda env create -f requirement.yml
    conda activate ironbird
    ```
4. 測試是否成功 (啟動 Streamlit 與執行 `app.py`)
    ```bash
    streamlit run app.py
    ```
    執行上面的程式碼後應該可以看到以下畫面：
    ![my app](https://i.imgur.com/AsRa3dk.png)

更多詳細內容請參考鐵人賽文章:
- [[Day 25] Final Project (1/5) — 目標、計畫說明](https://ithelp.ithome.com.tw/articles/10279962)
- [[Day 26] Final Project (2/5) — 準備開始](https://ithelp.ithome.com.tw/articles/10280136)
- [[Day 27] Final Project (3/5) — 讓 App 在本機端運行](https://ithelp.ithome.com.tw/articles/10280584)
- [[Day 28] Final Project (4/5) — 部署模型到 Google AI Platform](https://ithelp.ithome.com.tw/articles/10281097)
- [[Day 29] Final Project (5/5) — 部署 App 到 Google App Engine](https://ithelp.ithome.com.tw/articles/10281139)
