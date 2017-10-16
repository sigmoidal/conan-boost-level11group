from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    
    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"
    
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def test(self):
        with tools.environment_append(RunEnvironment(self).vars):
            if self.settings.os == "Windows":
                self.run(os.path.join("bin","test_package"))
            else:
                self.run("DYLD_LIBRARY_PATH=%s %s"%(os.environ['DYLD_LIBRARY_PATH'],os.path.join("bin","test_package")))
