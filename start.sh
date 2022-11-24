if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning Repo...."
  git clone https://github.com/maullikpatell/MdiskSearchBot.git /MdiskSearchBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MdiskSearchBot
fi  
cd /MdiskSearchBot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py



