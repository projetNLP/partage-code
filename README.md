### Outil visuel facilitant l'apprentissage d'une IA
Ce programme a été codé dans le cadre d'un projet informatique réalisé sur un semestre.
Ce fichier existe afin de procurer un tutoriel d'utilisation de notre programme. 

### Structure du projet
Les fichiers config.json et annotation.json contiennent les informations entrée/sortie (les questions qu'il faut pour faire l'annotation de la base de données et les réponses éventuelles) de l'interface.

Le fichier interface.py contient l'interface qui va être affichée.

Le fichier model.py contient les fonctions utiles pour faire les flux de données entre l'interface et les fichiers .json.

Les fichiers index.html et traitement.php forment un formulaire web qui permet aux utilisateurs d'entrer les questions et les réponses possibles et de mettre les données collectées dans un fichier config.json qui est stocké sur le serveur web.

### Utilisation
1. Pour commencer, l'utilisateur peut soit créer son propre fichier de configuration pour l'environnement en allant sur le site http://haozhe.sun.perso.centrale-marseille.fr/ soit utiliser un fichier existant en le mettant en format .json comme le prototype config.json dans le répertoire. Et quand il aura fini d'entrer les informations, il peut utiliser une application (Cyberduck, Filezilla, etc.) pour récupérer le fichier sur le serveur.

2. Il convient ensuite d'utiliser ce fichier en l'ajoutant dans ce répertoire et éxecuter le script interface.py. Les photos sont s'afficher une par une avec les questions correspondantes et les réponses éventuelles, il suffit que l'utilisateur réponde et qu'il clique sur le bouton suivant pour que les réponses soient enregistrées dans le fichier annotation.json.

3. Remarque : la ligne model.init_annotation() ne devrait être exécuter qu'une fois pour un répertoire donné. A partir de la deuxième fois, la commenter.