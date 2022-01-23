# tp4
Martin COVA et Hugues FARTHOUAT
https://github.com/HuguesFARTH/tp4

Cette version du Space Invaders comporte 4 types d'ennemis:
  - Jaune -> 1HP et ne tir pas et 10% de chance de drop un coeur.
  - Orange -> 1HP et tir droit et 10% de chance de drop un coeur.
  - Rouge claire -> 5HP et ne tir pas et 75% de chance de drop un coeur.
  - Rouge fonçé -> 5HP et tir en direction du joueur et 75% de chance de drop un coeur.

Les touches sont configurables, ainsi que deux types d'affichage pour les dégats des monstres/blocks avec un affichage par texte (en bleu le nombre de vie) ou par overlay (une image ajoutée par dessus)

Le système de création de niveau n'est pas totalement fonctionnel (pas d'interface de sélection faite) mais un niveau par défault est proposé.

Un exemple de liste utilisé serait dans IFrame dans la classe GameFrame avec le self.entities, liste où sont stockés toutes les entitées (blocks,projectiles,player,coeur)

Un exemple de fonction récursive: Level, la fonction permettant d'ajouter X block: addBlocks.
