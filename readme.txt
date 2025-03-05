安装，创建 与 激活虚拟环境
pip install virtualenv
python -m venv venv
source venv/bin/activate


将显示所有在虚拟环境中安装的包
 python -m pip list

将此列表放在 requirements.txt 文件中

python -m pip freeze > requirements.txt
pip freeze > requirements.txt

cat requirements.txt

安装
python -m pip install -r requirements.txt


https://114.251.228.195:5000/
https://192.168.50.2:5000/

正多服务器
pip install gunicorn

