%define version 0.202

Summary: Python bindings for leveldb database library
Name: python3-leveldb
Version: %{version}
Release: 1
Source0: leveldb-%{version}.tar.gz
License: BSD-3-Clause
Group: Development/Libraries
Vendor: Arni Mar Jonsson <arnimarkj@gmail.com>
Url: https://github.com/rjpower/py-leveldb
BuildRequires: python3-devel python3-setuptools

%description
Python bindings for leveldb database library

%prep
%setup -n leveldb-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENSE LICENSE.leveldb LICENSE.snappy
%doc README
%{_libdir}/python3*/site-packages/*.so
%{_libdir}/python3*/site-packages/*.egg-info/

%changelog
* Sun Jan 28 2024 Joachim Metz <joachim.metz@gmail.com> 0.202-1
- Auto-generated
