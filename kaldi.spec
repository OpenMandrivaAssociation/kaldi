%define major 0
%define libname %mklibname kaldi
%define devname %mklibname kaldi -d

Name: kaldi
Version: 2024.05.20
Release: 1
Source0: https://github.com/kaldi-asr/kaldi/archive/refs/heads/master.tar.gz#/kaldi-%{version}.tar.gz
# VOSK's fork directly:
#Source0: https://github.com/alphacep/kaldi/archive/refs/heads/vosk.tar.gz#/kaldi-%{version}.tar.gz
# Commit hash is from cmake/third_party/openfst.cmake
#Source1: https://github.com/kkm000/openfst/archive/338225416178ac36b8002d70387f5556e44c8d05.tar.gz
Summary: Speech recognition toolkit
# Also: https://kaldi-asr.org/
URL: https://github.com/kaldi-asr/kaldi
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake(OpenBLAS)
BuildRequires: pkgconfig(lapack)
BuildRequires: git-core
BuildSystem: cmake
BuildOption: -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
#BuildOption: -DKALDI_BUILD_TEST:BOOL=OFF

%patchlist
# From VOSK's fork: https://github.com/kaldi-asr/kaldi/compare/master...alphacep:kaldi:vosk
https://github.com/kaldi-asr/kaldi/commit/2b69aed630e26fb2c700bba8c45f3bd012371c5c.patch
https://github.com/kaldi-asr/kaldi/commit/11b67d387b547d1afb616ab8f95fd74c459d20c6.patch
# not useful, we use system openblas
#https://github.com/kaldi-asr/kaldi/commit/341d0a52e1a28d55dfcdf10356b5e0eccb9dd700.patch
https://github.com/kaldi-asr/kaldi/commit/7a7fbb447a00edd8d010a7cd111e7ccff37b484c.patch
# not useful, only touches build scripts we don't use
#https://github.com/kaldi-asr/kaldi/commit/d54092c0c51d931c51df602af204723378555138.patch
# Seems to be upstream already
#https://github.com/kaldi-asr/kaldi/commit/a25f216f5ce4eec5e45a6ab7651e20c9840a05cd.patch
# CUDA specific and seems to be solved differently upstream
#https://github.com/kaldi-asr/kaldi/commit/0fee1c17bd8c3c1111a6a70fb098f85007930756.patch
https://github.com/kaldi-asr/kaldi/commit/2abed6b15990d9438f70863f2b58bd8af8432043.patch
# Only touches build scripts we don't use
#https://github.com/kaldi-asr/kaldi/commit/52ab1a41a8942475feb699a0b103bb9307f2cf60.patch
# Seems to be upstream already
#https://github.com/kaldi-asr/kaldi/commit/173438905ccd96195982ccdc0195dc03e66cb1da.patch
#https://github.com/kaldi-asr/kaldi/commit/ca03ce4954f4f66042929dcc42d6d2da4caa1f92.patch
#https://github.com/kaldi-asr/kaldi/commit/44c8771a655bb5408507d62963b984b4835266c9.patch
https://github.com/kaldi-asr/kaldi/commit/93ef0019b847272a239fbb485ef97f29feb1d587.patch
https://github.com/kaldi-asr/kaldi/commit/ecb4b47159501ef0d67888633e65b8fc0c1f79d1.patch
https://github.com/kaldi-asr/kaldi/commit/531c651f629442220d3efada3da52913a7c95b11.patch
https://github.com/kaldi-asr/kaldi/commit/bf5874dbfbf57c63a90614ad0c0cad9bf1a72e16.patch
https://github.com/kaldi-asr/kaldi/commit/cd7afefa8d153199e9d940cc8657bb3a333ea8e4.patch
https://github.com/kaldi-asr/kaldi/commit/82dc187a4de08a67b7a9df50ee43e11f455a77e8.patch
# Only affects internalized openblas
#https://github.com/kaldi-asr/kaldi/commit/48455f99d04485e056a9ad59c85737c3bec96309.patch
#https://github.com/kaldi-asr/kaldi/commit/4989c2fa65ee7a4868a5d42edc469a070e9cbda1.patch
https://github.com/kaldi-asr/kaldi/commit/e9c3bca9a71fc82c41b990be09fb367bd69f5562.patch
https://github.com/kaldi-asr/kaldi/commit/98155d8ae0a7f6b2f5d5ed33c07927aaefe96622.patch
https://github.com/kaldi-asr/kaldi/commit/dd629c862e7ff45ed9fe79c38dcb7c793549dc03.patch
https://github.com/kaldi-asr/kaldi/commit/b499bbca50edef8bbfabf16f2526ad0b7367b500.patch
# Fixed differently upstream
#https://github.com/kaldi-asr/kaldi/commit/06d055cd93f9c03fe7047ff8ff97dee113b27202.patch
# Only affects internalized openblas
#https://github.com/kaldi-asr/kaldi/commit/d313a7dbfc5a6a4e071a017df70b07ec705523fd.patch
#https://github.com/kaldi-asr/kaldi/commit/85be09f1dde648834ead4c0a43b377a1a9049f28.patch
https://github.com/kaldi-asr/kaldi/commit/603496b91abe49cc4bf57611bd668e05fd9693e4.patch
https://github.com/kaldi-asr/kaldi/commit/79f77546d7d6d424f4ed3e0d3aa40c5f47d1bf2c.patch
https://github.com/kaldi-asr/kaldi/commit/97993cd5794b04f5cf959eda3a8e27f7860fd4b0.patch
https://github.com/kaldi-asr/kaldi/commit/25e0c75fff1ce5c2df4ebc81a08f51586466564a.patch
https://github.com/kaldi-asr/kaldi/commit/8842452f48a1aa88e32884d5fe99eae3e8222eb6.patch
# Only affects internalized openblas
#https://github.com/kaldi-asr/kaldi/commit/cb664d5a4523e87ca5433355150f085168d25870.patch
https://github.com/kaldi-asr/kaldi/commit/f2630f6c82d06834990ff812208d52c4e5357ccb.patch
https://github.com/kaldi-asr/kaldi/commit/783c1772da3345eec1a1f41e76c9b3107460459a.patch
# MODIFIED to remove a chunk that doesn't apply and isn't needed anymore
https://github.com/kaldi-asr/kaldi/commit/28c8976d7e6c499676cabc717e293288eabbb7d7.patch
https://github.com/kaldi-asr/kaldi/commit/8cbc20fbf66030fce8afbea803bd52335f4e52fa.patch
https://github.com/kaldi-asr/kaldi/commit/b6a9fefbb01384215aa045d72e6de243b68962bf.patch
kaldi-openfst-1.8.patch
kaldi-blas-linkage.patch

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
%autosetup -p1 -n kaldi-master

#mkdir -p _OMV_rpm_build/_deps
#mv openfst-* _OMV_rpm_build/_deps/openfst-src
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

%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib/cmake/kaldi/* %{buildroot}%{_libdir}/cmake/kaldi
%endif

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libkaldi*.so*

%files -n %{devname}
%{_includedir}/kaldi
%{_libdir}/cmake/*
