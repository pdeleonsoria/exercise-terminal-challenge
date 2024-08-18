from datetime import datetime
fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open ("/workspace/exercise-terminal-challenge/res/test.txt", "a")as archivo:

    archivo.write(f"Tarea finalizada a las {fecha_hora_actual}")


