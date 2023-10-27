steps to run this project:
step 1: mkvirtualenv myenvironment or you directly skip to step 3 if you face virtual env install issue
step 2: ./myenvironment/scripts/activate
step 3: pip install -r requiremsnts.txt
step 4: go to root project where manage.py file exists and run python manage.py runserver

urls:
get all subscriptions ->http://127.0.0.1:8000/subscriptionplandetails
get specific subscription details -> http://127.0.0.1:8000/subscriptionplandetail/<subscriptionid>

login api -> http://127.0.0.1:8000/login/ 
signup api -> http://127.0.0.1:8000/signup/ 
body: {
"username":"karthik",
"passowrd":"1234"
}

get all the subscription user boughts -> http://127.0.0.1:8000/user 
pass header with key : Authorization value: token token key (generate from login api)

buy specific subscription : http://127.0.0.1:8000/usersubcribed/2
pass header with key : Authorization value: token token key (generate from login api)


