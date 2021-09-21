import os
import shutil
import common as cmn

# Toolchain path
TOOLCHAIN_x86_64 = os.path.join(cmn.TOP_DIR, "cmake", "x86_64.gcc.toolchain.cmake")
TOOLCHAIN_arm64 = os.path.join(cmn.TOP_DIR, "cmake", "aarch64.gcc.toolchain.cmake")

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "linux")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_libpng("x86_64", "Debug")
  Build_libpng("x86_64", "Release")
  Build_libpng("arm64", "Debug")
  Build_libpng("arm64", "Release")

#------------------------------------------------------------
# libpngビルド
#    host       "x86_64" or "arm64"
#    build_type "Debug" or "Release"
def Build_libpng(host, build_type):
  cmn.Log("Build libpng host=" + host + " build_type=" + build_type)
  INSTALL_PREFIX = os.path.join(INSTALL_PREFIX_OS, host, build_type)
  os.chdir(cmn.LIBPNG_DIR)
  shutil.rmtree("build", ignore_errors=True)
  os.makedirs("build", exist_ok=True)
  os.chdir("build")
  # cmake generator
  cmd = ["cmake"]
  if host == "x86_64":
    cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN_x86_64]
  else:
    cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN_arm64]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += ["-DPNG_TESTS=OFF"]
  cmd += ["-DPNG_BUILD_ZLIB=ON"]
  cmd += ["-DZLIB_INCLUDE_DIR=" + os.path.join(INSTALL_PREFIX, "include")]
  cmd += ["-DZLIB_LIBRARY=" + os.path.join(INSTALL_PREFIX, "lib", "libz.a")]
  if build_type == "Debug":
    cmd += ["-DPNG_DEBUG=ON"]
  cmd += [".."]
  cmn.Do(cmd)
  # cmake build
  cmd = ["cmake --build ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)
  # cmake install
  cmd = ["cmake --install ."]
  cmd += ["--config " + build_type]
  cmn.Do(cmd)


if __name__ == '__main__':
    main()
