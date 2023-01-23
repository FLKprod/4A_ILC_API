# Workflows réalisé pour le TD : 

curl.yml : Action qui se déclenche sur commande manuel pour éxecuter une commande curl sur l'adresse wttr.in/Moon (réalisé par Romain)

curlBis.yml : Action qui se déclenche sur commande manuel pour éxecuter une commande curl sur l'adresse wttr.in/Moon (réalisé par Luke)

runmainbis.yml : Action qui se déclenche à chaque pull request et qui exécute la commande python main.py. Ce script python affiche "Hello there" (réalisé par Luke)

runmain.yml : Action qui se déclenche à chaque pull request et qui exécute la commande python main.py. Ce script python affiche "Hello there" (réalisé par Romain)

newpush.yml : Action qui se déclenche à chaque push pour exécuter "echo "New push!""

# Workflows réalisé pour le projet : 

buildAPP.yml : Action qui se déclenche à chaque push. Elle va pip3 install flask dans un premier temps puis elle va build notre app myFlask.py. (Correspond à la 1ère github action demandé)

docker-image.yml : Action qui se déclenche manuellement. On va build le dockerfile puis le push. Cette action a été créée durant le projet en classe mais ne s'est pas avéré utile par rapport au sujet du projet.

dockerImFonctionnel.yml : Action qui se déclenche manuellement. Elle permet de dockeriser notre image. (Correspond à la 2ème github action demandé)

pushImageSemver.yml : Action qui se déclenche à chaque release. Elle va permet de mettre le bon tag semver dans notre image poussé sur le registre (Correspond à la 3ème github action demandé)
