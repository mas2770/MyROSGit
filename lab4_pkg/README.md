В ходе данной лабораторной работы были рассмотрены основы TF. Были написаны два scripts файла и один launch файла: turtle_tf.launch запускает следующие узлы: keyboard (нужен для управления первой черепашкой с клавиатуры), turtle2_tf_broadcaster (нужен для преобразования полученных данных из топика input_pose и для публикации перемещения и поворота черепашки из фрейма world в фрейм turtle2), turtle1_tf_broadcaster (аналогичен turtle2_tf_broadcaster), turtle_pointer (нужен для управления второй черепашкой), rviz. turtle_tf_listener.py нужен для помещения второй черепашки на начальные координаты и задания перемещения и угла поворота для второй черепашки(вторая черепашка обращается вокруг первой) Для запуска вводим в консоль roslaunch lab4_pkg turtle_tf.launch