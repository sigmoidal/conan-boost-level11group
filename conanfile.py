from conans import ConanFile, tools, os


class BoostLevel11GroupConan(ConanFile):
    name = "Boost.Level11Group"
    version = "1.65.1"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-level11group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["date_time", "locale", "pool", "serialization", "spirit", "thread"]
    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"
    build_requires = "Boost.Generator/1.65.1@bincrafters/stable"
    requires = "Boost.Algorithm/1.65.1@bincrafters/stable",\
        "Boost.Array/1.65.1@bincrafters/stable",\
        "Boost.Assert/1.65.1@bincrafters/stable",\
        "Boost.Atomic/1.65.1@bincrafters/stable",\
        "Boost.Bind/1.65.1@bincrafters/stable",\
        "Boost.Chrono/1.65.1@bincrafters/stable",\
        "Boost.Concept_Check/1.65.1@bincrafters/stable",\
        "Boost.Config/1.65.1@bincrafters/stable",\
        "Boost.Container/1.65.1@bincrafters/stable",\
        "Boost.Core/1.65.1@bincrafters/stable",\
        "Boost.Detail/1.65.1@bincrafters/stable",\
        "Boost.Endian/1.65.1@bincrafters/stable",\
        "Boost.Exception/1.65.1@bincrafters/stable",\
        "Boost.Filesystem/1.65.1@bincrafters/stable",\
        "Boost.Foreach/1.65.1@bincrafters/stable",\
        "Boost.Function/1.65.1@bincrafters/stable",\
        "Boost.Function_Types/1.65.1@bincrafters/stable",\
        "Boost.Functional/1.65.1@bincrafters/stable",\
        "Boost.Fusion/1.65.1@bincrafters/stable",\
        "Boost.Integer/1.65.1@bincrafters/stable",\
        "Boost.Intrusive/1.65.1@bincrafters/stable",\
        "Boost.Io/1.65.1@bincrafters/stable",\
        "Boost.Iostreams/1.65.1@bincrafters/stable",\
        "Boost.Iterator/1.65.1@bincrafters/stable",\
        "Boost.Lexical_Cast/1.65.1@bincrafters/stable",\
        "Boost.Math/1.65.1@bincrafters/stable",\
        "Boost.Move/1.65.1@bincrafters/stable",\
        "Boost.Mpl/1.65.1@bincrafters/stable",\
        "Boost.Optional/1.65.1@bincrafters/stable",\
        "Boost.Phoenix/1.65.1@bincrafters/stable",\
        "Boost.Predef/1.65.1@bincrafters/stable",\
        "Boost.Preprocessor/1.65.1@bincrafters/stable",\
        "Boost.Proto/1.65.1@bincrafters/stable",\
        "Boost.Range/1.65.1@bincrafters/stable",\
        "Boost.Regex/1.65.1@bincrafters/stable",\
        "Boost.Smart_Ptr/1.65.1@bincrafters/stable",\
        "Boost.Static_Assert/1.65.1@bincrafters/stable",\
        "Boost.System/1.65.1@bincrafters/stable",\
        "Boost.Throw_Exception/1.65.1@bincrafters/stable",\
        "Boost.Tokenizer/1.65.1@bincrafters/stable",\
        "Boost.Tti/1.65.1@bincrafters/stable",\
        "Boost.Tuple/1.65.1@bincrafters/stable",\
        "Boost.Type_Traits/1.65.1@bincrafters/stable",\
        "Boost.Typeof/1.65.1@bincrafters/stable",\
        "Boost.Unordered/1.65.1@bincrafters/stable",\
        "Boost.Utility/1.65.1@bincrafters/stable",\
        "Boost.Variant/1.65.1@bincrafters/stable",\
        "Boost.Winapi/1.65.1@bincrafters/stable"

    # Date_Time Dependencies
    # algorithm9 assert1 config0 io1 lexical_cast8 mpl5 range7 serialization11 smart_ptr4
    # static_assert1 throw_exception2 tokenizer6 type_traits3 utility5
    
    # Locale Dependencies
    # assert1 config0 function5 iterator5 smart_ptr4 static_assert1 type_traits3

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

    def requirements(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command + self.b2_options)
    
    @property
    def b2_options(self):
        if self.options.use_icu:
            return " boost.locale.iconv=off boost.locale.icu=on"
        else:
            return " boost.locale.icu=off"

    def package(self):
        self.copy(pattern="*", dst="lib", src="stage/lib")
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_info(self):
        self.user_info.lib_short_names = ",".join(self.lib_short_names)
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")
        if self.options.use_icu:
            self.cpp_info.defines.append("BOOST_LOCALE_WITH_ICU=1") 
        elif self.settings.os == "Macos": 
            self.cpp_info.libs.append("iconv") 
        if self.settings.os != "Windows": 
            self.cpp_info.libs.append("pthread") 