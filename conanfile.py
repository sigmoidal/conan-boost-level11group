from conans import ConanFile, tools, os


class BoostLevel11GroupConan(ConanFile):
    name = "Boost.Level11Group"
    version = "1.64.0"
    generators = "txt"
    settings = "os", "arch", "compiler", "build_type"    
    url = "https://github.com/bincrafters/conan-boost-level11group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing"
    requires = "Boost.Algorithm/1.64.0@bincrafters/testing",\
        "Boost.Array/1.64.0@bincrafters/testing",\
        "Boost.Assert/1.64.0@bincrafters/testing",\
        "Boost.Atomic/1.64.0@bincrafters/testing",\
        "Boost.Bind/1.64.0@bincrafters/testing",\
        "Boost.Chrono/1.64.0@bincrafters/testing",\
        "Boost.Concept_Check/1.64.0@bincrafters/testing",\
        "Boost.Config/1.64.0@bincrafters/testing",\
        "Boost.Container/1.64.0@bincrafters/testing",\
        "Boost.Core/1.64.0@bincrafters/testing",\
        "Boost.Detail/1.64.0@bincrafters/testing",\
        "Boost.Endian/1.64.0@bincrafters/testing",\
        "Boost.Exception/1.64.0@bincrafters/testing",\
        "Boost.Filesystem/1.64.0@bincrafters/testing",\
        "Boost.Foreach/1.64.0@bincrafters/testing",\
        "Boost.Function/1.64.0@bincrafters/testing",\
        "Boost.Function_Types/1.64.0@bincrafters/testing",\
        "Boost.Functional/1.64.0@bincrafters/testing",\
        "Boost.Fusion/1.64.0@bincrafters/testing",\
        "Boost.Integer/1.64.0@bincrafters/testing",\
        "Boost.Intrusive/1.64.0@bincrafters/testing",\
        "Boost.Io/1.64.0@bincrafters/testing",\
        "Boost.Iostreams/1.64.0@bincrafters/testing",\
        "Boost.Iterator/1.64.0@bincrafters/testing",\
        "Boost.Lexical_Cast/1.64.0@bincrafters/testing",\
        "Boost.Locale/1.64.0@bincrafters/testing",\
        "Boost.Math/1.64.0@bincrafters/testing",\
        "Boost.Move/1.64.0@bincrafters/testing",\
        "Boost.Mpl/1.64.0@bincrafters/testing",\
        "Boost.Optional/1.64.0@bincrafters/testing",\
        "Boost.Phoenix/1.64.0@bincrafters/testing",\
        "Boost.Predef/1.64.0@bincrafters/testing",\
        "Boost.Preprocessor/1.64.0@bincrafters/testing",\
        "Boost.Proto/1.64.0@bincrafters/testing",\
        "Boost.Range/1.64.0@bincrafters/testing",\
        "Boost.Regex/1.64.0@bincrafters/testing",\
        "Boost.Smart_Ptr/1.64.0@bincrafters/testing",\
        "Boost.Static_Assert/1.64.0@bincrafters/testing",\
        "Boost.System/1.64.0@bincrafters/testing",\
        "Boost.Throw_Exception/1.64.0@bincrafters/testing",\
        "Boost.Tokenizer/1.64.0@bincrafters/testing",\
        "Boost.Tti/1.64.0@bincrafters/testing",\
        "Boost.Tuple/1.64.0@bincrafters/testing",\
        "Boost.Type_Traits/1.64.0@bincrafters/testing",\
        "Boost.Typeof/1.64.0@bincrafters/testing",\
        "Boost.Unordered/1.64.0@bincrafters/testing",\
        "Boost.Utility/1.64.0@bincrafters/testing",\
        "Boost.Variant/1.64.0@bincrafters/testing",\
        "Boost.Winapi/1.64.0@bincrafters/testing"

    # Date_Time Dependencies
    # algorithm9 assert1 config0 io1 lexical_cast8 mpl5 range7 serialization11 smart_ptr4
    # static_assert1 throw_exception2 tokenizer6 type_traits3 utility5

    # Pool Dependencies
    # assert1 config0 integer3 thread11 throw_exception2 type_traits3

    # Serialization Dependencies
    # array3 assert1 config0 core2 detail5 integer3 io1 iterator5 move3 mpl5 optional5 predef0
    # preprocessor0 smart_ptr4 spirit11 static_assert1 type_traits3 unordered8 utility5 variant9

    # Spirit Dependencies
    # algorithm9 array3 assert1 concept_check5 config0 core2 endian6 filesystem8 foreach8 function5
    # function_types5 fusion5 integer3 io1 iostreams10 iterator5 lexical_cast8 locale6 math8 mpl5
    # optional5 phoenix9 pool11 predef0 preprocessor0 proto8 range7 regex6 serialization11
    # smart_ptr4 static_assert1 thread11 throw_exception2 tti6 type_traits3 typeof5 unordered8 utility5 variant9

    # Thread Dependencies
    # assert1 atomic4 bind3 chrono8 concept_check5 config0 container7 core2 date_time11 exception5 function5
    # functional5 intrusive6 io1 move3 mpl5 optional5 predef0 preprocessor0 smart_ptr4 static_assert1
    # system3 throw_exception2 tuple4 type_traits3 utility5 winapi1

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/date_time"))     

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/pool"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/serialization"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/spirit"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/thread"))
               
    def package(self):

        date_time_dir = os.path.join(self.build_folder, "date_time", "include")
        self.copy(pattern="*", dst="include", src=date_time_dir)

        pool_dir = os.path.join(self.build_folder, "pool", "include")
        self.copy(pattern="*", dst="include", src=pool_dir)
        
        serialization_dir = os.path.join(self.build_folder, "serialization", "include")
        self.copy(pattern="*", dst="include", src=serialization_dir)

        spirit_dir = os.path.join(self.build_folder, "spirit", "include")
        self.copy(pattern="*", dst="include", src=spirit_dir)

        thread_types_dir = os.path.join(self.build_folder, "thread_types", "include")
        self.copy(pattern="*", dst="include", src=thread_types_dir)
        