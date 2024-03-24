cd ./coorlabchallenge/

python3 manage.py makemigrations

python3 manage.py migrate

cd ../frontend/

yarn serve &

yarn install

cd ../coorlabchallenge/

python3 manage.py runserver 

sleep 5