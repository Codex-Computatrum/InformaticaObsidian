## toy
```plantuml
!theme toy
state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}

state Minimized{

}

Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
```
## crt-amber
```plantuml
'!theme superhero-outline
'!theme blueprint
!theme crt-amber

state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}

state Minimized{

}

Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
```
## blueprint
```plantuml
!theme blueprint

state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}

state Minimized{

}

Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
```
## superhero-outline
```plantuml
!theme superhero-outline

state Visible{
Windowed --> Maximized: max()
Maximized --> Windowed: min()
}

state Minimized{

}

Visible --> Minimized: minimize()
Minimized --> Visible[H]: taskbarClick()
```