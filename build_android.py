import os
import shutil
import common as cmn

# Toolchain path
NDK_PATH = "/opt/android-sdk-linux/android-ndk-r21e"
TOOLCHAIN = os.path.join(NDK_PATH, "build/cmake/android.toolchain.cmake")
ANDROID_PLATFORM = "16"

# Install path
INSTALL_PREFIX_OS = os.path.join(cmn.INSTALL_PREFIX, "android")

def main():
  cmn.Log("Start " + __file__)
  cmn.Log("INSTALL_PREFIX_OS: " + INSTALL_PREFIX_OS)
  Build_libpng("x86_64", "Debug")
  Build_libpng("x86_64", "Release")
  Build_libpng("arm64-v8a", "Debug")
  Build_libpng("arm64-v8a", "Release")

#------------------------------------------------------------
# libpngビルド
#    host       "x86_64" or "arm64-v8a"
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
  cmd += ["-DCMAKE_TOOLCHAIN_FILE=" + TOOLCHAIN]
  cmd += ["-DANDROID_ABI=" + host]
  cmd += ["-DANDROID_PLATFORM=" + ANDROID_PLATFORM]
  cmd += ["-DCMAKE_INSTALL_PREFIX=" + INSTALL_PREFIX]
  cmd += ["-DPNG_TESTS=OFF -DHAVE_LD_VERSION_SCRIPT=OFF"]
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
