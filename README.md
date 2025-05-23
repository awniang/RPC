# Projet RPC

## Description

Ce projet consiste à implémenter un client et un serveur RPC (Remote Procedure Call) en Python 3, en suivant rigoureusement les spécifications des RFC 1831, 1832 et 1833.

Le protocole RPC permet d'exécuter des procédures à distance via le réseau, en utilisant les protocoles UDP (uniquement) pour la couche transport.

## Objectifs pédagogiques

- Comprendre et appliquer une documentation technique complexe.
- Implémenter un client/serveur RPC conforme à la norme, avec encodage/décodage XDR.
- Maîtriser la communication réseau via sockets UDP.
- Utiliser le service rpcbind pour l’enregistrement et la découverte des services RPC.

## Fonctionnalités principales

- Encodage/décodage des types XDR : int, uint, bool, double, string, structures.
- Construction et analyse des messages RPC (call et reply).
- Communication client-serveur via UDP avec gestion des appels et réponses RPC.
- Interaction avec le service rpcbind pour enregistrer, désenregistrer et découvrir les services RPC.
- Implémentation d’un serveur RPC de démonstration fournissant les procédures suivantes :  
  - `null()` (procédure vide)  
  - `pi()` (retourne 3.1415926)  
  - `inc(x)` (incrémente un entier)  
  - `add(x, y)` (additionne deux entiers)  
  - `echo(s)` (retourne la chaîne passée en argument)

## Structure du projet

- `xdr.py` : encodeurs/décodeurs XDR
- `rpcmsg.py` : construction et déconstruction des messages RPC
- `rpcnet.py` : gestion de la communication réseau UDP RPC
- `rpcbind.py` : interface avec le service rpcbind pour gestion des ports RPC
- `server.py` : serveur RPC de démonstration utilisant les modules précédents

## Utilisation

1. Lancer le serveur Python sur un port UDP, par exemple :  
   ```bash
   python3 server.py 7777
