Name:       libpng
Summary:    A library of functions for manipulating PNG image format files
Version:    1.6.40
Release:    1
License:    zlib
URL:        http://www.libpng.org/pub/png/libpng.html
Source0:    %{name}-%{version}.tar.bz2
Patch0:     libpng-multilib.patch
# Current APNG patch available from http://sourceforge.net/projects/libpng-apng/files/
Patch1:     libpng-1.6.40-apng.patch
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(zlib)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.


%package devel
Summary:    Development tools for programs to manipulate PNG image format files
Requires:   %{name} = %{version}-%{release}

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%reconfigure --disable-static --enable-hardware-optimizations
%make_build

%install
%make_install

# Tests are running too slow for ARM under qemu on OBS
%ifarch x86_64 %{ix86}
%check
make check
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/libpng*.so.*

%files devel
%defattr(-,root,root,-)
%doc libpng-manual.txt example.c TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/libpng*.pc
%{_mandir}/man3/*
%{_mandir}/man5/*
