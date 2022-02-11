# Processing
Processing is a free graphical library and integrated development environment (IDE) built for the electronic arts, new media art, and visual design communities with the purpose of teaching non-programmers the fundamentals of computer programming in a visual context.
Поэтапно, что я делаю:
1. Скачиваю Processing на [сайте](https://processing.org/download). Для ubuntu 20.04 выбрала версию Linux 64-bit
2. Распаковываю архив
3. Внутри папки processing-4.0b5 просто делаю ./processing
4. Изначально была установлена mode Java, но я ещё скачала Python
```
def setup():
    size(800, 200)
def draw():
    if mousePressed:
        fill(0,0,255)
    else:
        fill(255,64,64)
    ellipse(mouseX, mouseY, 80, 80)
```
![2_0](https://user-images.githubusercontent.com/84707645/132090087-bbdaf2db-9652-4add-90ad-ffaa82f6aca9.jpg)
Вот этот маленький миленький кусочек кода даёт следующее:
1. Мы установили размер окна `size(800, 200)`. Кстати, если задать размер окна гораздо больший, чем у вас разрешение экрана, то программе норм, она поёрзает, поёрзает да нарисует.
2. Говорим, что если мышь нажата, то рисуем кружочек синего цвета размером `(80, 80)`, который следует за курсором
3. Если мышь не нажата, то рисуем красный кружок такого же размера, тоже следующий за курсором
<p align="center">
	<img  src="https://user-images.githubusercontent.com/84707645/153473567-48ca4cd1-bf2c-4759-a387-c199aa41cd3f.png" width="800" height="200" />
</p>

Другой пример из папки Java_based_syntax
<p align="center">
	<img  src="https://user-images.githubusercontent.com/84707645/153637250-a4f6ee7e-5c21-4749-a34b-54de78ee472b.jpg" width="800" height="800" />
</p>
