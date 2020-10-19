#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : horovod
Version  : 0.20.3
Release  : 26
URL      : https://files.pythonhosted.org/packages/6f/bd/b979db25c1337967472630714d0f98ec596ad9f199a3d1777dc36453d713/horovod-0.20.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/6f/bd/b979db25c1337967472630714d0f98ec596ad9f199a3d1777dc36453d713/horovod-0.20.3.tar.gz
Summary  : Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: horovod-bin = %{version}-%{release}
Requires: horovod-license = %{version}-%{release}
Requires: horovod-python = %{version}-%{release}
Requires: horovod-python3 = %{version}-%{release}
Requires: Keras
Requires: PyYAML
Requires: cffi
Requires: cloudpickle
Requires: h5py
Requires: mxnet
Requires: numpy
Requires: openmpi
Requires: psutil
Requires: tensorflow
BuildRequires : Keras
BuildRequires : PyYAML
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cloudpickle
BuildRequires : h5py
BuildRequires : mxnet
BuildRequires : numpy
BuildRequires : openmpi
BuildRequires : openmpi-dev
BuildRequires : psutil
BuildRequires : python3-dev
BuildRequires : pytorch
BuildRequires : tensorflow
Patch1: 2338.patch

%description
The goal of Horovod is to make distributed Deep Learning fast and easy to use.

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
Provides: pypi(horovod)
Requires: pypi(cffi)
Requires: pypi(cloudpickle)
Requires: pypi(psutil)
Requires: pypi(pyyaml)

%description python3
python3 components for the horovod package.


%prep
%setup -q -n horovod-0.20.3
cd %{_builddir}/horovod-0.20.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603136048
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/horovod
cp %{_builddir}/horovod-0.20.3/LICENSE %{buildroot}/usr/share/package-licenses/horovod/bbce9e5e2c16889a1fdf197556e6b052e337a895
cp %{_builddir}/horovod-0.20.3/third_party/lbfgs/LICENSE.md %{buildroot}/usr/share/package-licenses/horovod/5fc0d512fe8797e2ba125c646447ce451689a129
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
