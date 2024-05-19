%define major 0
%define libname %mklibname kaldi
%define devname %mklibname kaldi -d

Name: kaldi
Version: 2024.05.19
Release: 1
Source0: https://github.com/kaldi-asr/kaldi/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
# Commit hash is from cmake/third_party/openfst.cmake
Source1: https://github.com/kkm000/openfst/archive/338225416178ac36b8002d70387f5556e44c8d05.tar.gz
Summary: Speech recognition toolkit
# Also: https://kaldi-asr.org/
URL: https://github.com/kaldi-asr/kaldi
License: GPL
Group: System/Libraries
BuildRequires: cmake(OpenBLAS)
BuildRequires: pkgconfig(lapack)
BuildSystem: cmake
BuildOption: -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
BuildRequires: git-core

%patchlist
kaldi-use-openblas.patch
openfst-compile.patch

%description
Kaldi is a toolkit for speech recognition, intended for use by speech
recognition researchers and professionals.

%package -n %{libname}
Summary: Library for speech recognition
Group: System/Libraries

%description -n %{libname}
Kaldi is a toolkit for speech recognition, intended for use by speech
recognition researchers and professionals.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -a 1 -n kaldi-master

mkdir -p _OMV_rpm_build/_deps
mv openfst-* _OMV_rpm_build/_deps/openfst-src
%if "%{_lib}" != "lib"
find . -name CMakeLists.txt |xargs sed -i -e 's,DESTINATION lib,DESTINATION %{_lib},g'
%endif

# The cmake files check .git for version information
find . -name "*.*~" |xargs rm
git init
git add *
git config user.name "OpenMandriva build system"
git config user.email info@openmandriva.org
git commit -am "Import into fake repository"

%install -a
rm -rf %{buildroot}%{_prefix}/testbin

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/fst
%{_libdir}/libfst*.so*
%{_libdir}/libkaldi*.so*

%files -n %{devname}
%{_includedir}/fst
%{_includedir}/kaldi
%{_libdir}/cmake/*
%{_prefix}/lib/cmake/*
