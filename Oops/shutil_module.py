import shutil

#copy/copy2
#shutil.copy("Constructor.py", "main.py")

#copytree
shutil.copytree("Oops", "main")

#move
shutil.move("Oops/Constructor.py", "main.py")

#rmtree - for delete
shutil.rmtree("main.py")