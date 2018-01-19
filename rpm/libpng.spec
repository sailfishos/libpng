Name:       libpng

Summary:    A library of functions for manipulating PNG image format files
Version:    1.6.34
Release:    1
Group:      System/Libraries
License:    zlib
URL:        http://www.libpng.org/pub/png/libpng.html
Source0:    ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.xz
Patch0:     libpng-multilib.patch
# Current APNG patch available from http://sourceforge.net/projects/libpng-apng/files/
Patch1:     libpng-1.6.34-apng.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)

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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libpng = %{version}-%{release}
Requires:   zlib-devel

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.



%prep
%setup -q -n %{name}-%{version}/upstream

# libpng-multilib.patch
%patch0 -p1
# libpng-%{version}-apng.patch
%patch1 -p1

%build
./autogen.sh
%configure --disable-static \
%ifarch %{arm}
    --enable-arm-neon
%endif

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/libpng*.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_mandir}/man5/*
%doc *.txt example.c README TODO CHANGES
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/*
%doc %{_mandir}/man3/*
