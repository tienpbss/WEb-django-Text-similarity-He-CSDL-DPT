
thu tu chay

git clone --depth 1 https://github.com/tienpbss/WEb-django-Text-similarity-He-CSDL-DPT.git

cd WEb-django-Text-similarity-He-CSDL-DPT

virtualenv env

env/scripts/activate


pip install -r requirements.txt 

cd .\find_document\  

python manage.py runserver

tạo một đường dẫn "D:\\Document-CSDLDPT" rồi nhét đống pdf vào đó hoặc là sửa biến file_path trong views.py 

pdf file ở trong repo Pre-data-Text-similarity-He-CSDL-DPT
