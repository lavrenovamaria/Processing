# Processing
Processing is a free graphical library and integrated development environment (IDE) built for the electronic arts, new media art, and visual design communities with the purpose of teaching non-programmers the fundamentals of computer programming in a visual context.
Поэтапно, что я делаю:
1. Скачиваю Processing на [сайте](https://processing.org/download). Для ubuntu 20.04 выбрала версию Linux 64-bit
2. Распаковываю архив
3. Внутри папки processing-4.0b5 просто делаю ./processing
4. Изначально была установлена mode Java, но я ещё скачала Python
<p align="left">
	<img  src="https://user-images.githubusercontent.com/84707645/153474057-e9bca11d-3f7d-47d8-b926-afa6f5178879.png" width="800" height="220" />
</p>

Вот этот маленький миленький кусочек кода даёт следующее:
1. Мы установили размер окна `size(800, 200)`. Кстати, если задать размер окна гораздо больший, чем у вас разрешение экрана, то программе норм, она поёрзает, поёрзает да нарисует.
2. Говорим, что если мышь нажата, то рисуем кружочек синего цвета размером `(80, 80)`, который следует за курсором
3. Если мышь не нажата, то рисуем красный кружок такого же размера, тоже следующий за курсором
<p align="left">
	<img  src="https://user-images.githubusercontent.com/84707645/153473567-48ca4cd1-bf2c-4759-a387-c199aa41cd3f.png" width="800" height="200" />
</p>

Другой пример из папки Java_based_syntax
<p align="left">
	<img  src="https://user-images.githubusercontent.com/84707645/153476453-4f7ab14e-a253-415b-8eb3-9b23b14f8c02.png" width="400" height="400" />
</p>

<p align="right">
	<img  src="https://user-images.githubusercontent.com/84707645/153476466-393fbda0-2038-4b07-9712-23f8c0f884db.png" width="400" height="400" />
</p>



<div class="image123">
    <div class="imgContainer">
        <img src="/images/tv.gif" height="200" width="200"/>
        <p>This is image 1</p>
    </div>
    <div class="imgContainer">
        <img class="middle-img" src="/images/tv.gif"/ height="200" width="200"/>
        <p>This is image 2</p>
    </div>
    <div class="imgContainer">
         <img src="/images/tv.gif"/ height="200" width="200"/>
        <p>This is image 3</p>
    </div>
</div>
