Name:           boost
Version:        1.59.0
Release:        16
License:        BSL-1.0
Summary:        Useful C++ source libraries
Url:            http://www.boost.org/
Group:          base
Source0:        http://downloads.sourceforge.net/boost/boost_1_59_0.tar.bz2
BuildRequires:  bzip2-dev
BuildRequires:  libstdc++-dev
BuildRequires:  python-core
BuildRequires:  pkgconfig(python2)
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
%setup -q -n %{name}_1_59_0

%build
./bootstrap.sh --prefix=%{buildroot}/usr --libdir=%{buildroot}/usr/lib64
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
