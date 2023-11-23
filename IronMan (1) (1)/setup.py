import cx_Freeze
executables = [cx_Freeze.Executable(script="jogo.py",icon="assets/ironIcon.ico")]


cx_Freeze.setup(
    name="Iron Man Marcão",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["assets"]}},
    executables = executables
    )


#python setup.py build
#python setup.py bdist_msi