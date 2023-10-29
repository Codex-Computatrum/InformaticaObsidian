---
author: Simone Parente
tags:
  - Java/modifiers
---

>[!info] 
Accesso consentito al codice **nello stesso package** e alle sottoclassi (nel caso di una classe) ma solo per ereditarietà, una sottoclasse in un altro package può accedere ad un membro protected della superclasse solo attraverso un riferimento a un oggetto del proprio tipo (come `this`).