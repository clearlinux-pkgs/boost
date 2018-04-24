Name:           boost
Version:        1.67.0
Release:        29
License:        BSL-1.0
Summary:        Useful C++ source libraries
Url:            http://www.boost.org/
Group:          base
Source0:        https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.bz2
BuildRequires:  bzip2-dev
BuildRequires:  libstdc++-dev
BuildRequires:  python-core
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gmp-dev mpfr-dev
BuildRequires:  icu4c-dev
BuildRequires:  valgrind-dev


%description
Useful C++ source libraries.

%package -n boost-dev
Summary:        Useful C++ source libraries
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description -n boost-dev
Useful C++ source libraries.

%prep
%setup -q -n %{name}_1_67_0

%build
./bootstrap.sh --prefix=%{buildroot}/usr --libdir=%{buildroot}/usr/lib64 --with-python=python3

# add include path for python headers
sed -i '/using python/ s|^\(.*using python : \([0-9.][0-9.]*\) .*\);$|\1: /usr/include/python\2m ;|' project-config.jam

./b2 %{?_smp_mflags} stage threading=multi link=shared

%install
./b2 %{?_smp_mflags} install threading=multi link=shared

%check
cd status
../b2 %{?_smp_mflags} threading=multi link=shared || :




%files
%{_libdir}/*.so.*

%files -n boost-dev
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/boost/
