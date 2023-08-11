# scidm cli

# 一、 說明
https://git.narl.org.tw/gitlab/datamarket-team/twdm-dev/-/issues/200
開發資料服務平台 CLI 使用套件，提供以 Python pip 快速安裝並提供以命令列使用之工具。

# 二、 用法

直接使用 pip 即可完成安裝
```
pip install scidmcli
```

# 三、 開發

## 3.1_ 開發工具包

```
pip install build twine
```

## 3.2_ 檔案結構
* README.md
* pyproject.toml
* src 
  * scidmcli
    * \_\_init\_\_.py
    * example.py


## 3.3_ 打包

```
python -m build
```

## 3.4_ 上傳到 PypI

```
twine upload dist/*
```

## 3.5 測試 (安裝)

套件會裝在 python的 library 庫中，如 anaconda3/lib/python3.xx/site-packages/xx
```
pip install scidmcli
```

```
pip uninstall scidmcli
```


# X、補充

## X1_ (optional) 打包到 測試服 做測試

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*  --verbose
```
```
pip install --index-url https://test.pypi.org/simple/ --no-deps scidmcli
```


## X2_ 用 token file 上傳到pypi 

- ~/.pypirc 
```
[distutils]
  index-servers =
    pypi

[pypi]
  username = __token__
  password = pypi-AgEIcH(....skip....)-P7f3FF-rbty7knQ
```

```
twine upload dist/*
```


