Name:           boost
Version:        1.77.0
Release:        66
License:        BSL-1.0
Summary:        Useful C++ source libraries
Url:            https://www.boost.org/
Group:          base
Source0:        https://boostorg.jfrog.io/artifactory/main/release/1.77.0/source/boost_1_77_0.tar.bz2
BuildRequires:  bzip2-dev
BuildRequires:  libstdc++-dev
BuildRequires:  python3-dev
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  gmp-dev
BuildRequires:  mpfr-dev
BuildRequires:  icu4c-dev
BuildRequires:  valgrind-dev
Patch1: no-async-pipe-test.patch


%description
Useful C++ source libraries.

%package dev
Summary:        Useful C++ source libraries
Group:          devel
Requires:       boost = %{version}-%{release}
Requires:       boost-extras = %{version}-%{release}

%description dev
Useful C++ source libraries.

%package extras
Summary:        Useful C++ source libraries
Group:          devel
Requires:       boost = %{version}-%{release}

%description extras
Useful C++ source libraries.

%prep
%setup -q -n boost_1_77_0
%patch1 -p1

%build
./bootstrap.sh --prefix=%{buildroot}/usr --libdir=%{buildroot}/usr/lib64 --with-python=python3

# add include path for python headers
sed -i '/using python/ s|^\(.*using python : \([0-9.][0-9.]*\) .*\);$|\1: /usr/include/python\2 ;|' project-config.jam

./b2 %{?_smp_mflags} stage threading=multi link=shared,static runtime-link=shared

%install
./b2 %{?_smp_mflags} install threading=multi link=shared,static runtime-link=shared

# FIXME: many of these cmake files contain references to %{buildroot}, so disable until that issue is fixed
rm -rf %{buildroot}/usr/lib64/cmake

%check
#cd status
#../b2 %{?_smp_mflags} threading=multi link=shared || :

%files
/usr/lib64/libboost_filesystem.so.*
/usr/lib64/libboost_iostreams.so.*
/usr/lib64/libboost_program_options.so.*
/usr/lib64/libboost_system.so.*

%files extras
/usr/lib64/libboost_atomic.so.*
/usr/lib64/libboost_chrono.so.*
/usr/lib64/libboost_container.so.*
/usr/lib64/libboost_context.so.*
/usr/lib64/libboost_contract.so.*
/usr/lib64/libboost_coroutine.so.*
/usr/lib64/libboost_date_time.so.*
/usr/lib64/libboost_fiber.so.*
/usr/lib64/libboost_graph.so.*
/usr/lib64/libboost_json.so.*
/usr/lib64/libboost_locale.so.*
/usr/lib64/libboost_log.so.*
/usr/lib64/libboost_log_setup.so.*
/usr/lib64/libboost_math_c99.so.*
/usr/lib64/libboost_math_c99f.so.*
/usr/lib64/libboost_math_c99l.so.*
/usr/lib64/libboost_math_tr1.so.*
/usr/lib64/libboost_math_tr1f.so.*
/usr/lib64/libboost_math_tr1l.so.*
/usr/lib64/libboost_nowide.so.*
/usr/lib64/libboost_prg_exec_monitor.so.*
/usr/lib64/libboost_python312.so.*
/usr/lib64/libboost_random.so.*
/usr/lib64/libboost_regex.so.*
/usr/lib64/libboost_serialization.so.*
/usr/lib64/libboost_stacktrace_addr2line.so.*
/usr/lib64/libboost_stacktrace_basic.so.*
/usr/lib64/libboost_stacktrace_noop.so.*
/usr/lib64/libboost_thread.so.*
/usr/lib64/libboost_timer.so.*
/usr/lib64/libboost_type_erasure.so.*
/usr/lib64/libboost_unit_test_framework.so.*
/usr/lib64/libboost_wave.so.*
/usr/lib64/libboost_wserialization.so.*

%files dev
/usr/lib64/*.so
/usr/lib64/*.a
/usr/include/boost/
