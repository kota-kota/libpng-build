import os
import shutil
import common as cmn

# Visual Studio
PROGRAM_FILES = os.environ.get("PROGRAMFILES(X86)")
VC_DIR = os.path.join(PROGRAM_FILES, "Microsoft Visual Studio 14.0", "VC")
VC_BIN_DIR = os.path.join(VC_DIR, "bin")
VCVARSALL_BAT = "\"" + os.path.join(VC_DIR, "vcvarsall.bat") + "\""

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "windows")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_libpng("x86", "Debug")
  Build_libpng("x86", "Release")
  Build_libpng("x64", "Debug")
  Build_libpng("x64", "Release")

#------------------------------------------------------------
# libpngビルド
#    host       "x86" or "x64"
#    build_type "Debug" or "Release"
def Build_libpng(host, build_type):
  cmn.Log("Build libpng host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.LIBPNG_DIR)
  shutil.rmtree("build", ignore_errors=True)
  os.makedirs("build", exist_ok=True)
  os.chdir("build")
  # cmake generator
  cmd = ["cmake -G \"Visual Studio 16 2019\""]
  if host == "x86":
    cmd += ["-A Win32"]
  else:
    cmd += ["-A x64"]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += ["-DPNG_TESTS=OFF"]
  if build_type == "Debug":
    cmd += ["-DPNG_DEBUG=ON"]
  cmd += [".."]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmd += ["--target INSTALL"]
  cmn.Do(cmd)


if __name__ == '__main__':
    main()
