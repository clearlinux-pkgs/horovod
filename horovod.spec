#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : horovod
Version  : 0.18.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/8b/a0/27b00807e6ed78bcab146594acd680e6493d9e49b43ed1649ccf70e2a95d/horovod-0.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/a0/27b00807e6ed78bcab146594acd680e6493d9e49b43ed1649ccf70e2a95d/horovod-0.18.1.tar.gz
Summary  : Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: horovod-bin = %{version}-%{release}
Requires: horovod-license = %{version}-%{release}
Requires: horovod-python = %{version}-%{release}
Requires: horovod-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cffi
Requires: cloudpickle
Requires: openmpi
Requires: psutil
Requires: six
BuildRequires : PyYAML
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cloudpickle
BuildRequires : openmpi
BuildRequires : openmpi-dev
BuildRequires : psutil
BuildRequires : pytorch
BuildRequires : six
BuildRequires : tensorflow

%description
# LBFGS++
**LBFGS++** is a header-only C++ library that implements the Limited-memory
BFGS algorithm (L-BFGS) for unconstrained minimization problem. The code is
derived and modified from the [libLBFGS](https://github.com/chokkan/liblbfgs)
library developed by [Naoaki Okazaki](http://www.chokkan.org/).

%package bin
Summary: bin components for the horovod package.
Group: Binaries
Requires: horovod-license = %{version}-%{release}

%description bin
bin components for the horovod package.


%package license
Summary: license components for the horovod package.
Group: Default

%description license
license components for the horovod package.


%package python
Summary: python components for the horovod package.
Group: Default
Requires: horovod-python3 = %{version}-%{release}

%description python
python components for the horovod package.


%package python3
Summary: python3 components for the horovod package.
Group: Default
Requires: python3-core

%description python3
python3 components for the horovod package.


%prep
%setup -q -n horovod-0.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570999067
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/horovod
cp %{_builddir}/horovod-0.18.1/LICENSE %{buildroot}/usr/share/package-licenses/horovod/bbce9e5e2c16889a1fdf197556e6b052e337a895
cp %{_builddir}/horovod-0.18.1/third_party/lbfgs/LICENSE.md %{buildroot}/usr/share/package-licenses/horovod/5fc0d512fe8797e2ba125c646447ce451689a129
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/horovodrun

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/horovod/5fc0d512fe8797e2ba125c646447ce451689a129
/usr/share/package-licenses/horovod/bbce9e5e2c16889a1fdf197556e6b052e337a895

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
