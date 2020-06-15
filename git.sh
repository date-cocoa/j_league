echo 'addするファイルを入力して下さい。'
read add_file
echo 'commit時のメッセージを入力して下さい。'
read commit_message
git add $add_file
git commit -m $commit_message
git push