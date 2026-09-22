Import("env")


def regenerate_compiledb(source, target, env):
    env.Execute("pio run -t compiledb")


env.AddPostAction("buildprog", regenerate_compiledb)
