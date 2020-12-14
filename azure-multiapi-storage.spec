#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-multiapi-storage
Version  : 0.3.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/4e/ff/2f9cc5f900c1a719ac22c855422c27c1e64aaebdbb5301bd6b8ce932dd75/azure-multiapi-storage-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/ff/2f9cc5f900c1a719ac22c855422c27c1e64aaebdbb5301bd6b8ce932dd75/azure-multiapi-storage-0.3.1.tar.gz
Summary  : Microsoft Azure Storage Client Library for Python with multi API version support.
Group    : Development/Tools
License  : MIT
Requires: azure-multiapi-storage-python = %{version}-%{release}
Requires: azure-multiapi-storage-python3 = %{version}-%{release}
Requires: azure-common
Requires: azure-core
Requires: azure-nspkg
Requires: cryptography
Requires: python-dateutil
Requires: requests
BuildRequires : azure-common
BuildRequires : azure-core
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : python-dateutil
BuildRequires : requests

%description
==================================================================================

%package python
Summary: python components for the azure-multiapi-storage package.
Group: Default
Requires: azure-multiapi-storage-python3 = %{version}-%{release}

%description python
python components for the azure-multiapi-storage package.


%package python3
Summary: python3 components for the azure-multiapi-storage package.
Group: Default
Requires: python3-core
Provides: pypi(azure_multiapi_storage)
Requires: pypi(azure_common)
Requires: pypi(azure_core)
Requires: pypi(cryptography)
Requires: pypi(python_dateutil)
Requires: pypi(requests)

%description python3
python3 components for the azure-multiapi-storage package.


%prep
%setup -q -n azure-multiapi-storage-0.3.1
cd %{_builddir}/azure-multiapi-storage-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607975853
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
