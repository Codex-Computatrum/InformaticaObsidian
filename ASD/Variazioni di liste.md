---
author: Lorenzo Tecchia
tags: [definition, dataStructure, to-do]
---
Definiamo oltre altri tipi di [[Lista|liste]]:
- **Lista doppiamente puntata** $\rightarrow$ Insieme dinamico in cui ogni elemento ha:
	- Una chiave;
	- Un riferimento (*next*) all'elemento successivo dell'insieme;
	- Un riferimento (*prev*) all'elemento precedente dell'insieme
- **Lista circolare puntata** $\rightarrow$ Insieme dinamico in cui ogni elemento ha:
	- Una chiave (*key*) e un riferimento (*next*) all'elemento successivo dell'insisme
	- L'ultimo elemento ha un riferimento alla testa della lista
- **Lista circolare doppiamente puntata**$\rightarrow$ Insieme dinamico che ha:
	- Una chiave (*key*), un riferimento (*next*) all'elemento successivo dell'insieme e un riferimento (*prev*) all'elemento precedente dell'insieme
	- L'ultimo elemento ha un riferimento (*next*) alla testa della lista, il primo ha un riferimento (*prev*) alla coda della lista,
