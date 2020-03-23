# AI勉強会用資料

## フォルダ説明
* cat-or-dog: 画像分類実践用
* movie: 動画素材
* opencv: Opencv実践用
* python: Python実践用

## 環境構築(mac os版)

### 1. Anaconda
#### 1.1 Anacondaの概要
* Anacondaは機械学習などの開発で便利なツールがまとめられた、Pythonのディストリビューションです。  
※ 「ディストリビューション」： 色々な便利ツールをひとまとめにしたもの  

* Anacondaには主に2つの特徴があります。  

1. Python本体だけではなく、機械学習や科学計算でよく使うライブラリが多くまとめられているため、ライブラリやツール等をひとつひとつ揃える必要が無くなる  
2. 仮想環境を構築できる

＜ライブラリ例＞  

|ライブラリ名|ライブラリの説明|
|:---|:---|
|Numpy|配列やベクトルなど、数値計算を行う為のライブラリ|
|Scipy|科学計算の為のライブラリ|
|Matplotlib|グラフを描画する際に使うライブラリ|
|Pandas|データ解析の為のライブラリ|
|scikit-learn|機械学習用のライブラリ|  

#### 1.2 Anacondaのインストール
1. Anacondaの公式サイトからパッケージをダウンロードする （Python3.7versionを選択）  
https://www.anaconda.com/distribution/  

2. ダウンロードしたパッケージを開き、インストーラーの指示通りインストールを行う   

---

### 2. OpenCV
#### 2.1 OpenCVの概要
* オープンソースのコンピューター・ビジョン・ライブラリで、コンピューターで画像や動画を処理するのに必要な機能が実装されています。  
* 画像処理を行うプログラムでは必ずというほど使われる有名なライブラリです。  
※ OpenCVはPython独自のライブラリではありません。  

#### 2.2 OpenCVのインストール
1. Wi-Fiをwave5に切り替える  

2. ターミナルを起動  

3. ターミナル上で以下のコマンドを入力  
`$ pip install opencv-python==3.4.2.16`  

---

### 3. Tensorflow
#### 3.1 Tensorflowの概要
* TensorflowはGoogleが開発しオープンソースで公開している機械学習用のフレームワークです。  
* 数ある機械学習フレームワークの中でユーザ人口トップ  

<Tensorflowの特徴>  
* 使いやすい  
* 分散学習が可能  
* Tensorboardによる学習の可視化が可能  
* シェア率が高い  

#### 3.2 Tensorflowのインストール
1. ターミナル上で以下のコマンドを入力  
`$ pip install tensorflow==1.14.0`  

---

### 4. Keras
#### 4.1 Kerasの概要
* Kerasは機械学習用のフレームワークの一つであり、ディープラーニングのベースとなっている数学的理論の部分をゼロから開発せずとも、比較的短いソースコードで実装することができます。その為、機械学習初学者が利用するのに向いています。  
* KerasのバックエンドではTensorflowやTheanoが動いています。  

<Kerasの特徴>  
* 簡易的なコードで実装  
* ネットワークモデルの構築が容易  
* 複雑な構成ができない  

#### 4.2 Kerasのインストール
1. ターミナル上で以下のコマンドを入力  
`$ pip install Keras==2.2.4`  

---

### 5. Jupyter notebook
* ノートブックと呼ばれる形式で作成したプログラムをブラウザ上で実行し、実行結果を記録しながら、データの分析作業を進めるためのツールです。  

* プログラムとその実行結果やその際のメモを簡単に作成、確認することができるため、自分自身の過去の作業内容の振り返りや、チームメンバーへ作業結果を共有する際に便利なほか、スクール形式での授業や研修などでの利用にも向いています。  

（起動方法①）  
* ターミナル上で以下のコマンドを入力  
`$ jupyter notebook`  

（起動方法②）  
* Anaconda Navigatorを開いてJupyter Notebookをクリック  
