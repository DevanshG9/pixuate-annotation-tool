curl https://install.meteor.com/ | sh
meteor npm install
echo 'export MONGO_URL="mongodb://user:password@127.0.0.1:27017/labeltool-local?authSource=admin"' >> ~/.bashrc
source ~/.bashrc
meteor npm start
