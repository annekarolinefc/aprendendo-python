# Como remover diretorios - excluir pastas

# os - rmdir - para remover diretorios vazios
import os 
os.rmdir("dir")

# shutil - rmtree - para remover diretorios com arquivos
import shutil
shutil.rmtree("dir")

# 0s - remove - remove arquivos
os.remove("nomearquivo.txt")