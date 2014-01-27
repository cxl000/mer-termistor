Summary: A drop-down terminal for Wayland
Name: termistor
Version: 0.0.0
Release: 1
License: GPLv3
Group: Development/Liraries
URL: https://github.com/giucam/termistor.git
Source0: %{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.8
BuildRequires: wayland-devel
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(libtsm)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires:  qt5-plugin-imageformat-jpeg
BuildRequires:  qt5-plugin-imageformat-gif
BuildRequires:  qt5-plugin-imageformat-ico
BuildRequires:  qt5-plugin-platform-eglfs
BuildRequires:  qt5-plugin-platform-kms
BuildRequires:  qt5-plugin-platform-minimal
BuildRequires:  qt5-plugin-platform-minimalegl
BuildRequires:  qt5-plugin-platform-linuxfb
BuildRequires:  qt5-plugin-platform-offscreen
BuildRequires:  qt5-plugin-platform-xcb


%description
terminal for wayland.

%prep
%setup -q
cd termistor

%build
cd termistor
%ifnarch %{ix86} x86_64
# HACK!!! Please remove when possible.
# cmake is accelerated but version is too old
mkdir /tmp/bin
cp -a /usr/bin/cmake /usr/share/cmake/Modules /usr/share/cmake/Templates /tmp/bin/
PATH=/tmp/bin:$PATH
/tmp/bin/cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_LIBDIR:PATH=/usr/lib -DINCLUDE_INSTALL_DIR:PATH=/usr/include -DLIB_INSTALL_DIR:PATH=/usr/lib -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=/usr/share -DCMAKE_SKIP_RPATH:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=ON . -DCMAKE_BUILD_TYPE=RelWithDebInfo
%else
%cmake
%endif
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
cd termistor
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/termistor

