---
author: Simone Parente
tags:
  - prolog
---

>[!summary] Definizione
>$E_1$ è un'istanza di $E_2$ se esiste una [[Sostituzione|sostituzione]] $\theta$ tale che $E_1 = E_2\theta$, cioè se $E_1$ è un *caso particolare* di $E_2$, dove alcune variabili di $E_2$ sono istanziate.

L'applicazione di una [[Sostituzione|sostituzione]] $\theta$ a una espressione $E$ crea un *caso particolare di $E$*, dove i [[Termini non-ground|termini non ground]] di $E$ vengono sostituiti con i termini ([[Termini ground|specificati]] o [[Termini non-ground|parzialmente specificati]]) di $\theta$.
### Esempio
$\theta = \{X=color(rgb, Y,Y,Y)\}$, 
$E=hasColor(o1, X)$.
- $E$ dice che $o1$ ha un colore non specificato
- L'applicazione della sostituzione $\theta$ a $E$, $(E\theta)$, specifica parzialmente che il colore è in formato *rgb* e tutti e 3 i valori sono uguali.
