rem change current path
cd /d %~dp0
cd ..

rem get news from website
python get_daily_news.py

rem push posts to github
git add _posts 
git commit -m "Add news post"
git push