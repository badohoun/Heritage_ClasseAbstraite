# Heritage_ClasseAbstraite



** Héritage en Python : 
Avez-vous déjà eu plusieurs classes avec des attributs et des méthodes similaires ?

Si tel est le cas, utilisez l'héritage pour organiser vos classes. L'héritage nous permet de définir une classe parent et des classes enfants. Une classe enfant hérite de toutes les méthodes et attributs de la classe parent.

** Classes abstraites : déclarer des méthodes sans implémentation
Parfois, vous souhaiterez peut-être que différentes classes utilisent les mêmes attributs et méthodes. Mais la mise en œuvre de ces méthodes peut être légèrement différente dans chaque classe.

Un bon moyen d’implémenter cela consiste à utiliser des classes abstraites. Une classe abstraite contient une ou plusieurs méthodes abstraites.

Une méthode abstraite est une méthode déclarée mais qui ne contient aucune implémentation. La méthode abstraite nécessite des sous-classes pour fournir des implémentations.


** Dans ce projet nous aborderons ces notions et verrons de manière pratique comment nous pouvons  les utiliser pour écrire du code propre et organisé en science des données dans le cadre du MLOPS 



# Packaging terms:
- Module 
- Package
- sub-package
- distribution package 


# Modern way to build package :

* the old format distribution is sdist : source distribution package : python setup.py sdist 

   1. May make assumptions about customer machine:
      e.g. requires "gcc" to run "gcc numpy/*.c"
   2. Is slow: setup.py must be executed, compilation may be required.
   3. Is insecure: setup.py may contain  arbitrary code.
* the  good and new  format distribution is wheel 
   1. First install wheel package 
   2. the command help us to build wheel package : python setup.py bdist_wheel 
   3.  realpython.com/python-wheels/ explain clearly how to read wheel format 
   4.  we need to add build dependencies  for reproducibility and for it we need pyproject.toml file and install build tool : pip install build 
   5. escaping config hell; use setup.cfg 


